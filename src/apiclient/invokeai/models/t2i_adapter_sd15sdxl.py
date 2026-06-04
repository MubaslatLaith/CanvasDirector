from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.t2i_adapter_sd15sdxl_resize_mode import T2IAdapterSD15SDXLResizeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="T2IAdapterSD15SDXL")


@_attrs_define
class T2IAdapterSD15SDXL:
    """Collects T2I-Adapter info to pass to other nodes.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['t2i_adapter']):  Default: 't2i_adapter'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The IP-Adapter image prompt.
        t2i_adapter_model (ModelIdentifierField | None | Unset): The T2I-Adapter model.
        weight (float | list[float] | Unset): The weight given to the T2I-Adapter Default: 1.0.
        begin_step_percent (float | Unset): When the T2I-Adapter is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the T2I-Adapter is last applied (% of total steps) Default: 1.0.
        resize_mode (T2IAdapterSD15SDXLResizeMode | Unset): The resize mode applied to the T2I-Adapter input image so
            that it matches the target output size. Default: T2IAdapterSD15SDXLResizeMode.JUST_RESIZE.
    """

    id: str
    type_: Literal["t2i_adapter"] = "t2i_adapter"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    t2i_adapter_model: ModelIdentifierField | None | Unset = UNSET
    weight: float | list[float] | Unset = 1.0
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    resize_mode: T2IAdapterSD15SDXLResizeMode | Unset = T2IAdapterSD15SDXLResizeMode.JUST_RESIZE
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

        t2i_adapter_model: dict[str, Any] | None | Unset
        if isinstance(self.t2i_adapter_model, Unset):
            t2i_adapter_model = UNSET
        elif isinstance(self.t2i_adapter_model, ModelIdentifierField):
            t2i_adapter_model = self.t2i_adapter_model.to_dict()
        else:
            t2i_adapter_model = self.t2i_adapter_model

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
        if t2i_adapter_model is not UNSET:
            field_dict["t2i_adapter_model"] = t2i_adapter_model
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
        id = d.pop("id")

        type_ = cast(Literal["t2i_adapter"], d.pop("type"))
        if type_ != "t2i_adapter":
            raise ValueError(f"type must match const 't2i_adapter', got '{type_}'")

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

        def _parse_t2i_adapter_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                t2i_adapter_model_type_0 = ModelIdentifierField.from_dict(data)

                return t2i_adapter_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        t2i_adapter_model = _parse_t2i_adapter_model(d.pop("t2i_adapter_model", UNSET))

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
        resize_mode: T2IAdapterSD15SDXLResizeMode | Unset
        if isinstance(_resize_mode, Unset):
            resize_mode = UNSET
        else:
            resize_mode = T2IAdapterSD15SDXLResizeMode(_resize_mode)

        t2i_adapter_sd15sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            t2i_adapter_model=t2i_adapter_model,
            weight=weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            resize_mode=resize_mode,
        )

        t2i_adapter_sd15sdxl.additional_properties = d
        return t2i_adapter_sd15sdxl

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
