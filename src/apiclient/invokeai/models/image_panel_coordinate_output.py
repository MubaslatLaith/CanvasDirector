from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImagePanelCoordinateOutput")


@_attrs_define
class ImagePanelCoordinateOutput:
    """
    Attributes:
        x_left (int): The left x-coordinate of the panel.
        y_top (int): The top y-coordinate of the panel.
        width (int): The width of the panel.
        height (int): The height of the panel.
        type_ (Literal['image_panel_coordinate_output']):  Default: 'image_panel_coordinate_output'.
    """

    x_left: int
    y_top: int
    width: int
    height: int
    type_: Literal["image_panel_coordinate_output"] = "image_panel_coordinate_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x_left = self.x_left

        y_top = self.y_top

        width = self.width

        height = self.height

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x_left": x_left,
                "y_top": y_top,
                "width": width,
                "height": height,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x_left = d.pop("x_left")

        y_top = d.pop("y_top")

        width = d.pop("width")

        height = d.pop("height")

        type_ = cast(Literal["image_panel_coordinate_output"], d.pop("type"))
        if type_ != "image_panel_coordinate_output":
            raise ValueError(f"type must match const 'image_panel_coordinate_output', got '{type_}'")

        image_panel_coordinate_output = cls(
            x_left=x_left,
            y_top=y_top,
            width=width,
            height=height,
            type_=type_,
        )

        image_panel_coordinate_output.additional_properties = d
        return image_panel_coordinate_output

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
