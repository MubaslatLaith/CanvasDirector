from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="URLRegexTokenPair")


@_attrs_define
class URLRegexTokenPair:
    """
    Attributes:
        url_regex (str): Regular expression to match against the URL
        token (str): Token to use when the URL matches the regex
    """

    url_regex: str
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_regex = self.url_regex

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url_regex": url_regex,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url_regex = d.pop("url_regex")

        token = d.pop("token")

        url_regex_token_pair = cls(
            url_regex=url_regex,
            token=token,
        )

        url_regex_token_pair.additional_properties = d
        return url_regex_token_pair

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
