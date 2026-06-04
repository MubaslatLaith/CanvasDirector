from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="LLaVAOneVisionVLLM")


@_attrs_define
class LLaVAOneVisionVLLM:
    """Run a LLaVA OneVision VLLM model.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['llava_onevision_vllm']):  Default: 'llava_onevision_vllm'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        images (ImageField | list[ImageField] | None | Unset): Input image.
        prompt (str | Unset): Input text prompt. Default: ''.
        vllm_model (ModelIdentifierField | None | Unset): The VLLM model to use
    """

    id: str
    type_: Literal["llava_onevision_vllm"] = "llava_onevision_vllm"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    images: ImageField | list[ImageField] | None | Unset = UNSET
    prompt: str | Unset = ""
    vllm_model: ModelIdentifierField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        images: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_type_0_item_data in self.images:
                images_type_0_type_0_item = images_type_0_type_0_item_data.to_dict()
                images.append(images_type_0_type_0_item)

        elif isinstance(self.images, ImageField):
            images = self.images.to_dict()
        else:
            images = self.images

        prompt = self.prompt

        vllm_model: dict[str, Any] | None | Unset
        if isinstance(self.vllm_model, Unset):
            vllm_model = UNSET
        elif isinstance(self.vllm_model, ModelIdentifierField):
            vllm_model = self.vllm_model.to_dict()
        else:
            vllm_model = self.vllm_model

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
        if images is not UNSET:
            field_dict["images"] = images
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if vllm_model is not UNSET:
            field_dict["vllm_model"] = vllm_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["llava_onevision_vllm"], d.pop("type"))
        if type_ != "llava_onevision_vllm":
            raise ValueError(f"type must match const 'llava_onevision_vllm', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_images(data: object) -> ImageField | list[ImageField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0_type_0 = []
                _images_type_0_type_0 = data
                for images_type_0_type_0_item_data in _images_type_0_type_0:
                    images_type_0_type_0_item = ImageField.from_dict(images_type_0_type_0_item_data)

                    images_type_0_type_0.append(images_type_0_type_0_item)

                return images_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                images_type_0_type_1 = ImageField.from_dict(data)

                return images_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | list[ImageField] | None | Unset, data)

        images = _parse_images(d.pop("images", UNSET))

        prompt = d.pop("prompt", UNSET)

        def _parse_vllm_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vllm_model_type_0 = ModelIdentifierField.from_dict(data)

                return vllm_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        vllm_model = _parse_vllm_model(d.pop("vllm_model", UNSET))

        l_la_va_one_vision_vllm = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            images=images,
            prompt=prompt,
            vllm_model=vllm_model,
        )

        l_la_va_one_vision_vllm.additional_properties = d
        return l_la_va_one_vision_vllm

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
