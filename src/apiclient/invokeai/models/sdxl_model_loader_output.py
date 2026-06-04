from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.u_net_field import UNetField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="SDXLModelLoaderOutput")


@_attrs_define
class SDXLModelLoaderOutput:
    """SDXL base model loader output

    Attributes:
        unet (UNetField):
        clip (CLIPField):
        clip2 (CLIPField):
        vae (VAEField):
        type_ (Literal['sdxl_model_loader_output']):  Default: 'sdxl_model_loader_output'.
    """

    unet: UNetField
    clip: CLIPField
    clip2: CLIPField
    vae: VAEField
    type_: Literal["sdxl_model_loader_output"] = "sdxl_model_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unet = self.unet.to_dict()

        clip = self.clip.to_dict()

        clip2 = self.clip2.to_dict()

        vae = self.vae.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unet": unet,
                "clip": clip,
                "clip2": clip2,
                "vae": vae,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        unet = UNetField.from_dict(d.pop("unet"))

        clip = CLIPField.from_dict(d.pop("clip"))

        clip2 = CLIPField.from_dict(d.pop("clip2"))

        vae = VAEField.from_dict(d.pop("vae"))

        type_ = cast(Literal["sdxl_model_loader_output"], d.pop("type"))
        if type_ != "sdxl_model_loader_output":
            raise ValueError(f"type must match const 'sdxl_model_loader_output', got '{type_}'")

        sdxl_model_loader_output = cls(
            unet=unet,
            clip=clip,
            clip2=clip2,
            vae=vae,
            type_=type_,
        )

        sdxl_model_loader_output.additional_properties = d
        return sdxl_model_loader_output

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
