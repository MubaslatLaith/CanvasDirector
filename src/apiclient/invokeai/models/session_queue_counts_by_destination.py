from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionQueueCountsByDestination")


@_attrs_define
class SessionQueueCountsByDestination:
    """
    Attributes:
        queue_id (str): The ID of the queue
        destination (str): The destination of queue items included in this status
        pending (int): Number of queue items with status 'pending' for the destination
        in_progress (int): Number of queue items with status 'in_progress' for the destination
        completed (int): Number of queue items with status 'complete' for the destination
        failed (int): Number of queue items with status 'error' for the destination
        canceled (int): Number of queue items with status 'canceled' for the destination
        total (int): Total number of queue items for the destination
    """

    queue_id: str
    destination: str
    pending: int
    in_progress: int
    completed: int
    failed: int
    canceled: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_id = self.queue_id

        destination = self.destination

        pending = self.pending

        in_progress = self.in_progress

        completed = self.completed

        failed = self.failed

        canceled = self.canceled

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue_id": queue_id,
                "destination": destination,
                "pending": pending,
                "in_progress": in_progress,
                "completed": completed,
                "failed": failed,
                "canceled": canceled,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queue_id = d.pop("queue_id")

        destination = d.pop("destination")

        pending = d.pop("pending")

        in_progress = d.pop("in_progress")

        completed = d.pop("completed")

        failed = d.pop("failed")

        canceled = d.pop("canceled")

        total = d.pop("total")

        session_queue_counts_by_destination = cls(
            queue_id=queue_id,
            destination=destination,
            pending=pending,
            in_progress=in_progress,
            completed=completed,
            failed=failed,
            canceled=canceled,
            total=total,
        )

        session_queue_counts_by_destination.additional_properties = d
        return session_queue_counts_by_destination

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
