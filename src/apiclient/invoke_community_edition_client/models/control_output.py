from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.control_field import ControlField


T = TypeVar("T", bound="ControlOutput")


@_attrs_define
class ControlOutput:
    """node output for ControlNet info

    Attributes:
        control (ControlField):
        type_ (Literal['control_output']):  Default: 'control_output'.
    """

    control: ControlField
    type_: Literal["control_output"] = "control_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control = self.control.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "control": control,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_field import ControlField

        d = dict(src_dict)
        control = ControlField.from_dict(d.pop("control"))

        type_ = cast(Literal["control_output"], d.pop("type"))
        if type_ != "control_output":
            raise ValueError(f"type must match const 'control_output', got '{type_}'")

        control_output = cls(
            control=control,
            type_=type_,
        )

        control_output.additional_properties = d
        return control_output

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
