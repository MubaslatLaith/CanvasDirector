from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalProviderConfigModel")


@_attrs_define
class ExternalProviderConfigModel:
    """
    Attributes:
        provider_id (str): The external provider identifier
        api_key_configured (bool): Whether an API key is configured
        base_url (None | str | Unset): Optional base URL override
    """

    provider_id: str
    api_key_configured: bool
    base_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        api_key_configured = self.api_key_configured

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_id": provider_id,
                "api_key_configured": api_key_configured,
            }
        )
        if base_url is not UNSET:
            field_dict["base_url"] = base_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("provider_id")

        api_key_configured = d.pop("api_key_configured")

        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))

        external_provider_config_model = cls(
            provider_id=provider_id,
            api_key_configured=api_key_configured,
            base_url=base_url,
        )

        external_provider_config_model.additional_properties = d
        return external_provider_config_model

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
