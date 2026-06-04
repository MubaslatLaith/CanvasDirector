from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddImagesToBoardResult")


@_attrs_define
class AddImagesToBoardResult:
    """
    Attributes:
        affected_boards (list[str]): The ids of boards affected by the delete operation
        added_images (list[str]): The image names that were added to the board
    """

    affected_boards: list[str]
    added_images: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_boards = self.affected_boards

        added_images = self.added_images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "affected_boards": affected_boards,
                "added_images": added_images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_boards = cast(list[str], d.pop("affected_boards"))

        added_images = cast(list[str], d.pop("added_images"))

        add_images_to_board_result = cls(
            affected_boards=affected_boards,
            added_images=added_images,
        )

        add_images_to_board_result.additional_properties = d
        return add_images_to_board_result

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
