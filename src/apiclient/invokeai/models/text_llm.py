from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="TextLLM")


@_attrs_define
class TextLLM:
    """Run a text language model to generate or expand text (e.g. for prompt expansion).

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['text_llm']):  Default: 'text_llm'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        prompt (str | Unset): Input text prompt. Default: ''.
        system_prompt (str | Unset): System prompt that guides the model's behavior. Default: 'You are an expert prompt
            writer for AI image generation. Given a brief description, expand it into a detailed, vivid prompt suitable for
            generating high-quality images. Only output the expanded prompt, nothing else.'.
        text_llm_model (ModelIdentifierField | None | Unset): The text language model to use for text generation
        max_tokens (int | Unset): Maximum number of tokens to generate. Default: 300.
    """

    id: str
    type_: Literal["text_llm"] = "text_llm"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    prompt: str | Unset = ""
    system_prompt: str | Unset = (
        "You are an expert prompt writer for AI image generation. Given a brief description, expand it into a detailed, vivid prompt suitable for generating high-quality images. Only output the expanded prompt, nothing else."
    )
    text_llm_model: ModelIdentifierField | None | Unset = UNSET
    max_tokens: int | Unset = 300
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        prompt = self.prompt

        system_prompt = self.system_prompt

        text_llm_model: dict[str, Any] | None | Unset
        if isinstance(self.text_llm_model, Unset):
            text_llm_model = UNSET
        elif isinstance(self.text_llm_model, ModelIdentifierField):
            text_llm_model = self.text_llm_model.to_dict()
        else:
            text_llm_model = self.text_llm_model

        max_tokens = self.max_tokens

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
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if text_llm_model is not UNSET:
            field_dict["text_llm_model"] = text_llm_model
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["text_llm"], d.pop("type"))
        if type_ != "text_llm":
            raise ValueError(f"type must match const 'text_llm', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        prompt = d.pop("prompt", UNSET)

        system_prompt = d.pop("system_prompt", UNSET)

        def _parse_text_llm_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                text_llm_model_type_0 = ModelIdentifierField.from_dict(data)

                return text_llm_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        text_llm_model = _parse_text_llm_model(d.pop("text_llm_model", UNSET))

        max_tokens = d.pop("max_tokens", UNSET)

        text_llm = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            prompt=prompt,
            system_prompt=system_prompt,
            text_llm_model=text_llm_model,
            max_tokens=max_tokens,
        )

        text_llm.additional_properties = d
        return text_llm

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
