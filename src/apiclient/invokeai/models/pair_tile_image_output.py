from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tile_with_image import TileWithImage


T = TypeVar("T", bound="PairTileImageOutput")


@_attrs_define
class PairTileImageOutput:
    """
    Attributes:
        tile_with_image (TileWithImage):
        type_ (Literal['pair_tile_image_output']):  Default: 'pair_tile_image_output'.
    """

    tile_with_image: TileWithImage
    type_: Literal["pair_tile_image_output"] = "pair_tile_image_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tile_with_image = self.tile_with_image.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tile_with_image": tile_with_image,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tile_with_image import TileWithImage

        d = dict(src_dict)
        tile_with_image = TileWithImage.from_dict(d.pop("tile_with_image"))

        type_ = cast(Literal["pair_tile_image_output"], d.pop("type"))
        if type_ != "pair_tile_image_output":
            raise ValueError(f"type must match const 'pair_tile_image_output', got '{type_}'")

        pair_tile_image_output = cls(
            tile_with_image=tile_with_image,
            type_=type_,
        )

        pair_tile_image_output.additional_properties = d
        return pair_tile_image_output

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
