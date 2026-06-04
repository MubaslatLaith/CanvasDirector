from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qwen_3_encoder_field import Qwen3EncoderField
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="AnimaLoRALoaderOutput")


@_attrs_define
class AnimaLoRALoaderOutput:
    """Anima LoRA Loader Output

    Attributes:
        transformer (None | TransformerField): Transformer
        qwen3_encoder (None | Qwen3EncoderField): Qwen3 tokenizer and text encoder
        type_ (Literal['anima_lora_loader_output']):  Default: 'anima_lora_loader_output'.
    """

    transformer: None | TransformerField
    qwen3_encoder: None | Qwen3EncoderField
    type_: Literal["anima_lora_loader_output"] = "anima_lora_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.transformer_field import TransformerField

        transformer: dict[str, Any] | None
        if isinstance(self.transformer, TransformerField):
            transformer = self.transformer.to_dict()
        else:
            transformer = self.transformer

        qwen3_encoder: dict[str, Any] | None
        if isinstance(self.qwen3_encoder, Qwen3EncoderField):
            qwen3_encoder = self.qwen3_encoder.to_dict()
        else:
            qwen3_encoder = self.qwen3_encoder

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "qwen3_encoder": qwen3_encoder,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
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

        def _parse_qwen3_encoder(data: object) -> None | Qwen3EncoderField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qwen3_encoder_type_0 = Qwen3EncoderField.from_dict(data)

                return qwen3_encoder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Qwen3EncoderField, data)

        qwen3_encoder = _parse_qwen3_encoder(d.pop("qwen3_encoder"))

        type_ = cast(Literal["anima_lora_loader_output"], d.pop("type"))
        if type_ != "anima_lora_loader_output":
            raise ValueError(f"type must match const 'anima_lora_loader_output', got '{type_}'")

        anima_lo_ra_loader_output = cls(
            transformer=transformer,
            qwen3_encoder=qwen3_encoder,
            type_=type_,
        )

        anima_lo_ra_loader_output.additional_properties = d
        return anima_lo_ra_loader_output

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
