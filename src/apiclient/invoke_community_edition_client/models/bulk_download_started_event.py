from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkDownloadStartedEvent")


@_attrs_define
class BulkDownloadStartedEvent:
    """Event model for bulk_download_started

    Attributes:
        timestamp (int): The timestamp of the event
        bulk_download_id (str): The ID of the bulk image download
        bulk_download_item_id (str): The ID of the bulk image download item
        bulk_download_item_name (str): The name of the bulk image download item
        user_id (str): The ID of the user who initiated the download Default: 'system'.
    """

    timestamp: int
    bulk_download_id: str
    bulk_download_item_id: str
    bulk_download_item_name: str
    user_id: str = "system"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        bulk_download_id = self.bulk_download_id

        bulk_download_item_id = self.bulk_download_item_id

        bulk_download_item_name = self.bulk_download_item_name

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "bulk_download_id": bulk_download_id,
                "bulk_download_item_id": bulk_download_item_id,
                "bulk_download_item_name": bulk_download_item_name,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        bulk_download_id = d.pop("bulk_download_id")

        bulk_download_item_id = d.pop("bulk_download_item_id")

        bulk_download_item_name = d.pop("bulk_download_item_name")

        user_id = d.pop("user_id")

        bulk_download_started_event = cls(
            timestamp=timestamp,
            bulk_download_id=bulk_download_id,
            bulk_download_item_id=bulk_download_item_id,
            bulk_download_item_name=bulk_download_item_name,
            user_id=user_id,
        )

        bulk_download_started_event.additional_properties = d
        return bulk_download_started_event

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
