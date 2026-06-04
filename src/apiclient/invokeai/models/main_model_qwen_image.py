from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="MainModelQwenImage")


@_attrs_define
class MainModelQwenImage:
    """Loads a Qwen Image model, outputting its submodels.

    The transformer is always loaded from the main model (Diffusers or GGUF).

    Components can be mixed and matched:
    - VAE: standalone Qwen Image VAE checkpoint, the Component Source (Diffusers),
      or the main model if it's Diffusers.
    - Qwen VL Encoder: standalone Qwen2.5-VL encoder, the Component Source
      (Diffusers), or the main model if it's Diffusers.

    Together, the standalone VAE and standalone encoder allow running a GGUF
    transformer without ever downloading the full ~40 GB Diffusers pipeline.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            model (ModelIdentifierField):
            type_ (Literal['qwen_image_model_loader']):  Default: 'qwen_image_model_loader'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            vae_model (ModelIdentifierField | None | Unset): Standalone Qwen Image VAE model. If not provided, VAE will be
                loaded from the Component Source (or from the main model if it is Diffusers).
            qwen_vl_encoder_model (ModelIdentifierField | None | Unset): Standalone Qwen2.5-VL encoder model. If not
                provided, the encoder will be loaded from the Component Source (or from the main model if it is Diffusers).
            component_source (ModelIdentifierField | None | Unset): Diffusers Qwen Image model to extract VAE and/or Qwen VL
                encoder from. Use this if you don't have separate VAE/encoder models. Ignored for any submodel that is provided
                separately.
    """

    id: str
    model: ModelIdentifierField
    type_: Literal["qwen_image_model_loader"] = "qwen_image_model_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    vae_model: ModelIdentifierField | None | Unset = UNSET
    qwen_vl_encoder_model: ModelIdentifierField | None | Unset = UNSET
    component_source: ModelIdentifierField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

        model = self.model.to_dict()

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        vae_model: dict[str, Any] | None | Unset
        if isinstance(self.vae_model, Unset):
            vae_model = UNSET
        elif isinstance(self.vae_model, ModelIdentifierField):
            vae_model = self.vae_model.to_dict()
        else:
            vae_model = self.vae_model

        qwen_vl_encoder_model: dict[str, Any] | None | Unset
        if isinstance(self.qwen_vl_encoder_model, Unset):
            qwen_vl_encoder_model = UNSET
        elif isinstance(self.qwen_vl_encoder_model, ModelIdentifierField):
            qwen_vl_encoder_model = self.qwen_vl_encoder_model.to_dict()
        else:
            qwen_vl_encoder_model = self.qwen_vl_encoder_model

        component_source: dict[str, Any] | None | Unset
        if isinstance(self.component_source, Unset):
            component_source = UNSET
        elif isinstance(self.component_source, ModelIdentifierField):
            component_source = self.component_source.to_dict()
        else:
            component_source = self.component_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model": model,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if vae_model is not UNSET:
            field_dict["vae_model"] = vae_model
        if qwen_vl_encoder_model is not UNSET:
            field_dict["qwen_vl_encoder_model"] = qwen_vl_encoder_model
        if component_source is not UNSET:
            field_dict["component_source"] = component_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        model = ModelIdentifierField.from_dict(d.pop("model"))

        type_ = cast(Literal["qwen_image_model_loader"], d.pop("type"))
        if type_ != "qwen_image_model_loader":
            raise ValueError(f"type must match const 'qwen_image_model_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_vae_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vae_model_type_0 = ModelIdentifierField.from_dict(data)

                return vae_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        vae_model = _parse_vae_model(d.pop("vae_model", UNSET))

        def _parse_qwen_vl_encoder_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qwen_vl_encoder_model_type_0 = ModelIdentifierField.from_dict(data)

                return qwen_vl_encoder_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        qwen_vl_encoder_model = _parse_qwen_vl_encoder_model(d.pop("qwen_vl_encoder_model", UNSET))

        def _parse_component_source(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_source_type_0 = ModelIdentifierField.from_dict(data)

                return component_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        component_source = _parse_component_source(d.pop("component_source", UNSET))

        main_model_qwen_image = cls(
            id=id,
            model=model,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            vae_model=vae_model,
            qwen_vl_encoder_model=qwen_vl_encoder_model,
            component_source=component_source,
        )

        main_model_qwen_image.additional_properties = d
        return main_model_qwen_image

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
