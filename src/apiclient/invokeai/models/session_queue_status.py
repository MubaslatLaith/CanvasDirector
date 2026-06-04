from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionQueueStatus")


@_attrs_define
class SessionQueueStatus:
    """
    Attributes:
        queue_id (str): The ID of the queue
        item_id (int | None): The current queue item id
        batch_id (None | str): The current queue item's batch id
        session_id (None | str): The current queue item's session id
        pending (int): Number of queue items with status 'pending'
        in_progress (int): Number of queue items with status 'in_progress'
        completed (int): Number of queue items with status 'complete'
        failed (int): Number of queue items with status 'error'
        canceled (int): Number of queue items with status 'canceled'
        total (int): Total number of queue items
    """

    queue_id: str
    item_id: int | None
    batch_id: None | str
    session_id: None | str
    pending: int
    in_progress: int
    completed: int
    failed: int
    canceled: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_id = self.queue_id

        item_id: int | None
        item_id = self.item_id

        batch_id: None | str
        batch_id = self.batch_id

        session_id: None | str
        session_id = self.session_id

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
                "item_id": item_id,
                "batch_id": batch_id,
                "session_id": session_id,
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

        def _parse_item_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        item_id = _parse_item_id(d.pop("item_id"))

        def _parse_batch_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        batch_id = _parse_batch_id(d.pop("batch_id"))

        def _parse_session_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        session_id = _parse_session_id(d.pop("session_id"))

        pending = d.pop("pending")

        in_progress = d.pop("in_progress")

        completed = d.pop("completed")

        failed = d.pop("failed")

        canceled = d.pop("canceled")

        total = d.pop("total")

        session_queue_status = cls(
            queue_id=queue_id,
            item_id=item_id,
            batch_id=batch_id,
            session_id=session_id,
            pending=pending,
            in_progress=in_progress,
            completed=completed,
            failed=failed,
            canceled=canceled,
            total=total,
        )

        session_queue_status.additional_properties = d
        return session_queue_status

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
