from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.board_visibility import BoardVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="BoardChanges")


@_attrs_define
class BoardChanges:
    """
    Attributes:
        board_name (None | str | Unset): The board's new name.
        cover_image_name (None | str | Unset): The name of the board's new cover image.
        archived (bool | None | Unset): Whether or not the board is archived
        board_visibility (BoardVisibility | None | Unset): The visibility of the board.
    """

    board_name: None | str | Unset = UNSET
    cover_image_name: None | str | Unset = UNSET
    archived: bool | None | Unset = UNSET
    board_visibility: BoardVisibility | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        board_name: None | str | Unset
        if isinstance(self.board_name, Unset):
            board_name = UNSET
        else:
            board_name = self.board_name

        cover_image_name: None | str | Unset
        if isinstance(self.cover_image_name, Unset):
            cover_image_name = UNSET
        else:
            cover_image_name = self.cover_image_name

        archived: bool | None | Unset
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        board_visibility: None | str | Unset
        if isinstance(self.board_visibility, Unset):
            board_visibility = UNSET
        elif isinstance(self.board_visibility, BoardVisibility):
            board_visibility = self.board_visibility.value
        else:
            board_visibility = self.board_visibility

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if board_name is not UNSET:
            field_dict["board_name"] = board_name
        if cover_image_name is not UNSET:
            field_dict["cover_image_name"] = cover_image_name
        if archived is not UNSET:
            field_dict["archived"] = archived
        if board_visibility is not UNSET:
            field_dict["board_visibility"] = board_visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_board_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        board_name = _parse_board_name(d.pop("board_name", UNSET))

        def _parse_cover_image_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image_name = _parse_cover_image_name(d.pop("cover_image_name", UNSET))

        def _parse_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        archived = _parse_archived(d.pop("archived", UNSET))

        def _parse_board_visibility(data: object) -> BoardVisibility | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                board_visibility_type_0 = BoardVisibility(data)

                return board_visibility_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BoardVisibility | None | Unset, data)

        board_visibility = _parse_board_visibility(d.pop("board_visibility", UNSET))

        board_changes = cls(
            board_name=board_name,
            cover_image_name=cover_image_name,
            archived=archived,
            board_visibility=board_visibility,
        )

        return board_changes
