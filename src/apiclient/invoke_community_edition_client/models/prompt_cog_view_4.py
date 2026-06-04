from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.glm_encoder_field import GlmEncoderField


T = TypeVar("T", bound="PromptCogView4")


@_attrs_define
class PromptCogView4:
    """Encodes and preps a prompt for a cogview4 image.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['cogview4_text_encoder']):  Default: 'cogview4_text_encoder'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        prompt (None | str | Unset): Text prompt to encode.
        glm_encoder (GlmEncoderField | None | Unset): GLM (THUDM) tokenizer and text encoder
    """

    id: str
    type_: Literal["cogview4_text_encoder"] = "cogview4_text_encoder"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    prompt: None | str | Unset = UNSET
    glm_encoder: GlmEncoderField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.glm_encoder_field import GlmEncoderField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        glm_encoder: dict[str, Any] | None | Unset
        if isinstance(self.glm_encoder, Unset):
            glm_encoder = UNSET
        elif isinstance(self.glm_encoder, GlmEncoderField):
            glm_encoder = self.glm_encoder.to_dict()
        else:
            glm_encoder = self.glm_encoder

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
        if glm_encoder is not UNSET:
            field_dict["glm_encoder"] = glm_encoder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.glm_encoder_field import GlmEncoderField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["cogview4_text_encoder"], d.pop("type"))
        if type_ != "cogview4_text_encoder":
            raise ValueError(f"type must match const 'cogview4_text_encoder', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_glm_encoder(data: object) -> GlmEncoderField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                glm_encoder_type_0 = GlmEncoderField.from_dict(data)

                return glm_encoder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GlmEncoderField | None | Unset, data)

        glm_encoder = _parse_glm_encoder(d.pop("glm_encoder", UNSET))

        prompt_cog_view_4 = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            prompt=prompt,
            glm_encoder=glm_encoder,
        )

        prompt_cog_view_4.additional_properties = d
        return prompt_cog_view_4

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
