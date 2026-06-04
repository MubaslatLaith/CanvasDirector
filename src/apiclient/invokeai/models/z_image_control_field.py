from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="ZImageControlField")


@_attrs_define
class ZImageControlField:
    """A Z-Image control conditioning field for spatial control (Canny, HED, Depth, Pose, MLSD).

    Attributes:
        image_name (str): The name of the preprocessed control image
        control_model (ModelIdentifierField):
        control_context_scale (float | Unset): The strength of the control signal. Recommended range: 0.65-0.80.
            Default: 0.75.
        begin_step_percent (float | Unset): When the control is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the control is last applied (% of total steps) Default: 1.0.
    """

    image_name: str
    control_model: ModelIdentifierField
    control_context_scale: float | Unset = 0.75
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_name = self.image_name

        control_model = self.control_model.to_dict()

        control_context_scale = self.control_context_scale

        begin_step_percent = self.begin_step_percent

        end_step_percent = self.end_step_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_name": image_name,
                "control_model": control_model,
            }
        )
        if control_context_scale is not UNSET:
            field_dict["control_context_scale"] = control_context_scale
        if begin_step_percent is not UNSET:
            field_dict["begin_step_percent"] = begin_step_percent
        if end_step_percent is not UNSET:
            field_dict["end_step_percent"] = end_step_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        image_name = d.pop("image_name")

        control_model = ModelIdentifierField.from_dict(d.pop("control_model"))

        control_context_scale = d.pop("control_context_scale", UNSET)

        begin_step_percent = d.pop("begin_step_percent", UNSET)

        end_step_percent = d.pop("end_step_percent", UNSET)

        z_image_control_field = cls(
            image_name=image_name,
            control_model=control_model,
            control_context_scale=control_context_scale,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
        )

        z_image_control_field.additional_properties = d
        return z_image_control_field

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
