from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UninstallNodePackResponse")


@_attrs_define
class UninstallNodePackResponse:
    """Response after uninstalling a node pack.

    Attributes:
        name (str): The name of the uninstalled node pack.
        success (bool): Whether the uninstall was successful.
        message (str): Status message.
    """

    name: str
    success: bool
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        success = self.success

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "success": success,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        success = d.pop("success")

        message = d.pop("message")

        uninstall_node_pack_response = cls(
            name=name,
            success=success,
            message=message,
        )

        uninstall_node_pack_response.additional_properties = d
        return uninstall_node_pack_response

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
