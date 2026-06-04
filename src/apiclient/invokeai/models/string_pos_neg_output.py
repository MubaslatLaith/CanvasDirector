from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StringPosNegOutput")


@_attrs_define
class StringPosNegOutput:
    """Base class for invocations that output a positive and negative string

    Attributes:
        positive_string (str): Positive string
        negative_string (str): Negative string
        type_ (Literal['string_pos_neg_output']):  Default: 'string_pos_neg_output'.
    """

    positive_string: str
    negative_string: str
    type_: Literal["string_pos_neg_output"] = "string_pos_neg_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        positive_string = self.positive_string

        negative_string = self.negative_string

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positive_string": positive_string,
                "negative_string": negative_string,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        positive_string = d.pop("positive_string")

        negative_string = d.pop("negative_string")

        type_ = cast(Literal["string_pos_neg_output"], d.pop("type"))
        if type_ != "string_pos_neg_output":
            raise ValueError(f"type must match const 'string_pos_neg_output', got '{type_}'")

        string_pos_neg_output = cls(
            positive_string=positive_string,
            negative_string=negative_string,
            type_=type_,
        )

        string_pos_neg_output.additional_properties = d
        return string_pos_neg_output

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
