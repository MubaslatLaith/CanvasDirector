from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_source_type import ModelSourceType

T = TypeVar("T", bound="QwenVLEncoderDiffusersConfig")


@_attrs_define
class QwenVLEncoderDiffusersConfig:
    """Configuration for standalone Qwen2.5-VL encoder models in diffusers-style folder layout.

    Expected structure:
        <model_root>/
            text_encoder/
                config.json (with `_class_name` or `architectures` listing
                             `Qwen2_5_VLForConditionalGeneration`)
                model.safetensors
            tokenizer/
                tokenizer_config.json
                ...
            processor/                  (optional, for vision preprocessing)
                preprocessor_config.json

    This lets users avoid downloading the full ~40 GB Qwen Image diffusers pipeline
    when they only need the Qwen2.5-VL encoder for use with a GGUF transformer.

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
            base (Literal['any']):  Default: 'any'.
            type_ (Literal['qwen_vl_encoder']):  Default: 'qwen_vl_encoder'.
            format_ (Literal['qwen_vl_encoder']):  Default: 'qwen_vl_encoder'.
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
    base: Literal["any"] = "any"
    type_: Literal["qwen_vl_encoder"] = "qwen_vl_encoder"
    format_: Literal["qwen_vl_encoder"] = "qwen_vl_encoder"
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

        base = self.base

        type_ = self.type_

        format_ = self.format_

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
                "base": base,
                "type": type_,
                "format": format_,
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

        base = cast(Literal["any"], d.pop("base"))
        if base != "any":
            raise ValueError(f"base must match const 'any', got '{base}'")

        type_ = cast(Literal["qwen_vl_encoder"], d.pop("type"))
        if type_ != "qwen_vl_encoder":
            raise ValueError(f"type must match const 'qwen_vl_encoder', got '{type_}'")

        format_ = cast(Literal["qwen_vl_encoder"], d.pop("format"))
        if format_ != "qwen_vl_encoder":
            raise ValueError(f"format must match const 'qwen_vl_encoder', got '{format_}'")

        qwen_vl_encoder_diffusers_config = cls(
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
        )

        qwen_vl_encoder_diffusers_config.additional_properties = d
        return qwen_vl_encoder_diffusers_config

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
