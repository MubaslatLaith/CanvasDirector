from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalApiModelDefaultSettings")


@_attrs_define
class ExternalApiModelDefaultSettings:
    """
    Attributes:
        width (int | None | Unset):
        height (int | None | Unset):
        num_images (int | None | Unset):
    """

    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    num_images: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        num_images: int | None | Unset
        if isinstance(self.num_images, Unset):
            num_images = UNSET
        else:
            num_images = self.num_images

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if num_images is not UNSET:
            field_dict["num_images"] = num_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_num_images(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_images = _parse_num_images(d.pop("num_images", UNSET))

        external_api_model_default_settings = cls(
            width=width,
            height=height,
            num_images=num_images,
        )

        return external_api_model_default_settings
