from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flux_control_net_field import FluxControlNetField


T = TypeVar("T", bound="FluxControlNetOutput")


@_attrs_define
class FluxControlNetOutput:
    """FLUX ControlNet info

    Attributes:
        control (FluxControlNetField):
        type_ (Literal['flux_controlnet_output']):  Default: 'flux_controlnet_output'.
    """

    control: FluxControlNetField
    type_: Literal["flux_controlnet_output"] = "flux_controlnet_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control = self.control.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "control": control,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flux_control_net_field import FluxControlNetField

        d = dict(src_dict)
        control = FluxControlNetField.from_dict(d.pop("control"))

        type_ = cast(Literal["flux_controlnet_output"], d.pop("type"))
        if type_ != "flux_controlnet_output":
            raise ValueError(f"type must match const 'flux_controlnet_output', got '{type_}'")

        flux_control_net_output = cls(
            control=control,
            type_=type_,
        )

        flux_control_net_output.additional_properties = d
        return flux_control_net_output

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
