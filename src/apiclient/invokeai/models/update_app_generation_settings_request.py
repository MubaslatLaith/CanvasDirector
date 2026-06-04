from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_app_generation_settings_request_image_subfolder_strategy import (
    UpdateAppGenerationSettingsRequestImageSubfolderStrategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppGenerationSettingsRequest")


@_attrs_define
class UpdateAppGenerationSettingsRequest:
    """Writable generation-related app settings.

    Attributes:
        image_subfolder_strategy (UpdateAppGenerationSettingsRequestImageSubfolderStrategy | Unset): Strategy for
            organizing images into subfolders.
        max_queue_history (int | None | Unset): Keep the last N completed, failed, and canceled queue items on startup.
            Set to 0 to prune all terminal items.
    """

    image_subfolder_strategy: UpdateAppGenerationSettingsRequestImageSubfolderStrategy | Unset = UNSET
    max_queue_history: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_subfolder_strategy: str | Unset = UNSET
        if not isinstance(self.image_subfolder_strategy, Unset):
            image_subfolder_strategy = self.image_subfolder_strategy.value

        max_queue_history: int | None | Unset
        if isinstance(self.max_queue_history, Unset):
            max_queue_history = UNSET
        else:
            max_queue_history = self.max_queue_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_subfolder_strategy is not UNSET:
            field_dict["image_subfolder_strategy"] = image_subfolder_strategy
        if max_queue_history is not UNSET:
            field_dict["max_queue_history"] = max_queue_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _image_subfolder_strategy = d.pop("image_subfolder_strategy", UNSET)
        image_subfolder_strategy: UpdateAppGenerationSettingsRequestImageSubfolderStrategy | Unset
        if isinstance(_image_subfolder_strategy, Unset):
            image_subfolder_strategy = UNSET
        else:
            image_subfolder_strategy = UpdateAppGenerationSettingsRequestImageSubfolderStrategy(
                _image_subfolder_strategy
            )

        def _parse_max_queue_history(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_queue_history = _parse_max_queue_history(d.pop("max_queue_history", UNSET))

        update_app_generation_settings_request = cls(
            image_subfolder_strategy=image_subfolder_strategy,
            max_queue_history=max_queue_history,
        )

        update_app_generation_settings_request.additional_properties = d
        return update_app_generation_settings_request

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
