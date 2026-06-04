from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetupStatusResponse")


@_attrs_define
class SetupStatusResponse:
    """Response for setup status check.

    Attributes:
        setup_required (bool): Whether initial setup is required
        multiuser_enabled (bool): Whether multiuser mode is enabled
        strict_password_checking (bool): Whether strict password requirements are enforced
        admin_email (None | str | Unset): Email of the first active admin user, if any
    """

    setup_required: bool
    multiuser_enabled: bool
    strict_password_checking: bool
    admin_email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        setup_required = self.setup_required

        multiuser_enabled = self.multiuser_enabled

        strict_password_checking = self.strict_password_checking

        admin_email: None | str | Unset
        if isinstance(self.admin_email, Unset):
            admin_email = UNSET
        else:
            admin_email = self.admin_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "setup_required": setup_required,
                "multiuser_enabled": multiuser_enabled,
                "strict_password_checking": strict_password_checking,
            }
        )
        if admin_email is not UNSET:
            field_dict["admin_email"] = admin_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        setup_required = d.pop("setup_required")

        multiuser_enabled = d.pop("multiuser_enabled")

        strict_password_checking = d.pop("strict_password_checking")

        def _parse_admin_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_email = _parse_admin_email(d.pop("admin_email", UNSET))

        setup_status_response = cls(
            setup_required=setup_required,
            multiuser_enabled=multiuser_enabled,
            strict_password_checking=strict_password_checking,
            admin_email=admin_email,
        )

        setup_status_response.additional_properties = d
        return setup_status_response

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
