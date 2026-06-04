from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoRARecallParameter")


@_attrs_define
class LoRARecallParameter:
    """LoRA configuration for recall

    Attributes:
        model_name (str): The name of the LoRA model
        weight (float | Unset): The weight for the LoRA Default: 0.75.
        is_enabled (bool | Unset): Whether the LoRA is enabled Default: True.
    """

    model_name: str
    weight: float | Unset = 0.75
    is_enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name

        weight = self.weight

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_name": model_name,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_name = d.pop("model_name")

        weight = d.pop("weight", UNSET)

        is_enabled = d.pop("is_enabled", UNSET)

        lo_ra_recall_parameter = cls(
            model_name=model_name,
            weight=weight,
            is_enabled=is_enabled,
        )

        lo_ra_recall_parameter.additional_properties = d
        return lo_ra_recall_parameter

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
