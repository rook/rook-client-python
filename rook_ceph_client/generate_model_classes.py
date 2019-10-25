"""
Generate Python files containing data Python models classes for
all properties of the all CRDs in the file

For example:
  python3 -m venv venv
  pip install -r requirements.txt
  python setup.py develop
  curl https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/ceph/common.yaml | generate-model-classes - rook-ceph-client
  generate-model-classes ~/go/src/github.com/rook/rook/cluster/examples/kubernetes/ceph/common.yaml rook-ceph-client

Usage:
  generate-model-classes [--create-package] <crds.yaml> <output-folder>
"""

from abc import ABC, abstractmethod
from collections import OrderedDict
from os.path import expanduser
from typing import List, Union, Iterator, Optional

import yaml
try:
    from dataclasses import dataclass
except ImportError:
    from attr import dataclass  # type: ignore
from docopt import docopt

header = '''"""
This file is automatically generated.
Do not modify.
"""

try:
    from typing import Any, Optional, Union, List
except ImportError:
    pass

from ._helper import _omit, CrdObject, CrdObjectList

'''

@dataclass  # type: ignore
class CRDBase(ABC):
    name: str
    nullable: bool
    required: bool

    @property
    def py_name(self):
        return self.name

    @property
    @abstractmethod
    def py_type(self):
        ...

    def py_property(self):
        return f"""
@property
def {self.py_name}(self):
    # type: () -> {self.py_property_return_type}
    return self._property_impl('{self.py_name}')

@{self.py_name}.setter
def {self.py_name}(self, new_val):
    # type: ({self.py_param_type}) -> None
    self._{self.py_name} = new_val
    """.strip()

    @property
    def py_param(self):
        if not self.has_default:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}=_omit,  # type: {self.py_param_type}'

    @property
    def has_default(self):
        return not self.required

    @property
    def py_param_type(self):
        return f'Optional[{self.py_type}]' if (self.nullable or not self.required) else self.py_type

    @property
    def py_property_return_type(self):
        return f'Optional[{self.py_type}]' if (self.nullable) else self.py_type

@dataclass
class CRDAttribute(CRDBase):
    type: str
    default_value: str='_omit'

    @property
    def py_param(self):
        if not self.has_default:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}={self.default_value},  # type: {self.py_param_type}'

    @property
    def has_default(self):
        return not self.required or self.default_value != '_omit'

    @property
    def py_type(self):
        return {
            'integer': 'int',
            'boolean': 'bool',
            'string': 'str',
            'object': 'Any',
        }[self.type]

    def flatten(self):
        yield from ()

    def toplevel(self):
        return ''


@dataclass
class CRDList(CRDBase):
    items: 'CRDClass'

    @property
    def py_name(self):
        return self.name

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:] + 'List'

    @property
    def py_param_type(self):
        inner = f'Union[List[{self.items.py_type}], CrdObjectList]'
        return f'Optional[{inner}]' if (self.nullable or not self.required) else inner

    @property
    def py_property_return_type(self):
        inner = f'Union[List[{self.items.py_type}], CrdObjectList]'
        return f'Optional[{inner}]' if (self.nullable) else inner

    def flatten(self):
        yield from self.items.flatten()
        yield self

    def toplevel(self):
        return f"""
class {self.py_type}(CrdObjectList):
{indent('_items_type = ' + self.items.py_type)}
""".strip()


@dataclass
class CRDClass(CRDBase):
    attrs: List[Union[CRDAttribute, 'CRDClass']]

    def toplevel(self):
        ps = '\n\n'.join(a.py_property() for a in self.attrs)
        return f"""class {self.py_type}(CrdObject):
{indent(self.py_properties())}        

{indent(self.py_init())}

{indent(ps)}
""".strip()

    @property
    def sub_classes(self) -> List["CRDClass"]:
        return [a for a in self.attrs if isinstance(a, CRDClass)]

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:]

    def py_properties(self):
        def a_to_tuple(a):
            return ', '.join((f"'{a.name}'",
                       f"'{a.py_name}'",
                       a.py_type.replace('Any', 'object'),
                       str(a.required),
                       str(a.nullable)))

        attrlist = ',\n'.join([f'({a_to_tuple(a)})' for a in self.attrs])
        return f"""_properties = [\n{indent(attrlist)}\n]"""

    def flatten(self) -> Iterator['CRDClass']:
        for sub_cls in self.attrs:
            yield from sub_cls.flatten()
        yield self

    def py_init(self):
        sorted_attrs = sorted(self.attrs, key=lambda a: a.has_default)
        params = '\n'.join(a.py_param for a in sorted_attrs)
        init_set = '\n'.join(f'self.{a.py_name} = {a.py_name}  # type: ignore' for a in sorted_attrs)
        return f"""
def __init__(self,
{indent(params, indent=4+9)}
             ):
{indent(init_set)}
""".strip()

def indent(s, indent=4):
    return '\n'.join(' '*indent + l for l in s.splitlines())


def handle_property(elem_name, elem: dict, required: bool):
    nullable = elem.get('nullable', False)
    if 'properties' in elem:
        ps = elem['properties']
        required_elems = elem.get('required', [])
        sub_props = [handle_property(k, v, k in required_elems) for k, v in ps.items()]
        return CRDClass(elem_name, nullable, required, sub_props)
    elif 'items' in elem:
        item = handle_property(elem_name + 'Item', elem['items'], False)
        return CRDList(elem_name, nullable, required, item)
    elif 'type' in elem:
        return CRDAttribute(elem_name, nullable, required, elem['type'])
    elif elem == {}:
        return CRDAttribute(elem_name, nullable, required, 'object')
    assert False, str((elem_name, elem))


def handle_crd(c_dict) -> Optional[CRDClass]:
    try:
        name = c_dict['spec']['names']['kind']
        s = c_dict['spec']['validation']['openAPIV3Schema']
    except (KeyError, TypeError):
        return None
    s['required'] = ['spec']
    c = handle_property(name, s, True)
    k8s_attrs = [CRDAttribute('apiVersion', False, True, 'string'),
                 CRDAttribute('kind', False, True, 'string', f'"{name}"'),
                 CRDAttribute('metadata', False, True, 'object'),
                 CRDAttribute('status', False, False, 'object')]
    return CRDClass(c.name, False, True, k8s_attrs + c.attrs)


def local(yaml_filename):
    with open(yaml_filename) as f:
        yamls = yaml.safe_load_all(f.read())
        for y in yamls:
            try:
                yield y
            except AttributeError:
                pass


def remove_duplicates(items):
    return OrderedDict.fromkeys(items).keys()


def get_toplevels(crd):
    elems = list(crd.flatten())

    def dup_elems(l):
        ds = set([x for x in l if l.count(x) > 1])
        return ds

    names = [t.name for t in elems]
    for dup_name in dup_elems(names):
        dups = set(e.toplevel() for e in elems if e.name == dup_name)
        assert len(dups) == 1, str(dups)
        
    return remove_duplicates(cls.toplevel() for cls in elems)


def create_package(outfolder):
    from shutil import copy
    from . import _helper
    
    copy(_helper.__file__, outfolder)
    open(f'{outfolder}/__init__.py', 'w').close()

    
def main():
    args = docopt(__doc__)
    yaml_filename = '/dev/stdin' if args["<crds.yaml>"] == '-' else args["<crds.yaml>"]
    outfolder = args["<output-folder>"]
    for crd in local(yaml_filename):
        valid_crd = handle_crd(crd)
        if valid_crd is not None:
            with open(f'{outfolder}/{valid_crd.name.lower()}.py', 'w') as f:
                f.write(header)
                classes = get_toplevels(valid_crd)
                f.write('\n\n\n'.join(classes))
                f.write('\n')
    if args['--create-package']:
        create_package(outfolder)

if __name__ == '__main__':
    main()