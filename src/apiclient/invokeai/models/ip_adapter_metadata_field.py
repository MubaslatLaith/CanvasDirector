from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_adapter_metadata_field_clip_vision_model import IPAdapterMetadataFieldClipVisionModel
from ..models.ip_adapter_metadata_field_method import IPAdapterMetadataFieldMethod

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="IPAdapterMetadataField")


@_attrs_define
class IPAdapterMetadataField:
    """IP Adapter Field, minus the CLIP Vision Encoder model

    Attributes:
        image (ImageField): An image primitive field
        ip_adapter_model (ModelIdentifierField):
        clip_vision_model (IPAdapterMetadataFieldClipVisionModel): The CLIP Vision model
        method (IPAdapterMetadataFieldMethod): Method to apply IP Weights with
        weight (float | list[float]): The weight given to the IP-Adapter
        begin_step_percent (float): When the IP-Adapter is first applied (% of total steps)
        end_step_percent (float): When the IP-Adapter is last applied (% of total steps)
    """

    image: ImageField
    ip_adapter_model: ModelIdentifierField
    clip_vision_model: IPAdapterMetadataFieldClipVisionModel
    method: IPAdapterMetadataFieldMethod
    weight: float | list[float]
    begin_step_percent: float
    end_step_percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_dict()

        ip_adapter_model = self.ip_adapter_model.to_dict()

        clip_vision_model = self.clip_vision_model.value

        method = self.method.value

        weight: float | list[float]
        if isinstance(self.weight, list):
            weight = self.weight

        else:
            weight = self.weight

        begin_step_percent = self.begin_step_percent

        end_step_percent = self.end_step_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "ip_adapter_model": ip_adapter_model,
                "clip_vision_model": clip_vision_model,
                "method": method,
                "weight": weight,
                "begin_step_percent": begin_step_percent,
                "end_step_percent": end_step_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        image = ImageField.from_dict(d.pop("image"))

        ip_adapter_model = ModelIdentifierField.from_dict(d.pop("ip_adapter_model"))

        clip_vision_model = IPAdapterMetadataFieldClipVisionModel(d.pop("clip_vision_model"))

        method = IPAdapterMetadataFieldMethod(d.pop("method"))

        def _parse_weight(data: object) -> float | list[float]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weight_type_1 = cast(list[float], data)

                return weight_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | list[float], data)

        weight = _parse_weight(d.pop("weight"))

        begin_step_percent = d.pop("begin_step_percent")

        end_step_percent = d.pop("end_step_percent")

        ip_adapter_metadata_field = cls(
            image=image,
            ip_adapter_model=ip_adapter_model,
            clip_vision_model=clip_vision_model,
            method=method,
            weight=weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
        )

        ip_adapter_metadata_field.additional_properties = d
        return ip_adapter_metadata_field

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
