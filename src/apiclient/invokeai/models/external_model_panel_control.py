from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.external_model_panel_control_name import ExternalModelPanelControlName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalModelPanelControl")


@_attrs_define
class ExternalModelPanelControl:
    """
    Attributes:
        name (ExternalModelPanelControlName):
        slider_min (float | None | Unset):
        slider_max (float | None | Unset):
        number_input_min (float | None | Unset):
        number_input_max (float | None | Unset):
        fine_step (float | None | Unset):
        coarse_step (float | None | Unset):
        marks (list[float] | None | Unset):
    """

    name: ExternalModelPanelControlName
    slider_min: float | None | Unset = UNSET
    slider_max: float | None | Unset = UNSET
    number_input_min: float | None | Unset = UNSET
    number_input_max: float | None | Unset = UNSET
    fine_step: float | None | Unset = UNSET
    coarse_step: float | None | Unset = UNSET
    marks: list[float] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        slider_min: float | None | Unset
        if isinstance(self.slider_min, Unset):
            slider_min = UNSET
        else:
            slider_min = self.slider_min

        slider_max: float | None | Unset
        if isinstance(self.slider_max, Unset):
            slider_max = UNSET
        else:
            slider_max = self.slider_max

        number_input_min: float | None | Unset
        if isinstance(self.number_input_min, Unset):
            number_input_min = UNSET
        else:
            number_input_min = self.number_input_min

        number_input_max: float | None | Unset
        if isinstance(self.number_input_max, Unset):
            number_input_max = UNSET
        else:
            number_input_max = self.number_input_max

        fine_step: float | None | Unset
        if isinstance(self.fine_step, Unset):
            fine_step = UNSET
        else:
            fine_step = self.fine_step

        coarse_step: float | None | Unset
        if isinstance(self.coarse_step, Unset):
            coarse_step = UNSET
        else:
            coarse_step = self.coarse_step

        marks: list[float] | None | Unset
        if isinstance(self.marks, Unset):
            marks = UNSET
        elif isinstance(self.marks, list):
            marks = self.marks

        else:
            marks = self.marks

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if slider_min is not UNSET:
            field_dict["slider_min"] = slider_min
        if slider_max is not UNSET:
            field_dict["slider_max"] = slider_max
        if number_input_min is not UNSET:
            field_dict["number_input_min"] = number_input_min
        if number_input_max is not UNSET:
            field_dict["number_input_max"] = number_input_max
        if fine_step is not UNSET:
            field_dict["fine_step"] = fine_step
        if coarse_step is not UNSET:
            field_dict["coarse_step"] = coarse_step
        if marks is not UNSET:
            field_dict["marks"] = marks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = ExternalModelPanelControlName(d.pop("name"))

        def _parse_slider_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slider_min = _parse_slider_min(d.pop("slider_min", UNSET))

        def _parse_slider_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slider_max = _parse_slider_max(d.pop("slider_max", UNSET))

        def _parse_number_input_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        number_input_min = _parse_number_input_min(d.pop("number_input_min", UNSET))

        def _parse_number_input_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        number_input_max = _parse_number_input_max(d.pop("number_input_max", UNSET))

        def _parse_fine_step(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fine_step = _parse_fine_step(d.pop("fine_step", UNSET))

        def _parse_coarse_step(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coarse_step = _parse_coarse_step(d.pop("coarse_step", UNSET))

        def _parse_marks(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                marks_type_0 = cast(list[float], data)

                return marks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        marks = _parse_marks(d.pop("marks", UNSET))

        external_model_panel_control = cls(
            name=name,
            slider_min=slider_min,
            slider_max=slider_max,
            number_input_min=number_input_min,
            number_input_max=number_input_max,
            fine_step=fine_step,
            coarse_step=coarse_step,
            marks=marks,
        )

        return external_model_panel_control
