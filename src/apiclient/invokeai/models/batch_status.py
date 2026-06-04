from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BatchStatus")


@_attrs_define
class BatchStatus:
    """
    Attributes:
        queue_id (str): The ID of the queue
        batch_id (str): The ID of the batch
        origin (None | str): The origin of the batch
        destination (None | str): The destination of the batch
        pending (int): Number of queue items with status 'pending'
        in_progress (int): Number of queue items with status 'in_progress'
        completed (int): Number of queue items with status 'complete'
        failed (int): Number of queue items with status 'error'
        canceled (int): Number of queue items with status 'canceled'
        total (int): Total number of queue items
    """

    queue_id: str
    batch_id: str
    origin: None | str
    destination: None | str
    pending: int
    in_progress: int
    completed: int
    failed: int
    canceled: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_id = self.queue_id

        batch_id = self.batch_id

        origin: None | str
        origin = self.origin

        destination: None | str
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
                "batch_id": batch_id,
                "origin": origin,
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

        batch_id = d.pop("batch_id")

        def _parse_origin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        origin = _parse_origin(d.pop("origin"))

        def _parse_destination(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        destination = _parse_destination(d.pop("destination"))

        pending = d.pop("pending")

        in_progress = d.pop("in_progress")

        completed = d.pop("completed")

        failed = d.pop("failed")

        canceled = d.pop("canceled")

        total = d.pop("total")

        batch_status = cls(
            queue_id=queue_id,
            batch_id=batch_id,
            origin=origin,
            destination=destination,
            pending=pending,
            in_progress=in_progress,
            completed=completed,
            failed=failed,
            canceled=canceled,
            total=total,
        )

        batch_status.additional_properties = d
        return batch_status

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
