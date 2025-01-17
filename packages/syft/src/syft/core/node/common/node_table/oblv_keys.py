# relative
from .syft_object import SyftObject


class NoSQLOblvKeys(SyftObject):
    # version
    __canonical_name__ = "OblvKeys"
    __version__ = 1

    # fields
    public_key: bytes
    private_key: bytes

    # serde / storage rules
    __attr_state__ = ["public_key", "private_key"]
    __attr_searchable__ = []
    __attr_unique__ = ["private_key"]
