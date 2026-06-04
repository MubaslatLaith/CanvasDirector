from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flux_model_loader_output_max_seq_length import FluxModelLoaderOutputMaxSeqLength

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.t5_encoder_field import T5EncoderField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="FluxModelLoaderOutput")


@_attrs_define
class FluxModelLoaderOutput:
    """Flux base model loader output

    Attributes:
        transformer (TransformerField):
        clip (CLIPField):
        t5_encoder (T5EncoderField):
        vae (VAEField):
        max_seq_len (FluxModelLoaderOutputMaxSeqLength): The max sequence length to used for the T5 encoder. (256 for
            schnell transformer, 512 for dev transformer)
        type_ (Literal['flux_model_loader_output']):  Default: 'flux_model_loader_output'.
    """

    transformer: TransformerField
    clip: CLIPField
    t5_encoder: T5EncoderField
    vae: VAEField
    max_seq_len: FluxModelLoaderOutputMaxSeqLength
    type_: Literal["flux_model_loader_output"] = "flux_model_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transformer = self.transformer.to_dict()

        clip = self.clip.to_dict()

        t5_encoder = self.t5_encoder.to_dict()

        vae = self.vae.to_dict()

        max_seq_len = self.max_seq_len.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "clip": clip,
                "t5_encoder": t5_encoder,
                "vae": vae,
                "max_seq_len": max_seq_len,
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

        clip = CLIPField.from_dict(d.pop("clip"))

        t5_encoder = T5EncoderField.from_dict(d.pop("t5_encoder"))

        vae = VAEField.from_dict(d.pop("vae"))

        max_seq_len = FluxModelLoaderOutputMaxSeqLength(d.pop("max_seq_len"))

        type_ = cast(Literal["flux_model_loader_output"], d.pop("type"))
        if type_ != "flux_model_loader_output":
            raise ValueError(f"type must match const 'flux_model_loader_output', got '{type_}'")

        flux_model_loader_output = cls(
            transformer=transformer,
            clip=clip,
            t5_encoder=t5_encoder,
            vae=vae,
            max_seq_len=max_seq_len,
            type_=type_,
        )

        flux_model_loader_output.additional_properties = d
        return flux_model_loader_output

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
