from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.glm_encoder_field import GlmEncoderField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="CogView4ModelLoaderOutput")


@_attrs_define
class CogView4ModelLoaderOutput:
    """CogView4 base model loader output.

    Attributes:
        transformer (TransformerField):
        glm_encoder (GlmEncoderField):
        vae (VAEField):
        type_ (Literal['cogview4_model_loader_output']):  Default: 'cogview4_model_loader_output'.
    """

    transformer: TransformerField
    glm_encoder: GlmEncoderField
    vae: VAEField
    type_: Literal["cogview4_model_loader_output"] = "cogview4_model_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transformer = self.transformer.to_dict()

        glm_encoder = self.glm_encoder.to_dict()

        vae = self.vae.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transformer": transformer,
                "glm_encoder": glm_encoder,
                "vae": vae,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.glm_encoder_field import GlmEncoderField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        transformer = TransformerField.from_dict(d.pop("transformer"))

        glm_encoder = GlmEncoderField.from_dict(d.pop("glm_encoder"))

        vae = VAEField.from_dict(d.pop("vae"))

        type_ = cast(Literal["cogview4_model_loader_output"], d.pop("type"))
        if type_ != "cogview4_model_loader_output":
            raise ValueError(f"type must match const 'cogview4_model_loader_output', got '{type_}'")

        cog_view_4_model_loader_output = cls(
            transformer=transformer,
            glm_encoder=glm_encoder,
            vae=vae,
            type_=type_,
        )

        cog_view_4_model_loader_output.additional_properties = d
        return cog_view_4_model_loader_output

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
