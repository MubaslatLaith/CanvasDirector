from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.u_net_field import UNetField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="SeamlessModeOutput")


@_attrs_define
class SeamlessModeOutput:
    """Modified Seamless Model output

    Attributes:
        unet (None | UNetField): UNet (scheduler, LoRAs)
        vae (None | VAEField): VAE
        type_ (Literal['seamless_output']):  Default: 'seamless_output'.
    """

    unet: None | UNetField
    vae: None | VAEField
    type_: Literal["seamless_output"] = "seamless_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        unet: dict[str, Any] | None
        if isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        vae: dict[str, Any] | None
        if isinstance(self.vae, VAEField):
            vae = self.vae.to_dict()
        else:
            vae = self.vae

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unet": unet,
                "vae": vae,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        d = dict(src_dict)

        def _parse_unet(data: object) -> None | UNetField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unet_type_0 = UNetField.from_dict(data)

                return unet_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UNetField, data)

        unet = _parse_unet(d.pop("unet"))

        def _parse_vae(data: object) -> None | VAEField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vae_type_0 = VAEField.from_dict(data)

                return vae_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VAEField, data)

        vae = _parse_vae(d.pop("vae"))

        type_ = cast(Literal["seamless_output"], d.pop("type"))
        if type_ != "seamless_output":
            raise ValueError(f"type must match const 'seamless_output', got '{type_}'")

        seamless_mode_output = cls(
            unet=unet,
            vae=vae,
            type_=type_,
        )

        seamless_mode_output.additional_properties = d
        return seamless_mode_output

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
