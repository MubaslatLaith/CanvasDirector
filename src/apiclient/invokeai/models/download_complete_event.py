from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DownloadCompleteEvent")


@_attrs_define
class DownloadCompleteEvent:
    """Event model for download_complete

    Attributes:
        timestamp (int): The timestamp of the event
        source (str): The source of the download
        download_path (str): The local path where the download is saved
        total_bytes (int): The total number of bytes downloaded
    """

    timestamp: int
    source: str
    download_path: str
    total_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        source = self.source

        download_path = self.download_path

        total_bytes = self.total_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "source": source,
                "download_path": download_path,
                "total_bytes": total_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        source = d.pop("source")

        download_path = d.pop("download_path")

        total_bytes = d.pop("total_bytes")

        download_complete_event = cls(
            timestamp=timestamp,
            source=source,
            download_path=download_path,
            total_bytes=total_bytes,
        )

        download_complete_event.additional_properties = d
        return download_complete_event

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
