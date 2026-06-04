from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="ControlLoRAFLUX")


@_attrs_define
class ControlLoRAFLUX:
    """LoRA model and Image to use with FLUX transformer generation.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['flux_control_lora_loader']):  Default: 'flux_control_lora_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        lora (ModelIdentifierField | None | Unset): Control LoRA model to load
        image (ImageField | None | Unset): The image to encode.
        weight (float | Unset): The weight of the LoRA. Default: 1.0.
    """

    id: str
    type_: Literal["flux_control_lora_loader"] = "flux_control_lora_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    lora: ModelIdentifierField | None | Unset = UNSET
    image: ImageField | None | Unset = UNSET
    weight: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        lora: dict[str, Any] | None | Unset
        if isinstance(self.lora, Unset):
            lora = UNSET
        elif isinstance(self.lora, ModelIdentifierField):
            lora = self.lora.to_dict()
        else:
            lora = self.lora

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        weight = self.weight

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
        if lora is not UNSET:
            field_dict["lora"] = lora
        if image is not UNSET:
            field_dict["image"] = image
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux_control_lora_loader"], d.pop("type"))
        if type_ != "flux_control_lora_loader":
            raise ValueError(f"type must match const 'flux_control_lora_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_lora(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lora_type_0 = ModelIdentifierField.from_dict(data)

                return lora_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        lora = _parse_lora(d.pop("lora", UNSET))

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

        weight = d.pop("weight", UNSET)

        control_lo_raflux = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            lora=lora,
            image=image,
            weight=weight,
        )

        control_lo_raflux.additional_properties = d
        return control_lo_raflux

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
