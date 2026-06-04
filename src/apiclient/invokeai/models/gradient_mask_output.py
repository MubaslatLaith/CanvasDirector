from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.denoise_mask_field import DenoiseMaskField
    from ..models.image_field import ImageField


T = TypeVar("T", bound="GradientMaskOutput")


@_attrs_define
class GradientMaskOutput:
    """Outputs a denoise mask and an image representing the total gradient of the mask.

    Attributes:
        denoise_mask (DenoiseMaskField): An inpaint mask field
        expanded_mask_area (ImageField): An image primitive field
        type_ (Literal['gradient_mask_output']):  Default: 'gradient_mask_output'.
    """

    denoise_mask: DenoiseMaskField
    expanded_mask_area: ImageField
    type_: Literal["gradient_mask_output"] = "gradient_mask_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denoise_mask = self.denoise_mask.to_dict()

        expanded_mask_area = self.expanded_mask_area.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "denoise_mask": denoise_mask,
                "expanded_mask_area": expanded_mask_area,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.image_field import ImageField

        d = dict(src_dict)
        denoise_mask = DenoiseMaskField.from_dict(d.pop("denoise_mask"))

        expanded_mask_area = ImageField.from_dict(d.pop("expanded_mask_area"))

        type_ = cast(Literal["gradient_mask_output"], d.pop("type"))
        if type_ != "gradient_mask_output":
            raise ValueError(f"type must match const 'gradient_mask_output', got '{type_}'")

        gradient_mask_output = cls(
            denoise_mask=denoise_mask,
            expanded_mask_area=expanded_mask_area,
            type_=type_,
        )

        gradient_mask_output.additional_properties = d
        return gradient_mask_output

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
