from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.latents_field import LatentsField


T = TypeVar("T", bound="LatentsOutput")


@_attrs_define
class LatentsOutput:
    """Base class for nodes that output a single latents tensor

    Attributes:
        latents (LatentsField): A latents tensor primitive field
        width (int): Width of output (px)
        height (int): Height of output (px)
        type_ (Literal['latents_output']):  Default: 'latents_output'.
    """

    latents: LatentsField
    width: int
    height: int
    type_: Literal["latents_output"] = "latents_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latents = self.latents.to_dict()

        width = self.width

        height = self.height

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latents": latents,
                "width": width,
                "height": height,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latents_field import LatentsField

        d = dict(src_dict)
        latents = LatentsField.from_dict(d.pop("latents"))

        width = d.pop("width")

        height = d.pop("height")

        type_ = cast(Literal["latents_output"], d.pop("type"))
        if type_ != "latents_output":
            raise ValueError(f"type must match const 'latents_output', got '{type_}'")

        latents_output = cls(
            latents=latents,
            width=width,
            height=height,
            type_=type_,
        )

        latents_output.additional_properties = d
        return latents_output

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
