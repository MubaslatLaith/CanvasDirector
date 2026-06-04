from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="BatchDatum")


@_attrs_define
class BatchDatum:
    """
    Attributes:
        node_path (str): The node into which this batch data collection will be substituted.
        field_name (str): The field into which this batch data collection will be substituted.
        items (list[float | ImageField | int | str] | Unset): The list of items to substitute into the node/field.
    """

    node_path: str
    field_name: str
    items: list[float | ImageField | int | str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField

        node_path = self.node_path

        field_name = self.field_name

        items: list[dict[str, Any] | float | int | str] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item: dict[str, Any] | float | int | str
                if isinstance(items_item_data, ImageField):
                    items_item = items_item_data.to_dict()
                else:
                    items_item = items_item_data
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_path": node_path,
                "field_name": field_name,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        node_path = d.pop("node_path")

        field_name = d.pop("field_name")

        _items = d.pop("items", UNSET)
        items: list[float | ImageField | int | str] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:

                def _parse_items_item(data: object) -> float | ImageField | int | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_item_type_3 = ImageField.from_dict(data)

                        return items_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(float | ImageField | int | str, data)

                items_item = _parse_items_item(items_item_data)

                items.append(items_item)

        batch_datum = cls(
            node_path=node_path,
            field_name=field_name,
            items=items,
        )

        batch_datum.additional_properties = d
        return batch_datum

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
