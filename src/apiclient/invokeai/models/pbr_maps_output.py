from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="PBRMapsOutput")


@_attrs_define
class PBRMapsOutput:
    """
    Attributes:
        normal_map (ImageField): An image primitive field
        roughness_map (ImageField): An image primitive field
        displacement_map (ImageField): An image primitive field
        type_ (Literal['pbr_maps-output']):  Default: 'pbr_maps-output'.
    """

    normal_map: ImageField
    roughness_map: ImageField
    displacement_map: ImageField
    type_: Literal["pbr_maps-output"] = "pbr_maps-output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        normal_map = self.normal_map.to_dict()

        roughness_map = self.roughness_map.to_dict()

        displacement_map = self.displacement_map.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "normal_map": normal_map,
                "roughness_map": roughness_map,
                "displacement_map": displacement_map,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        normal_map = ImageField.from_dict(d.pop("normal_map"))

        roughness_map = ImageField.from_dict(d.pop("roughness_map"))

        displacement_map = ImageField.from_dict(d.pop("displacement_map"))

        type_ = cast(Literal["pbr_maps-output"], d.pop("type"))
        if type_ != "pbr_maps-output":
            raise ValueError(f"type must match const 'pbr_maps-output', got '{type_}'")

        pbr_maps_output = cls(
            normal_map=normal_map,
            roughness_map=roughness_map,
            displacement_map=displacement_map,
            type_=type_,
        )

        pbr_maps_output.additional_properties = d
        return pbr_maps_output

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
