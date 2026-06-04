from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynamicPrompt")


@_attrs_define
class DynamicPrompt:
    """Parses a prompt using adieyal/dynamicprompts' random or combinatorial generator

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['dynamic_prompt']):  Default: 'dynamic_prompt'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: False.
        prompt (None | str | Unset): The prompt to parse with dynamicprompts
        max_prompts (int | Unset): The number of prompts to generate Default: 1.
        combinatorial (bool | Unset): Whether to use the combinatorial generator Default: False.
    """

    id: str
    type_: Literal["dynamic_prompt"] = "dynamic_prompt"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = False
    prompt: None | str | Unset = UNSET
    max_prompts: int | Unset = 1
    combinatorial: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        max_prompts = self.max_prompts

        combinatorial = self.combinatorial

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
        if max_prompts is not UNSET:
            field_dict["max_prompts"] = max_prompts
        if combinatorial is not UNSET:
            field_dict["combinatorial"] = combinatorial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["dynamic_prompt"], d.pop("type"))
        if type_ != "dynamic_prompt":
            raise ValueError(f"type must match const 'dynamic_prompt', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        max_prompts = d.pop("max_prompts", UNSET)

        combinatorial = d.pop("combinatorial", UNSET)

        dynamic_prompt = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            prompt=prompt,
            max_prompts=max_prompts,
            combinatorial=combinatorial,
        )

        dynamic_prompt.additional_properties = d
        return dynamic_prompt

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
