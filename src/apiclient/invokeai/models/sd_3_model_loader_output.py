from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.t5_encoder_field import T5EncoderField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="Sd3ModelLoaderOutput")


@_attrs_define
class Sd3ModelLoaderOutput:
    """SD3 base model loader output.

    Attributes:
        transformer (TransformerField):
        clip_l (CLIPField):
        clip_g (CLIPField):
        t5_encoder (T5EncoderField):
        vae (VAEField):
        type_ (Literal['sd3_model_loader_output']):  Default: 'sd3_model_loader_output'.
    """

    transformer: TransformerField
    clip_l: CLIPField
    clip_g: CLIPField
    t5_encoder: T5EncoderField
    vae: VAEField
    type_: Literal["sd3_model_loader_output"] = "sd3_model_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transformer = self.transformer.to_dict()

        clip_l = self.clip_l.to_dict()

        clip_g = self.clip_g.to_dict()

        t5_encoder = self.t5_encoder.to_dict()

        vae = self.vae.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "clip_l": clip_l,
                "clip_g": clip_g,
                "t5_encoder": t5_encoder,
                "vae": vae,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.t5_encoder_field import T5EncoderField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        transformer = TransformerField.from_dict(d.pop("transformer"))

        clip_l = CLIPField.from_dict(d.pop("clip_l"))

        clip_g = CLIPField.from_dict(d.pop("clip_g"))

        t5_encoder = T5EncoderField.from_dict(d.pop("t5_encoder"))

        vae = VAEField.from_dict(d.pop("vae"))

        type_ = cast(Literal["sd3_model_loader_output"], d.pop("type"))
        if type_ != "sd3_model_loader_output":
            raise ValueError(f"type must match const 'sd3_model_loader_output', got '{type_}'")

        sd_3_model_loader_output = cls(
            transformer=transformer,
            clip_l=clip_l,
            clip_g=clip_g,
            t5_encoder=t5_encoder,
            vae=vae,
            type_=type_,
        )

        sd_3_model_loader_output.additional_properties = d
        return sd_3_model_loader_output

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
