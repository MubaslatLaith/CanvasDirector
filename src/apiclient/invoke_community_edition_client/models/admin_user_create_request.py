from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminUserCreateRequest")


@_attrs_define
class AdminUserCreateRequest:
    """Request body for admin to create a new user.

    Attributes:
        email (str): User email address
        password (str): User password
        display_name (None | str | Unset): Display name
        is_admin (bool | Unset): Whether user should have admin privileges Default: False.
    """

    email: str
    password: str
    display_name: None | str | Unset = UNSET
    is_admin: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        is_admin = self.is_admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        is_admin = d.pop("is_admin", UNSET)

        admin_user_create_request = cls(
            email=email,
            password=password,
            display_name=display_name,
            is_admin=is_admin,
        )

        admin_user_create_request.additional_properties = d
        return admin_user_create_request

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
