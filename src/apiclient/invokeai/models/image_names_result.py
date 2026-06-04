from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImageNamesResult")


@_attrs_define
class ImageNamesResult:
    """Response containing ordered image names with metadata for optimistic updates.

    Attributes:
        image_names (list[str]): Ordered list of image names
        starred_count (int): Number of starred images (when starred_first=True)
        total_count (int): Total number of images matching the query
    """

    image_names: list[str]
    starred_count: int
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_names = self.image_names

        starred_count = self.starred_count

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_names": image_names,
                "starred_count": starred_count,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_names = cast(list[str], d.pop("image_names"))

        starred_count = d.pop("starred_count")

        total_count = d.pop("total_count")

        image_names_result = cls(
            image_names=image_names,
            starred_count=starred_count,
            total_count=total_count,
        )

        image_names_result.additional_properties = d
        return image_names_result

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
