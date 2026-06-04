from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grounding_dino_text_prompt_object_detection_model_type_0 import (
    GroundingDINOTextPromptObjectDetectionModelType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="GroundingDINOTextPromptObjectDetection")


@_attrs_define
class GroundingDINOTextPromptObjectDetection:
    """Runs a Grounding DINO model. Performs zero-shot bounding-box object detection from a text prompt.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['grounding_dino']):  Default: 'grounding_dino'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        model (GroundingDINOTextPromptObjectDetectionModelType0 | None | Unset): The Grounding DINO model to use.
        prompt (None | str | Unset): The prompt describing the object to segment.
        image (ImageField | None | Unset): The image to segment.
        detection_threshold (float | Unset): The detection threshold for the Grounding DINO model. All detected bounding
            boxes with scores above this threshold will be returned. Default: 0.3.
    """

    id: str
    type_: Literal["grounding_dino"] = "grounding_dino"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    model: GroundingDINOTextPromptObjectDetectionModelType0 | None | Unset = UNSET
    prompt: None | str | Unset = UNSET
    image: ImageField | None | Unset = UNSET
    detection_threshold: float | Unset = 0.3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, GroundingDINOTextPromptObjectDetectionModelType0):
            model = self.model.value
        else:
            model = self.model

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        detection_threshold = self.detection_threshold

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
        if model is not UNSET:
            field_dict["model"] = model
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if image is not UNSET:
            field_dict["image"] = image
        if detection_threshold is not UNSET:
            field_dict["detection_threshold"] = detection_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["grounding_dino"], d.pop("type"))
        if type_ != "grounding_dino":
            raise ValueError(f"type must match const 'grounding_dino', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_model(data: object) -> GroundingDINOTextPromptObjectDetectionModelType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_0 = GroundingDINOTextPromptObjectDetectionModelType0(data)

                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GroundingDINOTextPromptObjectDetectionModelType0 | None | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

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

        detection_threshold = d.pop("detection_threshold", UNSET)

        grounding_dino_text_prompt_object_detection = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            model=model,
            prompt=prompt,
            image=image,
            detection_threshold=detection_threshold,
        )

        grounding_dino_text_prompt_object_detection.additional_properties = d
        return grounding_dino_text_prompt_object_detection

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
