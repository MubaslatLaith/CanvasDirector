from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyCreateImageUploadEntry")


@_attrs_define
class BodyCreateImageUploadEntry:
    """
    Attributes:
        width (int): The width of the image
        height (int): The height of the image
        board_id (None | str | Unset): The board to add this image to, if any
    """

    width: int
    height: int
    board_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        board_id: None | str | Unset
        if isinstance(self.board_id, Unset):
            board_id = UNSET
        else:
            board_id = self.board_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width": width,
                "height": height,
            }
        )
        if board_id is not UNSET:
            field_dict["board_id"] = board_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width")

        height = d.pop("height")

        def _parse_board_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        board_id = _parse_board_id(d.pop("board_id", UNSET))

        body_create_image_upload_entry = cls(
            width=width,
            height=height,
            board_id=board_id,
        )

        body_create_image_upload_entry.additional_properties = d
        return body_create_image_upload_entry

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
