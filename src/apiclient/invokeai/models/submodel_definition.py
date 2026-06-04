from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clip_variant_type import ClipVariantType
from ..models.flux_2_variant_type import Flux2VariantType
from ..models.flux_variant_type import FluxVariantType
from ..models.model_type import ModelType
from ..models.model_variant_type import ModelVariantType
from ..models.qwen_3_variant_type import Qwen3VariantType
from ..models.qwen_image_variant_type import QwenImageVariantType
from ..models.z_image_variant_type import ZImageVariantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmodelDefinition")


@_attrs_define
class SubmodelDefinition:
    """
    Attributes:
        path_or_prefix (str):
        model_type (ModelType): Model type.
        variant (ClipVariantType | Flux2VariantType | FluxVariantType | ModelVariantType | None | Qwen3VariantType |
            QwenImageVariantType | Unset | ZImageVariantType):
    """

    path_or_prefix: str
    model_type: ModelType
    variant: (
        ClipVariantType
        | Flux2VariantType
        | FluxVariantType
        | ModelVariantType
        | None
        | Qwen3VariantType
        | QwenImageVariantType
        | Unset
        | ZImageVariantType
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path_or_prefix = self.path_or_prefix

        model_type = self.model_type.value

        variant: None | str | Unset
        if isinstance(self.variant, Unset):
            variant = UNSET
        elif isinstance(self.variant, ModelVariantType):
            variant = self.variant.value
        elif isinstance(self.variant, ClipVariantType):
            variant = self.variant.value
        elif isinstance(self.variant, FluxVariantType):
            variant = self.variant.value
        elif isinstance(self.variant, Flux2VariantType):
            variant = self.variant.value
        elif isinstance(self.variant, ZImageVariantType):
            variant = self.variant.value
        elif isinstance(self.variant, QwenImageVariantType):
            variant = self.variant.value
        elif isinstance(self.variant, Qwen3VariantType):
            variant = self.variant.value
        else:
            variant = self.variant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path_or_prefix": path_or_prefix,
                "model_type": model_type,
            }
        )
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path_or_prefix = d.pop("path_or_prefix")

        model_type = ModelType(d.pop("model_type"))

        def _parse_variant(
            data: object,
        ) -> (
            ClipVariantType
            | Flux2VariantType
            | FluxVariantType
            | ModelVariantType
            | None
            | Qwen3VariantType
            | QwenImageVariantType
            | Unset
            | ZImageVariantType
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_0 = ModelVariantType(data)

                return variant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_1 = ClipVariantType(data)

                return variant_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_2 = FluxVariantType(data)

                return variant_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_3 = Flux2VariantType(data)

                return variant_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_4 = ZImageVariantType(data)

                return variant_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_5 = QwenImageVariantType(data)

                return variant_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_6 = Qwen3VariantType(data)

                return variant_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ClipVariantType
                | Flux2VariantType
                | FluxVariantType
                | ModelVariantType
                | None
                | Qwen3VariantType
                | QwenImageVariantType
                | Unset
                | ZImageVariantType,
                data,
            )

        variant = _parse_variant(d.pop("variant", UNSET))

        submodel_definition = cls(
            path_or_prefix=path_or_prefix,
            model_type=model_type,
            variant=variant,
        )

        submodel_definition.additional_properties = d
        return submodel_definition

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
