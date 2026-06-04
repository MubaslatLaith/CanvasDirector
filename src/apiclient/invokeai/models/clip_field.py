from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lo_ra_field import LoRAField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="CLIPField")


@_attrs_define
class CLIPField:
    """
    Attributes:
        tokenizer (ModelIdentifierField):
        text_encoder (ModelIdentifierField):
        skipped_layers (int): Number of skipped layers in text_encoder
        loras (list[LoRAField]): LoRAs to apply on model loading
    """

    tokenizer: ModelIdentifierField
    text_encoder: ModelIdentifierField
    skipped_layers: int
    loras: list[LoRAField]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tokenizer = self.tokenizer.to_dict()

        text_encoder = self.text_encoder.to_dict()

        skipped_layers = self.skipped_layers

        loras = []
        for loras_item_data in self.loras:
            loras_item = loras_item_data.to_dict()
            loras.append(loras_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenizer": tokenizer,
                "text_encoder": text_encoder,
                "skipped_layers": skipped_layers,
                "loras": loras,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lo_ra_field import LoRAField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        tokenizer = ModelIdentifierField.from_dict(d.pop("tokenizer"))

        text_encoder = ModelIdentifierField.from_dict(d.pop("text_encoder"))

        skipped_layers = d.pop("skipped_layers")

        loras = []
        _loras = d.pop("loras")
        for loras_item_data in _loras:
            loras_item = LoRAField.from_dict(loras_item_data)

            loras.append(loras_item)

        clip_field = cls(
            tokenizer=tokenizer,
            text_encoder=text_encoder,
            skipped_layers=skipped_layers,
            loras=loras,
        )

        clip_field.additional_properties = d
        return clip_field

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
