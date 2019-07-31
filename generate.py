"""
Generate Python Sub file containing static type information for checking
the CRRs submitted to Rook
Usage:
Run
$ python ./generate.py

"""
from collections import namedtuple, OrderedDict
from os.path import expanduser
from typing import List, Union, Iterator, Optional

import yaml
from attr import dataclass

header = '''"""
This file is automatically generated.
Do not modify.
"""

from typing import List, Dict, Any, Optional

NoneType = type(None)  
_omit = None  # type: NoneType
_omit = object()  # type: ignore

'''

class CRDBase:
    def py_property(self):
        return f"""
@property
def {self.py_name}(self):
    # type: () -> {self.py_param_type}
    if self._{self.py_name} is _omit:
        raise AttributeError('{self.py_name} not found')
    return self._{self.py_name}

@{self.py_name}.setter
def {self.py_name}(self, new_val):
    # type: ({self.py_param_type}) -> None
    self._{self.py_name} = new_val
    """.strip()

    @property
    def py_param(self):
        if self.required:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}=_omit,  # type: {self.py_param_type}'

    @property
    def py_param_type(self):
        return f'Optional[{self.py_type}]' if (self.nullable or not self.required) else self.py_type

    @property
    def py_init_set(self):
        return f'self.{self.py_name} = {self.py_name}'

    @property
    def py_from_json_val(self):
        if self.required:
            return f"data['{self.name}']"
        return f"data.get('{self.name}', _omit)"

@dataclass
class CRDAttribute(CRDBase):
    name: str
    type: str
    nullable: bool
    required: bool
    default_value: str='_omit'

    @property
    def py_param(self):
        if self.required:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}={self.default_value},  # type: {self.py_param_type}'

    @property
    def py_name(self):
        return self.name

    @property
    def py_type(self):
        return {
            'integer': 'int',
            'boolean': 'bool',
            'string': 'str',
            'object': 'Any',
        }[self.type]

    @property
    def py_to_json_val(self):
        return 'self._' + self.py_name

    def flatten(self):
        yield from ()

    def toplevel(self):
        return ''


@dataclass
class CRDList(CRDBase):
    name: str
    items: 'CRDClass'
    nullable: bool
    required: bool

    @property
    def py_name(self):
        return self.name

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:] + 'List'

    def flatten(self):
        yield from self.items.flatten()
        yield self

    def toplevel(self):
        return f"""
class {self.py_type}(list):
{indent(self.py_to_json())}

{indent(self.py_from_json())}
""".strip()

    def py_to_json(self):
        return f"""
def to_json(self):
    return [e.to_json() for e in self]
""".strip()

    @property
    def py_to_json_val(self):
        return f'self.{self.py_name}.to_json() if self._{self.py_name} not in [None, _omit] else self._{self.py_name}'

    def py_from_json(self):
        return f"""
@classmethod
def from_json(cls, data):
    # type: (list) -> {self.py_param_type}
    return cls({self.items.py_type}.from_json(e) for e in data)
""".strip()

    @property
    def py_from_json_val(self):
        if self.required:
            return f"{self.py_type}.from_json(data['{self.name}'])"
        return f"{self.py_type}.from_json(data['{self.name}']) if '{self.name}' in data else _omit"


@dataclass
class CRDClass(CRDBase):
    name: str
    attrs: List[Union[CRDAttribute, 'CRDClass']]
    nullable: bool
    required: bool

    def toplevel(self):
        ps = '\n\n'.join(a.py_property() for a in self.attrs)
        return f"""class {self.py_type}(object):
{indent(self.py_init())}

{indent(ps)}

{indent(self.py_to_json())}

{indent(self.py_from_json())}
""".strip()

    @property
    def sub_classes(self) -> List["CRDClass"]:
        return [a for a in self.attrs if isinstance(a, CRDClass)]

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:]

    @property
    def py_name(self):
        return self.name

    def flatten(self) -> Iterator['CRDClass']:
        for sub_cls in self.attrs:
            yield from sub_cls.flatten()
        yield self

    def py_init(self):
        sorted_attrs = sorted(self.attrs, key=lambda a: a.required, reverse=True)
        params = '\n'.join(a.py_param for a in sorted_attrs)
        init_set = '\n'.join(a.py_init_set for a in sorted_attrs)
        return f"""
def __init__(self,
{indent(params, indent=4+9)}
             ):
{indent(init_set)}
""".strip()

    def py_to_json(self):
        elems = '\n'.join(f"'{a.name}': {a.py_to_json_val}," for a in self.attrs)
        return f"""
def to_json(self):
    res = {{
{indent(elems, 8)}
    }}
    return {{k: v for k, v in res.items() if v is not _omit}}
""".strip()

    @property
    def py_to_json_val(self):
        return f'self.{self.py_name}.to_json() if self._{self.py_name} not in [None, _omit] else self._{self.py_name}'

    def py_from_json(self):
        elems = '\n'.join(f"{a.py_name}={a.py_from_json_val}," for a in self.attrs)
        return f"""
@classmethod
def from_json(cls, data):
    # type: (dict) -> {self.py_param_type}
    return cls(
{indent(elems, 8)}
    )
""".strip()

    @property
    def py_from_json_val(self):
        from_json = f"{self.py_type}.from_json(data['{self.name}'])"
        if self.nullable:
            from_json = f"({from_json} if data['{self.name}'] is not None else None)"
        if self.required:
            return from_json
        return f"{from_json} if '{self.name}' in data else _omit"


def indent(s, indent=4):
    return '\n'.join(' '*indent + l for l in s.splitlines())


def handle_property(elem_name, elem: dict, required: bool):
    nullable = elem.get('nullable', False)
    if 'properties' in elem:
        ps = elem['properties']
        required_elems = elem.get('required', [])
        sub_props = [handle_property(k, v, k in required_elems) for k, v in ps.items()]
        return CRDClass(elem_name, sub_props, nullable, required)
    elif 'items' in elem:
        item = handle_property(elem_name + 'Item', elem['items'], False)
        return CRDList(elem_name, item, nullable, required)
    elif 'type' in elem:
        return CRDAttribute(elem_name, elem['type'], nullable, required)
    elif elem == {}:
        return CRDAttribute(elem_name, 'object', nullable, required)
    assert False, str((elem_name, elem))


def handle_crd(c_dict) -> Optional[CRDClass]:
    try:
        name = c_dict['spec']['names']['kind']
        s = c_dict['spec']['validation']['openAPIV3Schema']
    except (KeyError, TypeError):
        return None
    s['required'] = ['spec']
    c = handle_property(name, s, True)
    k8s_attrs = [CRDAttribute('apiVersion', 'string', False, True),
                 CRDAttribute('kind', 'string', False, True, f'"{name}"'),
                 CRDAttribute('metadata', 'object', False, True)]
    return CRDClass(c.name, k8s_attrs + c.attrs, False, True)


def download_yaml():
    import requests

    url = 'https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/ceph/common.yaml'
    r = requests.get(url, allow_redirects=True)
    yamls = yaml.safe_load_all(r.content.decode('utf-8'))
    for y in yamls:
        try:
            yield y
        except AttributeError:
            pass

def local():
    with open(expanduser('~/go/src/github.com/rook/rook/cluster/examples/kubernetes/ceph/common.yaml')) as f:
        yamls = yaml.safe_load_all(f.read())
        for y in yamls:
            try:
                yield y
            except AttributeError:
                pass


def remove_duplicates(items):
    return OrderedDict.fromkeys(items).keys()


def main():
    #for crd in download_yaml():
    for crd in local():
        valid_crd = handle_crd(crd)
        if valid_crd is not None:
            with open(f'rook_ceph_client/{valid_crd.name.lower()}.py', 'w') as f:
                f.write(header)
                classes = remove_duplicates(cls.toplevel() for cls in valid_crd.flatten())
                f.write('\n\n\n'.join(classes))
                f.write('\n')

if __name__ == '__main__':
    main()
