from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegerRangeOfSize")


@_attrs_define
class IntegerRangeOfSize:
    """Creates a range from start to start + (size * step) incremented by step

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['range_of_size']):  Default: 'range_of_size'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        start (int | Unset): The start of the range Default: 0.
        size (int | Unset): The number of values Default: 1.
        step (int | Unset): The step of the range Default: 1.
    """

    id: str
    type_: Literal["range_of_size"] = "range_of_size"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    start: int | Unset = 0
    size: int | Unset = 1
    step: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        start = self.start

        size = self.size

        step = self.step

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
        if size is not UNSET:
            field_dict["size"] = size
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["range_of_size"], d.pop("type"))
        if type_ != "range_of_size":
            raise ValueError(f"type must match const 'range_of_size', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        start = d.pop("start", UNSET)

        size = d.pop("size", UNSET)

        step = d.pop("step", UNSET)

        integer_range_of_size = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            start=start,
            size=size,
            step=step,
        )

        integer_range_of_size.additional_properties = d
        return integer_range_of_size

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
