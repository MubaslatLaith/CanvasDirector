from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.starter_model_bundle import StarterModelBundle


T = TypeVar("T", bound="StarterModelResponseStarterBundles")


@_attrs_define
class StarterModelResponseStarterBundles:
    """ """

    additional_properties: dict[str, StarterModelBundle] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.starter_model_bundle import StarterModelBundle

        d = dict(src_dict)
        starter_model_response_starter_bundles = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StarterModelBundle.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        starter_model_response_starter_bundles.additional_properties = additional_properties
        return starter_model_response_starter_bundles

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> StarterModelBundle:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: StarterModelBundle) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
