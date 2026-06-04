from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.model_source_type import ModelSourceType

if TYPE_CHECKING:
    from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
    from ..models.external_model_capabilities import ExternalModelCapabilities
    from ..models.external_model_panel_schema import ExternalModelPanelSchema


T = TypeVar("T", bound="ExternalApiModelConfig")


@_attrs_define
class ExternalApiModelConfig:
    """
    Attributes:
        key (str): A unique key for this model.
        hash_ (str):  Default: ''.
        path (str):  Default: ''.
        file_size (int):  Default: 0.
        name (str): Name of the model.
        description (None | str): Model description
        source (str):  Default: ''.
        source_type (ModelSourceType): Model source type.
        source_api_response (None | str): The original API response from the source, as stringified JSON.
        source_url (None | str): Optional URL for the model (e.g. download page or model page).
        cover_image (None | str): Url for image to preview model
        base (Literal['external']):  Default: 'external'.
        type_ (Literal['external_image_generator']):  Default: 'external_image_generator'.
        format_ (Literal['external_api']):  Default: 'external_api'.
        provider_id (str): External provider ID
        provider_model_id (str): Provider-specific model ID
        capabilities (ExternalModelCapabilities):
        default_settings (ExternalApiModelDefaultSettings | None):
        panel_schema (ExternalModelPanelSchema | None):
        tags (list[str] | None):
        is_default (bool):  Default: False.
    """

    key: str
    name: str
    description: None | str
    source_type: ModelSourceType
    source_api_response: None | str
    source_url: None | str
    cover_image: None | str
    provider_id: str
    provider_model_id: str
    capabilities: ExternalModelCapabilities
    default_settings: ExternalApiModelDefaultSettings | None
    panel_schema: ExternalModelPanelSchema | None
    tags: list[str] | None
    hash_: str = ""
    path: str = ""
    file_size: int = 0
    source: str = ""
    base: Literal["external"] = "external"
    type_: Literal["external_image_generator"] = "external_image_generator"
    format_: Literal["external_api"] = "external_api"
    is_default: bool = False

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
        from ..models.external_model_panel_schema import ExternalModelPanelSchema

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

        base = self.base

        type_ = self.type_

        format_ = self.format_

        provider_id = self.provider_id

        provider_model_id = self.provider_model_id

        capabilities = self.capabilities.to_dict()

        default_settings: dict[str, Any] | None
        if isinstance(self.default_settings, ExternalApiModelDefaultSettings):
            default_settings = self.default_settings.to_dict()
        else:
            default_settings = self.default_settings

        panel_schema: dict[str, Any] | None
        if isinstance(self.panel_schema, ExternalModelPanelSchema):
            panel_schema = self.panel_schema.to_dict()
        else:
            panel_schema = self.panel_schema

        tags: list[str] | None
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        is_default = self.is_default

        field_dict: dict[str, Any] = {}

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
                "base": base,
                "type": type_,
                "format": format_,
                "provider_id": provider_id,
                "provider_model_id": provider_model_id,
                "capabilities": capabilities,
                "default_settings": default_settings,
                "panel_schema": panel_schema,
                "tags": tags,
                "is_default": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_api_model_default_settings import ExternalApiModelDefaultSettings
        from ..models.external_model_capabilities import ExternalModelCapabilities
        from ..models.external_model_panel_schema import ExternalModelPanelSchema

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

        base = cast(Literal["external"], d.pop("base"))
        if base != "external":
            raise ValueError(f"base must match const 'external', got '{base}'")

        type_ = cast(Literal["external_image_generator"], d.pop("type"))
        if type_ != "external_image_generator":
            raise ValueError(f"type must match const 'external_image_generator', got '{type_}'")

        format_ = cast(Literal["external_api"], d.pop("format"))
        if format_ != "external_api":
            raise ValueError(f"format must match const 'external_api', got '{format_}'")

        provider_id = d.pop("provider_id")

        provider_model_id = d.pop("provider_model_id")

        capabilities = ExternalModelCapabilities.from_dict(d.pop("capabilities"))

        def _parse_default_settings(data: object) -> ExternalApiModelDefaultSettings | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_0 = ExternalApiModelDefaultSettings.from_dict(data)

                return default_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalApiModelDefaultSettings | None, data)

        default_settings = _parse_default_settings(d.pop("default_settings"))

        def _parse_panel_schema(data: object) -> ExternalModelPanelSchema | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                panel_schema_type_0 = ExternalModelPanelSchema.from_dict(data)

                return panel_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalModelPanelSchema | None, data)

        panel_schema = _parse_panel_schema(d.pop("panel_schema"))

        def _parse_tags(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tags = _parse_tags(d.pop("tags"))

        is_default = d.pop("is_default")

        external_api_model_config = cls(
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
            base=base,
            type_=type_,
            format_=format_,
            provider_id=provider_id,
            provider_model_id=provider_model_id,
            capabilities=capabilities,
            default_settings=default_settings,
            panel_schema=panel_schema,
            tags=tags,
            is_default=is_default,
        )

        return external_api_model_config
