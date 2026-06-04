from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bounding_box_field import BoundingBoxField


T = TypeVar("T", bound="BoundingBoxOutput")


@_attrs_define
class BoundingBoxOutput:
    """Base class for nodes that output a single bounding box

    Attributes:
        bounding_box (BoundingBoxField): A bounding box primitive value.
        type_ (Literal['bounding_box_output']):  Default: 'bounding_box_output'.
    """

    bounding_box: BoundingBoxField
    type_: Literal["bounding_box_output"] = "bounding_box_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bounding_box = self.bounding_box.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bounding_box": bounding_box,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bounding_box_field import BoundingBoxField

        d = dict(src_dict)
        bounding_box = BoundingBoxField.from_dict(d.pop("bounding_box"))

        type_ = cast(Literal["bounding_box_output"], d.pop("type"))
        if type_ != "bounding_box_output":
            raise ValueError(f"type must match const 'bounding_box_output', got '{type_}'")

        bounding_box_output = cls(
            bounding_box=bounding_box,
            type_=type_,
        )

        bounding_box_output.additional_properties = d
        return bounding_box_output

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
