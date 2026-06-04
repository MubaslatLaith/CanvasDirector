from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BoundingBox")


@_attrs_define
class BoundingBox:
    """Create a bounding box manually by supplying box coordinates

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['bounding_box']):  Default: 'bounding_box'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        x_min (int | Unset): x-coordinate of the bounding box's top left vertex Default: 0.
        y_min (int | Unset): y-coordinate of the bounding box's top left vertex Default: 0.
        x_max (int | Unset): x-coordinate of the bounding box's bottom right vertex Default: 0.
        y_max (int | Unset): y-coordinate of the bounding box's bottom right vertex Default: 0.
    """

    id: str
    type_: Literal["bounding_box"] = "bounding_box"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    x_min: int | Unset = 0
    y_min: int | Unset = 0
    x_max: int | Unset = 0
    y_max: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        x_min = self.x_min

        y_min = self.y_min

        x_max = self.x_max

        y_max = self.y_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if x_min is not UNSET:
            field_dict["x_min"] = x_min
        if y_min is not UNSET:
            field_dict["y_min"] = y_min
        if x_max is not UNSET:
            field_dict["x_max"] = x_max
        if y_max is not UNSET:
            field_dict["y_max"] = y_max

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["bounding_box"], d.pop("type"))
        if type_ != "bounding_box":
            raise ValueError(f"type must match const 'bounding_box', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        x_min = d.pop("x_min", UNSET)

        y_min = d.pop("y_min", UNSET)

        x_max = d.pop("x_max", UNSET)

        y_max = d.pop("y_max", UNSET)

        bounding_box = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            x_min=x_min,
            y_min=y_min,
            x_max=x_max,
            y_max=y_max,
        )

        bounding_box.additional_properties = d
        return bounding_box

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
