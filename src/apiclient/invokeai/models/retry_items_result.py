from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RetryItemsResult")


@_attrs_define
class RetryItemsResult:
    """
    Attributes:
        queue_id (str): The ID of the queue
        retried_item_ids (list[int]): The IDs of the queue items that were retried
    """

    queue_id: str
    retried_item_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_id = self.queue_id

        retried_item_ids = self.retried_item_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue_id": queue_id,
                "retried_item_ids": retried_item_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queue_id = d.pop("queue_id")

        retried_item_ids = cast(list[int], d.pop("retried_item_ids"))

        retry_items_result = cls(
            queue_id=queue_id,
            retried_item_ids=retried_item_ids,
        )

        retry_items_result.additional_properties = d
        return retry_items_result

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
