from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.qwen_vl_encoder_field import QwenVLEncoderField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="QwenImageModelLoaderOutput")


@_attrs_define
class QwenImageModelLoaderOutput:
    """Qwen Image model loader output.

    Attributes:
        transformer (TransformerField):
        qwen_vl_encoder (QwenVLEncoderField): Field for Qwen2.5-VL encoder used by Qwen Image Edit models.
        vae (VAEField):
        type_ (Literal['qwen_image_model_loader_output']):  Default: 'qwen_image_model_loader_output'.
    """

    transformer: TransformerField
    qwen_vl_encoder: QwenVLEncoderField
    vae: VAEField
    type_: Literal["qwen_image_model_loader_output"] = "qwen_image_model_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transformer = self.transformer.to_dict()

        qwen_vl_encoder = self.qwen_vl_encoder.to_dict()

        vae = self.vae.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "qwen_vl_encoder": qwen_vl_encoder,
                "vae": vae,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qwen_vl_encoder_field import QwenVLEncoderField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        transformer = TransformerField.from_dict(d.pop("transformer"))

        qwen_vl_encoder = QwenVLEncoderField.from_dict(d.pop("qwen_vl_encoder"))

        vae = VAEField.from_dict(d.pop("vae"))

        type_ = cast(Literal["qwen_image_model_loader_output"], d.pop("type"))
        if type_ != "qwen_image_model_loader_output":
            raise ValueError(f"type must match const 'qwen_image_model_loader_output', got '{type_}'")

        qwen_image_model_loader_output = cls(
            transformer=transformer,
            qwen_vl_encoder=qwen_vl_encoder,
            vae=vae,
            type_=type_,
        )

        qwen_image_model_loader_output.additional_properties = d
        return qwen_image_model_loader_output

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
