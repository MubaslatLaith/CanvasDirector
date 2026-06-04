from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.denoise_mask_field import DenoiseMaskField


T = TypeVar("T", bound="DenoiseMaskOutput")


@_attrs_define
class DenoiseMaskOutput:
    """Base class for nodes that output a single image

    Attributes:
        denoise_mask (DenoiseMaskField): An inpaint mask field
        type_ (Literal['denoise_mask_output']):  Default: 'denoise_mask_output'.
    """

    denoise_mask: DenoiseMaskField
    type_: Literal["denoise_mask_output"] = "denoise_mask_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denoise_mask = self.denoise_mask.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "denoise_mask": denoise_mask,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.denoise_mask_field import DenoiseMaskField

        d = dict(src_dict)
        denoise_mask = DenoiseMaskField.from_dict(d.pop("denoise_mask"))

        type_ = cast(Literal["denoise_mask_output"], d.pop("type"))
        if type_ != "denoise_mask_output":
            raise ValueError(f"type must match const 'denoise_mask_output', got '{type_}'")

        denoise_mask_output = cls(
            denoise_mask=denoise_mask,
            type_=type_,
        )

        denoise_mask_output.additional_properties = d
        return denoise_mask_output

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
