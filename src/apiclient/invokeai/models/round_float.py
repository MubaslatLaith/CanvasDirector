from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoundFloat")


@_attrs_define
class RoundFloat:
    """Rounds a float to a specified number of decimal places.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['round_float']):  Default: 'round_float'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        value (float | Unset): The float value Default: 0.0.
        decimals (int | Unset): The number of decimal places Default: 0.
    """

    id: str
    type_: Literal["round_float"] = "round_float"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    value: float | Unset = 0.0
    decimals: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        value = self.value

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
        if value is not UNSET:
            field_dict["value"] = value
        if decimals is not UNSET:
            field_dict["decimals"] = decimals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["round_float"], d.pop("type"))
        if type_ != "round_float":
            raise ValueError(f"type must match const 'round_float', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        value = d.pop("value", UNSET)

        decimals = d.pop("decimals", UNSET)

        round_float = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            value=value,
            decimals=decimals,
        )

        round_float.additional_properties = d
        return round_float

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
