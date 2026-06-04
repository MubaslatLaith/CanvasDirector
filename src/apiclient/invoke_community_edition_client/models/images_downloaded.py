from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImagesDownloaded")


@_attrs_define
class ImagesDownloaded:
    """
    Attributes:
        response (None | str | Unset): The message to display to the user when images begin downloading
        bulk_download_item_name (None | str | Unset): The name of the bulk download item for which events will be
            emitted
    """

    response: None | str | Unset = UNSET
    bulk_download_item_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response: None | str | Unset
        if isinstance(self.response, Unset):
            response = UNSET
        else:
            response = self.response

        bulk_download_item_name: None | str | Unset
        if isinstance(self.bulk_download_item_name, Unset):
            bulk_download_item_name = UNSET
        else:
            bulk_download_item_name = self.bulk_download_item_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response is not UNSET:
            field_dict["response"] = response
        if bulk_download_item_name is not UNSET:
            field_dict["bulk_download_item_name"] = bulk_download_item_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response = _parse_response(d.pop("response", UNSET))

        def _parse_bulk_download_item_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bulk_download_item_name = _parse_bulk_download_item_name(d.pop("bulk_download_item_name", UNSET))

        images_downloaded = cls(
            response=response,
            bulk_download_item_name=bulk_download_item_name,
        )

        images_downloaded.additional_properties = d
        return images_downloaded

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
