from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.z_image_conditioning_field import ZImageConditioningField


T = TypeVar("T", bound="ZImageConditioningOutput")


@_attrs_define
class ZImageConditioningOutput:
    """Base class for nodes that output a Z-Image text conditioning tensor.

    Attributes:
        conditioning (ZImageConditioningField): A Z-Image conditioning tensor primitive value
        type_ (Literal['z_image_conditioning_output']):  Default: 'z_image_conditioning_output'.
    """

    conditioning: ZImageConditioningField
    type_: Literal["z_image_conditioning_output"] = "z_image_conditioning_output"
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
        from ..models.z_image_conditioning_field import ZImageConditioningField

        d = dict(src_dict)
        conditioning = ZImageConditioningField.from_dict(d.pop("conditioning"))

        type_ = cast(Literal["z_image_conditioning_output"], d.pop("type"))
        if type_ != "z_image_conditioning_output":
            raise ValueError(f"type must match const 'z_image_conditioning_output', got '{type_}'")

        z_image_conditioning_output = cls(
            conditioning=conditioning,
            type_=type_,
        )

        z_image_conditioning_output.additional_properties = d
        return z_image_conditioning_output

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
