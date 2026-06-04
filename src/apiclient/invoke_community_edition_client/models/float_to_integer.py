from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.float_to_integer_method import FloatToIntegerMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="FloatToInteger")


@_attrs_define
class FloatToInteger:
    """Rounds a float number to (a multiple of) an integer.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['float_to_int']):  Default: 'float_to_int'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        value (float | Unset): The value to round Default: 0.0.
        multiple (int | Unset): The multiple to round to Default: 1.
        method (FloatToIntegerMethod | Unset): The method to use for rounding Default: FloatToIntegerMethod.NEAREST.
    """

    id: str
    type_: Literal["float_to_int"] = "float_to_int"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    value: float | Unset = 0.0
    multiple: int | Unset = 1
    method: FloatToIntegerMethod | Unset = FloatToIntegerMethod.NEAREST
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        value = self.value

        multiple = self.multiple

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

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
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["float_to_int"], d.pop("type"))
        if type_ != "float_to_int":
            raise ValueError(f"type must match const 'float_to_int', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        value = d.pop("value", UNSET)

        multiple = d.pop("multiple", UNSET)

        _method = d.pop("method", UNSET)
        method: FloatToIntegerMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = FloatToIntegerMethod(_method)

        float_to_integer = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            value=value,
            multiple=multiple,
            method=method,
        )

        float_to_integer.additional_properties = d
        return float_to_integer

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
