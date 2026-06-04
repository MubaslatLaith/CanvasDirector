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


T = TypeVar("T", bound="CanvasV2MaskAndCrop")


@_attrs_define
class CanvasV2MaskAndCrop:
    """Handles Canvas V2 image output masking and cropping

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['canvas_v2_mask_and_crop']):  Default: 'canvas_v2_mask_and_crop'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        source_image (ImageField | None | Unset): The source image onto which the masked generated image is pasted. If
            omitted, the masked generated image is returned with transparency.
        generated_image (ImageField | None | Unset): The image to apply the mask to
        mask (ImageField | None | Unset): The mask to apply
        mask_blur (int | Unset): The amount to blur the mask by Default: 0.
    """

    id: str
    type_: Literal["canvas_v2_mask_and_crop"] = "canvas_v2_mask_and_crop"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    source_image: ImageField | None | Unset = UNSET
    generated_image: ImageField | None | Unset = UNSET
    mask: ImageField | None | Unset = UNSET
    mask_blur: int | Unset = 0
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

        source_image: dict[str, Any] | None | Unset
        if isinstance(self.source_image, Unset):
            source_image = UNSET
        elif isinstance(self.source_image, ImageField):
            source_image = self.source_image.to_dict()
        else:
            source_image = self.source_image

        generated_image: dict[str, Any] | None | Unset
        if isinstance(self.generated_image, Unset):
            generated_image = UNSET
        elif isinstance(self.generated_image, ImageField):
            generated_image = self.generated_image.to_dict()
        else:
            generated_image = self.generated_image

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, ImageField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        mask_blur = self.mask_blur

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
        if generated_image is not UNSET:
            field_dict["generated_image"] = generated_image
        if mask is not UNSET:
            field_dict["mask"] = mask
        if mask_blur is not UNSET:
            field_dict["mask_blur"] = mask_blur

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["canvas_v2_mask_and_crop"], d.pop("type"))
        if type_ != "canvas_v2_mask_and_crop":
            raise ValueError(f"type must match const 'canvas_v2_mask_and_crop', got '{type_}'")

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

        def _parse_generated_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                generated_image_type_0 = ImageField.from_dict(data)

                return generated_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        generated_image = _parse_generated_image(d.pop("generated_image", UNSET))

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

        mask_blur = d.pop("mask_blur", UNSET)

        canvas_v2_mask_and_crop = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            source_image=source_image,
            generated_image=generated_image,
            mask=mask,
            mask_blur=mask_blur,
        )

        canvas_v2_mask_and_crop.additional_properties = d
        return canvas_v2_mask_and_crop

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
