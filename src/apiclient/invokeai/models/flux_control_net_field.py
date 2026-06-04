from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flux_control_net_field_resize_mode import FluxControlNetFieldResizeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="FluxControlNetField")


@_attrs_define
class FluxControlNetField:
    """
    Attributes:
        image (ImageField): An image primitive field
        control_model (ModelIdentifierField):
        control_weight (float | list[float] | Unset): The weight given to the ControlNet Default: 1.0.
        begin_step_percent (float | Unset): When the ControlNet is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the ControlNet is last applied (% of total steps) Default: 1.0.
        resize_mode (FluxControlNetFieldResizeMode | Unset): The resize mode to use Default:
            FluxControlNetFieldResizeMode.JUST_RESIZE.
        instantx_control_mode (int | None | Unset): The control mode for InstantX ControlNet union models. Ignored for
            other ControlNet models. The standard mapping is: canny (0), tile (1), depth (2), blur (3), pose (4), gray (5),
            low quality (6). Negative values will be treated as 'None'. Default: -1.
    """

    image: ImageField
    control_model: ModelIdentifierField
    control_weight: float | list[float] | Unset = 1.0
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    resize_mode: FluxControlNetFieldResizeMode | Unset = FluxControlNetFieldResizeMode.JUST_RESIZE
    instantx_control_mode: int | None | Unset = -1
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

        resize_mode: str | Unset = UNSET
        if not isinstance(self.resize_mode, Unset):
            resize_mode = self.resize_mode.value

        instantx_control_mode: int | None | Unset
        if isinstance(self.instantx_control_mode, Unset):
            instantx_control_mode = UNSET
        else:
            instantx_control_mode = self.instantx_control_mode

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
        if resize_mode is not UNSET:
            field_dict["resize_mode"] = resize_mode
        if instantx_control_mode is not UNSET:
            field_dict["instantx_control_mode"] = instantx_control_mode

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

        _resize_mode = d.pop("resize_mode", UNSET)
        resize_mode: FluxControlNetFieldResizeMode | Unset
        if isinstance(_resize_mode, Unset):
            resize_mode = UNSET
        else:
            resize_mode = FluxControlNetFieldResizeMode(_resize_mode)

        def _parse_instantx_control_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        instantx_control_mode = _parse_instantx_control_mode(d.pop("instantx_control_mode", UNSET))

        flux_control_net_field = cls(
            image=image,
            control_model=control_model,
            control_weight=control_weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            resize_mode=resize_mode,
            instantx_control_mode=instantx_control_mode,
        )

        flux_control_net_field.additional_properties = d
        return flux_control_net_field

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
