from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_repo_variant import ModelRepoVariant
from ..types import UNSET, Unset

T = TypeVar("T", bound="HFModelSource")


@_attrs_define
class HFModelSource:
    """A HuggingFace repo_id with optional variant, sub-folder(s) and access token.
    Note that the variant option, if not provided to the constructor, will default to fp16, which is
    what people (almost) always want.

    The subfolder can be a single path or multiple paths joined by '+' (e.g., "text_encoder+tokenizer").
    When multiple subfolders are specified, all of them will be downloaded and combined into the model directory.

        Attributes:
            repo_id (str):
            variant (ModelRepoVariant | None | Unset):  Default: ModelRepoVariant.FP16.
            subfolder (None | str | Unset):
            access_token (None | str | Unset):
            type_ (Literal['hf'] | Unset):  Default: 'hf'.
    """

    repo_id: str
    variant: ModelRepoVariant | None | Unset = ModelRepoVariant.FP16
    subfolder: None | str | Unset = UNSET
    access_token: None | str | Unset = UNSET
    type_: Literal["hf"] | Unset = "hf"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_id = self.repo_id

        variant: None | str | Unset
        if isinstance(self.variant, Unset):
            variant = UNSET
        elif isinstance(self.variant, ModelRepoVariant):
            variant = self.variant.value
        else:
            variant = self.variant

        subfolder: None | str | Unset
        if isinstance(self.subfolder, Unset):
            subfolder = UNSET
        else:
            subfolder = self.subfolder

        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repo_id": repo_id,
            }
        )
        if variant is not UNSET:
            field_dict["variant"] = variant
        if subfolder is not UNSET:
            field_dict["subfolder"] = subfolder
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_id = d.pop("repo_id")

        def _parse_variant(data: object) -> ModelRepoVariant | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_0 = ModelRepoVariant(data)

                return variant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelRepoVariant | None | Unset, data)

        variant = _parse_variant(d.pop("variant", UNSET))

        def _parse_subfolder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subfolder = _parse_subfolder(d.pop("subfolder", UNSET))

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("access_token", UNSET))

        type_ = cast(Literal["hf"] | Unset, d.pop("type", UNSET))
        if type_ != "hf" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'hf', got '{type_}'")

        hf_model_source = cls(
            repo_id=repo_id,
            variant=variant,
            subfolder=subfolder,
            access_token=access_token,
            type_=type_,
        )

        hf_model_source.additional_properties = d
        return hf_model_source

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
