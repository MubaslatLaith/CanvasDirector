from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.t2i_adapter_field_resize_mode import T2IAdapterFieldResizeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="T2IAdapterField")


@_attrs_define
class T2IAdapterField:
    """
    Attributes:
        image (ImageField): An image primitive field
        t2i_adapter_model (ModelIdentifierField):
        weight (float | list[float] | Unset): The weight given to the T2I-Adapter Default: 1.0.
        begin_step_percent (float | Unset): When the T2I-Adapter is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the T2I-Adapter is last applied (% of total steps) Default: 1.0.
        resize_mode (T2IAdapterFieldResizeMode | Unset): The resize mode to use Default:
            T2IAdapterFieldResizeMode.JUST_RESIZE.
    """

    image: ImageField
    t2i_adapter_model: ModelIdentifierField
    weight: float | list[float] | Unset = 1.0
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    resize_mode: T2IAdapterFieldResizeMode | Unset = T2IAdapterFieldResizeMode.JUST_RESIZE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_dict()

        t2i_adapter_model = self.t2i_adapter_model.to_dict()

        weight: float | list[float] | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        elif isinstance(self.weight, list):
            weight = self.weight

        else:
            weight = self.weight

        begin_step_percent = self.begin_step_percent

        end_step_percent = self.end_step_percent

        resize_mode: str | Unset = UNSET
        if not isinstance(self.resize_mode, Unset):
            resize_mode = self.resize_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "t2i_adapter_model": t2i_adapter_model,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight
        if begin_step_percent is not UNSET:
            field_dict["begin_step_percent"] = begin_step_percent
        if end_step_percent is not UNSET:
            field_dict["end_step_percent"] = end_step_percent
        if resize_mode is not UNSET:
            field_dict["resize_mode"] = resize_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        image = ImageField.from_dict(d.pop("image"))

        t2i_adapter_model = ModelIdentifierField.from_dict(d.pop("t2i_adapter_model"))

        def _parse_weight(data: object) -> float | list[float] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weight_type_1 = cast(list[float], data)

                return weight_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | list[float] | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))

        begin_step_percent = d.pop("begin_step_percent", UNSET)

        end_step_percent = d.pop("end_step_percent", UNSET)

        _resize_mode = d.pop("resize_mode", UNSET)
        resize_mode: T2IAdapterFieldResizeMode | Unset
        if isinstance(_resize_mode, Unset):
            resize_mode = UNSET
        else:
            resize_mode = T2IAdapterFieldResizeMode(_resize_mode)

        t2i_adapter_field = cls(
            image=image,
            t2i_adapter_model=t2i_adapter_model,
            weight=weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            resize_mode=resize_mode,
        )

        t2i_adapter_field.additional_properties = d
        return t2i_adapter_field

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
