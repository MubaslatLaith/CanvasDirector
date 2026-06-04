from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.u_net_field import UNetField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="ModelLoaderOutput")


@_attrs_define
class ModelLoaderOutput:
    """Model loader output

    Attributes:
        vae (VAEField):
        type_ (Literal['model_loader_output']):  Default: 'model_loader_output'.
        clip (CLIPField):
        unet (UNetField):
    """

    vae: VAEField
    clip: CLIPField
    unet: UNetField
    type_: Literal["model_loader_output"] = "model_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vae = self.vae.to_dict()

        type_ = self.type_

        clip = self.clip.to_dict()

        unet = self.unet.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vae": vae,
                "type": type_,
                "clip": clip,
                "unet": unet,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        vae = VAEField.from_dict(d.pop("vae"))

        type_ = cast(Literal["model_loader_output"], d.pop("type"))
        if type_ != "model_loader_output":
            raise ValueError(f"type must match const 'model_loader_output', got '{type_}'")

        clip = CLIPField.from_dict(d.pop("clip"))

        unet = UNetField.from_dict(d.pop("unet"))

        model_loader_output = cls(
            vae=vae,
            type_=type_,
            clip=clip,
            unet=unet,
        )

        model_loader_output.additional_properties = d
        return model_loader_output

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
