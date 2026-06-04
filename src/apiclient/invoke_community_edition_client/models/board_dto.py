from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.board_visibility import BoardVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="BoardDTO")


@_attrs_define
class BoardDTO:
    """Deserialized board record with cover image URL and image count.

    Attributes:
        board_id (str): The unique ID of the board.
        board_name (str): The name of the board.
        user_id (str): The user ID of the board owner.
        created_at (datetime.datetime | str): The created timestamp of the board.
        updated_at (datetime.datetime | str): The updated timestamp of the board.
        cover_image_name (None | str): The name of the board's cover image.
        archived (bool): Whether or not the board is archived.
        image_count (int): The number of images in the board.
        asset_count (int): The number of assets in the board.
        deleted_at (datetime.datetime | None | str | Unset): The deleted timestamp of the board.
        board_visibility (BoardVisibility | Unset): The visibility options for a board.
        owner_username (None | str | Unset): The username of the board owner (for admin view).
    """

    board_id: str
    board_name: str
    user_id: str
    created_at: datetime.datetime | str
    updated_at: datetime.datetime | str
    cover_image_name: None | str
    archived: bool
    image_count: int
    asset_count: int
    deleted_at: datetime.datetime | None | str | Unset = UNSET
    board_visibility: BoardVisibility | Unset = UNSET
    owner_username: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board_id = self.board_id

        board_name = self.board_name

        user_id = self.user_id

        created_at: str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        cover_image_name: None | str
        cover_image_name = self.cover_image_name

        archived = self.archived

        image_count = self.image_count

        asset_count = self.asset_count

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        board_visibility: str | Unset = UNSET
        if not isinstance(self.board_visibility, Unset):
            board_visibility = self.board_visibility.value

        owner_username: None | str | Unset
        if isinstance(self.owner_username, Unset):
            owner_username = UNSET
        else:
            owner_username = self.owner_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "board_id": board_id,
                "board_name": board_name,
                "user_id": user_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "cover_image_name": cover_image_name,
                "archived": archived,
                "image_count": image_count,
                "asset_count": asset_count,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if board_visibility is not UNSET:
            field_dict["board_visibility"] = board_visibility
        if owner_username is not UNSET:
            field_dict["owner_username"] = owner_username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        board_id = d.pop("board_id")

        board_name = d.pop("board_name")

        user_id = d.pop("user_id")

        def _parse_created_at(data: object) -> datetime.datetime | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> datetime.datetime | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_cover_image_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_image_name = _parse_cover_image_name(d.pop("cover_image_name"))

        archived = d.pop("archived")

        image_count = d.pop("image_count")

        asset_count = d.pop("asset_count")

        def _parse_deleted_at(data: object) -> datetime.datetime | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        _board_visibility = d.pop("board_visibility", UNSET)
        board_visibility: BoardVisibility | Unset
        if isinstance(_board_visibility, Unset):
            board_visibility = UNSET
        else:
            board_visibility = BoardVisibility(_board_visibility)

        def _parse_owner_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_username = _parse_owner_username(d.pop("owner_username", UNSET))

        board_dto = cls(
            board_id=board_id,
            board_name=board_name,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            cover_image_name=cover_image_name,
            archived=archived,
            image_count=image_count,
            asset_count=asset_count,
            deleted_at=deleted_at,
            board_visibility=board_visibility,
            owner_username=owner_username,
        )

        board_dto.additional_properties = d
        return board_dto

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
