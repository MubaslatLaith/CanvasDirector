from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scheduler_scheduler import SchedulerScheduler
from ..types import UNSET, Unset

T = TypeVar("T", bound="Scheduler")


@_attrs_define
class Scheduler:
    """Selects a scheduler.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['scheduler']):  Default: 'scheduler'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        scheduler (SchedulerScheduler | Unset): Scheduler to use during inference Default: SchedulerScheduler.EULER.
    """

    id: str
    type_: Literal["scheduler"] = "scheduler"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    scheduler: SchedulerScheduler | Unset = SchedulerScheduler.EULER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        scheduler: str | Unset = UNSET
        if not isinstance(self.scheduler, Unset):
            scheduler = self.scheduler.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["scheduler"], d.pop("type"))
        if type_ != "scheduler":
            raise ValueError(f"type must match const 'scheduler', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: SchedulerScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = SchedulerScheduler(_scheduler)

        scheduler = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            scheduler=scheduler,
        )

        scheduler.additional_properties = d
        return scheduler

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
