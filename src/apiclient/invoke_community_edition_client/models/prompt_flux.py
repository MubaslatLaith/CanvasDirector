from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prompt_fluxt5_max_seq_len_type_0 import PromptFLUXT5MaxSeqLenType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.t5_encoder_field import T5EncoderField
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="PromptFLUX")


@_attrs_define
class PromptFLUX:
    """Encodes and preps a prompt for a flux image.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['flux_text_encoder']):  Default: 'flux_text_encoder'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        clip (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        t5_encoder (None | T5EncoderField | Unset): T5 tokenizer and text encoder
        t5_max_seq_len (None | PromptFLUXT5MaxSeqLenType0 | Unset): Max sequence length for the T5 encoder. Expected to
            be 256 for FLUX schnell models and 512 for FLUX dev models.
        prompt (None | str | Unset): Text prompt to encode.
        mask (None | TensorField | Unset): A mask defining the region that this conditioning prompt applies to.
    """

    id: str
    type_: Literal["flux_text_encoder"] = "flux_text_encoder"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    clip: CLIPField | None | Unset = UNSET
    t5_encoder: None | T5EncoderField | Unset = UNSET
    t5_max_seq_len: None | PromptFLUXT5MaxSeqLenType0 | Unset = UNSET
    prompt: None | str | Unset = UNSET
    mask: None | TensorField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField
        from ..models.t5_encoder_field import T5EncoderField
        from ..models.tensor_field import TensorField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

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

        t5_max_seq_len: int | None | Unset
        if isinstance(self.t5_max_seq_len, Unset):
            t5_max_seq_len = UNSET
        elif isinstance(self.t5_max_seq_len, PromptFLUXT5MaxSeqLenType0):
            t5_max_seq_len = self.t5_max_seq_len.value
        else:
            t5_max_seq_len = self.t5_max_seq_len

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

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
        if clip is not UNSET:
            field_dict["clip"] = clip
        if t5_encoder is not UNSET:
            field_dict["t5_encoder"] = t5_encoder
        if t5_max_seq_len is not UNSET:
            field_dict["t5_max_seq_len"] = t5_max_seq_len
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if mask is not UNSET:
            field_dict["mask"] = mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.t5_encoder_field import T5EncoderField
        from ..models.tensor_field import TensorField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux_text_encoder"], d.pop("type"))
        if type_ != "flux_text_encoder":
            raise ValueError(f"type must match const 'flux_text_encoder', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

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

        def _parse_t5_max_seq_len(data: object) -> None | PromptFLUXT5MaxSeqLenType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                t5_max_seq_len_type_0 = PromptFLUXT5MaxSeqLenType0(data)

                return t5_max_seq_len_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptFLUXT5MaxSeqLenType0 | Unset, data)

        t5_max_seq_len = _parse_t5_max_seq_len(d.pop("t5_max_seq_len", UNSET))

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

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

        prompt_flux = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            clip=clip,
            t5_encoder=t5_encoder,
            t5_max_seq_len=t5_max_seq_len,
            prompt=prompt,
            mask=mask,
        )

        prompt_flux.additional_properties = d
        return prompt_flux

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
