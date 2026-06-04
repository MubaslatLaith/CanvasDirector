from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExternalResolutionPreset")


@_attrs_define
class ExternalResolutionPreset:
    """
    Attributes:
        label (str): Display label, e.g. '1:1 (1K)'
        aspect_ratio (str): Aspect ratio string, e.g. '1:1'
        image_size (str): Image size preset, e.g. '1K'
        width (int):
        height (int):
    """

    label: str
    aspect_ratio: str
    image_size: str
    width: int
    height: int

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        aspect_ratio = self.aspect_ratio

        image_size = self.image_size

        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "label": label,
                "aspect_ratio": aspect_ratio,
                "image_size": image_size,
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        aspect_ratio = d.pop("aspect_ratio")

        image_size = d.pop("image_size")

        width = d.pop("width")

        height = d.pop("height")

        external_resolution_preset = cls(
            label=label,
            aspect_ratio=aspect_ratio,
            image_size=image_size,
            width=width,
            height=height,
        )

        return external_resolution_preset
