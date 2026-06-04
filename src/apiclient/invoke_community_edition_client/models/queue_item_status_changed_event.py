from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.queue_item_status_changed_event_status import QueueItemStatusChangedEventStatus

if TYPE_CHECKING:
    from ..models.batch_status import BatchStatus
    from ..models.session_queue_status import SessionQueueStatus


T = TypeVar("T", bound="QueueItemStatusChangedEvent")


@_attrs_define
class QueueItemStatusChangedEvent:
    """Event model for queue_item_status_changed

    Attributes:
        timestamp (int): The timestamp of the event
        queue_id (str): The ID of the queue
        item_id (int): The ID of the queue item
        batch_id (str): The ID of the queue batch
        origin (None | str): The origin of the queue item
        destination (None | str): The destination of the queue item
        user_id (str): The ID of the user who created the queue item Default: 'system'.
        status (QueueItemStatusChangedEventStatus): The new status of the queue item
        status_sequence (int | None): A monotonically increasing version for this queue item's visible status lifecycle
        error_type (None | str): The error type, if any
        error_message (None | str): The error message, if any
        error_traceback (None | str): The error traceback, if any
        created_at (str): The timestamp when the queue item was created
        updated_at (str): The timestamp when the queue item was last updated
        started_at (None | str): The timestamp when the queue item was started
        completed_at (None | str): The timestamp when the queue item was completed
        batch_status (BatchStatus):
        queue_status (SessionQueueStatus):
        session_id (str): The ID of the session (aka graph execution state)
    """

    timestamp: int
    queue_id: str
    item_id: int
    batch_id: str
    origin: None | str
    destination: None | str
    status: QueueItemStatusChangedEventStatus
    status_sequence: int | None
    error_type: None | str
    error_message: None | str
    error_traceback: None | str
    created_at: str
    updated_at: str
    started_at: None | str
    completed_at: None | str
    batch_status: BatchStatus
    queue_status: SessionQueueStatus
    session_id: str
    user_id: str = "system"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        queue_id = self.queue_id

        item_id = self.item_id

        batch_id = self.batch_id

        origin: None | str
        origin = self.origin

        destination: None | str
        destination = self.destination

        user_id = self.user_id

        status = self.status.value

        status_sequence: int | None
        status_sequence = self.status_sequence

        error_type: None | str
        error_type = self.error_type

        error_message: None | str
        error_message = self.error_message

        error_traceback: None | str
        error_traceback = self.error_traceback

        created_at = self.created_at

        updated_at = self.updated_at

        started_at: None | str
        started_at = self.started_at

        completed_at: None | str
        completed_at = self.completed_at

        batch_status = self.batch_status.to_dict()

        queue_status = self.queue_status.to_dict()

        session_id = self.session_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "queue_id": queue_id,
                "item_id": item_id,
                "batch_id": batch_id,
                "origin": origin,
                "destination": destination,
                "user_id": user_id,
                "status": status,
                "status_sequence": status_sequence,
                "error_type": error_type,
                "error_message": error_message,
                "error_traceback": error_traceback,
                "created_at": created_at,
                "updated_at": updated_at,
                "started_at": started_at,
                "completed_at": completed_at,
                "batch_status": batch_status,
                "queue_status": queue_status,
                "session_id": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_status import BatchStatus
        from ..models.session_queue_status import SessionQueueStatus

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        queue_id = d.pop("queue_id")

        item_id = d.pop("item_id")

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

        user_id = d.pop("user_id")

        status = QueueItemStatusChangedEventStatus(d.pop("status"))

        def _parse_status_sequence(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        status_sequence = _parse_status_sequence(d.pop("status_sequence"))

        def _parse_error_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_type = _parse_error_type(d.pop("error_type"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        def _parse_error_traceback(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_traceback = _parse_error_traceback(d.pop("error_traceback"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        batch_status = BatchStatus.from_dict(d.pop("batch_status"))

        queue_status = SessionQueueStatus.from_dict(d.pop("queue_status"))

        session_id = d.pop("session_id")

        queue_item_status_changed_event = cls(
            timestamp=timestamp,
            queue_id=queue_id,
            item_id=item_id,
            batch_id=batch_id,
            origin=origin,
            destination=destination,
            user_id=user_id,
            status=status,
            status_sequence=status_sequence,
            error_type=error_type,
            error_message=error_message,
            error_traceback=error_traceback,
            created_at=created_at,
            updated_at=updated_at,
            started_at=started_at,
            completed_at=completed_at,
            batch_status=batch_status,
            queue_status=queue_status,
            session_id=session_id,
        )

        queue_item_status_changed_event.additional_properties = d
        return queue_item_status_changed_event

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
