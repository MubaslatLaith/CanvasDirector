from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lo_ra_field import LoRAField


T = TypeVar("T", bound="LoRASelectorOutput")


@_attrs_define
class LoRASelectorOutput:
    """Model loader output

    Attributes:
        lora (LoRAField):
        type_ (Literal['lora_selector_output']):  Default: 'lora_selector_output'.
    """

    lora: LoRAField
    type_: Literal["lora_selector_output"] = "lora_selector_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lora = self.lora.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lora": lora,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lo_ra_field import LoRAField

        d = dict(src_dict)
        lora = LoRAField.from_dict(d.pop("lora"))

        type_ = cast(Literal["lora_selector_output"], d.pop("type"))
        if type_ != "lora_selector_output":
            raise ValueError(f"type must match const 'lora_selector_output', got '{type_}'")

        lo_ra_selector_output = cls(
            lora=lora,
            type_=type_,
        )

        lo_ra_selector_output.additional_properties = d
        return lo_ra_selector_output

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
