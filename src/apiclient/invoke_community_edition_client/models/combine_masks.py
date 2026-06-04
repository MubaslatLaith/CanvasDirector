from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="CombineMasks")


@_attrs_define
class CombineMasks:
    """Combine two masks together by multiplying them using `PIL.ImageChops.multiply()`.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['mask_combine']):  Default: 'mask_combine'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        mask1 (ImageField | None | Unset): The first mask to combine
        mask2 (ImageField | None | Unset): The second image to combine
    """

    id: str
    type_: Literal["mask_combine"] = "mask_combine"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    mask1: ImageField | None | Unset = UNSET
    mask2: ImageField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
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

        mask1: dict[str, Any] | None | Unset
        if isinstance(self.mask1, Unset):
            mask1 = UNSET
        elif isinstance(self.mask1, ImageField):
            mask1 = self.mask1.to_dict()
        else:
            mask1 = self.mask1

        mask2: dict[str, Any] | None | Unset
        if isinstance(self.mask2, Unset):
            mask2 = UNSET
        elif isinstance(self.mask2, ImageField):
            mask2 = self.mask2.to_dict()
        else:
            mask2 = self.mask2

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
        if mask1 is not UNSET:
            field_dict["mask1"] = mask1
        if mask2 is not UNSET:
            field_dict["mask2"] = mask2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["mask_combine"], d.pop("type"))
        if type_ != "mask_combine":
            raise ValueError(f"type must match const 'mask_combine', got '{type_}'")

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

        def _parse_mask1(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask1_type_0 = ImageField.from_dict(data)

                return mask1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        mask1 = _parse_mask1(d.pop("mask1", UNSET))

        def _parse_mask2(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask2_type_0 = ImageField.from_dict(data)

                return mask2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        mask2 = _parse_mask2(d.pop("mask2", UNSET))

        combine_masks = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            mask1=mask1,
            mask2=mask2,
        )

        combine_masks.additional_properties = d
        return combine_masks

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
