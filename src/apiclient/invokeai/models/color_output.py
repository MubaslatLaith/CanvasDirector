from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.color_field import ColorField


T = TypeVar("T", bound="ColorOutput")


@_attrs_define
class ColorOutput:
    """Base class for nodes that output a single color

    Attributes:
        color (ColorField): A color primitive field
        type_ (Literal['color_output']):  Default: 'color_output'.
    """

    color: ColorField
    type_: Literal["color_output"] = "color_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_field import ColorField

        d = dict(src_dict)
        color = ColorField.from_dict(d.pop("color"))

        type_ = cast(Literal["color_output"], d.pop("type"))
        if type_ != "color_output":
            raise ValueError(f"type must match const 'color_output', got '{type_}'")

        color_output = cls(
            color=color,
            type_=type_,
        )

        color_output.additional_properties = d
        return color_output

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
