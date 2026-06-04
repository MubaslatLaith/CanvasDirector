from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvocationCacheStatus")


@_attrs_define
class InvocationCacheStatus:
    """
    Attributes:
        size (int): The current size of the invocation cache
        hits (int): The number of cache hits
        misses (int): The number of cache misses
        enabled (bool): Whether the invocation cache is enabled
        max_size (int): The maximum size of the invocation cache
    """

    size: int
    hits: int
    misses: int
    enabled: bool
    max_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        hits = self.hits

        misses = self.misses

        enabled = self.enabled

        max_size = self.max_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
                "hits": hits,
                "misses": misses,
                "enabled": enabled,
                "max_size": max_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size")

        hits = d.pop("hits")

        misses = d.pop("misses")

        enabled = d.pop("enabled")

        max_size = d.pop("max_size")

        invocation_cache_status = cls(
            size=size,
            hits=hits,
            misses=misses,
            enabled=enabled,
            max_size=max_size,
        )

        invocation_cache_status.additional_properties = d
        return invocation_cache_status

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
