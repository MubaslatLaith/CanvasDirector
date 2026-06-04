from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.t2i_adapter_field import T2IAdapterField


T = TypeVar("T", bound="T2IAdapterOutput")


@_attrs_define
class T2IAdapterOutput:
    """
    Attributes:
        t2i_adapter (T2IAdapterField):
        type_ (Literal['t2i_adapter_output']):  Default: 't2i_adapter_output'.
    """

    t2i_adapter: T2IAdapterField
    type_: Literal["t2i_adapter_output"] = "t2i_adapter_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        t2i_adapter = self.t2i_adapter.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "t2i_adapter": t2i_adapter,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.t2i_adapter_field import T2IAdapterField

        d = dict(src_dict)
        t2i_adapter = T2IAdapterField.from_dict(d.pop("t2i_adapter"))

        type_ = cast(Literal["t2i_adapter_output"], d.pop("type"))
        if type_ != "t2i_adapter_output":
            raise ValueError(f"type must match const 't2i_adapter_output', got '{type_}'")

        t2i_adapter_output = cls(
            t2i_adapter=t2i_adapter,
            type_=type_,
        )

        t2i_adapter_output.additional_properties = d
        return t2i_adapter_output

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
