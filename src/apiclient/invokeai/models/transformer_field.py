from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lo_ra_field import LoRAField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="TransformerField")


@_attrs_define
class TransformerField:
    """
    Attributes:
        transformer (ModelIdentifierField):
        loras (list[LoRAField]): LoRAs to apply on model loading
    """

    transformer: ModelIdentifierField
    loras: list[LoRAField]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transformer = self.transformer.to_dict()

        loras = []
        for loras_item_data in self.loras:
            loras_item = loras_item_data.to_dict()
            loras.append(loras_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "loras": loras,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lo_ra_field import LoRAField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        transformer = ModelIdentifierField.from_dict(d.pop("transformer"))

        loras = []
        _loras = d.pop("loras")
        for loras_item_data in _loras:
            loras_item = LoRAField.from_dict(loras_item_data)

            loras.append(loras_item)

        transformer_field = cls(
            transformer=transformer,
            loras=loras,
        )

        transformer_field.additional_properties = d
        return transformer_field

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
