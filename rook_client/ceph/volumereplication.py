"""
This file is automatically generated.
Do not modify.
"""

try:
    from typing import Any, Optional, Union, List
except ImportError:
    pass

from .._helper import _omit, CrdObject, CrdObjectList, CrdClass

class DataSource(CrdObject):
    _properties = [
        ('apiGroup', 'apiGroup', str, False, False),
        ('kind', 'kind', str, True, False),
        ('name', 'name', str, True, False)
    ]        

    def __init__(self,
                 kind,  # type: str
                 name,  # type: str
                 apiGroup=_omit,  # type: Optional[str]
                 ):
        super(DataSource, self).__init__(
            kind=kind,
            name=name,
            apiGroup=apiGroup,
        )

    @property
    def apiGroup(self):
        # type: () -> str
        return self._property_impl('apiGroup')
    
    @apiGroup.setter
    def apiGroup(self, new_val):
        # type: (Optional[str]) -> None
        self._apiGroup = new_val
    
    @property
    def kind(self):
        # type: () -> str
        return self._property_impl('kind')
    
    @kind.setter
    def kind(self, new_val):
        # type: (str) -> None
        self._kind = new_val
    
    @property
    def name(self):
        # type: () -> str
        return self._property_impl('name')
    
    @name.setter
    def name(self, new_val):
        # type: (str) -> None
        self._name = new_val


class Spec(CrdObject):
    _properties = [
        ('dataSource', 'dataSource', 'DataSource', True, False),
        ('replicationState', 'replicationState', str, True, False),
        ('volumeReplicationClass', 'volumeReplicationClass', str, True, False)
    ]        

    def __init__(self,
                 dataSource,  # type: DataSource
                 replicationState,  # type: str
                 volumeReplicationClass,  # type: str
                 ):
        super(Spec, self).__init__(
            dataSource=dataSource,
            replicationState=replicationState,
            volumeReplicationClass=volumeReplicationClass,
        )

    @property
    def dataSource(self):
        # type: () -> DataSource
        return self._property_impl('dataSource')
    
    @dataSource.setter
    def dataSource(self, new_val):
        # type: (DataSource) -> None
        self._dataSource = new_val
    
    @property
    def replicationState(self):
        # type: () -> str
        return self._property_impl('replicationState')
    
    @replicationState.setter
    def replicationState(self, new_val):
        # type: (str) -> None
        self._replicationState = new_val
    
    @property
    def volumeReplicationClass(self):
        # type: () -> str
        return self._property_impl('volumeReplicationClass')
    
    @volumeReplicationClass.setter
    def volumeReplicationClass(self, new_val):
        # type: (str) -> None
        self._volumeReplicationClass = new_val


class ConditionsItem(CrdObject):
    _properties = [
        ('lastTransitionTime', 'lastTransitionTime', str, True, False),
        ('message', 'message', str, True, False),
        ('observedGeneration', 'observedGeneration', int, False, False),
        ('reason', 'reason', str, True, False),
        ('status', 'status', str, True, False),
        ('type', 'type', str, True, False)
    ]        

    def __init__(self,
                 lastTransitionTime,  # type: str
                 message,  # type: str
                 reason,  # type: str
                 status,  # type: str
                 type,  # type: str
                 observedGeneration=_omit,  # type: Optional[int]
                 ):
        super(ConditionsItem, self).__init__(
            lastTransitionTime=lastTransitionTime,
            message=message,
            reason=reason,
            status=status,
            type=type,
            observedGeneration=observedGeneration,
        )

    @property
    def lastTransitionTime(self):
        # type: () -> str
        return self._property_impl('lastTransitionTime')
    
    @lastTransitionTime.setter
    def lastTransitionTime(self, new_val):
        # type: (str) -> None
        self._lastTransitionTime = new_val
    
    @property
    def message(self):
        # type: () -> str
        return self._property_impl('message')
    
    @message.setter
    def message(self, new_val):
        # type: (str) -> None
        self._message = new_val
    
    @property
    def observedGeneration(self):
        # type: () -> int
        return self._property_impl('observedGeneration')
    
    @observedGeneration.setter
    def observedGeneration(self, new_val):
        # type: (Optional[int]) -> None
        self._observedGeneration = new_val
    
    @property
    def reason(self):
        # type: () -> str
        return self._property_impl('reason')
    
    @reason.setter
    def reason(self, new_val):
        # type: (str) -> None
        self._reason = new_val
    
    @property
    def status(self):
        # type: () -> str
        return self._property_impl('status')
    
    @status.setter
    def status(self, new_val):
        # type: (str) -> None
        self._status = new_val
    
    @property
    def type(self):
        # type: () -> str
        return self._property_impl('type')
    
    @type.setter
    def type(self, new_val):
        # type: (str) -> None
        self._type = new_val


class ConditionsList(CrdObjectList):
    _items_type = ConditionsItem


class Status(CrdObject):
    _properties = [
        ('conditions', 'conditions', 'ConditionsList', False, False),
        ('lastCompletionTime', 'lastCompletionTime', str, False, False),
        ('lastStartTime', 'lastStartTime', str, False, False),
        ('message', 'message', str, False, False),
        ('observedGeneration', 'observedGeneration', int, False, False),
        ('state', 'state', str, False, False)
    ]        

    def __init__(self,
                 conditions=_omit,  # type: Optional[Union[List[ConditionsItem], CrdObjectList]]
                 lastCompletionTime=_omit,  # type: Optional[str]
                 lastStartTime=_omit,  # type: Optional[str]
                 message=_omit,  # type: Optional[str]
                 observedGeneration=_omit,  # type: Optional[int]
                 state=_omit,  # type: Optional[str]
                 ):
        super(Status, self).__init__(
            conditions=conditions,
            lastCompletionTime=lastCompletionTime,
            lastStartTime=lastStartTime,
            message=message,
            observedGeneration=observedGeneration,
            state=state,
        )

    @property
    def conditions(self):
        # type: () -> Union[List[ConditionsItem], CrdObjectList]
        return self._property_impl('conditions')
    
    @conditions.setter
    def conditions(self, new_val):
        # type: (Optional[Union[List[ConditionsItem], CrdObjectList]]) -> None
        self._conditions = new_val
    
    @property
    def lastCompletionTime(self):
        # type: () -> str
        return self._property_impl('lastCompletionTime')
    
    @lastCompletionTime.setter
    def lastCompletionTime(self, new_val):
        # type: (Optional[str]) -> None
        self._lastCompletionTime = new_val
    
    @property
    def lastStartTime(self):
        # type: () -> str
        return self._property_impl('lastStartTime')
    
    @lastStartTime.setter
    def lastStartTime(self, new_val):
        # type: (Optional[str]) -> None
        self._lastStartTime = new_val
    
    @property
    def message(self):
        # type: () -> str
        return self._property_impl('message')
    
    @message.setter
    def message(self, new_val):
        # type: (Optional[str]) -> None
        self._message = new_val
    
    @property
    def observedGeneration(self):
        # type: () -> int
        return self._property_impl('observedGeneration')
    
    @observedGeneration.setter
    def observedGeneration(self, new_val):
        # type: (Optional[int]) -> None
        self._observedGeneration = new_val
    
    @property
    def state(self):
        # type: () -> str
        return self._property_impl('state')
    
    @state.setter
    def state(self, new_val):
        # type: (Optional[str]) -> None
        self._state = new_val


class VolumeReplication(CrdClass):
    _properties = [
        ('apiVersion', 'apiVersion', str, False, False),
        ('kind', 'kind', str, False, False),
        ('metadata', 'metadata', object, False, False),
        ('spec', 'spec', 'Spec', True, False),
        ('status', 'status', 'Status', False, False)
    ]        

    def __init__(self,
                 spec,  # type: Spec
                 apiVersion=_omit,  # type: Optional[str]
                 kind=_omit,  # type: Optional[str]
                 metadata=_omit,  # type: Optional[Any]
                 status=_omit,  # type: Optional[Status]
                 ):
        super(VolumeReplication, self).__init__(
            spec=spec,
            apiVersion=apiVersion,
            kind=kind,
            metadata=metadata,
            status=status,
        )

    @property
    def apiVersion(self):
        # type: () -> str
        return self._property_impl('apiVersion')
    
    @apiVersion.setter
    def apiVersion(self, new_val):
        # type: (Optional[str]) -> None
        self._apiVersion = new_val
    
    @property
    def kind(self):
        # type: () -> str
        return self._property_impl('kind')
    
    @kind.setter
    def kind(self, new_val):
        # type: (Optional[str]) -> None
        self._kind = new_val
    
    @property
    def metadata(self):
        # type: () -> Any
        return self._property_impl('metadata')
    
    @metadata.setter
    def metadata(self, new_val):
        # type: (Optional[Any]) -> None
        self._metadata = new_val
    
    @property
    def spec(self):
        # type: () -> Spec
        return self._property_impl('spec')
    
    @spec.setter
    def spec(self, new_val):
        # type: (Spec) -> None
        self._spec = new_val
    
    @property
    def status(self):
        # type: () -> Status
        return self._property_impl('status')
    
    @status.setter
    def status(self, new_val):
        # type: (Optional[Status]) -> None
        self._status = new_val