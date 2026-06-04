from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField


T = TypeVar("T", bound="CLIPSkipInvocationOutput")


@_attrs_define
class CLIPSkipInvocationOutput:
    """CLIP skip node output

    Attributes:
        clip (CLIPField | None): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        type_ (Literal['clip_skip_output']):  Default: 'clip_skip_output'.
    """

    clip: CLIPField | None
    type_: Literal["clip_skip_output"] = "clip_skip_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField

        clip: dict[str, Any] | None
        if isinstance(self.clip, CLIPField):
            clip = self.clip.to_dict()
        else:
            clip = self.clip

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clip": clip,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField

        d = dict(src_dict)

        def _parse_clip(data: object) -> CLIPField | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_type_0 = CLIPField.from_dict(data)

                return clip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None, data)

        clip = _parse_clip(d.pop("clip"))

        type_ = cast(Literal["clip_skip_output"], d.pop("type"))
        if type_ != "clip_skip_output":
            raise ValueError(f"type must match const 'clip_skip_output', got '{type_}'")

        clip_skip_invocation_output = cls(
            clip=clip,
            type_=type_,
        )

        clip_skip_invocation_output.additional_properties = d
        return clip_skip_invocation_output

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
