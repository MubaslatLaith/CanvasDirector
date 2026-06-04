from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StringGeneratorOutput")


@_attrs_define
class StringGeneratorOutput:
    """Base class for nodes that output a collection of strings

    Attributes:
        strings (list[str]): The generated strings
        type_ (Literal['string_generator_output']):  Default: 'string_generator_output'.
    """

    strings: list[str]
    type_: Literal["string_generator_output"] = "string_generator_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strings = self.strings

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strings": strings,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strings = cast(list[str], d.pop("strings"))

        type_ = cast(Literal["string_generator_output"], d.pop("type"))
        if type_ != "string_generator_output":
            raise ValueError(f"type must match const 'string_generator_output', got '{type_}'")

        string_generator_output = cls(
            strings=strings,
            type_=type_,
        )

        string_generator_output.additional_properties = d
        return string_generator_output

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
