from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BoundingBoxField")


@_attrs_define
class BoundingBoxField:
    """A bounding box primitive value.

    Attributes:
        x_min (int): The minimum x-coordinate of the bounding box (inclusive).
        x_max (int): The maximum x-coordinate of the bounding box (exclusive).
        y_min (int): The minimum y-coordinate of the bounding box (inclusive).
        y_max (int): The maximum y-coordinate of the bounding box (exclusive).
        score (float | None | Unset): The score associated with the bounding box. In the range [0, 1]. This value is
            typically set when the bounding box was produced by a detector and has an associated confidence score.
    """

    x_min: int
    x_max: int
    y_min: int
    y_max: int
    score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x_min = self.x_min

        x_max = self.x_max

        y_min = self.y_min

        y_max = self.y_max

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x_min": x_min,
                "x_max": x_max,
                "y_min": y_min,
                "y_max": y_max,
            }
        )
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x_min = d.pop("x_min")

        x_max = d.pop("x_max")

        y_min = d.pop("y_min")

        y_max = d.pop("y_max")

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        bounding_box_field = cls(
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            score=score,
        )

        bounding_box_field.additional_properties = d
        return bounding_box_field

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
