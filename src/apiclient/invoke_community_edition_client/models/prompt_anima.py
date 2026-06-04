from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qwen_3_encoder_field import Qwen3EncoderField
    from ..models.t5_encoder_field import T5EncoderField
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="PromptAnima")


@_attrs_define
class PromptAnima:
    """Encodes and preps a prompt for an Anima image.

    Uses Qwen3 0.6B for hidden state extraction and T5-XXL tokenizer for
    token IDs (no T5 model weights needed). Both are combined by the
    LLM Adapter inside the Anima transformer during denoising.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['anima_text_encoder']):  Default: 'anima_text_encoder'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            prompt (None | str | Unset): Text prompt to encode.
            qwen3_encoder (None | Qwen3EncoderField | Unset): Qwen3 tokenizer and text encoder
            t5_encoder (None | T5EncoderField | Unset): T5 tokenizer and text encoder
            mask (None | TensorField | Unset): A mask defining the region that this conditioning prompt applies to.
    """

    id: str
    type_: Literal["anima_text_encoder"] = "anima_text_encoder"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    prompt: None | str | Unset = UNSET
    qwen3_encoder: None | Qwen3EncoderField | Unset = UNSET
    t5_encoder: None | T5EncoderField | Unset = UNSET
    mask: None | TensorField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.t5_encoder_field import T5EncoderField
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

        t5_encoder: dict[str, Any] | None | Unset
        if isinstance(self.t5_encoder, Unset):
            t5_encoder = UNSET
        elif isinstance(self.t5_encoder, T5EncoderField):
            t5_encoder = self.t5_encoder.to_dict()
        else:
            t5_encoder = self.t5_encoder

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
        if t5_encoder is not UNSET:
            field_dict["t5_encoder"] = t5_encoder
        if mask is not UNSET:
            field_dict["mask"] = mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qwen_3_encoder_field import Qwen3EncoderField
        from ..models.t5_encoder_field import T5EncoderField
        from ..models.tensor_field import TensorField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["anima_text_encoder"], d.pop("type"))
        if type_ != "anima_text_encoder":
            raise ValueError(f"type must match const 'anima_text_encoder', got '{type_}'")

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

        prompt_anima = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            prompt=prompt,
            qwen3_encoder=qwen3_encoder,
            t5_encoder=t5_encoder,
            mask=mask,
        )

        prompt_anima.additional_properties = d
        return prompt_anima

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
