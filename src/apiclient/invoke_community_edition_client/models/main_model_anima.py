from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="MainModelAnima")


@_attrs_define
class MainModelAnima:
    """Loads an Anima model, outputting its submodels.

    Anima uses:
    - Transformer: Cosmos Predict2 DiT + LLM Adapter (from single-file checkpoint)
    - Qwen3 Encoder: Qwen3 0.6B (standalone single-file)
    - VAE: AutoencoderKLQwenImage / Wan 2.1 VAE (standalone single-file or FLUX VAE)
    - T5 Encoder: T5-XXL model (only the tokenizer submodel is used, for LLM Adapter token IDs)

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            model (ModelIdentifierField):
            vae_model (ModelIdentifierField):
            qwen3_encoder_model (ModelIdentifierField):
            t5_encoder_model (ModelIdentifierField):
            type_ (Literal['anima_model_loader']):  Default: 'anima_model_loader'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
    """

    id: str
    model: ModelIdentifierField
    vae_model: ModelIdentifierField
    qwen3_encoder_model: ModelIdentifierField
    t5_encoder_model: ModelIdentifierField
    type_: Literal["anima_model_loader"] = "anima_model_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model = self.model.to_dict()

        vae_model = self.vae_model.to_dict()

        qwen3_encoder_model = self.qwen3_encoder_model.to_dict()

        t5_encoder_model = self.t5_encoder_model.to_dict()

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model": model,
                "vae_model": vae_model,
                "qwen3_encoder_model": qwen3_encoder_model,
                "t5_encoder_model": t5_encoder_model,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        model = ModelIdentifierField.from_dict(d.pop("model"))

        vae_model = ModelIdentifierField.from_dict(d.pop("vae_model"))

        qwen3_encoder_model = ModelIdentifierField.from_dict(d.pop("qwen3_encoder_model"))

        t5_encoder_model = ModelIdentifierField.from_dict(d.pop("t5_encoder_model"))

        type_ = cast(Literal["anima_model_loader"], d.pop("type"))
        if type_ != "anima_model_loader":
            raise ValueError(f"type must match const 'anima_model_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        main_model_anima = cls(
            id=id,
            model=model,
            vae_model=vae_model,
            qwen3_encoder_model=qwen3_encoder_model,
            t5_encoder_model=t5_encoder_model,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
        )

        main_model_anima.additional_properties = d
        return main_model_anima

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
