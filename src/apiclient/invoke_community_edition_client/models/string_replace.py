from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StringReplace")


@_attrs_define
class StringReplace:
    """Replaces the search string with the replace string

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['string_replace']):  Default: 'string_replace'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        string (str | Unset): String to work on Default: ''.
        search_string (str | Unset): String to search for Default: ''.
        replace_string (str | Unset): String to replace the search Default: ''.
        use_regex (bool | Unset): Use search string as a regex expression (non regex is case insensitive) Default:
            False.
    """

    id: str
    type_: Literal["string_replace"] = "string_replace"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    string: str | Unset = ""
    search_string: str | Unset = ""
    replace_string: str | Unset = ""
    use_regex: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        string = self.string

        search_string = self.search_string

        replace_string = self.replace_string

        use_regex = self.use_regex

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
        if search_string is not UNSET:
            field_dict["search_string"] = search_string
        if replace_string is not UNSET:
            field_dict["replace_string"] = replace_string
        if use_regex is not UNSET:
            field_dict["use_regex"] = use_regex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["string_replace"], d.pop("type"))
        if type_ != "string_replace":
            raise ValueError(f"type must match const 'string_replace', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        string = d.pop("string", UNSET)

        search_string = d.pop("search_string", UNSET)

        replace_string = d.pop("replace_string", UNSET)

        use_regex = d.pop("use_regex", UNSET)

        string_replace = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            string=string,
            search_string=search_string,
            replace_string=replace_string,
            use_regex=use_regex,
        )

        string_replace.additional_properties = d
        return string_replace

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
