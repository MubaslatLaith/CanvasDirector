from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.style_preset_field import StylePresetField


T = TypeVar("T", bound="PromptTemplate")


@_attrs_define
class PromptTemplate:
    """Applies a Style Preset template to positive and negative prompts.

    Select a Style Preset and provide positive/negative prompts. The node replaces
    {prompt} placeholders in the template with your input prompts.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['prompt_template']):  Default: 'prompt_template'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            style_preset (None | StylePresetField | Unset): The Style Preset to use as a template
            positive_prompt (str | Unset): The positive prompt to insert into the template's {prompt} placeholder Default:
                ''.
            negative_prompt (str | Unset): The negative prompt to insert into the template's {prompt} placeholder Default:
                ''.
    """

    id: str
    type_: Literal["prompt_template"] = "prompt_template"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    style_preset: None | StylePresetField | Unset = UNSET
    positive_prompt: str | Unset = ""
    negative_prompt: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.style_preset_field import StylePresetField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        style_preset: dict[str, Any] | None | Unset
        if isinstance(self.style_preset, Unset):
            style_preset = UNSET
        elif isinstance(self.style_preset, StylePresetField):
            style_preset = self.style_preset.to_dict()
        else:
            style_preset = self.style_preset

        positive_prompt = self.positive_prompt

        negative_prompt = self.negative_prompt

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
        if style_preset is not UNSET:
            field_dict["style_preset"] = style_preset
        if positive_prompt is not UNSET:
            field_dict["positive_prompt"] = positive_prompt
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.style_preset_field import StylePresetField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["prompt_template"], d.pop("type"))
        if type_ != "prompt_template":
            raise ValueError(f"type must match const 'prompt_template', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_style_preset(data: object) -> None | StylePresetField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                style_preset_type_0 = StylePresetField.from_dict(data)

                return style_preset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StylePresetField | Unset, data)

        style_preset = _parse_style_preset(d.pop("style_preset", UNSET))

        positive_prompt = d.pop("positive_prompt", UNSET)

        negative_prompt = d.pop("negative_prompt", UNSET)

        prompt_template = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            style_preset=style_preset,
            positive_prompt=positive_prompt,
            negative_prompt=negative_prompt,
        )

        prompt_template.additional_properties = d
        return prompt_template

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
