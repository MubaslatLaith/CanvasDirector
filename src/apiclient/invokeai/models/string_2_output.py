from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="String2Output")


@_attrs_define
class String2Output:
    """Base class for invocations that output two strings

    Attributes:
        string_1 (str): string 1
        string_2 (str): string 2
        type_ (Literal['string_2_output']):  Default: 'string_2_output'.
    """

    string_1: str
    string_2: str
    type_: Literal["string_2_output"] = "string_2_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        string_1 = self.string_1

        string_2 = self.string_2

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "string_1": string_1,
                "string_2": string_2,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        string_1 = d.pop("string_1")

        string_2 = d.pop("string_2")

        type_ = cast(Literal["string_2_output"], d.pop("type"))
        if type_ != "string_2_output":
            raise ValueError(f"type must match const 'string_2_output', got '{type_}'")

        string_2_output = cls(
            string_1=string_1,
            string_2=string_2,
            type_=type_,
        )

        string_2_output.additional_properties = d
        return string_2_output

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
