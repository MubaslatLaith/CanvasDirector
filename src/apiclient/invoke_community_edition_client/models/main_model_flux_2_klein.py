from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.main_model_flux_2_klein_max_seq_length import MainModelFlux2KleinMaxSeqLength
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="MainModelFlux2Klein")


@_attrs_define
class MainModelFlux2Klein:
    """Loads a Flux2 Klein model, outputting its submodels.

    Flux2 Klein uses Qwen3 as the text encoder instead of CLIP+T5.
    It uses a 32-channel VAE (AutoencoderKLFlux2) instead of the 16-channel FLUX.1 VAE.

    When using a Diffusers format model, both VAE and Qwen3 encoder are extracted
    automatically from the main model. You can override with standalone models:
    - Transformer: Always from Flux2 Klein main model
    - VAE: From main model (Diffusers) or standalone VAE
    - Qwen3 Encoder: From main model (Diffusers) or standalone Qwen3 model

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            model (ModelIdentifierField):
            type_ (Literal['flux2_klein_model_loader']):  Default: 'flux2_klein_model_loader'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            vae_model (ModelIdentifierField | None | Unset): Standalone VAE model. Flux2 Klein uses the same VAE as FLUX
                (16-channel). If not provided, VAE will be loaded from the Qwen3 Source model.
            qwen3_encoder_model (ModelIdentifierField | None | Unset): Standalone Qwen3 Encoder model. If not provided,
                encoder will be loaded from the Qwen3 Source model.
            qwen3_source_model (ModelIdentifierField | None | Unset): Diffusers Flux2 Klein model to extract VAE and/or
                Qwen3 encoder from. Use this if you don't have separate VAE/Qwen3 models. Ignored if both VAE and Qwen3 Encoder
                are provided separately.
            max_seq_len (MainModelFlux2KleinMaxSeqLength | Unset): Max sequence length for the Qwen3 encoder. Default:
                MainModelFlux2KleinMaxSeqLength.VALUE_512.
    """

    id: str
    model: ModelIdentifierField
    type_: Literal["flux2_klein_model_loader"] = "flux2_klein_model_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    vae_model: ModelIdentifierField | None | Unset = UNSET
    qwen3_encoder_model: ModelIdentifierField | None | Unset = UNSET
    qwen3_source_model: ModelIdentifierField | None | Unset = UNSET
    max_seq_len: MainModelFlux2KleinMaxSeqLength | Unset = MainModelFlux2KleinMaxSeqLength.VALUE_512
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

        qwen3_encoder_model: dict[str, Any] | None | Unset
        if isinstance(self.qwen3_encoder_model, Unset):
            qwen3_encoder_model = UNSET
        elif isinstance(self.qwen3_encoder_model, ModelIdentifierField):
            qwen3_encoder_model = self.qwen3_encoder_model.to_dict()
        else:
            qwen3_encoder_model = self.qwen3_encoder_model

        qwen3_source_model: dict[str, Any] | None | Unset
        if isinstance(self.qwen3_source_model, Unset):
            qwen3_source_model = UNSET
        elif isinstance(self.qwen3_source_model, ModelIdentifierField):
            qwen3_source_model = self.qwen3_source_model.to_dict()
        else:
            qwen3_source_model = self.qwen3_source_model

        max_seq_len: int | Unset = UNSET
        if not isinstance(self.max_seq_len, Unset):
            max_seq_len = self.max_seq_len.value

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
        if qwen3_encoder_model is not UNSET:
            field_dict["qwen3_encoder_model"] = qwen3_encoder_model
        if qwen3_source_model is not UNSET:
            field_dict["qwen3_source_model"] = qwen3_source_model
        if max_seq_len is not UNSET:
            field_dict["max_seq_len"] = max_seq_len

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        model = ModelIdentifierField.from_dict(d.pop("model"))

        type_ = cast(Literal["flux2_klein_model_loader"], d.pop("type"))
        if type_ != "flux2_klein_model_loader":
            raise ValueError(f"type must match const 'flux2_klein_model_loader', got '{type_}'")

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

        def _parse_qwen3_encoder_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qwen3_encoder_model_type_0 = ModelIdentifierField.from_dict(data)

                return qwen3_encoder_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        qwen3_encoder_model = _parse_qwen3_encoder_model(d.pop("qwen3_encoder_model", UNSET))

        def _parse_qwen3_source_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qwen3_source_model_type_0 = ModelIdentifierField.from_dict(data)

                return qwen3_source_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        qwen3_source_model = _parse_qwen3_source_model(d.pop("qwen3_source_model", UNSET))

        _max_seq_len = d.pop("max_seq_len", UNSET)
        max_seq_len: MainModelFlux2KleinMaxSeqLength | Unset
        if isinstance(_max_seq_len, Unset):
            max_seq_len = UNSET
        else:
            max_seq_len = MainModelFlux2KleinMaxSeqLength(_max_seq_len)

        main_model_flux_2_klein = cls(
            id=id,
            model=model,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            vae_model=vae_model,
            qwen3_encoder_model=qwen3_encoder_model,
            qwen3_source_model=qwen3_source_model,
            max_seq_len=max_seq_len,
        )

        main_model_flux_2_klein.additional_properties = d
        return main_model_flux_2_klein

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
