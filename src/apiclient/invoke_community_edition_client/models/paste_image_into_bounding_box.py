from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.bounding_box_field import BoundingBoxField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="PasteImageIntoBoundingBox")


@_attrs_define
class PasteImageIntoBoundingBox:
    """Paste the source image into the target image at the given bounding box.

    The source image must be the same size as the bounding box, and the bounding box must fit within the target image.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['paste_image_into_bounding_box']):  Default: 'paste_image_into_bounding_box'.
            board (BoardField | None | Unset): The board to save the image to
            metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            source_image (ImageField | None | Unset): The image to paste
            target_image (ImageField | None | Unset): The image to paste into
            bounding_box (BoundingBoxField | None | Unset): The bounding box to paste the image into
    """

    id: str
    type_: Literal["paste_image_into_bounding_box"] = "paste_image_into_bounding_box"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    source_image: ImageField | None | Unset = UNSET
    target_image: ImageField | None | Unset = UNSET
    bounding_box: BoundingBoxField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.board_field import BoardField
        from ..models.bounding_box_field import BoundingBoxField
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

        source_image: dict[str, Any] | None | Unset
        if isinstance(self.source_image, Unset):
            source_image = UNSET
        elif isinstance(self.source_image, ImageField):
            source_image = self.source_image.to_dict()
        else:
            source_image = self.source_image

        target_image: dict[str, Any] | None | Unset
        if isinstance(self.target_image, Unset):
            target_image = UNSET
        elif isinstance(self.target_image, ImageField):
            target_image = self.target_image.to_dict()
        else:
            target_image = self.target_image

        bounding_box: dict[str, Any] | None | Unset
        if isinstance(self.bounding_box, Unset):
            bounding_box = UNSET
        elif isinstance(self.bounding_box, BoundingBoxField):
            bounding_box = self.bounding_box.to_dict()
        else:
            bounding_box = self.bounding_box

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
        if source_image is not UNSET:
            field_dict["source_image"] = source_image
        if target_image is not UNSET:
            field_dict["target_image"] = target_image
        if bounding_box is not UNSET:
            field_dict["bounding_box"] = bounding_box

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.bounding_box_field import BoundingBoxField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["paste_image_into_bounding_box"], d.pop("type"))
        if type_ != "paste_image_into_bounding_box":
            raise ValueError(f"type must match const 'paste_image_into_bounding_box', got '{type_}'")

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

        def _parse_source_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_image_type_0 = ImageField.from_dict(data)

                return source_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        source_image = _parse_source_image(d.pop("source_image", UNSET))

        def _parse_target_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_image_type_0 = ImageField.from_dict(data)

                return target_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        target_image = _parse_target_image(d.pop("target_image", UNSET))

        def _parse_bounding_box(data: object) -> BoundingBoxField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bounding_box_type_0 = BoundingBoxField.from_dict(data)

                return bounding_box_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BoundingBoxField | None | Unset, data)

        bounding_box = _parse_bounding_box(d.pop("bounding_box", UNSET))

        paste_image_into_bounding_box = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            source_image=source_image,
            target_image=target_image,
            bounding_box=bounding_box,
        )

        paste_image_into_bounding_box.additional_properties = d
        return paste_image_into_bounding_box

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
