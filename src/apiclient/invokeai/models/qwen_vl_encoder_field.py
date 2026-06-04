from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="QwenVLEncoderField")


@_attrs_define
class QwenVLEncoderField:
    """Field for Qwen2.5-VL encoder used by Qwen Image Edit models.

    Attributes:
        tokenizer (ModelIdentifierField):
        text_encoder (ModelIdentifierField):
    """

    tokenizer: ModelIdentifierField
    text_encoder: ModelIdentifierField
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tokenizer = self.tokenizer.to_dict()

        text_encoder = self.text_encoder.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenizer": tokenizer,
                "text_encoder": text_encoder,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        tokenizer = ModelIdentifierField.from_dict(d.pop("tokenizer"))

        text_encoder = ModelIdentifierField.from_dict(d.pop("text_encoder"))

        qwen_vl_encoder_field = cls(
            tokenizer=tokenizer,
            text_encoder=text_encoder,
        )

        qwen_vl_encoder_field.additional_properties = d
        return qwen_vl_encoder_field

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
