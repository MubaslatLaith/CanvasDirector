from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StringSplit")


@_attrs_define
class StringSplit:
    """Splits string into two strings, based on the first occurance of the delimiter. The delimiter will be removed from
    the string

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['string_split']):  Default: 'string_split'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            string (str | Unset): String to split Default: ''.
            delimiter (str | Unset): Delimiter to spilt with. blank will split on the first whitespace Default: ''.
    """

    id: str
    type_: Literal["string_split"] = "string_split"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    string: str | Unset = ""
    delimiter: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        string = self.string

        delimiter = self.delimiter

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
        if string is not UNSET:
            field_dict["string"] = string
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["string_split"], d.pop("type"))
        if type_ != "string_split":
            raise ValueError(f"type must match const 'string_split', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        string = d.pop("string", UNSET)

        delimiter = d.pop("delimiter", UNSET)

        string_split = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            string=string,
            delimiter=delimiter,
        )

        string_split.additional_properties = d
        return string_split

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
