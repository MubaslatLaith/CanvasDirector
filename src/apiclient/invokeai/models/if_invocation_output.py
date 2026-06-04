from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IfInvocationOutput")


@_attrs_define
class IfInvocationOutput:
    """
    Attributes:
        value (Any | None): The selected value
        type_ (Literal['if_output']):  Default: 'if_output'.
    """

    value: Any | None
    type_: Literal["if_output"] = "if_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Any | None
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

        def _parse_value(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        value = _parse_value(d.pop("value"))

        type_ = cast(Literal["if_output"], d.pop("type"))
        if type_ != "if_output":
            raise ValueError(f"type must match const 'if_output', got '{type_}'")

        if_invocation_output = cls(
            value=value,
            type_=type_,
        )

        if_invocation_output.additional_properties = d
        return if_invocation_output

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
