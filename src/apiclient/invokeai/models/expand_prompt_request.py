from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpandPromptRequest")


@_attrs_define
class ExpandPromptRequest:
    """
    Attributes:
        prompt (str):
        model_key (str):
        max_tokens (int | Unset):  Default: 300.
        system_prompt (None | str | Unset):
    """

    prompt: str
    model_key: str
    max_tokens: int | Unset = 300
    system_prompt: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        model_key = self.model_key

        max_tokens = self.max_tokens

        system_prompt: None | str | Unset
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        else:
            system_prompt = self.system_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "model_key": model_key,
            }
        )
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt")

        model_key = d.pop("model_key")

        max_tokens = d.pop("max_tokens", UNSET)

        def _parse_system_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

        expand_prompt_request = cls(
            prompt=prompt,
            model_key=model_key,
            max_tokens=max_tokens,
            system_prompt=system_prompt,
        )

        expand_prompt_request.additional_properties = d
        return expand_prompt_request

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
