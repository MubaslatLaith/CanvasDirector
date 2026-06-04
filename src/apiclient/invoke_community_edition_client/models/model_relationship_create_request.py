from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelRelationshipCreateRequest")


@_attrs_define
class ModelRelationshipCreateRequest:
    """
    Attributes:
        model_key_1 (str): The key of the first model in the relationship
        model_key_2 (str): The key of the second model in the relationship
    """

    model_key_1: str
    model_key_2: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_key_1 = self.model_key_1

        model_key_2 = self.model_key_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_key_1": model_key_1,
                "model_key_2": model_key_2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_key_1 = d.pop("model_key_1")

        model_key_2 = d.pop("model_key_2")

        model_relationship_create_request = cls(
            model_key_1=model_key_1,
            model_key_2=model_key_2,
        )

        model_relationship_create_request.additional_properties = d
        return model_relationship_create_request

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
