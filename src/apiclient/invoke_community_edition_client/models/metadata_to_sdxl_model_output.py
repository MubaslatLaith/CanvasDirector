from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.model_identifier_field import ModelIdentifierField
    from ..models.u_net_field import UNetField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="MetadataToSDXLModelOutput")


@_attrs_define
class MetadataToSDXLModelOutput:
    """String to SDXL main model output

    Attributes:
        model (ModelIdentifierField):
        name (str): Model Name
        unet (UNetField):
        clip (CLIPField):
        clip2 (CLIPField):
        vae (VAEField):
        type_ (Literal['metadata_to_sdxl_model_output']):  Default: 'metadata_to_sdxl_model_output'.
    """

    model: ModelIdentifierField
    name: str
    unet: UNetField
    clip: CLIPField
    clip2: CLIPField
    vae: VAEField
    type_: Literal["metadata_to_sdxl_model_output"] = "metadata_to_sdxl_model_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model.to_dict()

        name = self.name

        unet = self.unet.to_dict()

        clip = self.clip.to_dict()

        clip2 = self.clip2.to_dict()

        vae = self.vae.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "name": name,
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
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        model = ModelIdentifierField.from_dict(d.pop("model"))

        name = d.pop("name")

        unet = UNetField.from_dict(d.pop("unet"))

        clip = CLIPField.from_dict(d.pop("clip"))

        clip2 = CLIPField.from_dict(d.pop("clip2"))

        vae = VAEField.from_dict(d.pop("vae"))

        type_ = cast(Literal["metadata_to_sdxl_model_output"], d.pop("type"))
        if type_ != "metadata_to_sdxl_model_output":
            raise ValueError(f"type must match const 'metadata_to_sdxl_model_output', got '{type_}'")

        metadata_to_sdxl_model_output = cls(
            model=model,
            name=name,
            unet=unet,
            clip=clip,
            clip2=clip2,
            vae=vae,
            type_=type_,
        )

        metadata_to_sdxl_model_output.additional_properties = d
        return metadata_to_sdxl_model_output

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
