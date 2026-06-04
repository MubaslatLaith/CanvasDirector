from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_adapter_field import IPAdapterField


T = TypeVar("T", bound="IPAdapterOutput")


@_attrs_define
class IPAdapterOutput:
    """
    Attributes:
        ip_adapter (IPAdapterField):
        type_ (Literal['ip_adapter_output']):  Default: 'ip_adapter_output'.
    """

    ip_adapter: IPAdapterField
    type_: Literal["ip_adapter_output"] = "ip_adapter_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_adapter = self.ip_adapter.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_adapter": ip_adapter,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_adapter_field import IPAdapterField

        d = dict(src_dict)
        ip_adapter = IPAdapterField.from_dict(d.pop("ip_adapter"))

        type_ = cast(Literal["ip_adapter_output"], d.pop("type"))
        if type_ != "ip_adapter_output":
            raise ValueError(f"type must match const 'ip_adapter_output', got '{type_}'")

        ip_adapter_output = cls(
            ip_adapter=ip_adapter,
            type_=type_,
        )

        ip_adapter_output.additional_properties = d
        return ip_adapter_output

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
