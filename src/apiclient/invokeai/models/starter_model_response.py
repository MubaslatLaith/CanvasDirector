from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.starter_model import StarterModel
    from ..models.starter_model_response_starter_bundles import StarterModelResponseStarterBundles


T = TypeVar("T", bound="StarterModelResponse")


@_attrs_define
class StarterModelResponse:
    """
    Attributes:
        starter_models (list[StarterModel]):
        starter_bundles (StarterModelResponseStarterBundles):
    """

    starter_models: list[StarterModel]
    starter_bundles: StarterModelResponseStarterBundles
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starter_models = []
        for starter_models_item_data in self.starter_models:
            starter_models_item = starter_models_item_data.to_dict()
            starter_models.append(starter_models_item)

        starter_bundles = self.starter_bundles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "starter_models": starter_models,
                "starter_bundles": starter_bundles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.starter_model import StarterModel
        from ..models.starter_model_response_starter_bundles import StarterModelResponseStarterBundles

        d = dict(src_dict)
        starter_models = []
        _starter_models = d.pop("starter_models")
        for starter_models_item_data in _starter_models:
            starter_models_item = StarterModel.from_dict(starter_models_item_data)

            starter_models.append(starter_models_item)

        starter_bundles = StarterModelResponseStarterBundles.from_dict(d.pop("starter_bundles"))

        starter_model_response = cls(
            starter_models=starter_models,
            starter_bundles=starter_bundles,
        )

        starter_model_response.additional_properties = d
        return starter_model_response

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
