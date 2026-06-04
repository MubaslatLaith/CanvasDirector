from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flux_2_klein_model_loader_output_max_seq_length import Flux2KleinModelLoaderOutputMaxSeqLength

if TYPE_CHECKING:
    from ..models.qwen_3_encoder_field import Qwen3EncoderField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="Flux2KleinModelLoaderOutput")


@_attrs_define
class Flux2KleinModelLoaderOutput:
    """Flux2 Klein model loader output.

    Attributes:
        transformer (TransformerField):
        qwen3_encoder (Qwen3EncoderField): Field for Qwen3 text encoder used by Z-Image models.
        vae (VAEField):
        max_seq_len (Flux2KleinModelLoaderOutputMaxSeqLength): The max sequence length for the Qwen3 encoder.
        type_ (Literal['flux2_klein_model_loader_output']):  Default: 'flux2_klein_model_loader_output'.
    """

    transformer: TransformerField
    qwen3_encoder: Qwen3EncoderField
    vae: VAEField
    max_seq_len: Flux2KleinModelLoaderOutputMaxSeqLength
    type_: Literal["flux2_klein_model_loader_output"] = "flux2_klein_model_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transformer = self.transformer.to_dict()

        qwen3_encoder = self.qwen3_encoder.to_dict()

        vae = self.vae.to_dict()

        max_seq_len = self.max_seq_len.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "qwen3_encoder": qwen3_encoder,
                "vae": vae,
                "max_seq_len": max_seq_len,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        transformer = TransformerField.from_dict(d.pop("transformer"))

        qwen3_encoder = Qwen3EncoderField.from_dict(d.pop("qwen3_encoder"))

        vae = VAEField.from_dict(d.pop("vae"))

        max_seq_len = Flux2KleinModelLoaderOutputMaxSeqLength(d.pop("max_seq_len"))

        type_ = cast(Literal["flux2_klein_model_loader_output"], d.pop("type"))
        if type_ != "flux2_klein_model_loader_output":
            raise ValueError(f"type must match const 'flux2_klein_model_loader_output', got '{type_}'")

        flux_2_klein_model_loader_output = cls(
            transformer=transformer,
            qwen3_encoder=qwen3_encoder,
            vae=vae,
            max_seq_len=max_seq_len,
            type_=type_,
        )

        flux_2_klein_model_loader_output.additional_properties = d
        return flux_2_klein_model_loader_output

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
