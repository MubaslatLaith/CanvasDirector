from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="VAEModelSD15SD2SDXLSD3FLUX")


@_attrs_define
class VAEModelSD15SD2SDXLSD3FLUX:
    """Loads a VAE model, outputting a VaeLoaderOutput

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['vae_loader']):  Default: 'vae_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        vae_model (ModelIdentifierField | None | Unset): VAE model to load
    """

    id: str
    type_: Literal["vae_loader"] = "vae_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    vae_model: ModelIdentifierField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

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
        if vae_model is not UNSET:
            field_dict["vae_model"] = vae_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["vae_loader"], d.pop("type"))
        if type_ != "vae_loader":
            raise ValueError(f"type must match const 'vae_loader', got '{type_}'")

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

        vae_model_sd15sd2sdxlsd3flux = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            vae_model=vae_model,
        )

        vae_model_sd15sd2sdxlsd3flux.additional_properties = d
        return vae_model_sd15sd2sdxlsd3flux

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
