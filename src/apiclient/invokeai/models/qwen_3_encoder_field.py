from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lo_ra_field import LoRAField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="Qwen3EncoderField")


@_attrs_define
class Qwen3EncoderField:
    """Field for Qwen3 text encoder used by Z-Image models.

    Attributes:
        tokenizer (ModelIdentifierField):
        text_encoder (ModelIdentifierField):
        loras (list[LoRAField] | Unset): LoRAs to apply on model loading
    """

    tokenizer: ModelIdentifierField
    text_encoder: ModelIdentifierField
    loras: list[LoRAField] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tokenizer = self.tokenizer.to_dict()

        text_encoder = self.text_encoder.to_dict()

        loras: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.loras, Unset):
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
            }
        )
        if loras is not UNSET:
            field_dict["loras"] = loras

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lo_ra_field import LoRAField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        tokenizer = ModelIdentifierField.from_dict(d.pop("tokenizer"))

        text_encoder = ModelIdentifierField.from_dict(d.pop("text_encoder"))

        _loras = d.pop("loras", UNSET)
        loras: list[LoRAField] | Unset = UNSET
        if _loras is not UNSET:
            loras = []
            for loras_item_data in _loras:
                loras_item = LoRAField.from_dict(loras_item_data)

                loras.append(loras_item)

        qwen_3_encoder_field = cls(
            tokenizer=tokenizer,
            text_encoder=text_encoder,
            loras=loras,
        )

        qwen_3_encoder_field.additional_properties = d
        return qwen_3_encoder_field

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
