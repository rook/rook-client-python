"""
This file is automatically generated.
Do not modify.
"""

try:
    from typing import Any, Optional, Union, List
except ImportError:
    pass

from .._helper import _omit, CrdObject, CrdObjectList, CrdClass

class Spec(CrdObject):
    _properties = [
        ('caps', 'caps', object, False, False)
    ]        

    def __init__(self,
                 caps=_omit,  # type: Optional[Any]
                 ):
        super(Spec, self).__init__(
            caps=caps,
        )

    @property
    def caps(self):
        # type: () -> Any
        return self._property_impl('caps')
    
    @caps.setter
    def caps(self, new_val):
        # type: (Optional[Any]) -> None
        self._caps = new_val


class CephClient(CrdClass):
    _properties = [
        ('apiVersion', 'apiVersion', str, True, False),
        ('metadata', 'metadata', object, True, False),
        ('status', 'status', object, False, False),
        ('spec', 'spec', Spec, True, False)
    ]        

    def __init__(self,
                 apiVersion,  # type: str
                 metadata,  # type: Any
                 spec,  # type: Spec
                 status=_omit,  # type: Optional[Any]
                 ):
        super(CephClient, self).__init__(
            apiVersion=apiVersion,
            metadata=metadata,
            spec=spec,
            status=status,
        )

    @property
    def apiVersion(self):
        # type: () -> str
        return self._property_impl('apiVersion')
    
    @apiVersion.setter
    def apiVersion(self, new_val):
        # type: (str) -> None
        self._apiVersion = new_val
    
    @property
    def metadata(self):
        # type: () -> Any
        return self._property_impl('metadata')
    
    @metadata.setter
    def metadata(self, new_val):
        # type: (Any) -> None
        self._metadata = new_val
    
    @property
    def status(self):
        # type: () -> Any
        return self._property_impl('status')
    
    @status.setter
    def status(self, new_val):
        # type: (Optional[Any]) -> None
        self._status = new_val
    
    @property
    def spec(self):
        # type: () -> Spec
        return self._property_impl('spec')
    
    @spec.setter
    def spec(self, new_val):
        # type: (Spec) -> None
        self._spec = new_val
