from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.conditioning_field import ConditioningField


T = TypeVar("T", bound="ConditioningOutput")


@_attrs_define
class ConditioningOutput:
    """Base class for nodes that output a single conditioning tensor

    Attributes:
        conditioning (ConditioningField): A conditioning tensor primitive value
        type_ (Literal['conditioning_output']):  Default: 'conditioning_output'.
    """

    conditioning: ConditioningField
    type_: Literal["conditioning_output"] = "conditioning_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditioning = self.conditioning.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditioning": conditioning,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditioning_field import ConditioningField

        d = dict(src_dict)
        conditioning = ConditioningField.from_dict(d.pop("conditioning"))

        type_ = cast(Literal["conditioning_output"], d.pop("type"))
        if type_ != "conditioning_output":
            raise ValueError(f"type must match const 'conditioning_output', got '{type_}'")

        conditioning_output = cls(
            conditioning=conditioning,
            type_=type_,
        )

        conditioning_output.additional_properties = d
        return conditioning_output

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
