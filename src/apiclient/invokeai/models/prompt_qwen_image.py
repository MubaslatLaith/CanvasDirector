from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prompt_qwen_image_quantization import PromptQwenImageQuantization
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.qwen_vl_encoder_field import QwenVLEncoderField


T = TypeVar("T", bound="PromptQwenImage")


@_attrs_define
class PromptQwenImage:
    """Encodes text and reference images for Qwen Image using Qwen2.5-VL.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['qwen_image_text_encoder']):  Default: 'qwen_image_text_encoder'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        prompt (None | str | Unset): Text prompt describing the desired edit.
        reference_images (list[ImageField] | Unset): Reference images to guide the edit. The model can use multiple
            reference images.
        qwen_vl_encoder (None | QwenVLEncoderField | Unset): Qwen2.5-VL tokenizer, processor and text/vision encoder
        quantization (PromptQwenImageQuantization | Unset): Quantize the Qwen VL encoder to reduce VRAM usage. 'nf4'
            (4-bit) saves the most memory, 'int8' (8-bit) is a middle ground. Default: PromptQwenImageQuantization.NONE.
    """

    id: str
    type_: Literal["qwen_image_text_encoder"] = "qwen_image_text_encoder"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    prompt: None | str | Unset = UNSET
    reference_images: list[ImageField] | Unset = UNSET
    qwen_vl_encoder: None | QwenVLEncoderField | Unset = UNSET
    quantization: PromptQwenImageQuantization | Unset = PromptQwenImageQuantization.NONE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.qwen_vl_encoder_field import QwenVLEncoderField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        reference_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reference_images, Unset):
            reference_images = []
            for reference_images_item_data in self.reference_images:
                reference_images_item = reference_images_item_data.to_dict()
                reference_images.append(reference_images_item)

        qwen_vl_encoder: dict[str, Any] | None | Unset
        if isinstance(self.qwen_vl_encoder, Unset):
            qwen_vl_encoder = UNSET
        elif isinstance(self.qwen_vl_encoder, QwenVLEncoderField):
            qwen_vl_encoder = self.qwen_vl_encoder.to_dict()
        else:
            qwen_vl_encoder = self.qwen_vl_encoder

        quantization: str | Unset = UNSET
        if not isinstance(self.quantization, Unset):
            quantization = self.quantization.value

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
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if reference_images is not UNSET:
            field_dict["reference_images"] = reference_images
        if qwen_vl_encoder is not UNSET:
            field_dict["qwen_vl_encoder"] = qwen_vl_encoder
        if quantization is not UNSET:
            field_dict["quantization"] = quantization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.qwen_vl_encoder_field import QwenVLEncoderField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["qwen_image_text_encoder"], d.pop("type"))
        if type_ != "qwen_image_text_encoder":
            raise ValueError(f"type must match const 'qwen_image_text_encoder', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        _reference_images = d.pop("reference_images", UNSET)
        reference_images: list[ImageField] | Unset = UNSET
        if _reference_images is not UNSET:
            reference_images = []
            for reference_images_item_data in _reference_images:
                reference_images_item = ImageField.from_dict(reference_images_item_data)

                reference_images.append(reference_images_item)

        def _parse_qwen_vl_encoder(data: object) -> None | QwenVLEncoderField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qwen_vl_encoder_type_0 = QwenVLEncoderField.from_dict(data)

                return qwen_vl_encoder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QwenVLEncoderField | Unset, data)

        qwen_vl_encoder = _parse_qwen_vl_encoder(d.pop("qwen_vl_encoder", UNSET))

        _quantization = d.pop("quantization", UNSET)
        quantization: PromptQwenImageQuantization | Unset
        if isinstance(_quantization, Unset):
            quantization = UNSET
        else:
            quantization = PromptQwenImageQuantization(_quantization)

        prompt_qwen_image = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            prompt=prompt,
            reference_images=reference_images,
            qwen_vl_encoder=qwen_vl_encoder,
            quantization=quantization,
        )

        prompt_qwen_image.additional_properties = d
        return prompt_qwen_image

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
