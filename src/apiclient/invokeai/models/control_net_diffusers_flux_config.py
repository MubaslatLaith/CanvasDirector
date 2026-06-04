from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_repo_variant import ModelRepoVariant
from ..models.model_source_type import ModelSourceType

if TYPE_CHECKING:
    from ..models.control_adapter_default_settings import ControlAdapterDefaultSettings


T = TypeVar("T", bound="ControlNetDiffusersFLUXConfig")


@_attrs_define
class ControlNetDiffusersFLUXConfig:
    """
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
        format_ (Literal['diffusers']):  Default: 'diffusers'.
        repo_variant (ModelRepoVariant): Various hugging face variants on the diffusers format.
        type_ (Literal['controlnet']):  Default: 'controlnet'.
        default_settings (ControlAdapterDefaultSettings | None):
        base (Literal['flux']):  Default: 'flux'.
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
    repo_variant: ModelRepoVariant
    default_settings: ControlAdapterDefaultSettings | None
    format_: Literal["diffusers"] = "diffusers"
    type_: Literal["controlnet"] = "controlnet"
    base: Literal["flux"] = "flux"
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

        format_ = self.format_

        repo_variant = self.repo_variant.value

        type_ = self.type_

        default_settings: dict[str, Any] | None
        if isinstance(self.default_settings, ControlAdapterDefaultSettings):
            default_settings = self.default_settings.to_dict()
        else:
            default_settings = self.default_settings

        base = self.base

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
                "format": format_,
                "repo_variant": repo_variant,
                "type": type_,
                "default_settings": default_settings,
                "base": base,
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

        format_ = cast(Literal["diffusers"], d.pop("format"))
        if format_ != "diffusers":
            raise ValueError(f"format must match const 'diffusers', got '{format_}'")

        repo_variant = ModelRepoVariant(d.pop("repo_variant"))

        type_ = cast(Literal["controlnet"], d.pop("type"))
        if type_ != "controlnet":
            raise ValueError(f"type must match const 'controlnet', got '{type_}'")

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

        control_net_diffusers_flux_config = cls(
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
            format_=format_,
            repo_variant=repo_variant,
            type_=type_,
            default_settings=default_settings,
            base=base,
        )

        control_net_diffusers_flux_config.additional_properties = d
        return control_net_diffusers_flux_config

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
