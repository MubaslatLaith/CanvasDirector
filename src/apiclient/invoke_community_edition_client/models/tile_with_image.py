from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.tile import Tile


T = TypeVar("T", bound="TileWithImage")


@_attrs_define
class TileWithImage:
    """
    Attributes:
        tile (Tile):
        image (ImageField): An image primitive field
    """

    tile: Tile
    image: ImageField
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tile = self.tile.to_dict()

        image = self.image.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tile": tile,
                "image": image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.tile import Tile

        d = dict(src_dict)
        tile = Tile.from_dict(d.pop("tile"))

        image = ImageField.from_dict(d.pop("image"))

        tile_with_image = cls(
            tile=tile,
            image=image,
        )

        tile_with_image.additional_properties = d
        return tile_with_image

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
