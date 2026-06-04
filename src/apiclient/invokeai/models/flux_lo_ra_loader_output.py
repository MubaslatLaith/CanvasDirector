from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.t5_encoder_field import T5EncoderField
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="FluxLoRALoaderOutput")


@_attrs_define
class FluxLoRALoaderOutput:
    """FLUX LoRA Loader Output

    Attributes:
        transformer (None | TransformerField): Transformer
        clip (CLIPField | None): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        t5_encoder (None | T5EncoderField): T5 tokenizer and text encoder
        type_ (Literal['flux_lora_loader_output']):  Default: 'flux_lora_loader_output'.
    """

    transformer: None | TransformerField
    clip: CLIPField | None
    t5_encoder: None | T5EncoderField
    type_: Literal["flux_lora_loader_output"] = "flux_lora_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField
        from ..models.t5_encoder_field import T5EncoderField
        from ..models.transformer_field import TransformerField

        transformer: dict[str, Any] | None
        if isinstance(self.transformer, TransformerField):
            transformer = self.transformer.to_dict()
        else:
            transformer = self.transformer

        clip: dict[str, Any] | None
        if isinstance(self.clip, CLIPField):
            clip = self.clip.to_dict()
        else:
            clip = self.clip

        t5_encoder: dict[str, Any] | None
        if isinstance(self.t5_encoder, T5EncoderField):
            t5_encoder = self.t5_encoder.to_dict()
        else:
            t5_encoder = self.t5_encoder

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "clip": clip,
                "t5_encoder": t5_encoder,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.t5_encoder_field import T5EncoderField
        from ..models.transformer_field import TransformerField

        d = dict(src_dict)

        def _parse_transformer(data: object) -> None | TransformerField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transformer_type_0 = TransformerField.from_dict(data)

                return transformer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransformerField, data)

        transformer = _parse_transformer(d.pop("transformer"))

        def _parse_clip(data: object) -> CLIPField | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_type_0 = CLIPField.from_dict(data)

                return clip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None, data)

        clip = _parse_clip(d.pop("clip"))

        def _parse_t5_encoder(data: object) -> None | T5EncoderField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                t5_encoder_type_0 = T5EncoderField.from_dict(data)

                return t5_encoder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | T5EncoderField, data)

        t5_encoder = _parse_t5_encoder(d.pop("t5_encoder"))

        type_ = cast(Literal["flux_lora_loader_output"], d.pop("type"))
        if type_ != "flux_lora_loader_output":
            raise ValueError(f"type must match const 'flux_lora_loader_output', got '{type_}'")

        flux_lo_ra_loader_output = cls(
            transformer=transformer,
            clip=clip,
            t5_encoder=t5_encoder,
            type_=type_,
        )

        flux_lo_ra_loader_output.additional_properties = d
        return flux_lo_ra_loader_output

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
