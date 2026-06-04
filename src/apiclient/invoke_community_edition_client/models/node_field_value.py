from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="NodeFieldValue")


@_attrs_define
class NodeFieldValue:
    """
    Attributes:
        node_path (str): The node into which this batch data item will be substituted.
        field_name (str): The field into which this batch data item will be substituted.
        value (float | ImageField | int | str): The value to substitute into the node/field.
    """

    node_path: str
    field_name: str
    value: float | ImageField | int | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField

        node_path = self.node_path

        field_name = self.field_name

        value: dict[str, Any] | float | int | str
        if isinstance(self.value, ImageField):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_path": node_path,
                "field_name": field_name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        node_path = d.pop("node_path")

        field_name = d.pop("field_name")

        def _parse_value(data: object) -> float | ImageField | int | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_3 = ImageField.from_dict(data)

                return value_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | ImageField | int | str, data)

        value = _parse_value(d.pop("value"))

        node_field_value = cls(
            node_path=node_path,
            field_name=field_name,
            value=value,
        )

        node_field_value.additional_properties = d
        return node_field_value

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
