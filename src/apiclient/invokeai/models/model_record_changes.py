from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_model_type import BaseModelType
from ..models.clip_variant_type import ClipVariantType
from ..models.flux_2_variant_type import Flux2VariantType
from ..models.flux_variant_type import FluxVariantType
from ..models.model_source_type import ModelSourceType
from ..models.model_type import ModelType
from ..models.model_variant_type import ModelVariantType
from ..models.qwen_3_variant_type import Qwen3VariantType
from ..models.qwen_image_variant_type import QwenImageVariantType
from ..models.scheduler_prediction_type import SchedulerPredictionType
from ..models.z_image_variant_type import ZImageVariantType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.control_adapter_default_settings import ControlAdapterDefaultSettings
    from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
    from ..models.external_model_capabilities import ExternalModelCapabilities
    from ..models.lora_model_default_settings import LoraModelDefaultSettings
    from ..models.main_model_default_settings import MainModelDefaultSettings


T = TypeVar("T", bound="ModelRecordChanges")


@_attrs_define
class ModelRecordChanges:
    """A set of changes to apply to a model.

    Attributes:
        source (None | str | Unset): original source of the model
        source_type (ModelSourceType | None | Unset): type of model source
        source_api_response (None | str | Unset): metadata from remote source
        source_url (None | str | Unset): Optional URL for the model (e.g. download page)
        name (None | str | Unset): Name of the model.
        path (None | str | Unset): Path to the model.
        description (None | str | Unset): Model description
        base (BaseModelType | None | Unset): The base model.
        type_ (ModelType | None | Unset): Type of model
        key (None | str | Unset): Database ID for this model
        hash_ (None | str | Unset): hash of model file
        file_size (int | None | Unset): Size of model file
        format_ (None | str | Unset): format of model file
        trigger_phrases (list[str] | None | Unset): Set of trigger phrases for this model
        default_settings (ControlAdapterDefaultSettings | ExternalApiModelDefaultSettings | LoraModelDefaultSettings |
            MainModelDefaultSettings | None | Unset): Default settings for this model
        provider_id (None | str | Unset): External provider identifier
        provider_model_id (None | str | Unset): External provider model identifier
        capabilities (ExternalModelCapabilities | None | Unset): External model capabilities
        cpu_only (bool | None | Unset): Whether this model should run on CPU only
        variant (ClipVariantType | Flux2VariantType | FluxVariantType | ModelVariantType | None | Qwen3VariantType |
            QwenImageVariantType | Unset | ZImageVariantType): The variant of the model.
        prediction_type (None | SchedulerPredictionType | Unset): The prediction type of the model.
        upcast_attention (bool | None | Unset): Whether to upcast attention.
        config_path (None | str | Unset): Path to config file for model
    """

    source: None | str | Unset = UNSET
    source_type: ModelSourceType | None | Unset = UNSET
    source_api_response: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    base: BaseModelType | None | Unset = UNSET
    type_: ModelType | None | Unset = UNSET
    key: None | str | Unset = UNSET
    hash_: None | str | Unset = UNSET
    file_size: int | None | Unset = UNSET
    format_: None | str | Unset = UNSET
    trigger_phrases: list[str] | None | Unset = UNSET
    default_settings: (
        ControlAdapterDefaultSettings
        | ExternalApiModelDefaultSettings
        | LoraModelDefaultSettings
        | MainModelDefaultSettings
        | None
        | Unset
    ) = UNSET
    provider_id: None | str | Unset = UNSET
    provider_model_id: None | str | Unset = UNSET
    capabilities: ExternalModelCapabilities | None | Unset = UNSET
    cpu_only: bool | None | Unset = UNSET
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
    prediction_type: None | SchedulerPredictionType | Unset = UNSET
    upcast_attention: bool | None | Unset = UNSET
    config_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_adapter_default_settings import ControlAdapterDefaultSettings
        from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
        from ..models.external_model_capabilities import ExternalModelCapabilities
        from ..models.lora_model_default_settings import LoraModelDefaultSettings
        from ..models.main_model_default_settings import MainModelDefaultSettings

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        elif isinstance(self.source_type, ModelSourceType):
            source_type = self.source_type.value
        else:
            source_type = self.source_type

        source_api_response: None | str | Unset
        if isinstance(self.source_api_response, Unset):
            source_api_response = UNSET
        else:
            source_api_response = self.source_api_response

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        base: None | str | Unset
        if isinstance(self.base, Unset):
            base = UNSET
        elif isinstance(self.base, BaseModelType):
            base = self.base.value
        else:
            base = self.base

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ModelType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        hash_: None | str | Unset
        if isinstance(self.hash_, Unset):
            hash_ = UNSET
        else:
            hash_ = self.hash_

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        trigger_phrases: list[str] | None | Unset
        if isinstance(self.trigger_phrases, Unset):
            trigger_phrases = UNSET
        elif isinstance(self.trigger_phrases, list):
            trigger_phrases = self.trigger_phrases

        else:
            trigger_phrases = self.trigger_phrases

        default_settings: dict[str, Any] | None | Unset
        if isinstance(self.default_settings, Unset):
            default_settings = UNSET
        elif isinstance(self.default_settings, MainModelDefaultSettings):
            default_settings = self.default_settings.to_dict()
        elif isinstance(self.default_settings, LoraModelDefaultSettings):
            default_settings = self.default_settings.to_dict()
        elif isinstance(self.default_settings, ControlAdapterDefaultSettings):
            default_settings = self.default_settings.to_dict()
        elif isinstance(self.default_settings, ExternalApiModelDefaultSettings):
            default_settings = self.default_settings.to_dict()
        else:
            default_settings = self.default_settings

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        provider_model_id: None | str | Unset
        if isinstance(self.provider_model_id, Unset):
            provider_model_id = UNSET
        else:
            provider_model_id = self.provider_model_id

        capabilities: dict[str, Any] | None | Unset
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, ExternalModelCapabilities):
            capabilities = self.capabilities.to_dict()
        else:
            capabilities = self.capabilities

        cpu_only: bool | None | Unset
        if isinstance(self.cpu_only, Unset):
            cpu_only = UNSET
        else:
            cpu_only = self.cpu_only

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

        prediction_type: None | str | Unset
        if isinstance(self.prediction_type, Unset):
            prediction_type = UNSET
        elif isinstance(self.prediction_type, SchedulerPredictionType):
            prediction_type = self.prediction_type.value
        else:
            prediction_type = self.prediction_type

        upcast_attention: bool | None | Unset
        if isinstance(self.upcast_attention, Unset):
            upcast_attention = UNSET
        else:
            upcast_attention = self.upcast_attention

        config_path: None | str | Unset
        if isinstance(self.config_path, Unset):
            config_path = UNSET
        else:
            config_path = self.config_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_api_response is not UNSET:
            field_dict["source_api_response"] = source_api_response
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if description is not UNSET:
            field_dict["description"] = description
        if base is not UNSET:
            field_dict["base"] = base
        if type_ is not UNSET:
            field_dict["type"] = type_
        if key is not UNSET:
            field_dict["key"] = key
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if format_ is not UNSET:
            field_dict["format"] = format_
        if trigger_phrases is not UNSET:
            field_dict["trigger_phrases"] = trigger_phrases
        if default_settings is not UNSET:
            field_dict["default_settings"] = default_settings
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if provider_model_id is not UNSET:
            field_dict["provider_model_id"] = provider_model_id
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if cpu_only is not UNSET:
            field_dict["cpu_only"] = cpu_only
        if variant is not UNSET:
            field_dict["variant"] = variant
        if prediction_type is not UNSET:
            field_dict["prediction_type"] = prediction_type
        if upcast_attention is not UNSET:
            field_dict["upcast_attention"] = upcast_attention
        if config_path is not UNSET:
            field_dict["config_path"] = config_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_adapter_default_settings import ControlAdapterDefaultSettings
        from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
        from ..models.external_model_capabilities import ExternalModelCapabilities
        from ..models.lora_model_default_settings import LoraModelDefaultSettings
        from ..models.main_model_default_settings import MainModelDefaultSettings

        d = dict(src_dict)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_source_type(data: object) -> ModelSourceType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_type_0 = ModelSourceType(data)

                return source_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelSourceType | None | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_source_api_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_api_response = _parse_source_api_response(d.pop("source_api_response", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_base(data: object) -> BaseModelType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_type_0 = BaseModelType(data)

                return base_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseModelType | None | Unset, data)

        base = _parse_base(d.pop("base", UNSET))

        def _parse_type_(data: object) -> ModelType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = ModelType(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_hash_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hash_ = _parse_hash_(d.pop("hash", UNSET))

        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_trigger_phrases(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trigger_phrases_type_0 = cast(list[str], data)

                return trigger_phrases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        trigger_phrases = _parse_trigger_phrases(d.pop("trigger_phrases", UNSET))

        def _parse_default_settings(
            data: object,
        ) -> (
            ControlAdapterDefaultSettings
            | ExternalApiModelDefaultSettings
            | LoraModelDefaultSettings
            | MainModelDefaultSettings
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_0 = MainModelDefaultSettings.from_dict(data)

                return default_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_1 = LoraModelDefaultSettings.from_dict(data)

                return default_settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_2 = ControlAdapterDefaultSettings.from_dict(data)

                return default_settings_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_3 = ExternalApiModelDefaultSettings.from_dict(data)

                return default_settings_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ControlAdapterDefaultSettings
                | ExternalApiModelDefaultSettings
                | LoraModelDefaultSettings
                | MainModelDefaultSettings
                | None
                | Unset,
                data,
            )

        default_settings = _parse_default_settings(d.pop("default_settings", UNSET))

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        def _parse_provider_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_model_id = _parse_provider_model_id(d.pop("provider_model_id", UNSET))

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

        def _parse_cpu_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cpu_only = _parse_cpu_only(d.pop("cpu_only", UNSET))

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

        def _parse_prediction_type(data: object) -> None | SchedulerPredictionType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                prediction_type_type_0 = SchedulerPredictionType(data)

                return prediction_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SchedulerPredictionType | Unset, data)

        prediction_type = _parse_prediction_type(d.pop("prediction_type", UNSET))

        def _parse_upcast_attention(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upcast_attention = _parse_upcast_attention(d.pop("upcast_attention", UNSET))

        def _parse_config_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config_path = _parse_config_path(d.pop("config_path", UNSET))

        model_record_changes = cls(
            source=source,
            source_type=source_type,
            source_api_response=source_api_response,
            source_url=source_url,
            name=name,
            path=path,
            description=description,
            base=base,
            type_=type_,
            key=key,
            hash_=hash_,
            file_size=file_size,
            format_=format_,
            trigger_phrases=trigger_phrases,
            default_settings=default_settings,
            provider_id=provider_id,
            provider_model_id=provider_model_id,
            capabilities=capabilities,
            cpu_only=cpu_only,
            variant=variant,
            prediction_type=prediction_type,
            upcast_attention=upcast_attention,
            config_path=config_path,
        )

        model_record_changes.additional_properties = d
        return model_record_changes

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
