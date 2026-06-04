from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flux_2_variant_type import Flux2VariantType
from ..models.model_source_type import ModelSourceType

if TYPE_CHECKING:
    from ..models.main_model_default_settings import MainModelDefaultSettings


T = TypeVar("T", bound="MainGGUFFlux2Config")


@_attrs_define
class MainGGUFFlux2Config:
    """Model config for GGUF-quantized FLUX.2 checkpoint models (e.g. Klein).

    Attributes:
        key (str): A unique key for this model.
        hash_ (str): The hash of the model file(s).
        path (str): Path to the model on the filesystem. Relative paths are relative to the Invoke root directory.
        file_size (int): The size of the model in bytes.
        name (str): Name of the model.
        description (None | str): Model description
        source (str): The original source of the model (path, URL or repo_id).
        source_type (ModelSourceType): Model source type.
        source_api_response (None | str): The original API response from the source, as stringified JSON.
        source_url (None | str): Optional URL for the model (e.g. download page or model page).
        cover_image (None | str): Url for image to preview model
        type_ (Literal['main']):  Default: 'main'.
        trigger_phrases (list[str] | None): Set of trigger phrases for this model
        default_settings (MainModelDefaultSettings | None): Default settings for this model
        config_path (None | str): Path to the config for this model, if any.
        base (Literal['flux2']):  Default: 'flux2'.
        format_ (Literal['gguf_quantized']):  Default: 'gguf_quantized'.
        variant (Flux2VariantType): FLUX.2 model variants.
    """

    key: str
    hash_: str
    path: str
    file_size: int
    name: str
    description: None | str
    source: str
    source_type: ModelSourceType
    source_api_response: None | str
    source_url: None | str
    cover_image: None | str
    trigger_phrases: list[str] | None
    default_settings: MainModelDefaultSettings | None
    config_path: None | str
    variant: Flux2VariantType
    type_: Literal["main"] = "main"
    base: Literal["flux2"] = "flux2"
    format_: Literal["gguf_quantized"] = "gguf_quantized"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.main_model_default_settings import MainModelDefaultSettings

        key = self.key

        hash_ = self.hash_

        path = self.path

        file_size = self.file_size

        name = self.name

        description: None | str
        description = self.description

        source = self.source

        source_type = self.source_type.value

        source_api_response: None | str
        source_api_response = self.source_api_response

        source_url: None | str
        source_url = self.source_url

        cover_image: None | str
        cover_image = self.cover_image

        type_ = self.type_

        trigger_phrases: list[str] | None
        if isinstance(self.trigger_phrases, list):
            trigger_phrases = self.trigger_phrases

        else:
            trigger_phrases = self.trigger_phrases

        default_settings: dict[str, Any] | None
        if isinstance(self.default_settings, MainModelDefaultSettings):
            default_settings = self.default_settings.to_dict()
        else:
            default_settings = self.default_settings

        config_path: None | str
        config_path = self.config_path

        base = self.base

        format_ = self.format_

        variant = self.variant.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "hash": hash_,
                "path": path,
                "file_size": file_size,
                "name": name,
                "description": description,
                "source": source,
                "source_type": source_type,
                "source_api_response": source_api_response,
                "source_url": source_url,
                "cover_image": cover_image,
                "type": type_,
                "trigger_phrases": trigger_phrases,
                "default_settings": default_settings,
                "config_path": config_path,
                "base": base,
                "format": format_,
                "variant": variant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.main_model_default_settings import MainModelDefaultSettings

        d = dict(src_dict)
        key = d.pop("key")

        hash_ = d.pop("hash")

        path = d.pop("path")

        file_size = d.pop("file_size")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        source = d.pop("source")

        source_type = ModelSourceType(d.pop("source_type"))

        def _parse_source_api_response(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_api_response = _parse_source_api_response(d.pop("source_api_response"))

        def _parse_source_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_url = _parse_source_url(d.pop("source_url"))

        def _parse_cover_image(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_image = _parse_cover_image(d.pop("cover_image"))

        type_ = cast(Literal["main"], d.pop("type"))
        if type_ != "main":
            raise ValueError(f"type must match const 'main', got '{type_}'")

        def _parse_trigger_phrases(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trigger_phrases_type_0 = cast(list[str], data)

                return trigger_phrases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        trigger_phrases = _parse_trigger_phrases(d.pop("trigger_phrases"))

        def _parse_default_settings(data: object) -> MainModelDefaultSettings | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_0 = MainModelDefaultSettings.from_dict(data)

                return default_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MainModelDefaultSettings | None, data)

        default_settings = _parse_default_settings(d.pop("default_settings"))

        def _parse_config_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        config_path = _parse_config_path(d.pop("config_path"))

        base = cast(Literal["flux2"], d.pop("base"))
        if base != "flux2":
            raise ValueError(f"base must match const 'flux2', got '{base}'")

        format_ = cast(Literal["gguf_quantized"], d.pop("format"))
        if format_ != "gguf_quantized":
            raise ValueError(f"format must match const 'gguf_quantized', got '{format_}'")

        variant = Flux2VariantType(d.pop("variant"))

        main_gguf_flux_2_config = cls(
            key=key,
            hash_=hash_,
            path=path,
            file_size=file_size,
            name=name,
            description=description,
            source=source,
            source_type=source_type,
            source_api_response=source_api_response,
            source_url=source_url,
            cover_image=cover_image,
            type_=type_,
            trigger_phrases=trigger_phrases,
            default_settings=default_settings,
            config_path=config_path,
            base=base,
            format_=format_,
            variant=variant,
        )

        main_gguf_flux_2_config.additional_properties = d
        return main_gguf_flux_2_config

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
