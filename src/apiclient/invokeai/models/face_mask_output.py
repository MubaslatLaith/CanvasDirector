from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="FaceMaskOutput")


@_attrs_define
class FaceMaskOutput:
    """Base class for FaceMask output

    Attributes:
        image (ImageField): An image primitive field
        width (int): The width of the image in pixels
        height (int): The height of the image in pixels
        type_ (Literal['face_mask_output']):  Default: 'face_mask_output'.
        mask (ImageField): An image primitive field
    """

    image: ImageField
    width: int
    height: int
    mask: ImageField
    type_: Literal["face_mask_output"] = "face_mask_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_dict()

        width = self.width

        height = self.height

        type_ = self.type_

        mask = self.mask.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "width": width,
                "height": height,
                "type": type_,
                "mask": mask,
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

        type_ = cast(Literal["face_mask_output"], d.pop("type"))
        if type_ != "face_mask_output":
            raise ValueError(f"type must match const 'face_mask_output', got '{type_}'")

        mask = ImageField.from_dict(d.pop("mask"))

        face_mask_output = cls(
            image=image,
            width=width,
            height=height,
            type_=type_,
            mask=mask,
        )

        face_mask_output.additional_properties = d
        return face_mask_output

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
