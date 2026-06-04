from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PresetData")


@_attrs_define
class PresetData:
    """
    Attributes:
        positive_prompt (str): Positive prompt
        negative_prompt (str): Negative prompt
    """

    positive_prompt: str
    negative_prompt: str

    def to_dict(self) -> dict[str, Any]:
        positive_prompt = self.positive_prompt

        negative_prompt = self.negative_prompt

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "positive_prompt": positive_prompt,
                "negative_prompt": negative_prompt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        positive_prompt = d.pop("positive_prompt")

        negative_prompt = d.pop("negative_prompt")

        preset_data = cls(
            positive_prompt=positive_prompt,
            negative_prompt=negative_prompt,
        )

        return preset_data
