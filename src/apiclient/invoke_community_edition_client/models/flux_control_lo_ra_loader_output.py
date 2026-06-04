from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.control_lo_ra_field import ControlLoRAField


T = TypeVar("T", bound="FluxControlLoRALoaderOutput")


@_attrs_define
class FluxControlLoRALoaderOutput:
    """Flux Control LoRA Loader Output

    Attributes:
        control_lora (ControlLoRAField):
        type_ (Literal['flux_control_lora_loader_output']):  Default: 'flux_control_lora_loader_output'.
    """

    control_lora: ControlLoRAField
    type_: Literal["flux_control_lora_loader_output"] = "flux_control_lora_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_lora = self.control_lora.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "control_lora": control_lora,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_lo_ra_field import ControlLoRAField

        d = dict(src_dict)
        control_lora = ControlLoRAField.from_dict(d.pop("control_lora"))

        type_ = cast(Literal["flux_control_lora_loader_output"], d.pop("type"))
        if type_ != "flux_control_lora_loader_output":
            raise ValueError(f"type must match const 'flux_control_lora_loader_output', got '{type_}'")

        flux_control_lo_ra_loader_output = cls(
            control_lora=control_lora,
            type_=type_,
        )

        flux_control_lo_ra_loader_output.additional_properties = d
        return flux_control_lo_ra_loader_output

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
