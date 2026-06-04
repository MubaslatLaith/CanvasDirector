from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_reidentify_models_response_failed_item import BulkReidentifyModelsResponseFailedItem


T = TypeVar("T", bound="BulkReidentifyModelsResponse")


@_attrs_define
class BulkReidentifyModelsResponse:
    """Response body for bulk model reidentification.

    Attributes:
        succeeded (list[str]): List of successfully reidentified model keys
        failed (list[BulkReidentifyModelsResponseFailedItem]): List of failed reidentifications with error messages
    """

    succeeded: list[str]
    failed: list[BulkReidentifyModelsResponseFailedItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        succeeded = self.succeeded

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "succeeded": succeeded,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_reidentify_models_response_failed_item import BulkReidentifyModelsResponseFailedItem

        d = dict(src_dict)
        succeeded = cast(list[str], d.pop("succeeded"))

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = BulkReidentifyModelsResponseFailedItem.from_dict(failed_item_data)

            failed.append(failed_item)

        bulk_reidentify_models_response = cls(
            succeeded=succeeded,
            failed=failed,
        )

        bulk_reidentify_models_response.additional_properties = d
        return bulk_reidentify_models_response

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
