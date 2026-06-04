from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch import Batch


T = TypeVar("T", bound="EnqueueBatchResult")


@_attrs_define
class EnqueueBatchResult:
    """
    Attributes:
        queue_id (str): The ID of the queue
        enqueued (int): The total number of queue items enqueued
        requested (int): The total number of queue items requested to be enqueued
        batch (Batch):
        priority (int): The priority of the enqueued batch
        item_ids (list[int]): The IDs of the queue items that were enqueued
    """

    queue_id: str
    enqueued: int
    requested: int
    batch: Batch
    priority: int
    item_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_id = self.queue_id

        enqueued = self.enqueued

        requested = self.requested

        batch = self.batch.to_dict()

        priority = self.priority

        item_ids = self.item_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue_id": queue_id,
                "enqueued": enqueued,
                "requested": requested,
                "batch": batch,
                "priority": priority,
                "item_ids": item_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch import Batch

        d = dict(src_dict)
        queue_id = d.pop("queue_id")

        enqueued = d.pop("enqueued")

        requested = d.pop("requested")

        batch = Batch.from_dict(d.pop("batch"))

        priority = d.pop("priority")

        item_ids = cast(list[int], d.pop("item_ids"))

        enqueue_batch_result = cls(
            queue_id=queue_id,
            enqueued=enqueued,
            requested=requested,
            batch=batch,
            priority=priority,
            item_ids=item_ids,
        )

        enqueue_batch_result.additional_properties = d
        return enqueue_batch_result

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
