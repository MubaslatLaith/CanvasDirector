from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="MainModelFLUX")


@_attrs_define
class MainModelFLUX:
    """Loads a flux base model, outputting its submodels.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['flux_model_loader']):  Default: 'flux_model_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        model (ModelIdentifierField | None | Unset): Flux model (Transformer) to load
        t5_encoder_model (ModelIdentifierField | None | Unset): T5 tokenizer and text encoder
        clip_embed_model (ModelIdentifierField | None | Unset): CLIP Embed loader
        vae_model (ModelIdentifierField | None | Unset): VAE model to load
    """

    id: str
    type_: Literal["flux_model_loader"] = "flux_model_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    model: ModelIdentifierField | None | Unset = UNSET
    t5_encoder_model: ModelIdentifierField | None | Unset = UNSET
    clip_embed_model: ModelIdentifierField | None | Unset = UNSET
    vae_model: ModelIdentifierField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        model: dict[str, Any] | None | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ModelIdentifierField):
            model = self.model.to_dict()
        else:
            model = self.model

        t5_encoder_model: dict[str, Any] | None | Unset
        if isinstance(self.t5_encoder_model, Unset):
            t5_encoder_model = UNSET
        elif isinstance(self.t5_encoder_model, ModelIdentifierField):
            t5_encoder_model = self.t5_encoder_model.to_dict()
        else:
            t5_encoder_model = self.t5_encoder_model

        clip_embed_model: dict[str, Any] | None | Unset
        if isinstance(self.clip_embed_model, Unset):
            clip_embed_model = UNSET
        elif isinstance(self.clip_embed_model, ModelIdentifierField):
            clip_embed_model = self.clip_embed_model.to_dict()
        else:
            clip_embed_model = self.clip_embed_model

        vae_model: dict[str, Any] | None | Unset
        if isinstance(self.vae_model, Unset):
            vae_model = UNSET
        elif isinstance(self.vae_model, ModelIdentifierField):
            vae_model = self.vae_model.to_dict()
        else:
            vae_model = self.vae_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if model is not UNSET:
            field_dict["model"] = model
        if t5_encoder_model is not UNSET:
            field_dict["t5_encoder_model"] = t5_encoder_model
        if clip_embed_model is not UNSET:
            field_dict["clip_embed_model"] = clip_embed_model
        if vae_model is not UNSET:
            field_dict["vae_model"] = vae_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux_model_loader"], d.pop("type"))
        if type_ != "flux_model_loader":
            raise ValueError(f"type must match const 'flux_model_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_0 = ModelIdentifierField.from_dict(data)

                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_t5_encoder_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                t5_encoder_model_type_0 = ModelIdentifierField.from_dict(data)

                return t5_encoder_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        t5_encoder_model = _parse_t5_encoder_model(d.pop("t5_encoder_model", UNSET))

        def _parse_clip_embed_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_embed_model_type_0 = ModelIdentifierField.from_dict(data)

                return clip_embed_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        clip_embed_model = _parse_clip_embed_model(d.pop("clip_embed_model", UNSET))

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

        main_model_flux = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            model=model,
            t5_encoder_model=t5_encoder_model,
            clip_embed_model=clip_embed_model,
            vae_model=vae_model,
        )

        main_model_flux.additional_properties = d
        return main_model_flux

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
