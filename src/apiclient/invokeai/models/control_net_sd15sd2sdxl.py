from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.control_net_sd15sd2sdxl_control_mode import ControlNetSD15SD2SDXLControlMode
from ..models.control_net_sd15sd2sdxl_resize_mode import ControlNetSD15SD2SDXLResizeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="ControlNetSD15SD2SDXL")


@_attrs_define
class ControlNetSD15SD2SDXL:
    """Collects ControlNet info to pass to other nodes

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['controlnet']):  Default: 'controlnet'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The control image
        control_model (ModelIdentifierField | None | Unset): ControlNet model to load
        control_weight (float | list[float] | Unset): The weight given to the ControlNet Default: 1.0.
        begin_step_percent (float | Unset): When the ControlNet is first applied (% of total steps) Default: 0.0.
        end_step_percent (float | Unset): When the ControlNet is last applied (% of total steps) Default: 1.0.
        control_mode (ControlNetSD15SD2SDXLControlMode | Unset): The control mode used Default:
            ControlNetSD15SD2SDXLControlMode.BALANCED.
        resize_mode (ControlNetSD15SD2SDXLResizeMode | Unset): The resize mode used Default:
            ControlNetSD15SD2SDXLResizeMode.JUST_RESIZE.
    """

    id: str
    type_: Literal["controlnet"] = "controlnet"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    control_model: ModelIdentifierField | None | Unset = UNSET
    control_weight: float | list[float] | Unset = 1.0
    begin_step_percent: float | Unset = 0.0
    end_step_percent: float | Unset = 1.0
    control_mode: ControlNetSD15SD2SDXLControlMode | Unset = ControlNetSD15SD2SDXLControlMode.BALANCED
    resize_mode: ControlNetSD15SD2SDXLResizeMode | Unset = ControlNetSD15SD2SDXLResizeMode.JUST_RESIZE
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

        control_model: dict[str, Any] | None | Unset
        if isinstance(self.control_model, Unset):
            control_model = UNSET
        elif isinstance(self.control_model, ModelIdentifierField):
            control_model = self.control_model.to_dict()
        else:
            control_model = self.control_model

        control_weight: float | list[float] | Unset
        if isinstance(self.control_weight, Unset):
            control_weight = UNSET
        elif isinstance(self.control_weight, list):
            control_weight = self.control_weight

        else:
            control_weight = self.control_weight

        begin_step_percent = self.begin_step_percent

        end_step_percent = self.end_step_percent

        control_mode: str | Unset = UNSET
        if not isinstance(self.control_mode, Unset):
            control_mode = self.control_mode.value

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
        if control_model is not UNSET:
            field_dict["control_model"] = control_model
        if control_weight is not UNSET:
            field_dict["control_weight"] = control_weight
        if begin_step_percent is not UNSET:
            field_dict["begin_step_percent"] = begin_step_percent
        if end_step_percent is not UNSET:
            field_dict["end_step_percent"] = end_step_percent
        if control_mode is not UNSET:
            field_dict["control_mode"] = control_mode
        if resize_mode is not UNSET:
            field_dict["resize_mode"] = resize_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["controlnet"], d.pop("type"))
        if type_ != "controlnet":
            raise ValueError(f"type must match const 'controlnet', got '{type_}'")

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

        def _parse_control_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_model_type_0 = ModelIdentifierField.from_dict(data)

                return control_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        control_model = _parse_control_model(d.pop("control_model", UNSET))

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

        _control_mode = d.pop("control_mode", UNSET)
        control_mode: ControlNetSD15SD2SDXLControlMode | Unset
        if isinstance(_control_mode, Unset):
            control_mode = UNSET
        else:
            control_mode = ControlNetSD15SD2SDXLControlMode(_control_mode)

        _resize_mode = d.pop("resize_mode", UNSET)
        resize_mode: ControlNetSD15SD2SDXLResizeMode | Unset
        if isinstance(_resize_mode, Unset):
            resize_mode = UNSET
        else:
            resize_mode = ControlNetSD15SD2SDXLResizeMode(_resize_mode)

        control_net_sd15sd2sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            control_model=control_model,
            control_weight=control_weight,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
            control_mode=control_mode,
            resize_mode=resize_mode,
        )

        control_net_sd15sd2sdxl.additional_properties = d
        return control_net_sd15sd2sdxl

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
