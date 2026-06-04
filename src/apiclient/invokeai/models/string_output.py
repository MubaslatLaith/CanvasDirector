from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StringOutput")


@_attrs_define
class StringOutput:
    """Base class for nodes that output a single string

    Attributes:
        value (str): The output string
        type_ (Literal['string_output']):  Default: 'string_output'.
    """

    value: str
    type_: Literal["string_output"] = "string_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        type_ = cast(Literal["string_output"], d.pop("type"))
        if type_ != "string_output":
            raise ValueError(f"type must match const 'string_output', got '{type_}'")

        string_output = cls(
            value=value,
            type_=type_,
        )

        string_output.additional_properties = d
        return string_output

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
