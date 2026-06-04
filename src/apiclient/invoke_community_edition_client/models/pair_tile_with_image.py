from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.tile import Tile


T = TypeVar("T", bound="PairTileWithImage")


@_attrs_define
class PairTileWithImage:
    """Pair an image with its tile properties.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['pair_tile_image']):  Default: 'pair_tile_image'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The tile image.
        tile (None | Tile | Unset): The tile properties.
    """

    id: str
    type_: Literal["pair_tile_image"] = "pair_tile_image"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    tile: None | Tile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.tile import Tile

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        tile: dict[str, Any] | None | Unset
        if isinstance(self.tile, Unset):
            tile = UNSET
        elif isinstance(self.tile, Tile):
            tile = self.tile.to_dict()
        else:
            tile = self.tile

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
        if image is not UNSET:
            field_dict["image"] = image
        if tile is not UNSET:
            field_dict["tile"] = tile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.tile import Tile

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["pair_tile_image"], d.pop("type"))
        if type_ != "pair_tile_image":
            raise ValueError(f"type must match const 'pair_tile_image', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = ImageField.from_dict(data)

                return image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_tile(data: object) -> None | Tile | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tile_type_0 = Tile.from_dict(data)

                return tile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Tile | Unset, data)

        tile = _parse_tile(d.pop("tile", UNSET))

        pair_tile_with_image = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            tile=tile,
        )

        pair_tile_with_image.additional_properties = d
        return pair_tile_with_image

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
