from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_image_mode import BlankImageMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.color_field import ColorField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="BlankImage")


@_attrs_define
class BlankImage:
    """Creates a blank image and forwards it to the pipeline

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['blank_image']):  Default: 'blank_image'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        width (int | Unset): The width of the image Default: 512.
        height (int | Unset): The height of the image Default: 512.
        mode (BlankImageMode | Unset): The mode of the image Default: BlankImageMode.RGB.
        color (ColorField | Unset): A color primitive field
    """

    id: str
    type_: Literal["blank_image"] = "blank_image"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    width: int | Unset = 512
    height: int | Unset = 512
    mode: BlankImageMode | Unset = BlankImageMode.RGB
    color: ColorField | Unset = UNSET
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

        width = self.width

        height = self.height

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

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
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if mode is not UNSET:
            field_dict["mode"] = mode
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.color_field import ColorField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["blank_image"], d.pop("type"))
        if type_ != "blank_image":
            raise ValueError(f"type must match const 'blank_image', got '{type_}'")

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

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: BlankImageMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = BlankImageMode(_mode)

        _color = d.pop("color", UNSET)
        color: ColorField | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = ColorField.from_dict(_color)

        blank_image = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            width=width,
            height=height,
            mode=mode,
            color=color,
        )

        blank_image.additional_properties = d
        return blank_image

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
