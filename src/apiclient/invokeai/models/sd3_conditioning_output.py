from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sd3_conditioning_field import SD3ConditioningField


T = TypeVar("T", bound="SD3ConditioningOutput")


@_attrs_define
class SD3ConditioningOutput:
    """Base class for nodes that output a single SD3 conditioning tensor

    Attributes:
        conditioning (SD3ConditioningField): A conditioning tensor primitive value
        type_ (Literal['sd3_conditioning_output']):  Default: 'sd3_conditioning_output'.
    """

    conditioning: SD3ConditioningField
    type_: Literal["sd3_conditioning_output"] = "sd3_conditioning_output"
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
        from ..models.sd3_conditioning_field import SD3ConditioningField

        d = dict(src_dict)
        conditioning = SD3ConditioningField.from_dict(d.pop("conditioning"))

        type_ = cast(Literal["sd3_conditioning_output"], d.pop("type"))
        if type_ != "sd3_conditioning_output":
            raise ValueError(f"type must match const 'sd3_conditioning_output', got '{type_}'")

        sd3_conditioning_output = cls(
            conditioning=conditioning,
            type_=type_,
        )

        sd3_conditioning_output.additional_properties = d
        return sd3_conditioning_output

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
