from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cache_stats_loaded_model_sizes import CacheStatsLoadedModelSizes


T = TypeVar("T", bound="CacheStats")


@_attrs_define
class CacheStats:
    """Collect statistics on cache performance.

    Attributes:
        hits (int | Unset):  Default: 0.
        misses (int | Unset):  Default: 0.
        high_watermark (int | Unset):  Default: 0.
        in_cache (int | Unset):  Default: 0.
        cleared (int | Unset):  Default: 0.
        cache_size (int | Unset):  Default: 0.
        loaded_model_sizes (CacheStatsLoadedModelSizes | Unset):
    """

    hits: int | Unset = 0
    misses: int | Unset = 0
    high_watermark: int | Unset = 0
    in_cache: int | Unset = 0
    cleared: int | Unset = 0
    cache_size: int | Unset = 0
    loaded_model_sizes: CacheStatsLoadedModelSizes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hits = self.hits

        misses = self.misses

        high_watermark = self.high_watermark

        in_cache = self.in_cache

        cleared = self.cleared

        cache_size = self.cache_size

        loaded_model_sizes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loaded_model_sizes, Unset):
            loaded_model_sizes = self.loaded_model_sizes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hits is not UNSET:
            field_dict["hits"] = hits
        if misses is not UNSET:
            field_dict["misses"] = misses
        if high_watermark is not UNSET:
            field_dict["high_watermark"] = high_watermark
        if in_cache is not UNSET:
            field_dict["in_cache"] = in_cache
        if cleared is not UNSET:
            field_dict["cleared"] = cleared
        if cache_size is not UNSET:
            field_dict["cache_size"] = cache_size
        if loaded_model_sizes is not UNSET:
            field_dict["loaded_model_sizes"] = loaded_model_sizes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_stats_loaded_model_sizes import CacheStatsLoadedModelSizes

        d = dict(src_dict)
        hits = d.pop("hits", UNSET)

        misses = d.pop("misses", UNSET)

        high_watermark = d.pop("high_watermark", UNSET)

        in_cache = d.pop("in_cache", UNSET)

        cleared = d.pop("cleared", UNSET)

        cache_size = d.pop("cache_size", UNSET)

        _loaded_model_sizes = d.pop("loaded_model_sizes", UNSET)
        loaded_model_sizes: CacheStatsLoadedModelSizes | Unset
        if isinstance(_loaded_model_sizes, Unset):
            loaded_model_sizes = UNSET
        else:
            loaded_model_sizes = CacheStatsLoadedModelSizes.from_dict(_loaded_model_sizes)

        cache_stats = cls(
            hits=hits,
            misses=misses,
            high_watermark=high_watermark,
            in_cache=in_cache,
            cleared=cleared,
            cache_size=cache_size,
            loaded_model_sizes=loaded_model_sizes,
        )

        cache_stats.additional_properties = d
        return cache_stats

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
