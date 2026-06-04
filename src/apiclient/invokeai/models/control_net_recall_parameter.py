from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.control_net_recall_parameter_control_mode_type_0 import ControlNetRecallParameterControlModeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlNetRecallParameter")


@_attrs_define
class ControlNetRecallParameter:
    """ControlNet configuration for recall

    Attributes:
        model_name (str): The name of the ControlNet/T2I Adapter/Control LoRA model
        image_name (None | str | Unset): The filename of the control image in outputs/images
        weight (float | Unset): The weight for the control adapter Default: 1.0.
        begin_step_percent (float | None | Unset): When the control adapter is first applied (% of total steps)
        end_step_percent (float | None | Unset): When the control adapter is last applied (% of total steps)
        control_mode (ControlNetRecallParameterControlModeType0 | None | Unset): The control mode (ControlNet only)
    """

    model_name: str
    image_name: None | str | Unset = UNSET
    weight: float | Unset = 1.0
    begin_step_percent: float | None | Unset = UNSET
    end_step_percent: float | None | Unset = UNSET
    control_mode: ControlNetRecallParameterControlModeType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name

        image_name: None | str | Unset
        if isinstance(self.image_name, Unset):
            image_name = UNSET
        else:
            image_name = self.image_name

        weight = self.weight

        begin_step_percent: float | None | Unset
        if isinstance(self.begin_step_percent, Unset):
            begin_step_percent = UNSET
        else:
            begin_step_percent = self.begin_step_percent

        end_step_percent: float | None | Unset
        if isinstance(self.end_step_percent, Unset):
            end_step_percent = UNSET
        else:
            end_step_percent = self.end_step_percent

        control_mode: None | str | Unset
        if isinstance(self.control_mode, Unset):
            control_mode = UNSET
        elif isinstance(self.control_mode, ControlNetRecallParameterControlModeType0):
            control_mode = self.control_mode.value
        else:
            control_mode = self.control_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_name": model_name,
            }
        )
        if image_name is not UNSET:
            field_dict["image_name"] = image_name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if begin_step_percent is not UNSET:
            field_dict["begin_step_percent"] = begin_step_percent
        if end_step_percent is not UNSET:
            field_dict["end_step_percent"] = end_step_percent
        if control_mode is not UNSET:
            field_dict["control_mode"] = control_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_name = d.pop("model_name")

        def _parse_image_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_name = _parse_image_name(d.pop("image_name", UNSET))

        weight = d.pop("weight", UNSET)

        def _parse_begin_step_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        begin_step_percent = _parse_begin_step_percent(d.pop("begin_step_percent", UNSET))

        def _parse_end_step_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        end_step_percent = _parse_end_step_percent(d.pop("end_step_percent", UNSET))

        def _parse_control_mode(data: object) -> ControlNetRecallParameterControlModeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                control_mode_type_0 = ControlNetRecallParameterControlModeType0(data)

                return control_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlNetRecallParameterControlModeType0 | None | Unset, data)

        control_mode = _parse_control_mode(d.pop("control_mode", UNSET))

        control_net_recall_parameter = cls(
            model_name=model_name,
            image_name=image_name,
            weight=weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            control_mode=control_mode,
        )

        control_net_recall_parameter.additional_properties = d
        return control_net_recall_parameter

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
