from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PromptTemplateOutput")


@_attrs_define
class PromptTemplateOutput:
    """Output for the Prompt Template node

    Attributes:
        positive_prompt (str): The positive prompt with the template applied
        negative_prompt (str): The negative prompt with the template applied
        type_ (Literal['prompt_template_output']):  Default: 'prompt_template_output'.
    """

    positive_prompt: str
    negative_prompt: str
    type_: Literal["prompt_template_output"] = "prompt_template_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        positive_prompt = self.positive_prompt

        negative_prompt = self.negative_prompt

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positive_prompt": positive_prompt,
                "negative_prompt": negative_prompt,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        positive_prompt = d.pop("positive_prompt")

        negative_prompt = d.pop("negative_prompt")

        type_ = cast(Literal["prompt_template_output"], d.pop("type"))
        if type_ != "prompt_template_output":
            raise ValueError(f"type must match const 'prompt_template_output', got '{type_}'")

        prompt_template_output = cls(
            positive_prompt=positive_prompt,
            negative_prompt=negative_prompt,
            type_=type_,
        )

        prompt_template_output.additional_properties = d
        return prompt_template_output

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
