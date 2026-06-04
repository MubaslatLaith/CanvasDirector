from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDTO")


@_attrs_define
class UserDTO:
    """User data transfer object.

    Attributes:
        user_id (str): Unique user identifier
        email (str): User email address
        created_at (datetime.datetime): When the user was created
        updated_at (datetime.datetime): When the user was last updated
        display_name (None | str | Unset): Display name
        is_admin (bool | Unset): Whether user has admin privileges Default: False.
        is_active (bool | Unset): Whether user account is active Default: True.
        last_login_at (datetime.datetime | None | Unset): When user last logged in
    """

    user_id: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    display_name: None | str | Unset = UNSET
    is_admin: bool | Unset = False
    is_active: bool | Unset = True
    last_login_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        email = self.email

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        is_admin = self.is_admin

        is_active = self.is_active

        last_login_at: None | str | Unset
        if isinstance(self.last_login_at, Unset):
            last_login_at = UNSET
        elif isinstance(self.last_login_at, datetime.datetime):
            last_login_at = self.last_login_at.isoformat()
        else:
            last_login_at = self.last_login_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "email": email,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_login_at is not UNSET:
            field_dict["last_login_at"] = last_login_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        email = d.pop("email")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        is_admin = d.pop("is_admin", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_last_login_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_login_at = _parse_last_login_at(d.pop("last_login_at", UNSET))

        user_dto = cls(
            user_id=user_id,
            email=email,
            created_at=created_at,
            updated_at=updated_at,
            display_name=display_name,
            is_admin=is_admin,
            is_active=is_active,
            last_login_at=last_login_at,
        )

        user_dto.additional_properties = d
        return user_dto

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
