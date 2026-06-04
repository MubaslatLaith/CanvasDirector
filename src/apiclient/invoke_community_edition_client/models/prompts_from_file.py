from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromptsFromFile")


@_attrs_define
class PromptsFromFile:
    """Loads prompts from a text file

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['prompt_from_file']):  Default: 'prompt_from_file'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        file_path (None | str | Unset): Path to prompt text file
        pre_prompt (None | str | Unset): String to prepend to each prompt
        post_prompt (None | str | Unset): String to append to each prompt
        start_line (int | Unset): Line in the file to start start from Default: 1.
        max_prompts (int | Unset): Max lines to read from file (0=all) Default: 1.
    """

    id: str
    type_: Literal["prompt_from_file"] = "prompt_from_file"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    file_path: None | str | Unset = UNSET
    pre_prompt: None | str | Unset = UNSET
    post_prompt: None | str | Unset = UNSET
    start_line: int | Unset = 1
    max_prompts: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        file_path: None | str | Unset
        if isinstance(self.file_path, Unset):
            file_path = UNSET
        else:
            file_path = self.file_path

        pre_prompt: None | str | Unset
        if isinstance(self.pre_prompt, Unset):
            pre_prompt = UNSET
        else:
            pre_prompt = self.pre_prompt

        post_prompt: None | str | Unset
        if isinstance(self.post_prompt, Unset):
            post_prompt = UNSET
        else:
            post_prompt = self.post_prompt

        start_line = self.start_line

        max_prompts = self.max_prompts

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
        if file_path is not UNSET:
            field_dict["file_path"] = file_path
        if pre_prompt is not UNSET:
            field_dict["pre_prompt"] = pre_prompt
        if post_prompt is not UNSET:
            field_dict["post_prompt"] = post_prompt
        if start_line is not UNSET:
            field_dict["start_line"] = start_line
        if max_prompts is not UNSET:
            field_dict["max_prompts"] = max_prompts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["prompt_from_file"], d.pop("type"))
        if type_ != "prompt_from_file":
            raise ValueError(f"type must match const 'prompt_from_file', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_path = _parse_file_path(d.pop("file_path", UNSET))

        def _parse_pre_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pre_prompt = _parse_pre_prompt(d.pop("pre_prompt", UNSET))

        def _parse_post_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_prompt = _parse_post_prompt(d.pop("post_prompt", UNSET))

        start_line = d.pop("start_line", UNSET)

        max_prompts = d.pop("max_prompts", UNSET)

        prompts_from_file = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            file_path=file_path,
            pre_prompt=pre_prompt,
            post_prompt=post_prompt,
            start_line=start_line,
            max_prompts=max_prompts,
        )

        prompts_from_file.additional_properties = d
        return prompts_from_file

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
