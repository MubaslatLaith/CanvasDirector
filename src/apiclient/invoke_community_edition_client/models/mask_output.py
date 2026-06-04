from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="MaskOutput")


@_attrs_define
class MaskOutput:
    """A torch mask tensor.

    Attributes:
        mask (TensorField): A tensor primitive field.
        width (int): The width of the mask in pixels.
        height (int): The height of the mask in pixels.
        type_ (Literal['mask_output']):  Default: 'mask_output'.
    """

    mask: TensorField
    width: int
    height: int
    type_: Literal["mask_output"] = "mask_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mask = self.mask.to_dict()

        width = self.width

        height = self.height

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mask": mask,
                "width": width,
                "height": height,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tensor_field import TensorField

        d = dict(src_dict)
        mask = TensorField.from_dict(d.pop("mask"))

        width = d.pop("width")

        height = d.pop("height")

        type_ = cast(Literal["mask_output"], d.pop("type"))
        if type_ != "mask_output":
            raise ValueError(f"type must match const 'mask_output', got '{type_}'")

        mask_output = cls(
            mask=mask,
            width=width,
            height=height,
            type_=type_,
        )

        mask_output.additional_properties = d
        return mask_output

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
