from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.session_queue_item_status import SessionQueueItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_execution_state import GraphExecutionState
    from ..models.node_field_value import NodeFieldValue
    from ..models.workflow_without_id import WorkflowWithoutID


T = TypeVar("T", bound="SessionQueueItem")


@_attrs_define
class SessionQueueItem:
    """Session queue item without the full graph. Used for serialization.

    Attributes:
        item_id (int): The identifier of the session queue item
        status (SessionQueueItemStatus): The status of this queue item Default: SessionQueueItemStatus.PENDING.
        priority (int): The priority of this queue item Default: 0.
        batch_id (str): The ID of the batch associated with this queue item
        session_id (str): The ID of the session associated with this queue item. The session doesn't exist in
            graph_executions until the queue item is executed.
        created_at (datetime.datetime | str): When this queue item was created
        updated_at (datetime.datetime | str): When this queue item was updated
        queue_id (str): The id of the queue with which this item is associated
        session (GraphExecutionState): Tracks source-graph expansion, execution progress, and runtime results.
        status_sequence (int | None | Unset): A monotonically increasing version for this queue item's visible status
            lifecycle
        origin (None | str | Unset): The origin of this queue item. This data is used by the frontend to determine how
            to handle results.
        destination (None | str | Unset): The origin of this queue item. This data is used by the frontend to determine
            how to handle results
        error_type (None | str | Unset): The error type if this queue item errored
        error_message (None | str | Unset): The error message if this queue item errored
        error_traceback (None | str | Unset): The error traceback if this queue item errored
        started_at (datetime.datetime | None | str | Unset): When this queue item was started
        completed_at (datetime.datetime | None | str | Unset): When this queue item was completed
        user_id (str | Unset): The id of the user who created this queue item Default: 'system'.
        user_display_name (None | str | Unset): The display name of the user who created this queue item, if available
        user_email (None | str | Unset): The email of the user who created this queue item, if available
        field_values (list[NodeFieldValue] | None | Unset): The field values that were used for this queue item
        retried_from_item_id (int | None | Unset): The item_id of the queue item that this item was retried from
        workflow (None | Unset | WorkflowWithoutID): The workflow associated with this queue item
    """

    item_id: int
    batch_id: str
    session_id: str
    created_at: datetime.datetime | str
    updated_at: datetime.datetime | str
    queue_id: str
    session: GraphExecutionState
    status: SessionQueueItemStatus = SessionQueueItemStatus.PENDING
    priority: int = 0
    status_sequence: int | None | Unset = UNSET
    origin: None | str | Unset = UNSET
    destination: None | str | Unset = UNSET
    error_type: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    error_traceback: None | str | Unset = UNSET
    started_at: datetime.datetime | None | str | Unset = UNSET
    completed_at: datetime.datetime | None | str | Unset = UNSET
    user_id: str | Unset = "system"
    user_display_name: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    field_values: list[NodeFieldValue] | None | Unset = UNSET
    retried_from_item_id: int | None | Unset = UNSET
    workflow: None | Unset | WorkflowWithoutID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_without_id import WorkflowWithoutID

        item_id = self.item_id

        status = self.status.value

        priority = self.priority

        batch_id = self.batch_id

        session_id = self.session_id

        created_at: str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        queue_id = self.queue_id

        session = self.session.to_dict()

        status_sequence: int | None | Unset
        if isinstance(self.status_sequence, Unset):
            status_sequence = UNSET
        else:
            status_sequence = self.status_sequence

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        destination: None | str | Unset
        if isinstance(self.destination, Unset):
            destination = UNSET
        else:
            destination = self.destination

        error_type: None | str | Unset
        if isinstance(self.error_type, Unset):
            error_type = UNSET
        else:
            error_type = self.error_type

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        error_traceback: None | str | Unset
        if isinstance(self.error_traceback, Unset):
            error_traceback = UNSET
        else:
            error_traceback = self.error_traceback

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        user_id = self.user_id

        user_display_name: None | str | Unset
        if isinstance(self.user_display_name, Unset):
            user_display_name = UNSET
        else:
            user_display_name = self.user_display_name

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        field_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.field_values, Unset):
            field_values = UNSET
        elif isinstance(self.field_values, list):
            field_values = []
            for field_values_type_0_item_data in self.field_values:
                field_values_type_0_item = field_values_type_0_item_data.to_dict()
                field_values.append(field_values_type_0_item)

        else:
            field_values = self.field_values

        retried_from_item_id: int | None | Unset
        if isinstance(self.retried_from_item_id, Unset):
            retried_from_item_id = UNSET
        else:
            retried_from_item_id = self.retried_from_item_id

        workflow: dict[str, Any] | None | Unset
        if isinstance(self.workflow, Unset):
            workflow = UNSET
        elif isinstance(self.workflow, WorkflowWithoutID):
            workflow = self.workflow.to_dict()
        else:
            workflow = self.workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "status": status,
                "priority": priority,
                "batch_id": batch_id,
                "session_id": session_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "queue_id": queue_id,
                "session": session,
            }
        )
        if status_sequence is not UNSET:
            field_dict["status_sequence"] = status_sequence
        if origin is not UNSET:
            field_dict["origin"] = origin
        if destination is not UNSET:
            field_dict["destination"] = destination
        if error_type is not UNSET:
            field_dict["error_type"] = error_type
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_display_name is not UNSET:
            field_dict["user_display_name"] = user_display_name
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if field_values is not UNSET:
            field_dict["field_values"] = field_values
        if retried_from_item_id is not UNSET:
            field_dict["retried_from_item_id"] = retried_from_item_id
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_execution_state import GraphExecutionState
        from ..models.node_field_value import NodeFieldValue
        from ..models.workflow_without_id import WorkflowWithoutID

        d = dict(src_dict)
        item_id = d.pop("item_id")

        status = SessionQueueItemStatus(d.pop("status"))

        priority = d.pop("priority")

        batch_id = d.pop("batch_id")

        session_id = d.pop("session_id")

        def _parse_created_at(data: object) -> datetime.datetime | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> datetime.datetime | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        queue_id = d.pop("queue_id")

        session = GraphExecutionState.from_dict(d.pop("session"))

        def _parse_status_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_sequence = _parse_status_sequence(d.pop("status_sequence", UNSET))

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_destination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination = _parse_destination(d.pop("destination", UNSET))

        def _parse_error_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_type = _parse_error_type(d.pop("error_type", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_error_traceback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_traceback = _parse_error_traceback(d.pop("error_traceback", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        user_id = d.pop("user_id", UNSET)

        def _parse_user_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_display_name = _parse_user_display_name(d.pop("user_display_name", UNSET))

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_field_values(data: object) -> list[NodeFieldValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_values_type_0 = []
                _field_values_type_0 = data
                for field_values_type_0_item_data in _field_values_type_0:
                    field_values_type_0_item = NodeFieldValue.from_dict(field_values_type_0_item_data)

                    field_values_type_0.append(field_values_type_0_item)

                return field_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NodeFieldValue] | None | Unset, data)

        field_values = _parse_field_values(d.pop("field_values", UNSET))

        def _parse_retried_from_item_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retried_from_item_id = _parse_retried_from_item_id(d.pop("retried_from_item_id", UNSET))

        def _parse_workflow(data: object) -> None | Unset | WorkflowWithoutID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workflow_type_0 = WorkflowWithoutID.from_dict(data)

                return workflow_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowWithoutID, data)

        workflow = _parse_workflow(d.pop("workflow", UNSET))

        session_queue_item = cls(
            item_id=item_id,
            status=status,
            priority=priority,
            batch_id=batch_id,
            session_id=session_id,
            created_at=created_at,
            updated_at=updated_at,
            queue_id=queue_id,
            session=session,
            status_sequence=status_sequence,
            origin=origin,
            destination=destination,
            error_type=error_type,
            error_message=error_message,
            error_traceback=error_traceback,
            started_at=started_at,
            completed_at=completed_at,
            user_id=user_id,
            user_display_name=user_display_name,
            user_email=user_email,
            field_values=field_values,
            retried_from_item_id=retried_from_item_id,
            workflow=workflow,
        )

        session_queue_item.additional_properties = d
        return session_queue_item

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
