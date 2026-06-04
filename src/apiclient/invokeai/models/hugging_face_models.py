from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HuggingFaceModels")


@_attrs_define
class HuggingFaceModels:
    """
    Attributes:
        urls (list[str] | None): URLs for all checkpoint format models in the metadata
        is_diffusers (bool): Whether the metadata is for a Diffusers format model
    """

    urls: list[str] | None
    is_diffusers: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        urls: list[str] | None
        if isinstance(self.urls, list):
            urls = self.urls

        else:
            urls = self.urls

        is_diffusers = self.is_diffusers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urls": urls,
                "is_diffusers": is_diffusers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_urls(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                urls_type_0 = cast(list[str], data)

                return urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        urls = _parse_urls(d.pop("urls"))

        is_diffusers = d.pop("is_diffusers")

        hugging_face_models = cls(
            urls=urls,
            is_diffusers=is_diffusers,
        )

        hugging_face_models.additional_properties = d
        return hugging_face_models

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
