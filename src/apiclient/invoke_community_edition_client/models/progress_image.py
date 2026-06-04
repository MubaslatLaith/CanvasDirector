from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProgressImage")


@_attrs_define
class ProgressImage:
    """The progress image sent intermittently during processing

    Attributes:
        width (int): The effective width of the image in pixels
        height (int): The effective height of the image in pixels
        data_url (str): The image data as a b64 data URL
    """

    width: int
    height: int
    data_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        data_url = self.data_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width": width,
                "height": height,
                "dataURL": data_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width")

        height = d.pop("height")

        data_url = d.pop("dataURL")

        progress_image = cls(
            width=width,
            height=height,
            data_url=data_url,
        )

        progress_image.additional_properties = d
        return progress_image

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
