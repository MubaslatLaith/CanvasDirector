from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.t2i_adapter_field import T2IAdapterField


T = TypeVar("T", bound="MDT2IAdapterListOutput")


@_attrs_define
class MDT2IAdapterListOutput:
    """
    Attributes:
        t2i_adapter_list (list[T2IAdapterField] | None | T2IAdapterField): T2I-Adapter(s) to apply
        type_ (Literal['md_ip_adapters_output']):  Default: 'md_ip_adapters_output'.
    """

    t2i_adapter_list: list[T2IAdapterField] | None | T2IAdapterField
    type_: Literal["md_ip_adapters_output"] = "md_ip_adapters_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.t2i_adapter_field import T2IAdapterField

        t2i_adapter_list: dict[str, Any] | list[dict[str, Any]] | None
        if isinstance(self.t2i_adapter_list, T2IAdapterField):
            t2i_adapter_list = self.t2i_adapter_list.to_dict()
        elif isinstance(self.t2i_adapter_list, list):
            t2i_adapter_list = []
            for t2i_adapter_list_type_1_item_data in self.t2i_adapter_list:
                t2i_adapter_list_type_1_item = t2i_adapter_list_type_1_item_data.to_dict()
                t2i_adapter_list.append(t2i_adapter_list_type_1_item)

        else:
            t2i_adapter_list = self.t2i_adapter_list

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "t2i_adapter_list": t2i_adapter_list,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.t2i_adapter_field import T2IAdapterField

        d = dict(src_dict)

        def _parse_t2i_adapter_list(data: object) -> list[T2IAdapterField] | None | T2IAdapterField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                t2i_adapter_list_type_0 = T2IAdapterField.from_dict(data)

                return t2i_adapter_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                t2i_adapter_list_type_1 = []
                _t2i_adapter_list_type_1 = data
                for t2i_adapter_list_type_1_item_data in _t2i_adapter_list_type_1:
                    t2i_adapter_list_type_1_item = T2IAdapterField.from_dict(t2i_adapter_list_type_1_item_data)

                    t2i_adapter_list_type_1.append(t2i_adapter_list_type_1_item)

                return t2i_adapter_list_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[T2IAdapterField] | None | T2IAdapterField, data)

        t2i_adapter_list = _parse_t2i_adapter_list(d.pop("t2i_adapter_list"))

        type_ = cast(Literal["md_ip_adapters_output"], d.pop("type"))
        if type_ != "md_ip_adapters_output":
            raise ValueError(f"type must match const 'md_ip_adapters_output', got '{type_}'")

        mdt2i_adapter_list_output = cls(
            t2i_adapter_list=t2i_adapter_list,
            type_=type_,
        )

        mdt2i_adapter_list_output.additional_properties = d
        return mdt2i_adapter_list_output

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
