from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prompt_flux_2_klein_max_seq_len import PromptFlux2KleinMaxSeqLen
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qwen_3_encoder_field import Qwen3EncoderField
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="PromptFlux2Klein")


@_attrs_define
class PromptFlux2Klein:
    """Encodes and preps a prompt for Flux2 Klein image generation.

    Flux2 Klein uses Qwen3 as the text encoder, extracting hidden states from
    layers (9, 18, 27) and stacking them for richer text representations.
    This matches the diffusers Flux2KleinPipeline implementation exactly.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['flux2_klein_text_encoder']):  Default: 'flux2_klein_text_encoder'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            prompt (None | str | Unset): Text prompt to encode.
            qwen3_encoder (None | Qwen3EncoderField | Unset): Qwen3 tokenizer and text encoder
            max_seq_len (PromptFlux2KleinMaxSeqLen | Unset): Max sequence length for the Qwen3 encoder. Default:
                PromptFlux2KleinMaxSeqLen.VALUE_512.
            mask (None | TensorField | Unset): A mask defining the region that this conditioning prompt applies to.
    """

    id: str
    type_: Literal["flux2_klein_text_encoder"] = "flux2_klein_text_encoder"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    prompt: None | str | Unset = UNSET
    qwen3_encoder: None | Qwen3EncoderField | Unset = UNSET
    max_seq_len: PromptFlux2KleinMaxSeqLen | Unset = PromptFlux2KleinMaxSeqLen.VALUE_512
    mask: None | TensorField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.tensor_field import TensorField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        qwen3_encoder: dict[str, Any] | None | Unset
        if isinstance(self.qwen3_encoder, Unset):
            qwen3_encoder = UNSET
        elif isinstance(self.qwen3_encoder, Qwen3EncoderField):
            qwen3_encoder = self.qwen3_encoder.to_dict()
        else:
            qwen3_encoder = self.qwen3_encoder

        max_seq_len: int | Unset = UNSET
        if not isinstance(self.max_seq_len, Unset):
            max_seq_len = self.max_seq_len.value

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, TensorField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

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
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if qwen3_encoder is not UNSET:
            field_dict["qwen3_encoder"] = qwen3_encoder
        if max_seq_len is not UNSET:
            field_dict["max_seq_len"] = max_seq_len
        if mask is not UNSET:
            field_dict["mask"] = mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.tensor_field import TensorField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux2_klein_text_encoder"], d.pop("type"))
        if type_ != "flux2_klein_text_encoder":
            raise ValueError(f"type must match const 'flux2_klein_text_encoder', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

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

        _max_seq_len = d.pop("max_seq_len", UNSET)
        max_seq_len: PromptFlux2KleinMaxSeqLen | Unset
        if isinstance(_max_seq_len, Unset):
            max_seq_len = UNSET
        else:
            max_seq_len = PromptFlux2KleinMaxSeqLen(_max_seq_len)

        def _parse_mask(data: object) -> None | TensorField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_type_0 = TensorField.from_dict(data)

                return mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TensorField | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))

        prompt_flux_2_klein = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            prompt=prompt,
            qwen3_encoder=qwen3_encoder,
            max_seq_len=max_seq_len,
            mask=mask,
        )

        prompt_flux_2_klein.additional_properties = d
        return prompt_flux_2_klein

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
