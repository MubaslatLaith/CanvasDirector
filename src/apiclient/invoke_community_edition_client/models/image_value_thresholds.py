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


T = TypeVar("T", bound="ImageValueThresholds")


@_attrs_define
class ImageValueThresholds:
    """Clip image to pure black/white past specified thresholds. Originally created by @dwringer

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['invokeai_img_val_thresholds']):  Default: 'invokeai_img_val_thresholds'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The image from which to create a mask
        invert_output (bool | Unset): Make light areas dark and vice versa Default: False.
        renormalize_values (bool | Unset): Rescale remaining values from minimum to maximum Default: False.
        lightness_only (bool | Unset): If true, only applies to image lightness (CIELa*b*) Default: False.
        threshold_upper (float | Unset): Threshold above which will be set to full value Default: 0.5.
        threshold_lower (float | Unset): Threshold below which will be set to minimum value Default: 0.5.
    """

    id: str
    type_: Literal["invokeai_img_val_thresholds"] = "invokeai_img_val_thresholds"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    invert_output: bool | Unset = False
    renormalize_values: bool | Unset = False
    lightness_only: bool | Unset = False
    threshold_upper: float | Unset = 0.5
    threshold_lower: float | Unset = 0.5
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

        invert_output = self.invert_output

        renormalize_values = self.renormalize_values

        lightness_only = self.lightness_only

        threshold_upper = self.threshold_upper

        threshold_lower = self.threshold_lower

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
        if invert_output is not UNSET:
            field_dict["invert_output"] = invert_output
        if renormalize_values is not UNSET:
            field_dict["renormalize_values"] = renormalize_values
        if lightness_only is not UNSET:
            field_dict["lightness_only"] = lightness_only
        if threshold_upper is not UNSET:
            field_dict["threshold_upper"] = threshold_upper
        if threshold_lower is not UNSET:
            field_dict["threshold_lower"] = threshold_lower

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["invokeai_img_val_thresholds"], d.pop("type"))
        if type_ != "invokeai_img_val_thresholds":
            raise ValueError(f"type must match const 'invokeai_img_val_thresholds', got '{type_}'")

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

        invert_output = d.pop("invert_output", UNSET)

        renormalize_values = d.pop("renormalize_values", UNSET)

        lightness_only = d.pop("lightness_only", UNSET)

        threshold_upper = d.pop("threshold_upper", UNSET)

        threshold_lower = d.pop("threshold_lower", UNSET)

        image_value_thresholds = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            invert_output=invert_output,
            renormalize_values=renormalize_values,
            lightness_only=lightness_only,
            threshold_upper=threshold_upper,
            threshold_lower=threshold_lower,
        )

        image_value_thresholds.additional_properties = d
        return image_value_thresholds

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
