from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BatchEnqueuedEvent")


@_attrs_define
class BatchEnqueuedEvent:
    """Event model for batch_enqueued

    Attributes:
        timestamp (int): The timestamp of the event
        queue_id (str): The ID of the queue
        batch_id (str): The ID of the batch
        enqueued (int): The number of invocations enqueued
        requested (int): The number of invocations initially requested to be enqueued (may be less than enqueued if
            queue was full)
        priority (int): The priority of the batch
        origin (None | str): The origin of the batch
        user_id (str): The ID of the user who enqueued the batch Default: 'system'.
    """

    timestamp: int
    queue_id: str
    batch_id: str
    enqueued: int
    requested: int
    priority: int
    origin: None | str
    user_id: str = "system"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        queue_id = self.queue_id

        batch_id = self.batch_id

        enqueued = self.enqueued

        requested = self.requested

        priority = self.priority

        origin: None | str
        origin = self.origin

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "queue_id": queue_id,
                "batch_id": batch_id,
                "enqueued": enqueued,
                "requested": requested,
                "priority": priority,
                "origin": origin,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        queue_id = d.pop("queue_id")

        batch_id = d.pop("batch_id")

        enqueued = d.pop("enqueued")

        requested = d.pop("requested")

        priority = d.pop("priority")

        def _parse_origin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        origin = _parse_origin(d.pop("origin"))

        user_id = d.pop("user_id")

        batch_enqueued_event = cls(
            timestamp=timestamp,
            queue_id=queue_id,
            batch_id=batch_id,
            enqueued=enqueued,
            requested=requested,
            priority=priority,
            origin=origin,
            user_id=user_id,
        )

        batch_enqueued_event.additional_properties = d
        return batch_enqueued_event

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
