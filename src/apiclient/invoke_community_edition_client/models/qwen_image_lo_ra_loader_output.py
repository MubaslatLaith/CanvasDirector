from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="QwenImageLoRALoaderOutput")


@_attrs_define
class QwenImageLoRALoaderOutput:
    """Qwen Image LoRA Loader Output

    Attributes:
        transformer (None | TransformerField): Transformer
        type_ (Literal['qwen_image_lora_loader_output']):  Default: 'qwen_image_lora_loader_output'.
    """

    transformer: None | TransformerField
    type_: Literal["qwen_image_lora_loader_output"] = "qwen_image_lora_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transformer_field import TransformerField

        transformer: dict[str, Any] | None
        if isinstance(self.transformer, TransformerField):
            transformer = self.transformer.to_dict()
        else:
            transformer = self.transformer

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transformer_field import TransformerField

        d = dict(src_dict)

        def _parse_transformer(data: object) -> None | TransformerField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transformer_type_0 = TransformerField.from_dict(data)

                return transformer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransformerField, data)

        transformer = _parse_transformer(d.pop("transformer"))

        type_ = cast(Literal["qwen_image_lora_loader_output"], d.pop("type"))
        if type_ != "qwen_image_lora_loader_output":
            raise ValueError(f"type must match const 'qwen_image_lora_loader_output', got '{type_}'")

        qwen_image_lo_ra_loader_output = cls(
            transformer=transformer,
            type_=type_,
        )

        qwen_image_lo_ra_loader_output.additional_properties = d
        return qwen_image_lo_ra_loader_output

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
