from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField


T = TypeVar("T", bound="CLIPOutput")


@_attrs_define
class CLIPOutput:
    """Base class for invocations that output a CLIP field

    Attributes:
        clip (CLIPField):
        type_ (Literal['clip_output']):  Default: 'clip_output'.
    """

    clip: CLIPField
    type_: Literal["clip_output"] = "clip_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clip = self.clip.to_dict()

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
        clip = CLIPField.from_dict(d.pop("clip"))

        type_ = cast(Literal["clip_output"], d.pop("type"))
        if type_ != "clip_output":
            raise ValueError(f"type must match const 'clip_output', got '{type_}'")

        clip_output = cls(
            clip=clip,
            type_=type_,
        )

        clip_output.additional_properties = d
        return clip_output

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
