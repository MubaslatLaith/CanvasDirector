from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FloatRange")


@_attrs_define
class FloatRange:
    """Creates a range

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['float_range']):  Default: 'float_range'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        start (float | Unset): The first value of the range Default: 5.0.
        stop (float | Unset): The last value of the range Default: 10.0.
        steps (int | Unset): number of values to interpolate over (including start and stop) Default: 30.
    """

    id: str
    type_: Literal["float_range"] = "float_range"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    start: float | Unset = 5.0
    stop: float | Unset = 10.0
    steps: int | Unset = 30
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        start = self.start

        stop = self.stop

        steps = self.steps

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
        if start is not UNSET:
            field_dict["start"] = start
        if stop is not UNSET:
            field_dict["stop"] = stop
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["float_range"], d.pop("type"))
        if type_ != "float_range":
            raise ValueError(f"type must match const 'float_range', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        start = d.pop("start", UNSET)

        stop = d.pop("stop", UNSET)

        steps = d.pop("steps", UNSET)

        float_range = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            start=start,
            stop=stop,
            steps=steps,
        )

        float_range.additional_properties = d
        return float_range

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
