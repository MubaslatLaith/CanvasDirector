from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NodePackInfo")


@_attrs_define
class NodePackInfo:
    """Information about an installed node pack.

    Attributes:
        name (str): The name of the node pack.
        path (str): The path to the node pack directory.
        node_count (int): The number of nodes in the pack.
        node_types (list[str]): The invocation types provided by this node pack.
    """

    name: str
    path: str
    node_count: int
    node_types: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        node_count = self.node_count

        node_types = self.node_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
                "node_count": node_count,
                "node_types": node_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        node_count = d.pop("node_count")

        node_types = cast(list[str], d.pop("node_types"))

        node_pack_info = cls(
            name=name,
            path=path,
            node_count=node_count,
            node_types=node_types,
        )

        node_pack_info.additional_properties = d
        return node_pack_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
