from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_pack_info import NodePackInfo


T = TypeVar("T", bound="NodePackListResponse")


@_attrs_define
class NodePackListResponse:
    """Response for listing installed node packs.

    Attributes:
        node_packs (list[NodePackInfo]): List of installed node packs.
        custom_nodes_path (str): The configured custom nodes directory path.
    """

    node_packs: list[NodePackInfo]
    custom_nodes_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_packs = []
        for node_packs_item_data in self.node_packs:
            node_packs_item = node_packs_item_data.to_dict()
            node_packs.append(node_packs_item)

        custom_nodes_path = self.custom_nodes_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_packs": node_packs,
                "custom_nodes_path": custom_nodes_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_pack_info import NodePackInfo

        d = dict(src_dict)
        node_packs = []
        _node_packs = d.pop("node_packs")
        for node_packs_item_data in _node_packs:
            node_packs_item = NodePackInfo.from_dict(node_packs_item_data)

            node_packs.append(node_packs_item)

        custom_nodes_path = d.pop("custom_nodes_path")

        node_pack_list_response = cls(
            node_packs=node_packs,
            custom_nodes_path=custom_nodes_path,
        )

        node_pack_list_response.additional_properties = d
        return node_pack_list_response

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
