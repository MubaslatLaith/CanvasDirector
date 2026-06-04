from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TileToPropertiesOutput")


@_attrs_define
class TileToPropertiesOutput:
    """
    Attributes:
        coords_left (int): Left coordinate of the tile relative to its parent image.
        coords_right (int): Right coordinate of the tile relative to its parent image.
        coords_top (int): Top coordinate of the tile relative to its parent image.
        coords_bottom (int): Bottom coordinate of the tile relative to its parent image.
        width (int): The width of the tile. Equal to coords_right - coords_left.
        height (int): The height of the tile. Equal to coords_bottom - coords_top.
        overlap_top (int): Overlap between this tile and its top neighbor.
        overlap_bottom (int): Overlap between this tile and its bottom neighbor.
        overlap_left (int): Overlap between this tile and its left neighbor.
        overlap_right (int): Overlap between this tile and its right neighbor.
        type_ (Literal['tile_to_properties_output']):  Default: 'tile_to_properties_output'.
    """

    coords_left: int
    coords_right: int
    coords_top: int
    coords_bottom: int
    width: int
    height: int
    overlap_top: int
    overlap_bottom: int
    overlap_left: int
    overlap_right: int
    type_: Literal["tile_to_properties_output"] = "tile_to_properties_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coords_left = self.coords_left

        coords_right = self.coords_right

        coords_top = self.coords_top

        coords_bottom = self.coords_bottom

        width = self.width

        height = self.height

        overlap_top = self.overlap_top

        overlap_bottom = self.overlap_bottom

        overlap_left = self.overlap_left

        overlap_right = self.overlap_right

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coords_left": coords_left,
                "coords_right": coords_right,
                "coords_top": coords_top,
                "coords_bottom": coords_bottom,
                "width": width,
                "height": height,
                "overlap_top": overlap_top,
                "overlap_bottom": overlap_bottom,
                "overlap_left": overlap_left,
                "overlap_right": overlap_right,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        coords_left = d.pop("coords_left")

        coords_right = d.pop("coords_right")

        coords_top = d.pop("coords_top")

        coords_bottom = d.pop("coords_bottom")

        width = d.pop("width")

        height = d.pop("height")

        overlap_top = d.pop("overlap_top")

        overlap_bottom = d.pop("overlap_bottom")

        overlap_left = d.pop("overlap_left")

        overlap_right = d.pop("overlap_right")

        type_ = cast(Literal["tile_to_properties_output"], d.pop("type"))
        if type_ != "tile_to_properties_output":
            raise ValueError(f"type must match const 'tile_to_properties_output', got '{type_}'")

        tile_to_properties_output = cls(
            coords_left=coords_left,
            coords_right=coords_right,
            coords_top=coords_top,
            coords_bottom=coords_bottom,
            width=width,
            height=height,
            overlap_top=overlap_top,
            overlap_bottom=overlap_bottom,
            overlap_left=overlap_left,
            overlap_right=overlap_right,
            type_=type_,
        )

        tile_to_properties_output.additional_properties = d
        return tile_to_properties_output

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
