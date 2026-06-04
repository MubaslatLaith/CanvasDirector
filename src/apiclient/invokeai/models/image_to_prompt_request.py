from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageToPromptRequest")


@_attrs_define
class ImageToPromptRequest:
    """
    Attributes:
        image_name (str):
        model_key (str):
        instruction (str | Unset):  Default: 'Describe this image in detail for use as an AI image generation prompt.'.
    """

    image_name: str
    model_key: str
    instruction: str | Unset = "Describe this image in detail for use as an AI image generation prompt."
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_name = self.image_name

        model_key = self.model_key

        instruction = self.instruction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_name": image_name,
                "model_key": model_key,
            }
        )
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_name = d.pop("image_name")

        model_key = d.pop("model_key")

        instruction = d.pop("instruction", UNSET)

        image_to_prompt_request = cls(
            image_name=image_name,
            model_key=model_key,
            instruction=instruction,
        )

        image_to_prompt_request.additional_properties = d
        return image_to_prompt_request

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
