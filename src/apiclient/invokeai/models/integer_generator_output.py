from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegerGeneratorOutput")


@_attrs_define
class IntegerGeneratorOutput:
    """
    Attributes:
        integers (list[int]): The generated integers
        type_ (Literal['integer_generator_output']):  Default: 'integer_generator_output'.
    """

    integers: list[int]
    type_: Literal["integer_generator_output"] = "integer_generator_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integers = self.integers

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integers": integers,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        integers = cast(list[int], d.pop("integers"))

        type_ = cast(Literal["integer_generator_output"], d.pop("type"))
        if type_ != "integer_generator_output":
            raise ValueError(f"type must match const 'integer_generator_output', got '{type_}'")

        integer_generator_output = cls(
            integers=integers,
            type_=type_,
        )

        integer_generator_output.additional_properties = d
        return integer_generator_output

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
