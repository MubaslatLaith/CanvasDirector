from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_adapter_sd15sdxl_clip_vision_model import IPAdapterSD15SDXLClipVisionModel
from ..models.ip_adapter_sd15sdxl_method import IPAdapterSD15SDXLMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="IPAdapterSD15SDXL")


@_attrs_define
class IPAdapterSD15SDXL:
    """Collects IP-Adapter info to pass to other nodes.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['ip_adapter']):  Default: 'ip_adapter'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | list[ImageField] | None | Unset): The IP-Adapter image prompt(s).
        ip_adapter_model (ModelIdentifierField | None | Unset): The IP-Adapter model.
        clip_vision_model (IPAdapterSD15SDXLClipVisionModel | Unset): CLIP Vision model to use. Overrides model
            settings. Mandatory for checkpoint models. Default: IPAdapterSD15SDXLClipVisionModel.VIT_H.
        weight (float | list[float] | Unset): The weight given to the IP-Adapter Default: 1.0.
        method (IPAdapterSD15SDXLMethod | Unset): The method to apply the IP-Adapter Default:
            IPAdapterSD15SDXLMethod.FULL.
        begin_step_percent (float | Unset): When the IP-Adapter is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the IP-Adapter is last applied (% of total steps) Default: 1.0.
        mask (None | TensorField | Unset): A mask defining the region that this IP-Adapter applies to.
    """

    id: str
    type_: Literal["ip_adapter"] = "ip_adapter"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | list[ImageField] | None | Unset = UNSET
    ip_adapter_model: ModelIdentifierField | None | Unset = UNSET
    clip_vision_model: IPAdapterSD15SDXLClipVisionModel | Unset = IPAdapterSD15SDXLClipVisionModel.VIT_H
    weight: float | list[float] | Unset = 1.0
    method: IPAdapterSD15SDXLMethod | Unset = IPAdapterSD15SDXLMethod.FULL
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    mask: None | TensorField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.tensor_field import TensorField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        image: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        elif isinstance(self.image, list):
            image = []
            for image_type_1_item_data in self.image:
                image_type_1_item = image_type_1_item_data.to_dict()
                image.append(image_type_1_item)

        else:
            image = self.image

        ip_adapter_model: dict[str, Any] | None | Unset
        if isinstance(self.ip_adapter_model, Unset):
            ip_adapter_model = UNSET
        elif isinstance(self.ip_adapter_model, ModelIdentifierField):
            ip_adapter_model = self.ip_adapter_model.to_dict()
        else:
            ip_adapter_model = self.ip_adapter_model

        clip_vision_model: str | Unset = UNSET
        if not isinstance(self.clip_vision_model, Unset):
            clip_vision_model = self.clip_vision_model.value

        weight: float | list[float] | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        elif isinstance(self.weight, list):
            weight = self.weight

        else:
            weight = self.weight

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

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
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if image is not UNSET:
            field_dict["image"] = image
        if ip_adapter_model is not UNSET:
            field_dict["ip_adapter_model"] = ip_adapter_model
        if clip_vision_model is not UNSET:
            field_dict["clip_vision_model"] = clip_vision_model
        if weight is not UNSET:
            field_dict["weight"] = weight
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
        id = d.pop("id")

        type_ = cast(Literal["ip_adapter"], d.pop("type"))
        if type_ != "ip_adapter":
            raise ValueError(f"type must match const 'ip_adapter', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_image(data: object) -> ImageField | list[ImageField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = ImageField.from_dict(data)

                return image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_type_1 = []
                _image_type_1 = data
                for image_type_1_item_data in _image_type_1:
                    image_type_1_item = ImageField.from_dict(image_type_1_item_data)

                    image_type_1.append(image_type_1_item)

                return image_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | list[ImageField] | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_ip_adapter_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ip_adapter_model_type_0 = ModelIdentifierField.from_dict(data)

                return ip_adapter_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        ip_adapter_model = _parse_ip_adapter_model(d.pop("ip_adapter_model", UNSET))

        _clip_vision_model = d.pop("clip_vision_model", UNSET)
        clip_vision_model: IPAdapterSD15SDXLClipVisionModel | Unset
        if isinstance(_clip_vision_model, Unset):
            clip_vision_model = UNSET
        else:
            clip_vision_model = IPAdapterSD15SDXLClipVisionModel(_clip_vision_model)

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

        _method = d.pop("method", UNSET)
        method: IPAdapterSD15SDXLMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = IPAdapterSD15SDXLMethod(_method)

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

        ip_adapter_sd15sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            ip_adapter_model=ip_adapter_model,
            clip_vision_model=clip_vision_model,
            weight=weight,
            method=method,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            mask=mask,
        )

        ip_adapter_sd15sdxl.additional_properties = d
        return ip_adapter_sd15sdxl

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
