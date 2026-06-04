from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ItemIdsResult")


@_attrs_define
class ItemIdsResult:
    """Response containing ordered item ids with metadata for optimistic updates.

    Attributes:
        item_ids (list[int]): Ordered list of item ids
        total_count (int): Total number of queue items matching the query
    """

    item_ids: list[int]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_ids = self.item_ids

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_ids": item_ids,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_ids = cast(list[int], d.pop("item_ids"))

        total_count = d.pop("total_count")

        item_ids_result = cls(
            item_ids=item_ids,
            total_count=total_count,
        )

        item_ids_result.additional_properties = d
        return item_ids_result

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
