from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.adjust_image_hue_plus_space import AdjustImageHuePlusSpace
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="AdjustImageHuePlus")


@_attrs_define
class AdjustImageHuePlus:
    """Adjusts the Hue of an image by rotating it in the selected color space. Originally created by @dwringer

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['invokeai_img_hue_adjust_plus']):  Default: 'invokeai_img_hue_adjust_plus'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The image to adjust
        space (AdjustImageHuePlusSpace | Unset): Color space in which to rotate hue by polar coords (*: non-invertible)
            Default: AdjustImageHuePlusSpace.HSV_HSL_RGB.
        degrees (float | Unset): Degrees by which to rotate image hue Default: 0.0.
        preserve_lightness (bool | Unset): Whether to preserve CIELAB lightness values Default: False.
        ok_adaptive_gamut (float | Unset): Higher preserves chroma at the expense of lightness (Oklab) Default: 0.05.
        ok_high_precision (bool | Unset): Use more steps in computing gamut (Oklab/Okhsv/Okhsl) Default: True.
    """

    id: str
    type_: Literal["invokeai_img_hue_adjust_plus"] = "invokeai_img_hue_adjust_plus"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    space: AdjustImageHuePlusSpace | Unset = AdjustImageHuePlusSpace.HSV_HSL_RGB
    degrees: float | Unset = 0.0
    preserve_lightness: bool | Unset = False
    ok_adaptive_gamut: float | Unset = 0.05
    ok_high_precision: bool | Unset = True
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

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        space: str | Unset = UNSET
        if not isinstance(self.space, Unset):
            space = self.space.value

        degrees = self.degrees

        preserve_lightness = self.preserve_lightness

        ok_adaptive_gamut = self.ok_adaptive_gamut

        ok_high_precision = self.ok_high_precision

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
        if image is not UNSET:
            field_dict["image"] = image
        if space is not UNSET:
            field_dict["space"] = space
        if degrees is not UNSET:
            field_dict["degrees"] = degrees
        if preserve_lightness is not UNSET:
            field_dict["preserve_lightness"] = preserve_lightness
        if ok_adaptive_gamut is not UNSET:
            field_dict["ok_adaptive_gamut"] = ok_adaptive_gamut
        if ok_high_precision is not UNSET:
            field_dict["ok_high_precision"] = ok_high_precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["invokeai_img_hue_adjust_plus"], d.pop("type"))
        if type_ != "invokeai_img_hue_adjust_plus":
            raise ValueError(f"type must match const 'invokeai_img_hue_adjust_plus', got '{type_}'")

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

        _space = d.pop("space", UNSET)
        space: AdjustImageHuePlusSpace | Unset
        if isinstance(_space, Unset):
            space = UNSET
        else:
            space = AdjustImageHuePlusSpace(_space)

        degrees = d.pop("degrees", UNSET)

        preserve_lightness = d.pop("preserve_lightness", UNSET)

        ok_adaptive_gamut = d.pop("ok_adaptive_gamut", UNSET)

        ok_high_precision = d.pop("ok_high_precision", UNSET)

        adjust_image_hue_plus = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            space=space,
            degrees=degrees,
            preserve_lightness=preserve_lightness,
            ok_adaptive_gamut=ok_adaptive_gamut,
            ok_high_precision=ok_high_precision,
        )

        adjust_image_hue_plus.additional_properties = d
        return adjust_image_hue_plus

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
