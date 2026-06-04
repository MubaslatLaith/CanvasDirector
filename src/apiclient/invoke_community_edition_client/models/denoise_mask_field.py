from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DenoiseMaskField")


@_attrs_define
class DenoiseMaskField:
    """An inpaint mask field

    Attributes:
        mask_name (str): The name of the mask image
        masked_latents_name (None | str | Unset): The name of the masked image latents
        gradient (bool | Unset): Used for gradient inpainting Default: False.
    """

    mask_name: str
    masked_latents_name: None | str | Unset = UNSET
    gradient: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mask_name = self.mask_name

        masked_latents_name: None | str | Unset
        if isinstance(self.masked_latents_name, Unset):
            masked_latents_name = UNSET
        else:
            masked_latents_name = self.masked_latents_name

        gradient = self.gradient

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mask_name": mask_name,
            }
        )
        if masked_latents_name is not UNSET:
            field_dict["masked_latents_name"] = masked_latents_name
        if gradient is not UNSET:
            field_dict["gradient"] = gradient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mask_name = d.pop("mask_name")

        def _parse_masked_latents_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        masked_latents_name = _parse_masked_latents_name(d.pop("masked_latents_name", UNSET))

        gradient = d.pop("gradient", UNSET)

        denoise_mask_field = cls(
            mask_name=mask_name,
            masked_latents_name=masked_latents_name,
            gradient=gradient,
        )

        denoise_mask_field.additional_properties = d
        return denoise_mask_field

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
