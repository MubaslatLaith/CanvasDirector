from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_model_type import BaseModelType
from ..models.clip_variant_type import ClipVariantType
from ..models.flux_2_variant_type import Flux2VariantType
from ..models.flux_variant_type import FluxVariantType
from ..models.model_format import ModelFormat
from ..models.model_type import ModelType
from ..models.model_variant_type import ModelVariantType
from ..models.qwen_3_variant_type import Qwen3VariantType
from ..models.qwen_image_variant_type import QwenImageVariantType
from ..models.z_image_variant_type import ZImageVariantType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
    from ..models.external_model_capabilities import ExternalModelCapabilities
    from ..models.external_model_panel_schema import ExternalModelPanelSchema


T = TypeVar("T", bound="StarterModelWithoutDependencies")


@_attrs_define
class StarterModelWithoutDependencies:
    """
    Attributes:
        description (str):
        source (str):
        name (str):
        base (BaseModelType): An enumeration of base model architectures. For example, Stable Diffusion 1.x, Stable
            Diffusion 2.x, FLUX, etc.

            Every model config must have a base architecture type.

            Not all models are associated with a base architecture. For example, CLIP models are their own thing, not
            related
            to any particular model architecture. To simplify internal APIs and make it easier to work with models, we use a
            fallback/null value `BaseModelType.Any` for these models, instead of making the model base optional.
        type_ (ModelType): Model type.
        format_ (ModelFormat | None | Unset):
        variant (ClipVariantType | Flux2VariantType | FluxVariantType | ModelVariantType | None | Qwen3VariantType |
            QwenImageVariantType | Unset | ZImageVariantType):
        is_installed (bool | Unset):  Default: False.
        capabilities (ExternalModelCapabilities | None | Unset):
        default_settings (ExternalApiModelDefaultSettings | None | Unset):
        panel_schema (ExternalModelPanelSchema | None | Unset):
        previous_names (list[str] | Unset):
    """

    description: str
    source: str
    name: str
    base: BaseModelType
    type_: ModelType
    format_: ModelFormat | None | Unset = UNSET
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
    is_installed: bool | Unset = False
    capabilities: ExternalModelCapabilities | None | Unset = UNSET
    default_settings: ExternalApiModelDefaultSettings | None | Unset = UNSET
    panel_schema: ExternalModelPanelSchema | None | Unset = UNSET
    previous_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
        from ..models.external_model_capabilities import ExternalModelCapabilities
        from ..models.external_model_panel_schema import ExternalModelPanelSchema

        description = self.description

        source = self.source

        name = self.name

        base = self.base.value

        type_ = self.type_.value

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        elif isinstance(self.format_, ModelFormat):
            format_ = self.format_.value
        else:
            format_ = self.format_

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

        is_installed = self.is_installed

        capabilities: dict[str, Any] | None | Unset
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, ExternalModelCapabilities):
            capabilities = self.capabilities.to_dict()
        else:
            capabilities = self.capabilities

        default_settings: dict[str, Any] | None | Unset
        if isinstance(self.default_settings, Unset):
            default_settings = UNSET
        elif isinstance(self.default_settings, ExternalApiModelDefaultSettings):
            default_settings = self.default_settings.to_dict()
        else:
            default_settings = self.default_settings

        panel_schema: dict[str, Any] | None | Unset
        if isinstance(self.panel_schema, Unset):
            panel_schema = UNSET
        elif isinstance(self.panel_schema, ExternalModelPanelSchema):
            panel_schema = self.panel_schema.to_dict()
        else:
            panel_schema = self.panel_schema

        previous_names: list[str] | Unset = UNSET
        if not isinstance(self.previous_names, Unset):
            previous_names = self.previous_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "source": source,
                "name": name,
                "base": base,
                "type": type_,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if variant is not UNSET:
            field_dict["variant"] = variant
        if is_installed is not UNSET:
            field_dict["is_installed"] = is_installed
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if default_settings is not UNSET:
            field_dict["default_settings"] = default_settings
        if panel_schema is not UNSET:
            field_dict["panel_schema"] = panel_schema
        if previous_names is not UNSET:
            field_dict["previous_names"] = previous_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
        from ..models.external_model_capabilities import ExternalModelCapabilities
        from ..models.external_model_panel_schema import ExternalModelPanelSchema

        d = dict(src_dict)
        description = d.pop("description")

        source = d.pop("source")

        name = d.pop("name")

        base = BaseModelType(d.pop("base"))

        type_ = ModelType(d.pop("type"))

        def _parse_format_(data: object) -> ModelFormat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_0 = ModelFormat(data)

                return format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelFormat | None | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

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

        is_installed = d.pop("is_installed", UNSET)

        def _parse_capabilities(data: object) -> ExternalModelCapabilities | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                capabilities_type_0 = ExternalModelCapabilities.from_dict(data)

                return capabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalModelCapabilities | None | Unset, data)

        capabilities = _parse_capabilities(d.pop("capabilities", UNSET))

        def _parse_default_settings(data: object) -> ExternalApiModelDefaultSettings | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_0 = ExternalApiModelDefaultSettings.from_dict(data)

                return default_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalApiModelDefaultSettings | None | Unset, data)

        default_settings = _parse_default_settings(d.pop("default_settings", UNSET))

        def _parse_panel_schema(data: object) -> ExternalModelPanelSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                panel_schema_type_0 = ExternalModelPanelSchema.from_dict(data)

                return panel_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalModelPanelSchema | None | Unset, data)

        panel_schema = _parse_panel_schema(d.pop("panel_schema", UNSET))

        previous_names = cast(list[str], d.pop("previous_names", UNSET))

        starter_model_without_dependencies = cls(
            description=description,
            source=source,
            name=name,
            base=base,
            type_=type_,
            format_=format_,
            variant=variant,
            is_installed=is_installed,
            capabilities=capabilities,
            default_settings=default_settings,
            panel_schema=panel_schema,
            previous_names=previous_names,
        )

        starter_model_without_dependencies.additional_properties = d
        return starter_model_without_dependencies

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
