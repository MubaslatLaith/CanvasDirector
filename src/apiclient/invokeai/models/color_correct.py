from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_correct_color_space import ColorCorrectColorSpace
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="ColorCorrect")


@_attrs_define
class ColorCorrect:
    """Matches the color histogram of a base image to a reference image, optionally
    using a mask to only color-correct certain regions of the base image.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['color_correct']):  Default: 'color_correct'.
            board (BoardField | None | Unset): The board to save the image to
            metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            base_image (ImageField | None | Unset): The image to color-correct
            color_reference (ImageField | None | Unset): Reference image for color-correction
            mask (ImageField | None | Unset): Optional mask to limit color correction area
            colorspace (ColorCorrectColorSpace | Unset): Colorspace in which to apply histogram matching Default:
                ColorCorrectColorSpace.RGB.
    """

    id: str
    type_: Literal["color_correct"] = "color_correct"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    base_image: ImageField | None | Unset = UNSET
    color_reference: ImageField | None | Unset = UNSET
    mask: ImageField | None | Unset = UNSET
    colorspace: ColorCorrectColorSpace | Unset = ColorCorrectColorSpace.RGB
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

        base_image: dict[str, Any] | None | Unset
        if isinstance(self.base_image, Unset):
            base_image = UNSET
        elif isinstance(self.base_image, ImageField):
            base_image = self.base_image.to_dict()
        else:
            base_image = self.base_image

        color_reference: dict[str, Any] | None | Unset
        if isinstance(self.color_reference, Unset):
            color_reference = UNSET
        elif isinstance(self.color_reference, ImageField):
            color_reference = self.color_reference.to_dict()
        else:
            color_reference = self.color_reference

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, ImageField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        colorspace: str | Unset = UNSET
        if not isinstance(self.colorspace, Unset):
            colorspace = self.colorspace.value

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
        if base_image is not UNSET:
            field_dict["base_image"] = base_image
        if color_reference is not UNSET:
            field_dict["color_reference"] = color_reference
        if mask is not UNSET:
            field_dict["mask"] = mask
        if colorspace is not UNSET:
            field_dict["colorspace"] = colorspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["color_correct"], d.pop("type"))
        if type_ != "color_correct":
            raise ValueError(f"type must match const 'color_correct', got '{type_}'")

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

        def _parse_base_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                base_image_type_0 = ImageField.from_dict(data)

                return base_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        base_image = _parse_base_image(d.pop("base_image", UNSET))

        def _parse_color_reference(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                color_reference_type_0 = ImageField.from_dict(data)

                return color_reference_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        color_reference = _parse_color_reference(d.pop("color_reference", UNSET))

        def _parse_mask(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_type_0 = ImageField.from_dict(data)

                return mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))

        _colorspace = d.pop("colorspace", UNSET)
        colorspace: ColorCorrectColorSpace | Unset
        if isinstance(_colorspace, Unset):
            colorspace = UNSET
        else:
            colorspace = ColorCorrectColorSpace(_colorspace)

        color_correct = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            base_image=base_image,
            color_reference=color_reference,
            mask=mask,
            colorspace=colorspace,
        )

        color_correct.additional_properties = d
        return color_correct

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
