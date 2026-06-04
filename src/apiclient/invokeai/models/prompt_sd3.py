from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.t5_encoder_field import T5EncoderField


T = TypeVar("T", bound="PromptSD3")


@_attrs_define
class PromptSD3:
    """Encodes and preps a prompt for a SD3 image.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['sd3_text_encoder']):  Default: 'sd3_text_encoder'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        clip_l (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        clip_g (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        t5_encoder (None | T5EncoderField | Unset): T5 tokenizer and text encoder
        prompt (None | str | Unset): Text prompt to encode.
    """

    id: str
    type_: Literal["sd3_text_encoder"] = "sd3_text_encoder"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    clip_l: CLIPField | None | Unset = UNSET
    clip_g: CLIPField | None | Unset = UNSET
    t5_encoder: None | T5EncoderField | Unset = UNSET
    prompt: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField
        from ..models.t5_encoder_field import T5EncoderField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        clip_l: dict[str, Any] | None | Unset
        if isinstance(self.clip_l, Unset):
            clip_l = UNSET
        elif isinstance(self.clip_l, CLIPField):
            clip_l = self.clip_l.to_dict()
        else:
            clip_l = self.clip_l

        clip_g: dict[str, Any] | None | Unset
        if isinstance(self.clip_g, Unset):
            clip_g = UNSET
        elif isinstance(self.clip_g, CLIPField):
            clip_g = self.clip_g.to_dict()
        else:
            clip_g = self.clip_g

        t5_encoder: dict[str, Any] | None | Unset
        if isinstance(self.t5_encoder, Unset):
            t5_encoder = UNSET
        elif isinstance(self.t5_encoder, T5EncoderField):
            t5_encoder = self.t5_encoder.to_dict()
        else:
            t5_encoder = self.t5_encoder

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

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
        if clip_l is not UNSET:
            field_dict["clip_l"] = clip_l
        if clip_g is not UNSET:
            field_dict["clip_g"] = clip_g
        if t5_encoder is not UNSET:
            field_dict["t5_encoder"] = t5_encoder
        if prompt is not UNSET:
            field_dict["prompt"] = prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.t5_encoder_field import T5EncoderField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["sd3_text_encoder"], d.pop("type"))
        if type_ != "sd3_text_encoder":
            raise ValueError(f"type must match const 'sd3_text_encoder', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_clip_l(data: object) -> CLIPField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_l_type_0 = CLIPField.from_dict(data)

                return clip_l_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None | Unset, data)

        clip_l = _parse_clip_l(d.pop("clip_l", UNSET))

        def _parse_clip_g(data: object) -> CLIPField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_g_type_0 = CLIPField.from_dict(data)

                return clip_g_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None | Unset, data)

        clip_g = _parse_clip_g(d.pop("clip_g", UNSET))

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

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        prompt_sd3 = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            clip_l=clip_l,
            clip_g=clip_g,
            t5_encoder=t5_encoder,
            prompt=prompt,
        )

        prompt_sd3.additional_properties = d
        return prompt_sd3

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
