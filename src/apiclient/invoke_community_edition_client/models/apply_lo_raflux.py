from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.model_identifier_field import ModelIdentifierField
    from ..models.t5_encoder_field import T5EncoderField
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="ApplyLoRAFLUX")


@_attrs_define
class ApplyLoRAFLUX:
    """Apply a LoRA model to a FLUX transformer and/or text encoder.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['flux_lora_loader']):  Default: 'flux_lora_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        lora (ModelIdentifierField | None | Unset): LoRA model to load
        weight (float | Unset): The weight at which the LoRA is applied to each model Default: 0.75.
        transformer (None | TransformerField | Unset): Transformer
        clip (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        t5_encoder (None | T5EncoderField | Unset): T5 tokenizer and text encoder
    """

    id: str
    type_: Literal["flux_lora_loader"] = "flux_lora_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    lora: ModelIdentifierField | None | Unset = UNSET
    weight: float | Unset = 0.75
    transformer: None | TransformerField | Unset = UNSET
    clip: CLIPField | None | Unset = UNSET
    t5_encoder: None | T5EncoderField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.t5_encoder_field import T5EncoderField
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

        clip: dict[str, Any] | None | Unset
        if isinstance(self.clip, Unset):
            clip = UNSET
        elif isinstance(self.clip, CLIPField):
            clip = self.clip.to_dict()
        else:
            clip = self.clip

        t5_encoder: dict[str, Any] | None | Unset
        if isinstance(self.t5_encoder, Unset):
            t5_encoder = UNSET
        elif isinstance(self.t5_encoder, T5EncoderField):
            t5_encoder = self.t5_encoder.to_dict()
        else:
            t5_encoder = self.t5_encoder

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
        if clip is not UNSET:
            field_dict["clip"] = clip
        if t5_encoder is not UNSET:
            field_dict["t5_encoder"] = t5_encoder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.t5_encoder_field import T5EncoderField
        from ..models.transformer_field import TransformerField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux_lora_loader"], d.pop("type"))
        if type_ != "flux_lora_loader":
            raise ValueError(f"type must match const 'flux_lora_loader', got '{type_}'")

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

        def _parse_clip(data: object) -> CLIPField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_type_0 = CLIPField.from_dict(data)

                return clip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None | Unset, data)

        clip = _parse_clip(d.pop("clip", UNSET))

        def _parse_t5_encoder(data: object) -> None | T5EncoderField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                t5_encoder_type_0 = T5EncoderField.from_dict(data)

                return t5_encoder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | T5EncoderField | Unset, data)

        t5_encoder = _parse_t5_encoder(d.pop("t5_encoder", UNSET))

        apply_lo_raflux = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            lora=lora,
            weight=weight,
            transformer=transformer,
            clip=clip,
            t5_encoder=t5_encoder,
        )

        apply_lo_raflux.additional_properties = d
        return apply_lo_raflux

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
