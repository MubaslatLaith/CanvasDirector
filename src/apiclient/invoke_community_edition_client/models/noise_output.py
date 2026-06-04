from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.latents_field import LatentsField


T = TypeVar("T", bound="NoiseOutput")


@_attrs_define
class NoiseOutput:
    """Invocation noise output

    Attributes:
        noise (LatentsField): A latents tensor primitive field
        width (int): Width of output (px)
        height (int): Height of output (px)
        type_ (Literal['noise_output']):  Default: 'noise_output'.
    """

    noise: LatentsField
    width: int
    height: int
    type_: Literal["noise_output"] = "noise_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        noise = self.noise.to_dict()

        width = self.width

        height = self.height

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noise": noise,
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
        noise = LatentsField.from_dict(d.pop("noise"))

        width = d.pop("width")

        height = d.pop("height")

        type_ = cast(Literal["noise_output"], d.pop("type"))
        if type_ != "noise_output":
            raise ValueError(f"type must match const 'noise_output', got '{type_}'")

        noise_output = cls(
            noise=noise,
            width=width,
            height=height,
            type_=type_,
        )

        noise_output.additional_properties = d
        return noise_output

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
