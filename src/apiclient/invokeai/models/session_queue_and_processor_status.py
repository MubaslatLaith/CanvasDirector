from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.session_processor_status import SessionProcessorStatus
    from ..models.session_queue_status import SessionQueueStatus


T = TypeVar("T", bound="SessionQueueAndProcessorStatus")


@_attrs_define
class SessionQueueAndProcessorStatus:
    """The overall status of session queue and processor

    Attributes:
        queue (SessionQueueStatus):
        processor (SessionProcessorStatus):
    """

    queue: SessionQueueStatus
    processor: SessionProcessorStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue = self.queue.to_dict()

        processor = self.processor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue": queue,
                "processor": processor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_processor_status import SessionProcessorStatus
        from ..models.session_queue_status import SessionQueueStatus

        d = dict(src_dict)
        queue = SessionQueueStatus.from_dict(d.pop("queue"))

        processor = SessionProcessorStatus.from_dict(d.pop("processor"))

        session_queue_and_processor_status = cls(
            queue=queue,
            processor=processor,
        )

        session_queue_and_processor_status.additional_properties = d
        return session_queue_and_processor_status

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
