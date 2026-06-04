from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_adapter_field import IPAdapterField


T = TypeVar("T", bound="MDIPAdapterListOutput")


@_attrs_define
class MDIPAdapterListOutput:
    """
    Attributes:
        ip_adapter_list (IPAdapterField | list[IPAdapterField] | None): IP-Adapter to apply
        type_ (Literal['md_ip_adapter_list_output']):  Default: 'md_ip_adapter_list_output'.
    """

    ip_adapter_list: IPAdapterField | list[IPAdapterField] | None
    type_: Literal["md_ip_adapter_list_output"] = "md_ip_adapter_list_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ip_adapter_field import IPAdapterField

        ip_adapter_list: dict[str, Any] | list[dict[str, Any]] | None
        if isinstance(self.ip_adapter_list, IPAdapterField):
            ip_adapter_list = self.ip_adapter_list.to_dict()
        elif isinstance(self.ip_adapter_list, list):
            ip_adapter_list = []
            for ip_adapter_list_type_1_item_data in self.ip_adapter_list:
                ip_adapter_list_type_1_item = ip_adapter_list_type_1_item_data.to_dict()
                ip_adapter_list.append(ip_adapter_list_type_1_item)

        else:
            ip_adapter_list = self.ip_adapter_list

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_adapter_list": ip_adapter_list,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_adapter_field import IPAdapterField

        d = dict(src_dict)

        def _parse_ip_adapter_list(data: object) -> IPAdapterField | list[IPAdapterField] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ip_adapter_list_type_0 = IPAdapterField.from_dict(data)

                return ip_adapter_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_adapter_list_type_1 = []
                _ip_adapter_list_type_1 = data
                for ip_adapter_list_type_1_item_data in _ip_adapter_list_type_1:
                    ip_adapter_list_type_1_item = IPAdapterField.from_dict(ip_adapter_list_type_1_item_data)

                    ip_adapter_list_type_1.append(ip_adapter_list_type_1_item)

                return ip_adapter_list_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAdapterField | list[IPAdapterField] | None, data)

        ip_adapter_list = _parse_ip_adapter_list(d.pop("ip_adapter_list"))

        type_ = cast(Literal["md_ip_adapter_list_output"], d.pop("type"))
        if type_ != "md_ip_adapter_list_output":
            raise ValueError(f"type must match const 'md_ip_adapter_list_output', got '{type_}'")

        mdip_adapter_list_output = cls(
            ip_adapter_list=ip_adapter_list,
            type_=type_,
        )

        mdip_adapter_list_output.additional_properties = d
        return mdip_adapter_list_output

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
