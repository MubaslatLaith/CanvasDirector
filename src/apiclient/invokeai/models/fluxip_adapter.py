from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="FLUXIPAdapter")


@_attrs_define
class FLUXIPAdapter:
    """Collects FLUX IP-Adapter info to pass to other nodes.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['flux_ip_adapter']):  Default: 'flux_ip_adapter'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The IP-Adapter image prompt(s).
        ip_adapter_model (ModelIdentifierField | None | Unset): The IP-Adapter model.
        clip_vision_model (Literal['ViT-L'] | Unset): CLIP Vision model to use. Default: 'ViT-L'.
        weight (float | list[float] | Unset): The weight given to the IP-Adapter Default: 1.0.
        begin_step_percent (float | Unset): When the IP-Adapter is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the IP-Adapter is last applied (% of total steps) Default: 1.0.
    """

    id: str
    type_: Literal["flux_ip_adapter"] = "flux_ip_adapter"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    ip_adapter_model: ModelIdentifierField | None | Unset = UNSET
    clip_vision_model: Literal["ViT-L"] | Unset = "ViT-L"
    weight: float | list[float] | Unset = 1.0
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        ip_adapter_model: dict[str, Any] | None | Unset
        if isinstance(self.ip_adapter_model, Unset):
            ip_adapter_model = UNSET
        elif isinstance(self.ip_adapter_model, ModelIdentifierField):
            ip_adapter_model = self.ip_adapter_model.to_dict()
        else:
            ip_adapter_model = self.ip_adapter_model

        clip_vision_model = self.clip_vision_model

        weight: float | list[float] | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        elif isinstance(self.weight, list):
            weight = self.weight

        else:
            weight = self.weight

        begin_step_percent = self.begin_step_percent

        end_step_percent = self.end_step_percent

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
        if begin_step_percent is not UNSET:
            field_dict["begin_step_percent"] = begin_step_percent
        if end_step_percent is not UNSET:
            field_dict["end_step_percent"] = end_step_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux_ip_adapter"], d.pop("type"))
        if type_ != "flux_ip_adapter":
            raise ValueError(f"type must match const 'flux_ip_adapter', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_image(data: object) -> ImageField | None | Unset:
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
            return cast(ImageField | None | Unset, data)

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

        clip_vision_model = cast(Literal["ViT-L"] | Unset, d.pop("clip_vision_model", UNSET))
        if clip_vision_model != "ViT-L" and not isinstance(clip_vision_model, Unset):
            raise ValueError(f"clip_vision_model must match const 'ViT-L', got '{clip_vision_model}'")

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

        fluxip_adapter = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            ip_adapter_model=ip_adapter_model,
            clip_vision_model=clip_vision_model,
            weight=weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
        )

        fluxip_adapter.additional_properties = d
        return fluxip_adapter

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
