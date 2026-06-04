from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.u_net_field import UNetField


T = TypeVar("T", bound="UNetOutput")


@_attrs_define
class UNetOutput:
    """Base class for invocations that output a UNet field.

    Attributes:
        unet (UNetField):
        type_ (Literal['unet_output']):  Default: 'unet_output'.
    """

    unet: UNetField
    type_: Literal["unet_output"] = "unet_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unet = self.unet.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unet": unet,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_net_field import UNetField

        d = dict(src_dict)
        unet = UNetField.from_dict(d.pop("unet"))

        type_ = cast(Literal["unet_output"], d.pop("type"))
        if type_ != "unet_output":
            raise ValueError(f"type must match const 'unet_output', got '{type_}'")

        u_net_output = cls(
            unet=unet,
            type_=type_,
        )

        u_net_output.additional_properties = d
        return u_net_output

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
