from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sam_point import SAMPoint


T = TypeVar("T", bound="SAMPointsField")


@_attrs_define
class SAMPointsField:
    """
    Attributes:
        points (list[SAMPoint]): The points of the object
    """

    points: list[SAMPoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sam_point import SAMPoint

        d = dict(src_dict)
        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = SAMPoint.from_dict(points_item_data)

            points.append(points_item)

        sam_points_field = cls(
            points=points,
        )

        sam_points_field.additional_properties = d
        return sam_points_field

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
