from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merge_tiles_to_image_blend_mode import MergeTilesToImageBlendMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.metadata_field import MetadataField
    from ..models.tile_with_image import TileWithImage


T = TypeVar("T", bound="MergeTilesToImage")


@_attrs_define
class MergeTilesToImage:
    """Merge multiple tile images into a single image.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['merge_tiles_to_image']):  Default: 'merge_tiles_to_image'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        tiles_with_images (list[TileWithImage] | None | Unset): A list of tile images with tile properties.
        blend_mode (MergeTilesToImageBlendMode | Unset): blending type Linear or Seam Default:
            MergeTilesToImageBlendMode.SEAM.
        blend_amount (int | Unset): The amount to blend adjacent tiles in pixels. Must be <= the amount of overlap
            between adjacent tiles. Default: 32.
    """

    id: str
    type_: Literal["merge_tiles_to_image"] = "merge_tiles_to_image"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    tiles_with_images: list[TileWithImage] | None | Unset = UNSET
    blend_mode: MergeTilesToImageBlendMode | Unset = MergeTilesToImageBlendMode.SEAM
    blend_amount: int | Unset = 32
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.board_field import BoardField
        from ..models.metadata_field import MetadataField

        id = self.id

        type_ = self.type_

        board: dict[str, Any] | None | Unset
        if isinstance(self.board, Unset):
            board = UNSET
        elif isinstance(self.board, BoardField):
            board = self.board.to_dict()
        else:
            board = self.board

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, MetadataField):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        tiles_with_images: list[dict[str, Any]] | None | Unset
        if isinstance(self.tiles_with_images, Unset):
            tiles_with_images = UNSET
        elif isinstance(self.tiles_with_images, list):
            tiles_with_images = []
            for tiles_with_images_type_0_item_data in self.tiles_with_images:
                tiles_with_images_type_0_item = tiles_with_images_type_0_item_data.to_dict()
                tiles_with_images.append(tiles_with_images_type_0_item)

        else:
            tiles_with_images = self.tiles_with_images

        blend_mode: str | Unset = UNSET
        if not isinstance(self.blend_mode, Unset):
            blend_mode = self.blend_mode.value

        blend_amount = self.blend_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if board is not UNSET:
            field_dict["board"] = board
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if tiles_with_images is not UNSET:
            field_dict["tiles_with_images"] = tiles_with_images
        if blend_mode is not UNSET:
            field_dict["blend_mode"] = blend_mode
        if blend_amount is not UNSET:
            field_dict["blend_amount"] = blend_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.metadata_field import MetadataField
        from ..models.tile_with_image import TileWithImage

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["merge_tiles_to_image"], d.pop("type"))
        if type_ != "merge_tiles_to_image":
            raise ValueError(f"type must match const 'merge_tiles_to_image', got '{type_}'")

        def _parse_board(data: object) -> BoardField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                board_type_0 = BoardField.from_dict(data)

                return board_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BoardField | None | Unset, data)

        board = _parse_board(d.pop("board", UNSET))

        def _parse_metadata(data: object) -> MetadataField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MetadataField.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataField | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_tiles_with_images(data: object) -> list[TileWithImage] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tiles_with_images_type_0 = []
                _tiles_with_images_type_0 = data
                for tiles_with_images_type_0_item_data in _tiles_with_images_type_0:
                    tiles_with_images_type_0_item = TileWithImage.from_dict(tiles_with_images_type_0_item_data)

                    tiles_with_images_type_0.append(tiles_with_images_type_0_item)

                return tiles_with_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TileWithImage] | None | Unset, data)

        tiles_with_images = _parse_tiles_with_images(d.pop("tiles_with_images", UNSET))

        _blend_mode = d.pop("blend_mode", UNSET)
        blend_mode: MergeTilesToImageBlendMode | Unset
        if isinstance(_blend_mode, Unset):
            blend_mode = UNSET
        else:
            blend_mode = MergeTilesToImageBlendMode(_blend_mode)

        blend_amount = d.pop("blend_amount", UNSET)

        merge_tiles_to_image = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            tiles_with_images=tiles_with_images,
            blend_mode=blend_mode,
            blend_amount=blend_amount,
        )

        merge_tiles_to_image.additional_properties = d
        return merge_tiles_to_image

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
