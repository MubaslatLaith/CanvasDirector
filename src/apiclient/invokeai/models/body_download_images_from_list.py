from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyDownloadImagesFromList")


@_attrs_define
class BodyDownloadImagesFromList:
    """
    Attributes:
        image_names (list[str] | None | Unset): The list of names of images to download
        board_id (None | str | Unset): The board from which image should be downloaded
    """

    image_names: list[str] | None | Unset = UNSET
    board_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_names: list[str] | None | Unset
        if isinstance(self.image_names, Unset):
            image_names = UNSET
        elif isinstance(self.image_names, list):
            image_names = self.image_names

        else:
            image_names = self.image_names

        board_id: None | str | Unset
        if isinstance(self.board_id, Unset):
            board_id = UNSET
        else:
            board_id = self.board_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_names is not UNSET:
            field_dict["image_names"] = image_names
        if board_id is not UNSET:
            field_dict["board_id"] = board_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_image_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_names_type_0 = cast(list[str], data)

                return image_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_names = _parse_image_names(d.pop("image_names", UNSET))

        def _parse_board_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        board_id = _parse_board_id(d.pop("board_id", UNSET))

        body_download_images_from_list = cls(
            image_names=image_names,
            board_id=board_id,
        )

        body_download_images_from_list.additional_properties = d
        return body_download_images_from_list

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
