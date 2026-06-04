from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.control_field_control_mode import ControlFieldControlMode
from ..models.control_field_resize_mode import ControlFieldResizeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="ControlField")


@_attrs_define
class ControlField:
    """
    Attributes:
        image (ImageField): An image primitive field
        control_model (ModelIdentifierField):
        control_weight (float | list[float] | Unset): The weight given to the ControlNet Default: 1.0.
        begin_step_percent (float | Unset): When the ControlNet is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the ControlNet is last applied (% of total steps) Default: 1.0.
        control_mode (ControlFieldControlMode | Unset): The control mode to use Default:
            ControlFieldControlMode.BALANCED.
        resize_mode (ControlFieldResizeMode | Unset): The resize mode to use Default:
            ControlFieldResizeMode.JUST_RESIZE.
    """

    image: ImageField
    control_model: ModelIdentifierField
    control_weight: float | list[float] | Unset = 1.0
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    control_mode: ControlFieldControlMode | Unset = ControlFieldControlMode.BALANCED
    resize_mode: ControlFieldResizeMode | Unset = ControlFieldResizeMode.JUST_RESIZE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_dict()

        control_model = self.control_model.to_dict()

        control_weight: float | list[float] | Unset
        if isinstance(self.control_weight, Unset):
            control_weight = UNSET
        elif isinstance(self.control_weight, list):
            control_weight = self.control_weight

        else:
            control_weight = self.control_weight

        begin_step_percent = self.begin_step_percent

        end_step_percent = self.end_step_percent

        control_mode: str | Unset = UNSET
        if not isinstance(self.control_mode, Unset):
            control_mode = self.control_mode.value

        resize_mode: str | Unset = UNSET
        if not isinstance(self.resize_mode, Unset):
            resize_mode = self.resize_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "control_model": control_model,
            }
        )
        if control_weight is not UNSET:
            field_dict["control_weight"] = control_weight
        if begin_step_percent is not UNSET:
            field_dict["begin_step_percent"] = begin_step_percent
        if end_step_percent is not UNSET:
            field_dict["end_step_percent"] = end_step_percent
        if control_mode is not UNSET:
            field_dict["control_mode"] = control_mode
        if resize_mode is not UNSET:
            field_dict["resize_mode"] = resize_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        image = ImageField.from_dict(d.pop("image"))

        control_model = ModelIdentifierField.from_dict(d.pop("control_model"))

        def _parse_control_weight(data: object) -> float | list[float] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_weight_type_1 = cast(list[float], data)

                return control_weight_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | list[float] | Unset, data)

        control_weight = _parse_control_weight(d.pop("control_weight", UNSET))

        begin_step_percent = d.pop("begin_step_percent", UNSET)

        end_step_percent = d.pop("end_step_percent", UNSET)

        _control_mode = d.pop("control_mode", UNSET)
        control_mode: ControlFieldControlMode | Unset
        if isinstance(_control_mode, Unset):
            control_mode = UNSET
        else:
            control_mode = ControlFieldControlMode(_control_mode)

        _resize_mode = d.pop("resize_mode", UNSET)
        resize_mode: ControlFieldResizeMode | Unset
        if isinstance(_resize_mode, Unset):
            resize_mode = UNSET
        else:
            resize_mode = ControlFieldResizeMode(_resize_mode)

        control_field = cls(
            image=image,
            control_model=control_model,
            control_weight=control_weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            control_mode=control_mode,
            resize_mode=resize_mode,
        )

        control_field.additional_properties = d
        return control_field

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
