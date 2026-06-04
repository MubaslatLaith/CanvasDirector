from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyDownload")


@_attrs_define
class BodyDownload:
    """
    Attributes:
        source (str): download source
        dest (str): download destination
        priority (int | Unset): queue priority Default: 10.
        access_token (None | str | Unset): token for authorization to download
    """

    source: str
    dest: str
    priority: int | Unset = 10
    access_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        dest = self.dest

        priority = self.priority

        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "dest": dest,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if access_token is not UNSET:
            field_dict["access_token"] = access_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        dest = d.pop("dest")

        priority = d.pop("priority", UNSET)

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("access_token", UNSET))

        body_download = cls(
            source=source,
            dest=dest,
            priority=priority,
            access_token=access_token,
        )

        body_download.additional_properties = d
        return body_download

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
