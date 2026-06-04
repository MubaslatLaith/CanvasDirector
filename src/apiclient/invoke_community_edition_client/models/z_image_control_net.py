from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="ZImageControlNet")


@_attrs_define
class ZImageControlNet:
    """Configure Z-Image ControlNet for spatial conditioning.

    Takes a preprocessed control image (e.g., Canny edges, depth map, pose)
    and a Z-Image ControlNet adapter model to enable spatial control.

    Supports 5 control modes: Canny, HED, Depth, Pose, MLSD.
    Recommended control_context_scale: 0.65-0.80.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['z_image_control']):  Default: 'z_image_control'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            image (ImageField | None | Unset): The preprocessed control image (Canny, HED, Depth, Pose, or MLSD)
            control_model (ModelIdentifierField | None | Unset): ControlNet model to load
            control_context_scale (float | Unset): Strength of the control signal. Recommended range: 0.65-0.80. Default:
                0.75.
            begin_step_percent (float | Unset): When the control is first applied (% of total steps) Default: 0.0.
            end_step_percent (float | Unset): When the control is last applied (% of total steps) Default: 1.0.
    """

    id: str
    type_: Literal["z_image_control"] = "z_image_control"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    control_model: ModelIdentifierField | None | Unset = UNSET
    control_context_scale: float | Unset = 0.75
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

        control_model: dict[str, Any] | None | Unset
        if isinstance(self.control_model, Unset):
            control_model = UNSET
        elif isinstance(self.control_model, ModelIdentifierField):
            control_model = self.control_model.to_dict()
        else:
            control_model = self.control_model

        control_context_scale = self.control_context_scale

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
        if control_model is not UNSET:
            field_dict["control_model"] = control_model
        if control_context_scale is not UNSET:
            field_dict["control_context_scale"] = control_context_scale
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

        type_ = cast(Literal["z_image_control"], d.pop("type"))
        if type_ != "z_image_control":
            raise ValueError(f"type must match const 'z_image_control', got '{type_}'")

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

        control_context_scale = d.pop("control_context_scale", UNSET)

        begin_step_percent = d.pop("begin_step_percent", UNSET)

        end_step_percent = d.pop("end_step_percent", UNSET)

        z_image_control_net = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            control_model=control_model,
            control_context_scale=control_context_scale,
            begin_step_percent=begin_step_percent,
            end_step_percent=end_step_percent,
        )

        z_image_control_net.additional_properties = d
        return z_image_control_net

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
