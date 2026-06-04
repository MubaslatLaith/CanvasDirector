from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_adapter_recall_parameter_image_influence_type_0 import IPAdapterRecallParameterImageInfluenceType0
from ..models.ip_adapter_recall_parameter_method_type_0 import IPAdapterRecallParameterMethodType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="IPAdapterRecallParameter")


@_attrs_define
class IPAdapterRecallParameter:
    """IP Adapter configuration for recall

    Attributes:
        model_name (str): The name of the IP Adapter model
        image_name (None | str | Unset): The filename of the reference image in outputs/images
        weight (float | Unset): The weight for the IP Adapter Default: 1.0.
        begin_step_percent (float | None | Unset): When the IP Adapter is first applied (% of total steps)
        end_step_percent (float | None | Unset): When the IP Adapter is last applied (% of total steps)
        method (IPAdapterRecallParameterMethodType0 | None | Unset): The IP Adapter method
        image_influence (IPAdapterRecallParameterImageInfluenceType0 | None | Unset): FLUX Redux image influence (if
            model is flux_redux)
    """

    model_name: str
    image_name: None | str | Unset = UNSET
    weight: float | Unset = 1.0
    begin_step_percent: float | None | Unset = UNSET
    end_step_percent: float | None | Unset = UNSET
    method: IPAdapterRecallParameterMethodType0 | None | Unset = UNSET
    image_influence: IPAdapterRecallParameterImageInfluenceType0 | None | Unset = UNSET
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

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        elif isinstance(self.method, IPAdapterRecallParameterMethodType0):
            method = self.method.value
        else:
            method = self.method

        image_influence: None | str | Unset
        if isinstance(self.image_influence, Unset):
            image_influence = UNSET
        elif isinstance(self.image_influence, IPAdapterRecallParameterImageInfluenceType0):
            image_influence = self.image_influence.value
        else:
            image_influence = self.image_influence

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
        if method is not UNSET:
            field_dict["method"] = method
        if image_influence is not UNSET:
            field_dict["image_influence"] = image_influence

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

        def _parse_method(data: object) -> IPAdapterRecallParameterMethodType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_type_0 = IPAdapterRecallParameterMethodType0(data)

                return method_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAdapterRecallParameterMethodType0 | None | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_image_influence(data: object) -> IPAdapterRecallParameterImageInfluenceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                image_influence_type_0 = IPAdapterRecallParameterImageInfluenceType0(data)

                return image_influence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAdapterRecallParameterImageInfluenceType0 | None | Unset, data)

        image_influence = _parse_image_influence(d.pop("image_influence", UNSET))

        ip_adapter_recall_parameter = cls(
            model_name=model_name,
            image_name=image_name,
            weight=weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            method=method,
            image_influence=image_influence,
        )

        ip_adapter_recall_parameter.additional_properties = d
        return ip_adapter_recall_parameter

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
