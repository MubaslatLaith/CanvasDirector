from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField
    from ..models.qwen_3_encoder_field import Qwen3EncoderField
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="ApplyLoRAAnima")


@_attrs_define
class ApplyLoRAAnima:
    """Apply a LoRA model to an Anima transformer and/or Qwen3 text encoder.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['anima_lora_loader']):  Default: 'anima_lora_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        lora (ModelIdentifierField | None | Unset): LoRA model to load
        weight (float | Unset): The weight at which the LoRA is applied to each model Default: 0.75.
        transformer (None | TransformerField | Unset): Transformer
        qwen3_encoder (None | Qwen3EncoderField | Unset): Qwen3 tokenizer and text encoder
    """

    id: str
    type_: Literal["anima_lora_loader"] = "anima_lora_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    lora: ModelIdentifierField | None | Unset = UNSET
    weight: float | Unset = 0.75
    transformer: None | TransformerField | Unset = UNSET
    qwen3_encoder: None | Qwen3EncoderField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.transformer_field import TransformerField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        lora: dict[str, Any] | None | Unset
        if isinstance(self.lora, Unset):
            lora = UNSET
        elif isinstance(self.lora, ModelIdentifierField):
            lora = self.lora.to_dict()
        else:
            lora = self.lora

        weight = self.weight

        transformer: dict[str, Any] | None | Unset
        if isinstance(self.transformer, Unset):
            transformer = UNSET
        elif isinstance(self.transformer, TransformerField):
            transformer = self.transformer.to_dict()
        else:
            transformer = self.transformer

        qwen3_encoder: dict[str, Any] | None | Unset
        if isinstance(self.qwen3_encoder, Unset):
            qwen3_encoder = UNSET
        elif isinstance(self.qwen3_encoder, Qwen3EncoderField):
            qwen3_encoder = self.qwen3_encoder.to_dict()
        else:
            qwen3_encoder = self.qwen3_encoder

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
        if lora is not UNSET:
            field_dict["lora"] = lora
        if weight is not UNSET:
            field_dict["weight"] = weight
        if transformer is not UNSET:
            field_dict["transformer"] = transformer
        if qwen3_encoder is not UNSET:
            field_dict["qwen3_encoder"] = qwen3_encoder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.transformer_field import TransformerField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["anima_lora_loader"], d.pop("type"))
        if type_ != "anima_lora_loader":
            raise ValueError(f"type must match const 'anima_lora_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_lora(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lora_type_0 = ModelIdentifierField.from_dict(data)

                return lora_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        lora = _parse_lora(d.pop("lora", UNSET))

        weight = d.pop("weight", UNSET)

        def _parse_transformer(data: object) -> None | TransformerField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transformer_type_0 = TransformerField.from_dict(data)

                return transformer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransformerField | Unset, data)

        transformer = _parse_transformer(d.pop("transformer", UNSET))

        def _parse_qwen3_encoder(data: object) -> None | Qwen3EncoderField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qwen3_encoder_type_0 = Qwen3EncoderField.from_dict(data)

                return qwen3_encoder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Qwen3EncoderField | Unset, data)

        qwen3_encoder = _parse_qwen3_encoder(d.pop("qwen3_encoder", UNSET))

        apply_lo_ra_anima = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            lora=lora,
            weight=weight,
            transformer=transformer,
            qwen3_encoder=qwen3_encoder,
        )

        apply_lo_ra_anima.additional_properties = d
        return apply_lo_ra_anima

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
