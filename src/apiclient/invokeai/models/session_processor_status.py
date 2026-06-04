from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionProcessorStatus")


@_attrs_define
class SessionProcessorStatus:
    """
    Attributes:
        is_started (bool): Whether the session processor is started
        is_processing (bool): Whether a session is being processed
    """

    is_started: bool
    is_processing: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_started = self.is_started

        is_processing = self.is_processing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_started": is_started,
                "is_processing": is_processing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_started = d.pop("is_started")

        is_processing = d.pop("is_processing")

        session_processor_status = cls(
            is_started=is_started,
            is_processing=is_processing,
        )

        session_processor_status.additional_properties = d
        return session_processor_status

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
