from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyParseDynamicprompts")


@_attrs_define
class BodyParseDynamicprompts:
    """
    Attributes:
        prompt (str): The prompt to parse with dynamicprompts
        max_prompts (int | Unset): The max number of prompts to generate Default: 1000.
        combinatorial (bool | Unset): Whether to use the combinatorial generator Default: True.
        seed (int | None | Unset): The seed to use for random generation. Only used if not combinatorial
    """

    prompt: str
    max_prompts: int | Unset = 1000
    combinatorial: bool | Unset = True
    seed: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        max_prompts = self.max_prompts

        combinatorial = self.combinatorial

        seed: int | None | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
            }
        )
        if max_prompts is not UNSET:
            field_dict["max_prompts"] = max_prompts
        if combinatorial is not UNSET:
            field_dict["combinatorial"] = combinatorial
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt")

        max_prompts = d.pop("max_prompts", UNSET)

        combinatorial = d.pop("combinatorial", UNSET)

        def _parse_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))

        body_parse_dynamicprompts = cls(
            prompt=prompt,
            max_prompts=max_prompts,
            combinatorial=combinatorial,
            seed=seed,
        )

        body_parse_dynamicprompts.additional_properties = d
        return body_parse_dynamicprompts

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
