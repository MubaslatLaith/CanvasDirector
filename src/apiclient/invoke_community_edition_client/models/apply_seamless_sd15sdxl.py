from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.u_net_field import UNetField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="ApplySeamlessSD15SDXL")


@_attrs_define
class ApplySeamlessSD15SDXL:
    """Applies the seamless transformation to the Model UNet and VAE.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['seamless']):  Default: 'seamless'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        unet (None | UNetField | Unset): UNet (scheduler, LoRAs)
        vae (None | Unset | VAEField): VAE model to load
        seamless_y (bool | Unset): Specify whether Y axis is seamless Default: True.
        seamless_x (bool | Unset): Specify whether X axis is seamless Default: True.
    """

    id: str
    type_: Literal["seamless"] = "seamless"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    unet: None | UNetField | Unset = UNSET
    vae: None | Unset | VAEField = UNSET
    seamless_y: bool | Unset = True
    seamless_x: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        unet: dict[str, Any] | None | Unset
        if isinstance(self.unet, Unset):
            unet = UNSET
        elif isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        vae: dict[str, Any] | None | Unset
        if isinstance(self.vae, Unset):
            vae = UNSET
        elif isinstance(self.vae, VAEField):
            vae = self.vae.to_dict()
        else:
            vae = self.vae

        seamless_y = self.seamless_y

        seamless_x = self.seamless_x

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if unet is not UNSET:
            field_dict["unet"] = unet
        if vae is not UNSET:
            field_dict["vae"] = vae
        if seamless_y is not UNSET:
            field_dict["seamless_y"] = seamless_y
        if seamless_x is not UNSET:
            field_dict["seamless_x"] = seamless_x

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["seamless"], d.pop("type"))
        if type_ != "seamless":
            raise ValueError(f"type must match const 'seamless', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_unet(data: object) -> None | UNetField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unet_type_0 = UNetField.from_dict(data)

                return unet_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UNetField | Unset, data)

        unet = _parse_unet(d.pop("unet", UNSET))

        def _parse_vae(data: object) -> None | Unset | VAEField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vae_type_0 = VAEField.from_dict(data)

                return vae_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VAEField, data)

        vae = _parse_vae(d.pop("vae", UNSET))

        seamless_y = d.pop("seamless_y", UNSET)

        seamless_x = d.pop("seamless_x", UNSET)

        apply_seamless_sd15sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            unet=unet,
            vae=vae,
            seamless_y=seamless_y,
            seamless_x=seamless_x,
        )

        apply_seamless_sd15sdxl.additional_properties = d
        return apply_seamless_sd15sdxl

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
