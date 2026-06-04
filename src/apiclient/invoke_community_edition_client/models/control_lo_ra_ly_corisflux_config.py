from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_source_type import ModelSourceType

if TYPE_CHECKING:
    from ..models.control_adapter_default_settings import ControlAdapterDefaultSettings


T = TypeVar("T", bound="ControlLoRALyCORISFLUXConfig")


@_attrs_define
class ControlLoRALyCORISFLUXConfig:
    """Model config for Control LoRA models.

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
        default_settings (ControlAdapterDefaultSettings | None):
        base (Literal['flux']):  Default: 'flux'.
        type_ (Literal['control_lora']):  Default: 'control_lora'.
        format_ (Literal['lycoris']):  Default: 'lycoris'.
        trigger_phrases (list[str] | None):
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
    default_settings: ControlAdapterDefaultSettings | None
    trigger_phrases: list[str] | None
    base: Literal["flux"] = "flux"
    type_: Literal["control_lora"] = "control_lora"
    format_: Literal["lycoris"] = "lycoris"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_adapter_default_settings import ControlAdapterDefaultSettings

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

        default_settings: dict[str, Any] | None
        if isinstance(self.default_settings, ControlAdapterDefaultSettings):
            default_settings = self.default_settings.to_dict()
        else:
            default_settings = self.default_settings

        base = self.base

        type_ = self.type_

        format_ = self.format_

        trigger_phrases: list[str] | None
        if isinstance(self.trigger_phrases, list):
            trigger_phrases = self.trigger_phrases

        else:
            trigger_phrases = self.trigger_phrases

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
                "default_settings": default_settings,
                "base": base,
                "type": type_,
                "format": format_,
                "trigger_phrases": trigger_phrases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_adapter_default_settings import ControlAdapterDefaultSettings

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

        def _parse_default_settings(data: object) -> ControlAdapterDefaultSettings | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_settings_type_0 = ControlAdapterDefaultSettings.from_dict(data)

                return default_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlAdapterDefaultSettings | None, data)

        default_settings = _parse_default_settings(d.pop("default_settings"))

        base = cast(Literal["flux"], d.pop("base"))
        if base != "flux":
            raise ValueError(f"base must match const 'flux', got '{base}'")

        type_ = cast(Literal["control_lora"], d.pop("type"))
        if type_ != "control_lora":
            raise ValueError(f"type must match const 'control_lora', got '{type_}'")

        format_ = cast(Literal["lycoris"], d.pop("format"))
        if format_ != "lycoris":
            raise ValueError(f"format must match const 'lycoris', got '{format_}'")

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

        control_lo_ra_ly_corisflux_config = cls(
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
            default_settings=default_settings,
            base=base,
            type_=type_,
            format_=format_,
            trigger_phrases=trigger_phrases,
        )

        control_lo_ra_ly_corisflux_config.additional_properties = d
        return control_lo_ra_ly_corisflux_config

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
