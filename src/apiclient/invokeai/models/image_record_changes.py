from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_category import ImageCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageRecordChanges")


@_attrs_define
class ImageRecordChanges:
    """A set of changes to apply to an image record.

    Only limited changes are valid:
      - `image_category`: change the category of an image
      - `session_id`: change the session associated with an image
      - `is_intermediate`: change the image's `is_intermediate` flag
      - `starred`: change whether the image is starred

        Attributes:
            image_category (ImageCategory | None | Unset): The image's new category.
            session_id (None | str | Unset): The image's new session ID.
            is_intermediate (bool | None | Unset): The image's new `is_intermediate` flag.
            starred (bool | None | Unset): The image's new `starred` state
    """

    image_category: ImageCategory | None | Unset = UNSET
    session_id: None | str | Unset = UNSET
    is_intermediate: bool | None | Unset = UNSET
    starred: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_category: None | str | Unset
        if isinstance(self.image_category, Unset):
            image_category = UNSET
        elif isinstance(self.image_category, ImageCategory):
            image_category = self.image_category.value
        else:
            image_category = self.image_category

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        is_intermediate: bool | None | Unset
        if isinstance(self.is_intermediate, Unset):
            is_intermediate = UNSET
        else:
            is_intermediate = self.is_intermediate

        starred: bool | None | Unset
        if isinstance(self.starred, Unset):
            starred = UNSET
        else:
            starred = self.starred

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_category is not UNSET:
            field_dict["image_category"] = image_category
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if starred is not UNSET:
            field_dict["starred"] = starred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_image_category(data: object) -> ImageCategory | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                image_category_type_0 = ImageCategory(data)

                return image_category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageCategory | None | Unset, data)

        image_category = _parse_image_category(d.pop("image_category", UNSET))

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_is_intermediate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_intermediate = _parse_is_intermediate(d.pop("is_intermediate", UNSET))

        def _parse_starred(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        starred = _parse_starred(d.pop("starred", UNSET))

        image_record_changes = cls(
            image_category=image_category,
            session_id=session_id,
            is_intermediate=is_intermediate,
            starred=starred,
        )

        image_record_changes.additional_properties = d
        return image_record_changes

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
