from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReferenceImageRecallParameter")


@_attrs_define
class ReferenceImageRecallParameter:
    """Global reference-image configuration for recall.

    Used for reference images that feed directly into the main model rather
    than through a separate IP-Adapter / ControlNet model — for example
    FLUX.2 Klein, FLUX Kontext, and Qwen Image Edit. The receiving frontend
    picks the correct config type (``flux2_reference_image`` /
    ``qwen_image_reference_image`` / ``flux_kontext_reference_image``) based
    on the currently-selected main model.

        Attributes:
            image_name (str): The filename of the reference image in outputs/images
    """

    image_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_name = self.image_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_name": image_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_name = d.pop("image_name")

        reference_image_recall_parameter = cls(
            image_name=image_name,
        )

        reference_image_recall_parameter.additional_properties = d
        return reference_image_recall_parameter

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
