from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.starter_model import StarterModel


T = TypeVar("T", bound="StarterModelBundle")


@_attrs_define
class StarterModelBundle:
    """
    Attributes:
        name (str):
        models (list[StarterModel]):
    """

    name: str
    models: list[StarterModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "models": models,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.starter_model import StarterModel

        d = dict(src_dict)
        name = d.pop("name")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = StarterModel.from_dict(models_item_data)

            models.append(models_item)

        starter_model_bundle = cls(
            name=name,
            models=models,
        )

        starter_model_bundle.additional_properties = d
        return starter_model_bundle

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
