from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RandomFloat")


@_attrs_define
class RandomFloat:
    """Outputs a single random float

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['rand_float']):  Default: 'rand_float'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: False.
        low (float | Unset): The inclusive low value Default: 0.0.
        high (float | Unset): The exclusive high value Default: 1.0.
        decimals (int | Unset): The number of decimal places to round to Default: 2.
    """

    id: str
    type_: Literal["rand_float"] = "rand_float"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = False
    low: float | Unset = 0.0
    high: float | Unset = 1.0
    decimals: int | Unset = 2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        low = self.low

        high = self.high

        decimals = self.decimals

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
        if decimals is not UNSET:
            field_dict["decimals"] = decimals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["rand_float"], d.pop("type"))
        if type_ != "rand_float":
            raise ValueError(f"type must match const 'rand_float', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        low = d.pop("low", UNSET)

        high = d.pop("high", UNSET)

        decimals = d.pop("decimals", UNSET)

        random_float = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            low=low,
            high=high,
            decimals=decimals,
        )

        random_float.additional_properties = d
        return random_float

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
