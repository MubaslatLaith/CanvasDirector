from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualSubBoardDTO")


@_attrs_define
class VirtualSubBoardDTO:
    """A virtual sub-board computed from image metadata, not stored in the database.

    Attributes:
        virtual_board_id (str): The virtual board ID, e.g. 'by_date:2026-03-18'.
        board_name (str): The display name of the virtual sub-board, e.g. '2026-03-18'.
        date (str): The ISO date string, e.g. '2026-03-18'.
        image_count (int): The number of general images for this date.
        asset_count (int): The number of asset images for this date.
        cover_image_name (None | str | Unset): The most recent image name for this date.
    """

    virtual_board_id: str
    board_name: str
    date: str
    image_count: int
    asset_count: int
    cover_image_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_board_id = self.virtual_board_id

        board_name = self.board_name

        date = self.date

        image_count = self.image_count

        asset_count = self.asset_count

        cover_image_name: None | str | Unset
        if isinstance(self.cover_image_name, Unset):
            cover_image_name = UNSET
        else:
            cover_image_name = self.cover_image_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "virtual_board_id": virtual_board_id,
                "board_name": board_name,
                "date": date,
                "image_count": image_count,
                "asset_count": asset_count,
            }
        )
        if cover_image_name is not UNSET:
            field_dict["cover_image_name"] = cover_image_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        virtual_board_id = d.pop("virtual_board_id")

        board_name = d.pop("board_name")

        date = d.pop("date")

        image_count = d.pop("image_count")

        asset_count = d.pop("asset_count")

        def _parse_cover_image_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image_name = _parse_cover_image_name(d.pop("cover_image_name", UNSET))

        virtual_sub_board_dto = cls(
            virtual_board_id=virtual_board_id,
            board_name=board_name,
            date=date,
            image_count=image_count,
            asset_count=asset_count,
            cover_image_name=cover_image_name,
        )

        virtual_sub_board_dto.additional_properties = d
        return virtual_sub_board_dto

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
