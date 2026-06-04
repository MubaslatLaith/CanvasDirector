from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_category import WorkflowCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowRecordListItemWithThumbnailDTO")


@_attrs_define
class WorkflowRecordListItemWithThumbnailDTO:
    """
    Attributes:
        workflow_id (str): The id of the workflow.
        name (str): The name of the workflow.
        created_at (datetime.datetime | str): The created timestamp of the workflow.
        updated_at (datetime.datetime | str): The updated timestamp of the workflow.
        user_id (str): The id of the user who owns this workflow.
        is_public (bool): Whether this workflow is shared with all users.
        description (str): The description of the workflow.
        category (WorkflowCategory):
        tags (str): The tags of the workflow.
        opened_at (datetime.datetime | None | str | Unset): The opened timestamp of the workflow.
        thumbnail_url (None | str | Unset): The URL of the workflow thumbnail.
    """

    workflow_id: str
    name: str
    created_at: datetime.datetime | str
    updated_at: datetime.datetime | str
    user_id: str
    is_public: bool
    description: str
    category: WorkflowCategory
    tags: str
    opened_at: datetime.datetime | None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        name = self.name

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

        user_id = self.user_id

        is_public = self.is_public

        description = self.description

        category = self.category.value

        tags = self.tags

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflow_id": workflow_id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "user_id": user_id,
                "is_public": is_public,
                "description": description,
                "category": category,
                "tags": tags,
            }
        )
        if opened_at is not UNSET:
            field_dict["opened_at"] = opened_at
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow_id = d.pop("workflow_id")

        name = d.pop("name")

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

        user_id = d.pop("user_id")

        is_public = d.pop("is_public")

        description = d.pop("description")

        category = WorkflowCategory(d.pop("category"))

        tags = d.pop("tags")

        def _parse_opened_at(data: object) -> datetime.datetime | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)

                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | str | Unset, data)

        opened_at = _parse_opened_at(d.pop("opened_at", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url", UNSET))

        workflow_record_list_item_with_thumbnail_dto = cls(
            workflow_id=workflow_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            is_public=is_public,
            description=description,
            category=category,
            tags=tags,
            opened_at=opened_at,
            thumbnail_url=thumbnail_url,
        )

        workflow_record_list_item_with_thumbnail_dto.additional_properties = d
        return workflow_record_list_item_with_thumbnail_dto

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
