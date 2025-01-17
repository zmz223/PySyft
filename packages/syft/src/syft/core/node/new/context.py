# stdlib
from typing import Optional

# relative
from ..common.node_table.syft_object import SyftBaseObject
from .credentials import SyftVerifyKey
from .node import NewNode


class NodeServiceContext(SyftBaseObject):
    __canonical_name__ = "NodeServiceContext"
    __version__ = 1
    node: Optional[NewNode]


class AuthedServiceContext(NodeServiceContext):
    __canonical_name__ = "AuthedServiceContext"
    __version__ = 1

    credentials: SyftVerifyKey
