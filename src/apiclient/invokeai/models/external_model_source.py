from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalModelSource")


@_attrs_define
class ExternalModelSource:
    """An external provider model identifier.

    Attributes:
        provider_id (str):
        provider_model_id (str):
        type_ (Literal['external'] | Unset):  Default: 'external'.
    """

    provider_id: str
    provider_model_id: str
    type_: Literal["external"] | Unset = "external"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        provider_model_id = self.provider_model_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_id": provider_id,
                "provider_model_id": provider_model_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("provider_id")

        provider_model_id = d.pop("provider_model_id")

        type_ = cast(Literal["external"] | Unset, d.pop("type", UNSET))
        if type_ != "external" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'external', got '{type_}'")

        external_model_source = cls(
            provider_id=provider_id,
            provider_model_id=provider_model_id,
            type_=type_,
        )

        external_model_source.additional_properties = d
        return external_model_source

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
