from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remote_model_file import RemoteModelFile


T = TypeVar("T", bound="HuggingFaceMetadata")


@_attrs_define
class HuggingFaceMetadata:
    """Extended metadata fields provided by HuggingFace.

    Attributes:
        name (str): model's name
        id (str): The HF model id
        files (list[RemoteModelFile] | Unset): model files and their sizes
        type_ (Literal['huggingface'] | Unset):  Default: 'huggingface'.
        api_response (None | str | Unset): Response from the HF API as stringified JSON
        is_diffusers (bool | Unset): Whether the metadata is for a Diffusers format model Default: False.
        ckpt_urls (list[str] | None | Unset): URLs for all checkpoint format models in the metadata
    """

    name: str
    id: str
    files: list[RemoteModelFile] | Unset = UNSET
    type_: Literal["huggingface"] | Unset = "huggingface"
    api_response: None | str | Unset = UNSET
    is_diffusers: bool | Unset = False
    ckpt_urls: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        type_ = self.type_

        api_response: None | str | Unset
        if isinstance(self.api_response, Unset):
            api_response = UNSET
        else:
            api_response = self.api_response

        is_diffusers = self.is_diffusers

        ckpt_urls: list[str] | None | Unset
        if isinstance(self.ckpt_urls, Unset):
            ckpt_urls = UNSET
        elif isinstance(self.ckpt_urls, list):
            ckpt_urls = self.ckpt_urls

        else:
            ckpt_urls = self.ckpt_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files
        if type_ is not UNSET:
            field_dict["type"] = type_
        if api_response is not UNSET:
            field_dict["api_response"] = api_response
        if is_diffusers is not UNSET:
            field_dict["is_diffusers"] = is_diffusers
        if ckpt_urls is not UNSET:
            field_dict["ckpt_urls"] = ckpt_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remote_model_file import RemoteModelFile

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id")

        _files = d.pop("files", UNSET)
        files: list[RemoteModelFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = RemoteModelFile.from_dict(files_item_data)

                files.append(files_item)

        type_ = cast(Literal["huggingface"] | Unset, d.pop("type", UNSET))
        if type_ != "huggingface" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'huggingface', got '{type_}'")

        def _parse_api_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_response = _parse_api_response(d.pop("api_response", UNSET))

        is_diffusers = d.pop("is_diffusers", UNSET)

        def _parse_ckpt_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ckpt_urls_type_0 = cast(list[str], data)

                return ckpt_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ckpt_urls = _parse_ckpt_urls(d.pop("ckpt_urls", UNSET))

        hugging_face_metadata = cls(
            name=name,
            id=id,
            files=files,
            type_=type_,
            api_response=api_response,
            is_diffusers=is_diffusers,
            ckpt_urls=ckpt_urls,
        )

        hugging_face_metadata.additional_properties = d
        return hugging_face_metadata

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
