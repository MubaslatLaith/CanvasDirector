from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FloatOutput")


@_attrs_define
class FloatOutput:
    """Base class for nodes that output a single float

    Attributes:
        value (float): The output float
        type_ (Literal['float_output']):  Default: 'float_output'.
    """

    value: float
    type_: Literal["float_output"] = "float_output"
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

        type_ = cast(Literal["float_output"], d.pop("type"))
        if type_ != "float_output":
            raise ValueError(f"type must match const 'float_output', got '{type_}'")

        float_output = cls(
            value=value,
            type_=type_,
        )

        float_output.additional_properties = d
        return float_output

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
