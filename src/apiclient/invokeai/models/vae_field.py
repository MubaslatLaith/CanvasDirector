from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="VAEField")


@_attrs_define
class VAEField:
    """
    Attributes:
        vae (ModelIdentifierField):
        seamless_axes (list[str] | Unset): Axes("x" and "y") to which apply seamless
    """

    vae: ModelIdentifierField
    seamless_axes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vae = self.vae.to_dict()

        seamless_axes: list[str] | Unset = UNSET
        if not isinstance(self.seamless_axes, Unset):
            seamless_axes = self.seamless_axes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vae": vae,
            }
        )
        if seamless_axes is not UNSET:
            field_dict["seamless_axes"] = seamless_axes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        vae = ModelIdentifierField.from_dict(d.pop("vae"))

        seamless_axes = cast(list[str], d.pop("seamless_axes", UNSET))

        vae_field = cls(
            vae=vae,
            seamless_axes=seamless_axes,
        )

        vae_field.additional_properties = d
        return vae_field

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
