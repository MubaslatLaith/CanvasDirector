from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField


T = TypeVar("T", bound="PromptSDXLRefiner")


@_attrs_define
class PromptSDXLRefiner:
    """Parse prompt using compel package to conditioning.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['sdxl_refiner_compel_prompt']):  Default: 'sdxl_refiner_compel_prompt'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        style (str | Unset): Prompt to be parsed by Compel to create a conditioning tensor Default: ''.
        original_width (int | Unset):  Default: 1024.
        original_height (int | Unset):  Default: 1024.
        crop_top (int | Unset):  Default: 0.
        crop_left (int | Unset):  Default: 0.
        aesthetic_score (float | Unset): The aesthetic score to apply to the conditioning tensor Default: 6.0.
        clip2 (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
    """

    id: str
    type_: Literal["sdxl_refiner_compel_prompt"] = "sdxl_refiner_compel_prompt"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    style: str | Unset = ""
    original_width: int | Unset = 1024
    original_height: int | Unset = 1024
    crop_top: int | Unset = 0
    crop_left: int | Unset = 0
    aesthetic_score: float | Unset = 6.0
    clip2: CLIPField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        style = self.style

        original_width = self.original_width

        original_height = self.original_height

        crop_top = self.crop_top

        crop_left = self.crop_left

        aesthetic_score = self.aesthetic_score

        clip2: dict[str, Any] | None | Unset
        if isinstance(self.clip2, Unset):
            clip2 = UNSET
        elif isinstance(self.clip2, CLIPField):
            clip2 = self.clip2.to_dict()
        else:
            clip2 = self.clip2

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
        if style is not UNSET:
            field_dict["style"] = style
        if original_width is not UNSET:
            field_dict["original_width"] = original_width
        if original_height is not UNSET:
            field_dict["original_height"] = original_height
        if crop_top is not UNSET:
            field_dict["crop_top"] = crop_top
        if crop_left is not UNSET:
            field_dict["crop_left"] = crop_left
        if aesthetic_score is not UNSET:
            field_dict["aesthetic_score"] = aesthetic_score
        if clip2 is not UNSET:
            field_dict["clip2"] = clip2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["sdxl_refiner_compel_prompt"], d.pop("type"))
        if type_ != "sdxl_refiner_compel_prompt":
            raise ValueError(f"type must match const 'sdxl_refiner_compel_prompt', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        style = d.pop("style", UNSET)

        original_width = d.pop("original_width", UNSET)

        original_height = d.pop("original_height", UNSET)

        crop_top = d.pop("crop_top", UNSET)

        crop_left = d.pop("crop_left", UNSET)

        aesthetic_score = d.pop("aesthetic_score", UNSET)

        def _parse_clip2(data: object) -> CLIPField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip2_type_0 = CLIPField.from_dict(data)

                return clip2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None | Unset, data)

        clip2 = _parse_clip2(d.pop("clip2", UNSET))

        prompt_sdxl_refiner = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            style=style,
            original_width=original_width,
            original_height=original_height,
            crop_top=crop_top,
            crop_left=crop_left,
            aesthetic_score=aesthetic_score,
            clip2=clip2,
        )

        prompt_sdxl_refiner.additional_properties = d
        return prompt_sdxl_refiner

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
