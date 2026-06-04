from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueueItemsRetriedEvent")


@_attrs_define
class QueueItemsRetriedEvent:
    """Event model for queue_items_retried

    Attributes:
        timestamp (int): The timestamp of the event
        queue_id (str): The ID of the queue
        retried_item_ids (list[int]): The IDs of the queue items that were retried
    """

    timestamp: int
    queue_id: str
    retried_item_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        queue_id = self.queue_id

        retried_item_ids = self.retried_item_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "queue_id": queue_id,
                "retried_item_ids": retried_item_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        queue_id = d.pop("queue_id")

        retried_item_ids = cast(list[int], d.pop("retried_item_ids"))

        queue_items_retried_event = cls(
            timestamp=timestamp,
            queue_id=queue_id,
            retried_item_ids=retried_item_ids,
        )

        queue_items_retried_event.additional_properties = d
        return queue_items_retried_event

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
