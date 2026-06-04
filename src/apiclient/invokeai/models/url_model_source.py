from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="URLModelSource")


@_attrs_define
class URLModelSource:
    """A generic URL point to a checkpoint file.

    Attributes:
        url (str):
        access_token (None | str | Unset):
        type_ (Literal['url'] | Unset):  Default: 'url'.
    """

    url: str
    access_token: None | str | Unset = UNSET
    type_: Literal["url"] | Unset = "url"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

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
                "url": url,
            }
        )
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("access_token", UNSET))

        type_ = cast(Literal["url"] | Unset, d.pop("type", UNSET))
        if type_ != "url" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'url', got '{type_}'")

        url_model_source = cls(
            url=url,
            access_token=access_token,
            type_=type_,
        )

        url_model_source.additional_properties = d
        return url_model_source

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
