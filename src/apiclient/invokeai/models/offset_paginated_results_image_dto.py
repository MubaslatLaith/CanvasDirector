from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.image_dto import ImageDTO


T = TypeVar("T", bound="OffsetPaginatedResultsImageDTO")


@_attrs_define
class OffsetPaginatedResultsImageDTO:
    """
    Attributes:
        limit (int): Limit of items to get
        offset (int): Offset from which to retrieve items
        total (int): Total number of items in result
        items (list[ImageDTO]): Items
    """

    limit: int
    offset: int
    total: int
    items: list[ImageDTO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        total = self.total

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
                "total": total,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_dto import ImageDTO

        d = dict(src_dict)
        limit = d.pop("limit")

        offset = d.pop("offset")

        total = d.pop("total")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ImageDTO.from_dict(items_item_data)

            items.append(items_item)

        offset_paginated_results_image_dto = cls(
            limit=limit,
            offset=offset,
            total=total,
            items=items,
        )

        offset_paginated_results_image_dto.additional_properties = d
        return offset_paginated_results_image_dto

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
