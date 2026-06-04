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


T = TypeVar("T", bound="ImageCompositor")


@_attrs_define
class ImageCompositor:
    """Removes backdrop from subject image then overlays subject on background image. Originally created by @dwringer

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['invokeai_img_composite']):  Default: 'invokeai_img_composite'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image_subject (ImageField | None | Unset): Image of the subject on a plain monochrome background
        image_background (ImageField | None | Unset): Image of a background scene
        chroma_key (str | Unset): Can be empty for corner flood select, or CSS-3 color or tuple Default: ''.
        threshold (int | Unset): Subject isolation flood-fill threshold Default: 50.
        fill_x (bool | Unset): Scale base subject image to fit background width Default: False.
        fill_y (bool | Unset): Scale base subject image to fit background height Default: True.
        x_offset (int | Unset): x-offset for the subject Default: 0.
        y_offset (int | Unset): y-offset for the subject Default: 0.
    """

    id: str
    type_: Literal["invokeai_img_composite"] = "invokeai_img_composite"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image_subject: ImageField | None | Unset = UNSET
    image_background: ImageField | None | Unset = UNSET
    chroma_key: str | Unset = ""
    threshold: int | Unset = 50
    fill_x: bool | Unset = False
    fill_y: bool | Unset = True
    x_offset: int | Unset = 0
    y_offset: int | Unset = 0
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

        image_subject: dict[str, Any] | None | Unset
        if isinstance(self.image_subject, Unset):
            image_subject = UNSET
        elif isinstance(self.image_subject, ImageField):
            image_subject = self.image_subject.to_dict()
        else:
            image_subject = self.image_subject

        image_background: dict[str, Any] | None | Unset
        if isinstance(self.image_background, Unset):
            image_background = UNSET
        elif isinstance(self.image_background, ImageField):
            image_background = self.image_background.to_dict()
        else:
            image_background = self.image_background

        chroma_key = self.chroma_key

        threshold = self.threshold

        fill_x = self.fill_x

        fill_y = self.fill_y

        x_offset = self.x_offset

        y_offset = self.y_offset

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
        if image_subject is not UNSET:
            field_dict["image_subject"] = image_subject
        if image_background is not UNSET:
            field_dict["image_background"] = image_background
        if chroma_key is not UNSET:
            field_dict["chroma_key"] = chroma_key
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if fill_x is not UNSET:
            field_dict["fill_x"] = fill_x
        if fill_y is not UNSET:
            field_dict["fill_y"] = fill_y
        if x_offset is not UNSET:
            field_dict["x_offset"] = x_offset
        if y_offset is not UNSET:
            field_dict["y_offset"] = y_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["invokeai_img_composite"], d.pop("type"))
        if type_ != "invokeai_img_composite":
            raise ValueError(f"type must match const 'invokeai_img_composite', got '{type_}'")

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

        def _parse_image_subject(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_subject_type_0 = ImageField.from_dict(data)

                return image_subject_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        image_subject = _parse_image_subject(d.pop("image_subject", UNSET))

        def _parse_image_background(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_background_type_0 = ImageField.from_dict(data)

                return image_background_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        image_background = _parse_image_background(d.pop("image_background", UNSET))

        chroma_key = d.pop("chroma_key", UNSET)

        threshold = d.pop("threshold", UNSET)

        fill_x = d.pop("fill_x", UNSET)

        fill_y = d.pop("fill_y", UNSET)

        x_offset = d.pop("x_offset", UNSET)

        y_offset = d.pop("y_offset", UNSET)

        image_compositor = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image_subject=image_subject,
            image_background=image_background,
            chroma_key=chroma_key,
            threshold=threshold,
            fill_x=fill_x,
            fill_y=fill_y,
            x_offset=x_offset,
            y_offset=y_offset,
        )

        image_compositor.additional_properties = d
        return image_compositor

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
