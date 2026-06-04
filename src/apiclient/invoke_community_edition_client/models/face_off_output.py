from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="FaceOffOutput")


@_attrs_define
class FaceOffOutput:
    """Base class for FaceOff Output

    Attributes:
        image (ImageField): An image primitive field
        width (int): The width of the image in pixels
        height (int): The height of the image in pixels
        type_ (Literal['face_off_output']):  Default: 'face_off_output'.
        mask (ImageField): An image primitive field
        x (int): The x coordinate of the bounding box's left side
        y (int): The y coordinate of the bounding box's top side
    """

    image: ImageField
    width: int
    height: int
    mask: ImageField
    x: int
    y: int
    type_: Literal["face_off_output"] = "face_off_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_dict()

        width = self.width

        height = self.height

        type_ = self.type_

        mask = self.mask.to_dict()

        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "width": width,
                "height": height,
                "type": type_,
                "mask": mask,
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        image = ImageField.from_dict(d.pop("image"))

        width = d.pop("width")

        height = d.pop("height")

        type_ = cast(Literal["face_off_output"], d.pop("type"))
        if type_ != "face_off_output":
            raise ValueError(f"type must match const 'face_off_output', got '{type_}'")

        mask = ImageField.from_dict(d.pop("mask"))

        x = d.pop("x")

        y = d.pop("y")

        face_off_output = cls(
            image=image,
            width=width,
            height=height,
            type_=type_,
            mask=mask,
            x=x,
            y=y,
        )

        face_off_output.additional_properties = d
        return face_off_output

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
