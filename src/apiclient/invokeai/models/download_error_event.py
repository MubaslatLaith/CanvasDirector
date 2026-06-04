from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DownloadErrorEvent")


@_attrs_define
class DownloadErrorEvent:
    """Event model for download_error

    Attributes:
        timestamp (int): The timestamp of the event
        source (str): The source of the download
        error_type (str): The type of error
        error (str): The error message
    """

    timestamp: int
    source: str
    error_type: str
    error: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        source = self.source

        error_type = self.error_type

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "source": source,
                "error_type": error_type,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        source = d.pop("source")

        error_type = d.pop("error_type")

        error = d.pop("error")

        download_error_event = cls(
            timestamp=timestamp,
            source=source,
            error_type=error_type,
            error=error,
        )

        download_error_event.additional_properties = d
        return download_error_event

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
