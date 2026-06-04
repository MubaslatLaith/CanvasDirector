from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="IPAdapterField")


@_attrs_define
class IPAdapterField:
    """
    Attributes:
        image (ImageField | list[ImageField]): The IP-Adapter image prompt(s).
        ip_adapter_model (ModelIdentifierField):
        image_encoder_model (ModelIdentifierField):
        weight (float | list[float] | Unset): The weight given to the IP-Adapter. Default: 1.0.
        target_blocks (list[str] | Unset): The IP Adapter blocks to apply
        method (str | Unset): Weight apply method Default: 'full'.
        begin_step_percent (float | Unset): When the IP-Adapter is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the IP-Adapter is last applied (% of total steps) Default: 1.0.
        mask (None | TensorField | Unset): The bool mask associated with this IP-Adapter. Excluded regions should be set
            to False, included regions should be set to True.
    """

    image: ImageField | list[ImageField]
    ip_adapter_model: ModelIdentifierField
    image_encoder_model: ModelIdentifierField
    weight: float | list[float] | Unset = 1.0
    target_blocks: list[str] | Unset = UNSET
    method: str | Unset = "full"
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    mask: None | TensorField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.tensor_field import TensorField

        image: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = []
            for image_type_1_item_data in self.image:
                image_type_1_item = image_type_1_item_data.to_dict()
                image.append(image_type_1_item)

        ip_adapter_model = self.ip_adapter_model.to_dict()

        image_encoder_model = self.image_encoder_model.to_dict()

        weight: float | list[float] | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        elif isinstance(self.weight, list):
            weight = self.weight

        else:
            weight = self.weight

        target_blocks: list[str] | Unset = UNSET
        if not isinstance(self.target_blocks, Unset):
            target_blocks = self.target_blocks

        method = self.method

        begin_step_percent = self.begin_step_percent

        end_step_percent = self.end_step_percent

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, TensorField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "ip_adapter_model": ip_adapter_model,
                "image_encoder_model": image_encoder_model,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight
        if target_blocks is not UNSET:
            field_dict["target_blocks"] = target_blocks
        if method is not UNSET:
            field_dict["method"] = method
        if begin_step_percent is not UNSET:
            field_dict["begin_step_percent"] = begin_step_percent
        if end_step_percent is not UNSET:
            field_dict["end_step_percent"] = end_step_percent
        if mask is not UNSET:
            field_dict["mask"] = mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.tensor_field import TensorField

        d = dict(src_dict)

        def _parse_image(data: object) -> ImageField | list[ImageField]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = ImageField.from_dict(data)

                return image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            image_type_1 = []
            _image_type_1 = data
            for image_type_1_item_data in _image_type_1:
                image_type_1_item = ImageField.from_dict(image_type_1_item_data)

                image_type_1.append(image_type_1_item)

            return image_type_1

        image = _parse_image(d.pop("image"))

        ip_adapter_model = ModelIdentifierField.from_dict(d.pop("ip_adapter_model"))

        image_encoder_model = ModelIdentifierField.from_dict(d.pop("image_encoder_model"))

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

        target_blocks = cast(list[str], d.pop("target_blocks", UNSET))

        method = d.pop("method", UNSET)

        begin_step_percent = d.pop("begin_step_percent", UNSET)

        end_step_percent = d.pop("end_step_percent", UNSET)

        def _parse_mask(data: object) -> None | TensorField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_type_0 = TensorField.from_dict(data)

                return mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TensorField | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))

        ip_adapter_field = cls(
            image=image,
            ip_adapter_model=ip_adapter_model,
            image_encoder_model=image_encoder_model,
            weight=weight,
            target_blocks=target_blocks,
            method=method,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            mask=mask,
        )

        ip_adapter_field.additional_properties = d
        return ip_adapter_field

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
