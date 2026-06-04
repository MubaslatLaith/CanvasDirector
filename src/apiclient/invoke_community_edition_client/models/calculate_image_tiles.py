from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalculateImageTiles")


@_attrs_define
class CalculateImageTiles:
    """Calculate the coordinates and overlaps of tiles that cover a target image shape.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['calculate_image_tiles']):  Default: 'calculate_image_tiles'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image_width (int | Unset): The image width, in pixels, to calculate tiles for. Default: 1024.
        image_height (int | Unset): The image height, in pixels, to calculate tiles for. Default: 1024.
        tile_width (int | Unset): The tile width, in pixels. Default: 576.
        tile_height (int | Unset): The tile height, in pixels. Default: 576.
        overlap (int | Unset): The target overlap, in pixels, between adjacent tiles. Adjacent tiles will overlap by at
            least this amount Default: 128.
    """

    id: str
    type_: Literal["calculate_image_tiles"] = "calculate_image_tiles"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image_width: int | Unset = 1024
    image_height: int | Unset = 1024
    tile_width: int | Unset = 576
    tile_height: int | Unset = 576
    overlap: int | Unset = 128
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        image_width = self.image_width

        image_height = self.image_height

        tile_width = self.tile_width

        tile_height = self.tile_height

        overlap = self.overlap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if image_width is not UNSET:
            field_dict["image_width"] = image_width
        if image_height is not UNSET:
            field_dict["image_height"] = image_height
        if tile_width is not UNSET:
            field_dict["tile_width"] = tile_width
        if tile_height is not UNSET:
            field_dict["tile_height"] = tile_height
        if overlap is not UNSET:
            field_dict["overlap"] = overlap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["calculate_image_tiles"], d.pop("type"))
        if type_ != "calculate_image_tiles":
            raise ValueError(f"type must match const 'calculate_image_tiles', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        image_width = d.pop("image_width", UNSET)

        image_height = d.pop("image_height", UNSET)

        tile_width = d.pop("tile_width", UNSET)

        tile_height = d.pop("tile_height", UNSET)

        overlap = d.pop("overlap", UNSET)

        calculate_image_tiles = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image_width=image_width,
            image_height=image_height,
            tile_width=tile_width,
            tile_height=tile_height,
            overlap=overlap,
        )

        calculate_image_tiles.additional_properties = d
        return calculate_image_tiles

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
