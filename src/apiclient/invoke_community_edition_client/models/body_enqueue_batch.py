from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch import Batch


T = TypeVar("T", bound="BodyEnqueueBatch")


@_attrs_define
class BodyEnqueueBatch:
    """
    Attributes:
        batch (Batch):
        prepend (bool | Unset): Whether or not to prepend this batch in the queue Default: False.
    """

    batch: Batch
    prepend: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch = self.batch.to_dict()

        prepend = self.prepend

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch": batch,
            }
        )
        if prepend is not UNSET:
            field_dict["prepend"] = prepend

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch import Batch

        d = dict(src_dict)
        batch = Batch.from_dict(d.pop("batch"))

        prepend = d.pop("prepend", UNSET)

        body_enqueue_batch = cls(
            batch=batch,
            prepend=prepend,
        )

        body_enqueue_batch.additional_properties = d
        return body_enqueue_batch

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
