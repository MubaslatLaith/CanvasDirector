from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RandomRange")


@_attrs_define
class RandomRange:
    """Creates a collection of random numbers

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['random_range']):  Default: 'random_range'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: False.
        low (int | Unset): The inclusive low value Default: 0.
        high (int | Unset): The exclusive high value Default: 2147483647.
        size (int | Unset): The number of values to generate Default: 1.
        seed (int | Unset): The seed for the RNG (omit for random) Default: 0.
    """

    id: str
    type_: Literal["random_range"] = "random_range"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = False
    low: int | Unset = 0
    high: int | Unset = 2147483647
    size: int | Unset = 1
    seed: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        low = self.low

        high = self.high

        size = self.size

        seed = self.seed

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
        if low is not UNSET:
            field_dict["low"] = low
        if high is not UNSET:
            field_dict["high"] = high
        if size is not UNSET:
            field_dict["size"] = size
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["random_range"], d.pop("type"))
        if type_ != "random_range":
            raise ValueError(f"type must match const 'random_range', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        low = d.pop("low", UNSET)

        high = d.pop("high", UNSET)

        size = d.pop("size", UNSET)

        seed = d.pop("seed", UNSET)

        random_range = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            low=low,
            high=high,
            size=size,
            seed=seed,
        )

        random_range.additional_properties = d
        return random_range

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
