from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tile import Tile


T = TypeVar("T", bound="CalculateImageTilesOutput")


@_attrs_define
class CalculateImageTilesOutput:
    """
    Attributes:
        tiles (list[Tile]): The tiles coordinates that cover a particular image shape.
        type_ (Literal['calculate_image_tiles_output']):  Default: 'calculate_image_tiles_output'.
    """

    tiles: list[Tile]
    type_: Literal["calculate_image_tiles_output"] = "calculate_image_tiles_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tiles = []
        for tiles_item_data in self.tiles:
            tiles_item = tiles_item_data.to_dict()
            tiles.append(tiles_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tiles": tiles,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tile import Tile

        d = dict(src_dict)
        tiles = []
        _tiles = d.pop("tiles")
        for tiles_item_data in _tiles:
            tiles_item = Tile.from_dict(tiles_item_data)

            tiles.append(tiles_item)

        type_ = cast(Literal["calculate_image_tiles_output"], d.pop("type"))
        if type_ != "calculate_image_tiles_output":
            raise ValueError(f"type must match const 'calculate_image_tiles_output', got '{type_}'")

        calculate_image_tiles_output = cls(
            tiles=tiles,
            type_=type_,
        )

        calculate_image_tiles_output.additional_properties = d
        return calculate_image_tiles_output

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
