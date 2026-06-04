from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StarredImagesResult")


@_attrs_define
class StarredImagesResult:
    """
    Attributes:
        affected_boards (list[str]): The ids of boards affected by the delete operation
        starred_images (list[str]): The names of the images that were starred
    """

    affected_boards: list[str]
    starred_images: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_boards = self.affected_boards

        starred_images = self.starred_images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "affected_boards": affected_boards,
                "starred_images": starred_images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_boards = cast(list[str], d.pop("affected_boards"))

        starred_images = cast(list[str], d.pop("starred_images"))

        starred_images_result = cls(
            affected_boards=affected_boards,
            starred_images=starred_images,
        )

        starred_images_result.additional_properties = d
        return starred_images_result

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
