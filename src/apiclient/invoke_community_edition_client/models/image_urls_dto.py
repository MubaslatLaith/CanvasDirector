from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImageUrlsDTO")


@_attrs_define
class ImageUrlsDTO:
    """The URLs for an image and its thumbnail.

    Attributes:
        image_name (str): The unique name of the image.
        image_url (str): The URL of the image.
        thumbnail_url (str): The URL of the image's thumbnail.
    """

    image_name: str
    image_url: str
    thumbnail_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_name = self.image_name

        image_url = self.image_url

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_name": image_name,
                "image_url": image_url,
                "thumbnail_url": thumbnail_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_name = d.pop("image_name")

        image_url = d.pop("image_url")

        thumbnail_url = d.pop("thumbnail_url")

        image_urls_dto = cls(
            image_name=image_name,
            image_url=image_url,
            thumbnail_url=thumbnail_url,
        )

        image_urls_dto.additional_properties = d
        return image_urls_dto

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
