"""
This file is automatically generated.
Do not modify.
"""

try:
    from typing import Any, Optional, Union, List
except ImportError:
    pass

from .._helper import _omit, CrdObject, CrdObjectList, CrdClass

class ErasureCoded(CrdObject):
    _properties = [
        ('algorithm', 'algorithm', str, False, False),
        ('codingChunks', 'codingChunks', int, True, False),
        ('dataChunks', 'dataChunks', int, True, False)
    ]        

    def __init__(self,
                 codingChunks,  # type: int
                 dataChunks,  # type: int
                 algorithm=_omit,  # type: Optional[str]
                 ):
        super(ErasureCoded, self).__init__(
            codingChunks=codingChunks,
            dataChunks=dataChunks,
            algorithm=algorithm,
        )

    @property
    def algorithm(self):
        # type: () -> str
        return self._property_impl('algorithm')
    
    @algorithm.setter
    def algorithm(self, new_val):
        # type: (Optional[str]) -> None
        self._algorithm = new_val
    
    @property
    def codingChunks(self):
        # type: () -> int
        return self._property_impl('codingChunks')
    
    @codingChunks.setter
    def codingChunks(self, new_val):
        # type: (int) -> None
        self._codingChunks = new_val
    
    @property
    def dataChunks(self):
        # type: () -> int
        return self._property_impl('dataChunks')
    
    @dataChunks.setter
    def dataChunks(self, new_val):
        # type: (int) -> None
        self._dataChunks = new_val


class SnapshotSchedulesItem(CrdObject):
    _properties = [
        ('interval', 'interval', str, False, False),
        ('startTime', 'startTime', str, False, False)
    ]        

    def __init__(self,
                 interval=_omit,  # type: Optional[str]
                 startTime=_omit,  # type: Optional[str]
                 ):
        super(SnapshotSchedulesItem, self).__init__(
            interval=interval,
            startTime=startTime,
        )

    @property
    def interval(self):
        # type: () -> str
        return self._property_impl('interval')
    
    @interval.setter
    def interval(self, new_val):
        # type: (Optional[str]) -> None
        self._interval = new_val
    
    @property
    def startTime(self):
        # type: () -> str
        return self._property_impl('startTime')
    
    @startTime.setter
    def startTime(self, new_val):
        # type: (Optional[str]) -> None
        self._startTime = new_val


class SnapshotSchedulesList(CrdObjectList):
    _items_type = SnapshotSchedulesItem


class Mirroring(CrdObject):
    _properties = [
        ('enabled', 'enabled', bool, False, False),
        ('mode', 'mode', str, False, False),
        ('snapshotSchedules', 'snapshotSchedules', 'SnapshotSchedulesList', False, False)
    ]        

    def __init__(self,
                 enabled=_omit,  # type: Optional[bool]
                 mode=_omit,  # type: Optional[str]
                 snapshotSchedules=_omit,  # type: Optional[Union[List[SnapshotSchedulesItem], CrdObjectList]]
                 ):
        super(Mirroring, self).__init__(
            enabled=enabled,
            mode=mode,
            snapshotSchedules=snapshotSchedules,
        )

    @property
    def enabled(self):
        # type: () -> bool
        return self._property_impl('enabled')
    
    @enabled.setter
    def enabled(self, new_val):
        # type: (Optional[bool]) -> None
        self._enabled = new_val
    
    @property
    def mode(self):
        # type: () -> str
        return self._property_impl('mode')
    
    @mode.setter
    def mode(self, new_val):
        # type: (Optional[str]) -> None
        self._mode = new_val
    
    @property
    def snapshotSchedules(self):
        # type: () -> Union[List[SnapshotSchedulesItem], CrdObjectList]
        return self._property_impl('snapshotSchedules')
    
    @snapshotSchedules.setter
    def snapshotSchedules(self, new_val):
        # type: (Optional[Union[List[SnapshotSchedulesItem], CrdObjectList]]) -> None
        self._snapshotSchedules = new_val


class Quotas(CrdObject):
    _properties = [
        ('maxBytes', 'maxBytes', int, False, False),
        ('maxObjects', 'maxObjects', int, False, False),
        ('maxSize', 'maxSize', str, False, False)
    ]        

    def __init__(self,
                 maxBytes=_omit,  # type: Optional[int]
                 maxObjects=_omit,  # type: Optional[int]
                 maxSize=_omit,  # type: Optional[str]
                 ):
        super(Quotas, self).__init__(
            maxBytes=maxBytes,
            maxObjects=maxObjects,
            maxSize=maxSize,
        )

    @property
    def maxBytes(self):
        # type: () -> int
        return self._property_impl('maxBytes')
    
    @maxBytes.setter
    def maxBytes(self, new_val):
        # type: (Optional[int]) -> None
        self._maxBytes = new_val
    
    @property
    def maxObjects(self):
        # type: () -> int
        return self._property_impl('maxObjects')
    
    @maxObjects.setter
    def maxObjects(self, new_val):
        # type: (Optional[int]) -> None
        self._maxObjects = new_val
    
    @property
    def maxSize(self):
        # type: () -> str
        return self._property_impl('maxSize')
    
    @maxSize.setter
    def maxSize(self, new_val):
        # type: (Optional[str]) -> None
        self._maxSize = new_val


class Replicated(CrdObject):
    _properties = [
        ('replicasPerFailureDomain', 'replicasPerFailureDomain', int, False, False),
        ('requireSafeReplicaSize', 'requireSafeReplicaSize', bool, False, False),
        ('size', 'size', int, True, False),
        ('subFailureDomain', 'subFailureDomain', str, False, False),
        ('targetSizeRatio', 'targetSizeRatio', float, False, False)
    ]        

    def __init__(self,
                 size,  # type: int
                 replicasPerFailureDomain=_omit,  # type: Optional[int]
                 requireSafeReplicaSize=_omit,  # type: Optional[bool]
                 subFailureDomain=_omit,  # type: Optional[str]
                 targetSizeRatio=_omit,  # type: Optional[float]
                 ):
        super(Replicated, self).__init__(
            size=size,
            replicasPerFailureDomain=replicasPerFailureDomain,
            requireSafeReplicaSize=requireSafeReplicaSize,
            subFailureDomain=subFailureDomain,
            targetSizeRatio=targetSizeRatio,
        )

    @property
    def replicasPerFailureDomain(self):
        # type: () -> int
        return self._property_impl('replicasPerFailureDomain')
    
    @replicasPerFailureDomain.setter
    def replicasPerFailureDomain(self, new_val):
        # type: (Optional[int]) -> None
        self._replicasPerFailureDomain = new_val
    
    @property
    def requireSafeReplicaSize(self):
        # type: () -> bool
        return self._property_impl('requireSafeReplicaSize')
    
    @requireSafeReplicaSize.setter
    def requireSafeReplicaSize(self, new_val):
        # type: (Optional[bool]) -> None
        self._requireSafeReplicaSize = new_val
    
    @property
    def size(self):
        # type: () -> int
        return self._property_impl('size')
    
    @size.setter
    def size(self, new_val):
        # type: (int) -> None
        self._size = new_val
    
    @property
    def subFailureDomain(self):
        # type: () -> str
        return self._property_impl('subFailureDomain')
    
    @subFailureDomain.setter
    def subFailureDomain(self, new_val):
        # type: (Optional[str]) -> None
        self._subFailureDomain = new_val
    
    @property
    def targetSizeRatio(self):
        # type: () -> float
        return self._property_impl('targetSizeRatio')
    
    @targetSizeRatio.setter
    def targetSizeRatio(self, new_val):
        # type: (Optional[float]) -> None
        self._targetSizeRatio = new_val


class Mirror(CrdObject):
    _properties = [
        ('disabled', 'disabled', bool, False, False),
        ('interval', 'interval', str, False, False),
        ('timeout', 'timeout', str, False, False)
    ]        

    def __init__(self,
                 disabled=_omit,  # type: Optional[bool]
                 interval=_omit,  # type: Optional[str]
                 timeout=_omit,  # type: Optional[str]
                 ):
        super(Mirror, self).__init__(
            disabled=disabled,
            interval=interval,
            timeout=timeout,
        )

    @property
    def disabled(self):
        # type: () -> bool
        return self._property_impl('disabled')
    
    @disabled.setter
    def disabled(self, new_val):
        # type: (Optional[bool]) -> None
        self._disabled = new_val
    
    @property
    def interval(self):
        # type: () -> str
        return self._property_impl('interval')
    
    @interval.setter
    def interval(self, new_val):
        # type: (Optional[str]) -> None
        self._interval = new_val
    
    @property
    def timeout(self):
        # type: () -> str
        return self._property_impl('timeout')
    
    @timeout.setter
    def timeout(self, new_val):
        # type: (Optional[str]) -> None
        self._timeout = new_val


class StatusCheck(CrdObject):
    _properties = [
        ('mirror', 'mirror', 'Mirror', False, True)
    ]        

    def __init__(self,
                 mirror=_omit,  # type: Optional[Mirror]
                 ):
        super(StatusCheck, self).__init__(
            mirror=mirror,
        )

    @property
    def mirror(self):
        # type: () -> Optional[Mirror]
        return self._property_impl('mirror')
    
    @mirror.setter
    def mirror(self, new_val):
        # type: (Optional[Mirror]) -> None
        self._mirror = new_val


class DataPool(CrdObject):
    _properties = [
        ('compressionMode', 'compressionMode', str, False, True),
        ('crushRoot', 'crushRoot', str, False, True),
        ('deviceClass', 'deviceClass', str, False, True),
        ('enableRBDStats', 'enableRBDStats', bool, False, False),
        ('erasureCoded', 'erasureCoded', 'ErasureCoded', False, False),
        ('failureDomain', 'failureDomain', str, False, False),
        ('mirroring', 'mirroring', 'Mirroring', False, False),
        ('parameters', 'parameters', object, False, True),
        ('quotas', 'quotas', 'Quotas', False, True),
        ('replicated', 'replicated', 'Replicated', False, False),
        ('statusCheck', 'statusCheck', 'StatusCheck', False, False)
    ]        

    def __init__(self,
                 compressionMode=_omit,  # type: Optional[str]
                 crushRoot=_omit,  # type: Optional[str]
                 deviceClass=_omit,  # type: Optional[str]
                 enableRBDStats=_omit,  # type: Optional[bool]
                 erasureCoded=_omit,  # type: Optional[ErasureCoded]
                 failureDomain=_omit,  # type: Optional[str]
                 mirroring=_omit,  # type: Optional[Mirroring]
                 parameters=_omit,  # type: Optional[Any]
                 quotas=_omit,  # type: Optional[Quotas]
                 replicated=_omit,  # type: Optional[Replicated]
                 statusCheck=_omit,  # type: Optional[StatusCheck]
                 ):
        super(DataPool, self).__init__(
            compressionMode=compressionMode,
            crushRoot=crushRoot,
            deviceClass=deviceClass,
            enableRBDStats=enableRBDStats,
            erasureCoded=erasureCoded,
            failureDomain=failureDomain,
            mirroring=mirroring,
            parameters=parameters,
            quotas=quotas,
            replicated=replicated,
            statusCheck=statusCheck,
        )

    @property
    def compressionMode(self):
        # type: () -> Optional[str]
        return self._property_impl('compressionMode')
    
    @compressionMode.setter
    def compressionMode(self, new_val):
        # type: (Optional[str]) -> None
        self._compressionMode = new_val
    
    @property
    def crushRoot(self):
        # type: () -> Optional[str]
        return self._property_impl('crushRoot')
    
    @crushRoot.setter
    def crushRoot(self, new_val):
        # type: (Optional[str]) -> None
        self._crushRoot = new_val
    
    @property
    def deviceClass(self):
        # type: () -> Optional[str]
        return self._property_impl('deviceClass')
    
    @deviceClass.setter
    def deviceClass(self, new_val):
        # type: (Optional[str]) -> None
        self._deviceClass = new_val
    
    @property
    def enableRBDStats(self):
        # type: () -> bool
        return self._property_impl('enableRBDStats')
    
    @enableRBDStats.setter
    def enableRBDStats(self, new_val):
        # type: (Optional[bool]) -> None
        self._enableRBDStats = new_val
    
    @property
    def erasureCoded(self):
        # type: () -> ErasureCoded
        return self._property_impl('erasureCoded')
    
    @erasureCoded.setter
    def erasureCoded(self, new_val):
        # type: (Optional[ErasureCoded]) -> None
        self._erasureCoded = new_val
    
    @property
    def failureDomain(self):
        # type: () -> str
        return self._property_impl('failureDomain')
    
    @failureDomain.setter
    def failureDomain(self, new_val):
        # type: (Optional[str]) -> None
        self._failureDomain = new_val
    
    @property
    def mirroring(self):
        # type: () -> Mirroring
        return self._property_impl('mirroring')
    
    @mirroring.setter
    def mirroring(self, new_val):
        # type: (Optional[Mirroring]) -> None
        self._mirroring = new_val
    
    @property
    def parameters(self):
        # type: () -> Optional[Any]
        return self._property_impl('parameters')
    
    @parameters.setter
    def parameters(self, new_val):
        # type: (Optional[Any]) -> None
        self._parameters = new_val
    
    @property
    def quotas(self):
        # type: () -> Optional[Quotas]
        return self._property_impl('quotas')
    
    @quotas.setter
    def quotas(self, new_val):
        # type: (Optional[Quotas]) -> None
        self._quotas = new_val
    
    @property
    def replicated(self):
        # type: () -> Replicated
        return self._property_impl('replicated')
    
    @replicated.setter
    def replicated(self, new_val):
        # type: (Optional[Replicated]) -> None
        self._replicated = new_val
    
    @property
    def statusCheck(self):
        # type: () -> StatusCheck
        return self._property_impl('statusCheck')
    
    @statusCheck.setter
    def statusCheck(self, new_val):
        # type: (Optional[StatusCheck]) -> None
        self._statusCheck = new_val


class MetadataPool(CrdObject):
    _properties = [
        ('compressionMode', 'compressionMode', str, False, True),
        ('crushRoot', 'crushRoot', str, False, True),
        ('deviceClass', 'deviceClass', str, False, True),
        ('enableRBDStats', 'enableRBDStats', bool, False, False),
        ('erasureCoded', 'erasureCoded', 'ErasureCoded', False, False),
        ('failureDomain', 'failureDomain', str, False, False),
        ('mirroring', 'mirroring', 'Mirroring', False, False),
        ('parameters', 'parameters', object, False, True),
        ('quotas', 'quotas', 'Quotas', False, True),
        ('replicated', 'replicated', 'Replicated', False, False),
        ('statusCheck', 'statusCheck', 'StatusCheck', False, False)
    ]        

    def __init__(self,
                 compressionMode=_omit,  # type: Optional[str]
                 crushRoot=_omit,  # type: Optional[str]
                 deviceClass=_omit,  # type: Optional[str]
                 enableRBDStats=_omit,  # type: Optional[bool]
                 erasureCoded=_omit,  # type: Optional[ErasureCoded]
                 failureDomain=_omit,  # type: Optional[str]
                 mirroring=_omit,  # type: Optional[Mirroring]
                 parameters=_omit,  # type: Optional[Any]
                 quotas=_omit,  # type: Optional[Quotas]
                 replicated=_omit,  # type: Optional[Replicated]
                 statusCheck=_omit,  # type: Optional[StatusCheck]
                 ):
        super(MetadataPool, self).__init__(
            compressionMode=compressionMode,
            crushRoot=crushRoot,
            deviceClass=deviceClass,
            enableRBDStats=enableRBDStats,
            erasureCoded=erasureCoded,
            failureDomain=failureDomain,
            mirroring=mirroring,
            parameters=parameters,
            quotas=quotas,
            replicated=replicated,
            statusCheck=statusCheck,
        )

    @property
    def compressionMode(self):
        # type: () -> Optional[str]
        return self._property_impl('compressionMode')
    
    @compressionMode.setter
    def compressionMode(self, new_val):
        # type: (Optional[str]) -> None
        self._compressionMode = new_val
    
    @property
    def crushRoot(self):
        # type: () -> Optional[str]
        return self._property_impl('crushRoot')
    
    @crushRoot.setter
    def crushRoot(self, new_val):
        # type: (Optional[str]) -> None
        self._crushRoot = new_val
    
    @property
    def deviceClass(self):
        # type: () -> Optional[str]
        return self._property_impl('deviceClass')
    
    @deviceClass.setter
    def deviceClass(self, new_val):
        # type: (Optional[str]) -> None
        self._deviceClass = new_val
    
    @property
    def enableRBDStats(self):
        # type: () -> bool
        return self._property_impl('enableRBDStats')
    
    @enableRBDStats.setter
    def enableRBDStats(self, new_val):
        # type: (Optional[bool]) -> None
        self._enableRBDStats = new_val
    
    @property
    def erasureCoded(self):
        # type: () -> ErasureCoded
        return self._property_impl('erasureCoded')
    
    @erasureCoded.setter
    def erasureCoded(self, new_val):
        # type: (Optional[ErasureCoded]) -> None
        self._erasureCoded = new_val
    
    @property
    def failureDomain(self):
        # type: () -> str
        return self._property_impl('failureDomain')
    
    @failureDomain.setter
    def failureDomain(self, new_val):
        # type: (Optional[str]) -> None
        self._failureDomain = new_val
    
    @property
    def mirroring(self):
        # type: () -> Mirroring
        return self._property_impl('mirroring')
    
    @mirroring.setter
    def mirroring(self, new_val):
        # type: (Optional[Mirroring]) -> None
        self._mirroring = new_val
    
    @property
    def parameters(self):
        # type: () -> Optional[Any]
        return self._property_impl('parameters')
    
    @parameters.setter
    def parameters(self, new_val):
        # type: (Optional[Any]) -> None
        self._parameters = new_val
    
    @property
    def quotas(self):
        # type: () -> Optional[Quotas]
        return self._property_impl('quotas')
    
    @quotas.setter
    def quotas(self, new_val):
        # type: (Optional[Quotas]) -> None
        self._quotas = new_val
    
    @property
    def replicated(self):
        # type: () -> Replicated
        return self._property_impl('replicated')
    
    @replicated.setter
    def replicated(self, new_val):
        # type: (Optional[Replicated]) -> None
        self._replicated = new_val
    
    @property
    def statusCheck(self):
        # type: () -> StatusCheck
        return self._property_impl('statusCheck')
    
    @statusCheck.setter
    def statusCheck(self, new_val):
        # type: (Optional[StatusCheck]) -> None
        self._statusCheck = new_val


class Spec(CrdObject):
    _properties = [
        ('dataPool', 'dataPool', 'DataPool', True, True),
        ('metadataPool', 'metadataPool', 'MetadataPool', True, True),
        ('zoneGroup', 'zoneGroup', str, True, False)
    ]        

    def __init__(self,
                 dataPool,  # type: Optional[DataPool]
                 metadataPool,  # type: Optional[MetadataPool]
                 zoneGroup,  # type: str
                 ):
        super(Spec, self).__init__(
            dataPool=dataPool,
            metadataPool=metadataPool,
            zoneGroup=zoneGroup,
        )

    @property
    def dataPool(self):
        # type: () -> Optional[DataPool]
        return self._property_impl('dataPool')
    
    @dataPool.setter
    def dataPool(self, new_val):
        # type: (Optional[DataPool]) -> None
        self._dataPool = new_val
    
    @property
    def metadataPool(self):
        # type: () -> Optional[MetadataPool]
        return self._property_impl('metadataPool')
    
    @metadataPool.setter
    def metadataPool(self, new_val):
        # type: (Optional[MetadataPool]) -> None
        self._metadataPool = new_val
    
    @property
    def zoneGroup(self):
        # type: () -> str
        return self._property_impl('zoneGroup')
    
    @zoneGroup.setter
    def zoneGroup(self, new_val):
        # type: (str) -> None
        self._zoneGroup = new_val


class Status(CrdObject):
    _properties = [
        ('phase', 'phase', str, False, False)
    ]        

    def __init__(self,
                 phase=_omit,  # type: Optional[str]
                 ):
        super(Status, self).__init__(
            phase=phase,
        )

    @property
    def phase(self):
        # type: () -> str
        return self._property_impl('phase')
    
    @phase.setter
    def phase(self, new_val):
        # type: (Optional[str]) -> None
        self._phase = new_val


class CephObjectZone(CrdClass):
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
        super(CephObjectZone, self).__init__(
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