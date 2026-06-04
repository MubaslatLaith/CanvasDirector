from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_category import ImageCategory
from ..models.resource_origin import ResourceOrigin
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageDTO")


@_attrs_define
class ImageDTO:
    """Deserialized image record, enriched for the frontend.

    Attributes:
        image_name (str): The unique name of the image.
        image_url (str): The URL of the image.
        thumbnail_url (str): The URL of the image's thumbnail.
        image_origin (ResourceOrigin): The origin of a resource (eg image).

            - INTERNAL: The resource was created by the application.
            - EXTERNAL: The resource was not created by the application.
            This may be a user-initiated upload, or an internal application upload (eg Canvas init image).
        image_category (ImageCategory): The category of an image.

            - GENERAL: The image is an output, init image, or otherwise an image without a specialized purpose.
            - MASK: The image is a mask image.
            - CONTROL: The image is a ControlNet control image.
            - USER: The image is a user-provide image.
            - OTHER: The image is some other type of image with a specialized purpose. To be used by external nodes.
        width (int): The width of the image in px.
        height (int): The height of the image in px.
        created_at (datetime.datetime | str): The created timestamp of the image.
        updated_at (datetime.datetime | str): The updated timestamp of the image.
        is_intermediate (bool): Whether this is an intermediate image.
        starred (bool): Whether this image is starred.
        has_workflow (bool): Whether this image has a workflow.
        deleted_at (datetime.datetime | None | str | Unset): The deleted timestamp of the image.
        session_id (None | str | Unset): The session ID that generated this image, if it is a generated image.
        node_id (None | str | Unset): The node ID that generated this image, if it is a generated image.
        image_subfolder (str | Unset): The subfolder where the image is stored on disk. Default: ''.
        board_id (None | str | Unset): The id of the board the image belongs to, if one exists.
    """

    image_name: str
    image_url: str
    thumbnail_url: str
    image_origin: ResourceOrigin
    image_category: ImageCategory
    width: int
    height: int
    created_at: datetime.datetime | str
    updated_at: datetime.datetime | str
    is_intermediate: bool
    starred: bool
    has_workflow: bool
    deleted_at: datetime.datetime | None | str | Unset = UNSET
    session_id: None | str | Unset = UNSET
    node_id: None | str | Unset = UNSET
    image_subfolder: str | Unset = ""
    board_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_name = self.image_name

        image_url = self.image_url

        thumbnail_url = self.thumbnail_url

        image_origin = self.image_origin.value

        image_category = self.image_category.value

        width = self.width

        height = self.height

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

        is_intermediate = self.is_intermediate

        starred = self.starred

        has_workflow = self.has_workflow

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        node_id: None | str | Unset
        if isinstance(self.node_id, Unset):
            node_id = UNSET
        else:
            node_id = self.node_id

        image_subfolder = self.image_subfolder

        board_id: None | str | Unset
        if isinstance(self.board_id, Unset):
            board_id = UNSET
        else:
            board_id = self.board_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_name": image_name,
                "image_url": image_url,
                "thumbnail_url": thumbnail_url,
                "image_origin": image_origin,
                "image_category": image_category,
                "width": width,
                "height": height,
                "created_at": created_at,
                "updated_at": updated_at,
                "is_intermediate": is_intermediate,
                "starred": starred,
                "has_workflow": has_workflow,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if image_subfolder is not UNSET:
            field_dict["image_subfolder"] = image_subfolder
        if board_id is not UNSET:
            field_dict["board_id"] = board_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_name = d.pop("image_name")

        image_url = d.pop("image_url")

        thumbnail_url = d.pop("thumbnail_url")

        image_origin = ResourceOrigin(d.pop("image_origin"))

        image_category = ImageCategory(d.pop("image_category"))

        width = d.pop("width")

        height = d.pop("height")

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

        is_intermediate = d.pop("is_intermediate")

        starred = d.pop("starred")

        has_workflow = d.pop("has_workflow")

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

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_node_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_id = _parse_node_id(d.pop("node_id", UNSET))

        image_subfolder = d.pop("image_subfolder", UNSET)

        def _parse_board_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        board_id = _parse_board_id(d.pop("board_id", UNSET))

        image_dto = cls(
            image_name=image_name,
            image_url=image_url,
            thumbnail_url=thumbnail_url,
            image_origin=image_origin,
            image_category=image_category,
            width=width,
            height=height,
            created_at=created_at,
            updated_at=updated_at,
            is_intermediate=is_intermediate,
            starred=starred,
            has_workflow=has_workflow,
            deleted_at=deleted_at,
            session_id=session_id,
            node_id=node_id,
            image_subfolder=image_subfolder,
            board_id=board_id,
        )

        image_dto.additional_properties = d
        return image_dto

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
