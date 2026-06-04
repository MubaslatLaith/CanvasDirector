from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.external_model_capabilities_input_image_required_for_type_0_item import (
    ExternalModelCapabilitiesInputImageRequiredForType0Item,
)
from ..models.external_model_capabilities_mask_format import ExternalModelCapabilitiesMaskFormat
from ..models.external_model_capabilities_modes_item import ExternalModelCapabilitiesModesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_image_size import ExternalImageSize
    from ..models.external_model_capabilities_aspect_ratio_sizes_type_0 import (
        ExternalModelCapabilitiesAspectRatioSizesType0,
    )
    from ..models.external_resolution_preset import ExternalResolutionPreset


T = TypeVar("T", bound="ExternalModelCapabilities")


@_attrs_define
class ExternalModelCapabilities:
    """
    Attributes:
        modes (list[ExternalModelCapabilitiesModesItem] | Unset):
        supports_reference_images (bool | Unset):  Default: False.
        supports_negative_prompt (bool | Unset):  Default: True.
        supports_seed (bool | Unset):  Default: False.
        supports_guidance (bool | Unset):  Default: False.
        supports_steps (bool | Unset):  Default: False.
        max_images_per_request (int | None | Unset):
        max_image_size (ExternalImageSize | None | Unset):
        allowed_aspect_ratios (list[str] | None | Unset):
        aspect_ratio_sizes (ExternalModelCapabilitiesAspectRatioSizesType0 | None | Unset):
        resolution_presets (list[ExternalResolutionPreset] | None | Unset):
        max_reference_images (int | None | Unset):
        mask_format (ExternalModelCapabilitiesMaskFormat | Unset):  Default: ExternalModelCapabilitiesMaskFormat.NONE.
        input_image_required_for (list[ExternalModelCapabilitiesInputImageRequiredForType0Item] | None | Unset):
    """

    modes: list[ExternalModelCapabilitiesModesItem] | Unset = UNSET
    supports_reference_images: bool | Unset = False
    supports_negative_prompt: bool | Unset = True
    supports_seed: bool | Unset = False
    supports_guidance: bool | Unset = False
    supports_steps: bool | Unset = False
    max_images_per_request: int | None | Unset = UNSET
    max_image_size: ExternalImageSize | None | Unset = UNSET
    allowed_aspect_ratios: list[str] | None | Unset = UNSET
    aspect_ratio_sizes: ExternalModelCapabilitiesAspectRatioSizesType0 | None | Unset = UNSET
    resolution_presets: list[ExternalResolutionPreset] | None | Unset = UNSET
    max_reference_images: int | None | Unset = UNSET
    mask_format: ExternalModelCapabilitiesMaskFormat | Unset = ExternalModelCapabilitiesMaskFormat.NONE
    input_image_required_for: list[ExternalModelCapabilitiesInputImageRequiredForType0Item] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_image_size import ExternalImageSize
        from ..models.external_model_capabilities_aspect_ratio_sizes_type_0 import (
            ExternalModelCapabilitiesAspectRatioSizesType0,
        )

        modes: list[str] | Unset = UNSET
        if not isinstance(self.modes, Unset):
            modes = []
            for modes_item_data in self.modes:
                modes_item = modes_item_data.value
                modes.append(modes_item)

        supports_reference_images = self.supports_reference_images

        supports_negative_prompt = self.supports_negative_prompt

        supports_seed = self.supports_seed

        supports_guidance = self.supports_guidance

        supports_steps = self.supports_steps

        max_images_per_request: int | None | Unset
        if isinstance(self.max_images_per_request, Unset):
            max_images_per_request = UNSET
        else:
            max_images_per_request = self.max_images_per_request

        max_image_size: dict[str, Any] | None | Unset
        if isinstance(self.max_image_size, Unset):
            max_image_size = UNSET
        elif isinstance(self.max_image_size, ExternalImageSize):
            max_image_size = self.max_image_size.to_dict()
        else:
            max_image_size = self.max_image_size

        allowed_aspect_ratios: list[str] | None | Unset
        if isinstance(self.allowed_aspect_ratios, Unset):
            allowed_aspect_ratios = UNSET
        elif isinstance(self.allowed_aspect_ratios, list):
            allowed_aspect_ratios = self.allowed_aspect_ratios

        else:
            allowed_aspect_ratios = self.allowed_aspect_ratios

        aspect_ratio_sizes: dict[str, Any] | None | Unset
        if isinstance(self.aspect_ratio_sizes, Unset):
            aspect_ratio_sizes = UNSET
        elif isinstance(self.aspect_ratio_sizes, ExternalModelCapabilitiesAspectRatioSizesType0):
            aspect_ratio_sizes = self.aspect_ratio_sizes.to_dict()
        else:
            aspect_ratio_sizes = self.aspect_ratio_sizes

        resolution_presets: list[dict[str, Any]] | None | Unset
        if isinstance(self.resolution_presets, Unset):
            resolution_presets = UNSET
        elif isinstance(self.resolution_presets, list):
            resolution_presets = []
            for resolution_presets_type_0_item_data in self.resolution_presets:
                resolution_presets_type_0_item = resolution_presets_type_0_item_data.to_dict()
                resolution_presets.append(resolution_presets_type_0_item)

        else:
            resolution_presets = self.resolution_presets

        max_reference_images: int | None | Unset
        if isinstance(self.max_reference_images, Unset):
            max_reference_images = UNSET
        else:
            max_reference_images = self.max_reference_images

        mask_format: str | Unset = UNSET
        if not isinstance(self.mask_format, Unset):
            mask_format = self.mask_format.value

        input_image_required_for: list[str] | None | Unset
        if isinstance(self.input_image_required_for, Unset):
            input_image_required_for = UNSET
        elif isinstance(self.input_image_required_for, list):
            input_image_required_for = []
            for input_image_required_for_type_0_item_data in self.input_image_required_for:
                input_image_required_for_type_0_item = input_image_required_for_type_0_item_data.value
                input_image_required_for.append(input_image_required_for_type_0_item)

        else:
            input_image_required_for = self.input_image_required_for

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if modes is not UNSET:
            field_dict["modes"] = modes
        if supports_reference_images is not UNSET:
            field_dict["supports_reference_images"] = supports_reference_images
        if supports_negative_prompt is not UNSET:
            field_dict["supports_negative_prompt"] = supports_negative_prompt
        if supports_seed is not UNSET:
            field_dict["supports_seed"] = supports_seed
        if supports_guidance is not UNSET:
            field_dict["supports_guidance"] = supports_guidance
        if supports_steps is not UNSET:
            field_dict["supports_steps"] = supports_steps
        if max_images_per_request is not UNSET:
            field_dict["max_images_per_request"] = max_images_per_request
        if max_image_size is not UNSET:
            field_dict["max_image_size"] = max_image_size
        if allowed_aspect_ratios is not UNSET:
            field_dict["allowed_aspect_ratios"] = allowed_aspect_ratios
        if aspect_ratio_sizes is not UNSET:
            field_dict["aspect_ratio_sizes"] = aspect_ratio_sizes
        if resolution_presets is not UNSET:
            field_dict["resolution_presets"] = resolution_presets
        if max_reference_images is not UNSET:
            field_dict["max_reference_images"] = max_reference_images
        if mask_format is not UNSET:
            field_dict["mask_format"] = mask_format
        if input_image_required_for is not UNSET:
            field_dict["input_image_required_for"] = input_image_required_for

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_image_size import ExternalImageSize
        from ..models.external_model_capabilities_aspect_ratio_sizes_type_0 import (
            ExternalModelCapabilitiesAspectRatioSizesType0,
        )
        from ..models.external_resolution_preset import ExternalResolutionPreset

        d = dict(src_dict)
        _modes = d.pop("modes", UNSET)
        modes: list[ExternalModelCapabilitiesModesItem] | Unset = UNSET
        if _modes is not UNSET:
            modes = []
            for modes_item_data in _modes:
                modes_item = ExternalModelCapabilitiesModesItem(modes_item_data)

                modes.append(modes_item)

        supports_reference_images = d.pop("supports_reference_images", UNSET)

        supports_negative_prompt = d.pop("supports_negative_prompt", UNSET)

        supports_seed = d.pop("supports_seed", UNSET)

        supports_guidance = d.pop("supports_guidance", UNSET)

        supports_steps = d.pop("supports_steps", UNSET)

        def _parse_max_images_per_request(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_images_per_request = _parse_max_images_per_request(d.pop("max_images_per_request", UNSET))

        def _parse_max_image_size(data: object) -> ExternalImageSize | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                max_image_size_type_0 = ExternalImageSize.from_dict(data)

                return max_image_size_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalImageSize | None | Unset, data)

        max_image_size = _parse_max_image_size(d.pop("max_image_size", UNSET))

        def _parse_allowed_aspect_ratios(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_aspect_ratios_type_0 = cast(list[str], data)

                return allowed_aspect_ratios_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_aspect_ratios = _parse_allowed_aspect_ratios(d.pop("allowed_aspect_ratios", UNSET))

        def _parse_aspect_ratio_sizes(data: object) -> ExternalModelCapabilitiesAspectRatioSizesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                aspect_ratio_sizes_type_0 = ExternalModelCapabilitiesAspectRatioSizesType0.from_dict(data)

                return aspect_ratio_sizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalModelCapabilitiesAspectRatioSizesType0 | None | Unset, data)

        aspect_ratio_sizes = _parse_aspect_ratio_sizes(d.pop("aspect_ratio_sizes", UNSET))

        def _parse_resolution_presets(data: object) -> list[ExternalResolutionPreset] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolution_presets_type_0 = []
                _resolution_presets_type_0 = data
                for resolution_presets_type_0_item_data in _resolution_presets_type_0:
                    resolution_presets_type_0_item = ExternalResolutionPreset.from_dict(
                        resolution_presets_type_0_item_data
                    )

                    resolution_presets_type_0.append(resolution_presets_type_0_item)

                return resolution_presets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalResolutionPreset] | None | Unset, data)

        resolution_presets = _parse_resolution_presets(d.pop("resolution_presets", UNSET))

        def _parse_max_reference_images(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_reference_images = _parse_max_reference_images(d.pop("max_reference_images", UNSET))

        _mask_format = d.pop("mask_format", UNSET)
        mask_format: ExternalModelCapabilitiesMaskFormat | Unset
        if isinstance(_mask_format, Unset):
            mask_format = UNSET
        else:
            mask_format = ExternalModelCapabilitiesMaskFormat(_mask_format)

        def _parse_input_image_required_for(
            data: object,
        ) -> list[ExternalModelCapabilitiesInputImageRequiredForType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_image_required_for_type_0 = []
                _input_image_required_for_type_0 = data
                for input_image_required_for_type_0_item_data in _input_image_required_for_type_0:
                    input_image_required_for_type_0_item = ExternalModelCapabilitiesInputImageRequiredForType0Item(
                        input_image_required_for_type_0_item_data
                    )

                    input_image_required_for_type_0.append(input_image_required_for_type_0_item)

                return input_image_required_for_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExternalModelCapabilitiesInputImageRequiredForType0Item] | None | Unset, data)

        input_image_required_for = _parse_input_image_required_for(d.pop("input_image_required_for", UNSET))

        external_model_capabilities = cls(
            modes=modes,
            supports_reference_images=supports_reference_images,
            supports_negative_prompt=supports_negative_prompt,
            supports_seed=supports_seed,
            supports_guidance=supports_guidance,
            supports_steps=supports_steps,
            max_images_per_request=max_images_per_request,
            max_image_size=max_image_size,
            allowed_aspect_ratios=allowed_aspect_ratios,
            aspect_ratio_sizes=aspect_ratio_sizes,
            resolution_presets=resolution_presets,
            max_reference_images=max_reference_images,
            mask_format=mask_format,
            input_image_required_for=input_image_required_for,
        )

        return external_model_capabilities
