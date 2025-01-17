# future
from __future__ import annotations

# stdlib
from typing import List
from typing import Optional

# relative
from ..common.serde.serializable import serializable
from ..common.uid import UID
from .storeable_object import StorableObject


@serializable(recursive_serde=True)
class Dataset:
    __attr_allowlist__ = [
        "id",
        "data",
        "description",
        "tags",
        "search_permissions",
        "read_permissions",
    ]

    """
    Dataset is a wrapper over a collection of Serializable objects.

    Arguments:
        id (UID): the id at which to store the data.
        data (List[Serializable]): A list of serializable objects.
        description (Optional[str]): An optional string that describes what you are storing. Useful
        when searching.
        tags (Optional[List[str]]): An optional list of strings that are tags used at search.
        TODO: add docs about read_permission and search_permission

    Attributes:
        id (UID): the id at which to store the data.
        data (List[Serializable]): A list of serializable objects.
        description (Optional[str]): An optional string that describes what you are storing. Useful
        when searching.
        tags (Optional[List[str]]): An optional list of strings that are tags used at search.

    """

    def __init__(
        self,
        id: UID,
        data: List[StorableObject],
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        read_permissions: Optional[dict] = None,
        search_permissions: Optional[dict] = None,
    ):
        self.id = id
        self.data = data
        self._description: str = description if description else ""
        self._tags: List[str] = tags if tags else []

        # the dict key of "verify key" objects corresponding to people
        # the value is the original request_id to allow lookup later
        # who are allowed to call .get() and download this object.
        self.read_permissions = read_permissions if read_permissions else {}

        # the dict key of "verify key" objects corresponding to people
        # the value is the original request_id to allow lookup later
        # who are allowed to know that the tensor exists (via search or other means)
        self.search_permissions: dict = search_permissions if search_permissions else {}

    @property
    def tags(self) -> Optional[List[str]]:
        return self._tags

    @tags.setter
    def tags(self, value: Optional[List[str]]) -> None:
        self._tags = value if value else []

    @property
    def description(self) -> Optional[str]:
        return self._description

    @description.setter
    def description(self, description: Optional[str]) -> None:
        self._description = description if description else ""

    @property
    def class_name(self) -> str:
        return str(self.__class__.__name__)

    def __contains__(self, _id: UID) -> bool:
        return _id in [el.id for el in self.data]

    def keys(self) -> List[UID]:
        return [el.id for el in self.data]

    def __getitem__(self, _id: UID) -> List[StorableObject]:
        return [el for el in self.data if el.id == _id]

    def __delitem__(self, _id: UID) -> None:
        self.data = [el for el in self.data if el.id != _id]
