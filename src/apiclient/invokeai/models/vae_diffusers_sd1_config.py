from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_repo_variant import ModelRepoVariant
from ..models.model_source_type import ModelSourceType

T = TypeVar("T", bound="VAEDiffusersSD1Config")


@_attrs_define
class VAEDiffusersSD1Config:
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
        type_ (Literal['vae']):  Default: 'vae'.
        base (Literal['sd-1']):  Default: 'sd-1'.
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
    format_: Literal["diffusers"] = "diffusers"
    type_: Literal["vae"] = "vae"
    base: Literal["sd-1"] = "sd-1"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
                "base": base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        type_ = cast(Literal["vae"], d.pop("type"))
        if type_ != "vae":
            raise ValueError(f"type must match const 'vae', got '{type_}'")

        base = cast(Literal["sd-1"], d.pop("base"))
        if base != "sd-1":
            raise ValueError(f"base must match const 'sd-1', got '{base}'")

        vae_diffusers_sd1_config = cls(
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
            base=base,
        )

        vae_diffusers_sd1_config.additional_properties = d
        return vae_diffusers_sd1_config

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
