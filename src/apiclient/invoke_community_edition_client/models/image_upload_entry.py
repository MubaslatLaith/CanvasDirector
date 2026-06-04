from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.image_dto import ImageDTO


T = TypeVar("T", bound="ImageUploadEntry")


@_attrs_define
class ImageUploadEntry:
    """
    Attributes:
        image_dto (ImageDTO): Deserialized image record, enriched for the frontend.
        presigned_url (str): The URL to get the presigned URL for the image upload
    """

    image_dto: ImageDTO
    presigned_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_dto = self.image_dto.to_dict()

        presigned_url = self.presigned_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_dto": image_dto,
                "presigned_url": presigned_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_dto import ImageDTO

        d = dict(src_dict)
        image_dto = ImageDTO.from_dict(d.pop("image_dto"))

        presigned_url = d.pop("presigned_url")

        image_upload_entry = cls(
            image_dto=image_dto,
            presigned_url=presigned_url,
        )

        image_upload_entry.additional_properties = d
        return image_upload_entry

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
