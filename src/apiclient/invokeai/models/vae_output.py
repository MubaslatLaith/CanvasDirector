from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="VAEOutput")


@_attrs_define
class VAEOutput:
    """Base class for invocations that output a VAE field

    Attributes:
        vae (VAEField):
        type_ (Literal['vae_output']):  Default: 'vae_output'.
    """

    vae: VAEField
    type_: Literal["vae_output"] = "vae_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vae = self.vae.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vae": vae,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        vae = VAEField.from_dict(d.pop("vae"))

        type_ = cast(Literal["vae_output"], d.pop("type"))
        if type_ != "vae_output":
            raise ValueError(f"type must match const 'vae_output', got '{type_}'")

        vae_output = cls(
            vae=vae,
            type_=type_,
        )

        vae_output.additional_properties = d
        return vae_output

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
