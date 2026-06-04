from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoraModelDefaultSettings")


@_attrs_define
class LoraModelDefaultSettings:
    """
    Attributes:
        weight (float | None | Unset): Default weight for this model
    """

    weight: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        weight: float | None | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_weight(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))

        lora_model_default_settings = cls(
            weight=weight,
        )

        return lora_model_default_settings
