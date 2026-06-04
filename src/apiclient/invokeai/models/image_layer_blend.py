from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_layer_blend_blend_mode import ImageLayerBlendBlendMode
from ..models.image_layer_blend_color_space import ImageLayerBlendColorSpace
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="ImageLayerBlend")


@_attrs_define
class ImageLayerBlend:
    """Blend two images together, with optional opacity, mask, and blend modes. Originally created by @dwringer

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['invokeai_img_blend']):  Default: 'invokeai_img_blend'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        layer_upper (ImageField | None | Unset): The top image to blend
        blend_mode (ImageLayerBlendBlendMode | Unset): Available blend modes Default: ImageLayerBlendBlendMode.NORMAL.
        opacity (float | Unset): Desired opacity of the upper layer Default: 1.0.
        mask (ImageField | None | Unset): Optional mask, used to restrict areas from blending
        fit_to_width (bool | Unset): Scale upper layer to fit base width Default: False.
        fit_to_height (bool | Unset): Scale upper layer to fit base height Default: True.
        layer_base (ImageField | None | Unset): The bottom image to blend
        color_space (ImageLayerBlendColorSpace | Unset): Available color spaces for blend computations Default:
            ImageLayerBlendColorSpace.RGB.
        adaptive_gamut (float | Unset): Adaptive gamut clipping (0=off). Higher prioritizes chroma over lightness
            Default: 0.0.
        high_precision (bool | Unset): Use more steps in computing gamut when possible Default: True.
    """

    id: str
    type_: Literal["invokeai_img_blend"] = "invokeai_img_blend"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    layer_upper: ImageField | None | Unset = UNSET
    blend_mode: ImageLayerBlendBlendMode | Unset = ImageLayerBlendBlendMode.NORMAL
    opacity: float | Unset = 1.0
    mask: ImageField | None | Unset = UNSET
    fit_to_width: bool | Unset = False
    fit_to_height: bool | Unset = True
    layer_base: ImageField | None | Unset = UNSET
    color_space: ImageLayerBlendColorSpace | Unset = ImageLayerBlendColorSpace.RGB
    adaptive_gamut: float | Unset = 0.0
    high_precision: bool | Unset = True
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

        layer_upper: dict[str, Any] | None | Unset
        if isinstance(self.layer_upper, Unset):
            layer_upper = UNSET
        elif isinstance(self.layer_upper, ImageField):
            layer_upper = self.layer_upper.to_dict()
        else:
            layer_upper = self.layer_upper

        blend_mode: str | Unset = UNSET
        if not isinstance(self.blend_mode, Unset):
            blend_mode = self.blend_mode.value

        opacity = self.opacity

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, ImageField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        fit_to_width = self.fit_to_width

        fit_to_height = self.fit_to_height

        layer_base: dict[str, Any] | None | Unset
        if isinstance(self.layer_base, Unset):
            layer_base = UNSET
        elif isinstance(self.layer_base, ImageField):
            layer_base = self.layer_base.to_dict()
        else:
            layer_base = self.layer_base

        color_space: str | Unset = UNSET
        if not isinstance(self.color_space, Unset):
            color_space = self.color_space.value

        adaptive_gamut = self.adaptive_gamut

        high_precision = self.high_precision

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
        if layer_upper is not UNSET:
            field_dict["layer_upper"] = layer_upper
        if blend_mode is not UNSET:
            field_dict["blend_mode"] = blend_mode
        if opacity is not UNSET:
            field_dict["opacity"] = opacity
        if mask is not UNSET:
            field_dict["mask"] = mask
        if fit_to_width is not UNSET:
            field_dict["fit_to_width"] = fit_to_width
        if fit_to_height is not UNSET:
            field_dict["fit_to_height"] = fit_to_height
        if layer_base is not UNSET:
            field_dict["layer_base"] = layer_base
        if color_space is not UNSET:
            field_dict["color_space"] = color_space
        if adaptive_gamut is not UNSET:
            field_dict["adaptive_gamut"] = adaptive_gamut
        if high_precision is not UNSET:
            field_dict["high_precision"] = high_precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["invokeai_img_blend"], d.pop("type"))
        if type_ != "invokeai_img_blend":
            raise ValueError(f"type must match const 'invokeai_img_blend', got '{type_}'")

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

        def _parse_layer_upper(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                layer_upper_type_0 = ImageField.from_dict(data)

                return layer_upper_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        layer_upper = _parse_layer_upper(d.pop("layer_upper", UNSET))

        _blend_mode = d.pop("blend_mode", UNSET)
        blend_mode: ImageLayerBlendBlendMode | Unset
        if isinstance(_blend_mode, Unset):
            blend_mode = UNSET
        else:
            blend_mode = ImageLayerBlendBlendMode(_blend_mode)

        opacity = d.pop("opacity", UNSET)

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

        fit_to_width = d.pop("fit_to_width", UNSET)

        fit_to_height = d.pop("fit_to_height", UNSET)

        def _parse_layer_base(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                layer_base_type_0 = ImageField.from_dict(data)

                return layer_base_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        layer_base = _parse_layer_base(d.pop("layer_base", UNSET))

        _color_space = d.pop("color_space", UNSET)
        color_space: ImageLayerBlendColorSpace | Unset
        if isinstance(_color_space, Unset):
            color_space = UNSET
        else:
            color_space = ImageLayerBlendColorSpace(_color_space)

        adaptive_gamut = d.pop("adaptive_gamut", UNSET)

        high_precision = d.pop("high_precision", UNSET)

        image_layer_blend = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            layer_upper=layer_upper,
            blend_mode=blend_mode,
            opacity=opacity,
            mask=mask,
            fit_to_width=fit_to_width,
            fit_to_height=fit_to_height,
            layer_base=layer_base,
            color_space=color_space,
            adaptive_gamut=adaptive_gamut,
            high_precision=high_precision,
        )

        image_layer_blend.additional_properties = d
        return image_layer_blend

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
