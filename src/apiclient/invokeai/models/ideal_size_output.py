from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IdealSizeOutput")


@_attrs_define
class IdealSizeOutput:
    """Base class for invocations that output an image

    Attributes:
        width (int): The ideal width of the image (in pixels)
        height (int): The ideal height of the image (in pixels)
        type_ (Literal['ideal_size_output']):  Default: 'ideal_size_output'.
    """

    width: int
    height: int
    type_: Literal["ideal_size_output"] = "ideal_size_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width": width,
                "height": height,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width")

        height = d.pop("height")

        type_ = cast(Literal["ideal_size_output"], d.pop("type"))
        if type_ != "ideal_size_output":
            raise ValueError(f"type must match const 'ideal_size_output', got '{type_}'")

        ideal_size_output = cls(
            width=width,
            height=height,
            type_=type_,
        )

        ideal_size_output.additional_properties = d
        return ideal_size_output

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
