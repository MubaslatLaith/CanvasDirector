from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="PromptSD15")


@_attrs_define
class PromptSD15:
    """Parse prompt using compel package to conditioning.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['compel']):  Default: 'compel'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        prompt (str | Unset): Prompt to be parsed by Compel to create a conditioning tensor Default: ''.
        clip (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        mask (None | TensorField | Unset): A mask defining the region that this conditioning prompt applies to.
    """

    id: str
    type_: Literal["compel"] = "compel"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    prompt: str | Unset = ""
    clip: CLIPField | None | Unset = UNSET
    mask: None | TensorField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField
        from ..models.tensor_field import TensorField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        prompt = self.prompt

        clip: dict[str, Any] | None | Unset
        if isinstance(self.clip, Unset):
            clip = UNSET
        elif isinstance(self.clip, CLIPField):
            clip = self.clip.to_dict()
        else:
            clip = self.clip

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
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if clip is not UNSET:
            field_dict["clip"] = clip
        if mask is not UNSET:
            field_dict["mask"] = mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.tensor_field import TensorField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["compel"], d.pop("type"))
        if type_ != "compel":
            raise ValueError(f"type must match const 'compel', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        prompt = d.pop("prompt", UNSET)

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

        prompt_sd15 = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            prompt=prompt,
            clip=clip,
            mask=mask,
        )

        prompt_sd15.additional_properties = d
        return prompt_sd15

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
