from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preset_type import PresetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preset_data import PresetData


T = TypeVar("T", bound="StylePresetRecordWithImage")


@_attrs_define
class StylePresetRecordWithImage:
    """
    Attributes:
        name (str): The name of the style preset.
        preset_data (PresetData):
        type_ (PresetType):
        id (str): The style preset ID.
        user_id (str): The user who owns this style preset.
        image (None | str): The path for image
        is_public (bool | Unset): Whether the preset is visible to other users. Default: False.
    """

    name: str
    preset_data: PresetData
    type_: PresetType
    id: str
    user_id: str
    image: None | str
    is_public: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        preset_data = self.preset_data.to_dict()

        type_ = self.type_.value

        id = self.id

        user_id = self.user_id

        image: None | str
        image = self.image

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "preset_data": preset_data,
                "type": type_,
                "id": id,
                "user_id": user_id,
                "image": image,
            }
        )
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preset_data import PresetData

        d = dict(src_dict)
        name = d.pop("name")

        preset_data = PresetData.from_dict(d.pop("preset_data"))

        type_ = PresetType(d.pop("type"))

        id = d.pop("id")

        user_id = d.pop("user_id")

        def _parse_image(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image = _parse_image(d.pop("image"))

        is_public = d.pop("is_public", UNSET)

        style_preset_record_with_image = cls(
            name=name,
            preset_data=preset_data,
            type_=type_,
            id=id,
            user_id=user_id,
            image=image,
            is_public=is_public,
        )

        style_preset_record_with_image.additional_properties = d
        return style_preset_record_with_image

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
