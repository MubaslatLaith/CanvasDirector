from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StringJoinThree")


@_attrs_define
class StringJoinThree:
    """Joins string left to string middle to string right

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['string_join_three']):  Default: 'string_join_three'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        string_left (str | Unset): String Left Default: ''.
        string_middle (str | Unset): String Middle Default: ''.
        string_right (str | Unset): String Right Default: ''.
    """

    id: str
    type_: Literal["string_join_three"] = "string_join_three"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    string_left: str | Unset = ""
    string_middle: str | Unset = ""
    string_right: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        string_left = self.string_left

        string_middle = self.string_middle

        string_right = self.string_right

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
        if string_left is not UNSET:
            field_dict["string_left"] = string_left
        if string_middle is not UNSET:
            field_dict["string_middle"] = string_middle
        if string_right is not UNSET:
            field_dict["string_right"] = string_right

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["string_join_three"], d.pop("type"))
        if type_ != "string_join_three":
            raise ValueError(f"type must match const 'string_join_three', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        string_left = d.pop("string_left", UNSET)

        string_middle = d.pop("string_middle", UNSET)

        string_right = d.pop("string_right", UNSET)

        string_join_three = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            string_left=string_left,
            string_middle=string_middle,
            string_right=string_right,
        )

        string_join_three.additional_properties = d
        return string_join_three

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
