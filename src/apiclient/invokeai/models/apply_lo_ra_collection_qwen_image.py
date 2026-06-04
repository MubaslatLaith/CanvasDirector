from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lo_ra_field import LoRAField
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="ApplyLoRACollectionQwenImage")


@_attrs_define
class ApplyLoRACollectionQwenImage:
    """Applies a collection of LoRAs to a Qwen Image transformer.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['qwen_image_lora_collection_loader']):  Default: 'qwen_image_lora_collection_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        loras (list[LoRAField] | LoRAField | None | Unset): LoRA models and weights. May be a single LoRA or collection.
        transformer (None | TransformerField | Unset): Transformer
    """

    id: str
    type_: Literal["qwen_image_lora_collection_loader"] = "qwen_image_lora_collection_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    loras: list[LoRAField] | LoRAField | None | Unset = UNSET
    transformer: None | TransformerField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lo_ra_field import LoRAField
        from ..models.transformer_field import TransformerField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        loras: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.loras, Unset):
            loras = UNSET
        elif isinstance(self.loras, LoRAField):
            loras = self.loras.to_dict()
        elif isinstance(self.loras, list):
            loras = []
            for loras_type_1_item_data in self.loras:
                loras_type_1_item = loras_type_1_item_data.to_dict()
                loras.append(loras_type_1_item)

        else:
            loras = self.loras

        transformer: dict[str, Any] | None | Unset
        if isinstance(self.transformer, Unset):
            transformer = UNSET
        elif isinstance(self.transformer, TransformerField):
            transformer = self.transformer.to_dict()
        else:
            transformer = self.transformer

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
        if loras is not UNSET:
            field_dict["loras"] = loras
        if transformer is not UNSET:
            field_dict["transformer"] = transformer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lo_ra_field import LoRAField
        from ..models.transformer_field import TransformerField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["qwen_image_lora_collection_loader"], d.pop("type"))
        if type_ != "qwen_image_lora_collection_loader":
            raise ValueError(f"type must match const 'qwen_image_lora_collection_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_loras(data: object) -> list[LoRAField] | LoRAField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                loras_type_0 = LoRAField.from_dict(data)

                return loras_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                loras_type_1 = []
                _loras_type_1 = data
                for loras_type_1_item_data in _loras_type_1:
                    loras_type_1_item = LoRAField.from_dict(loras_type_1_item_data)

                    loras_type_1.append(loras_type_1_item)

                return loras_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoRAField] | LoRAField | None | Unset, data)

        loras = _parse_loras(d.pop("loras", UNSET))

        def _parse_transformer(data: object) -> None | TransformerField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transformer_type_0 = TransformerField.from_dict(data)

                return transformer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransformerField | Unset, data)

        transformer = _parse_transformer(d.pop("transformer", UNSET))

        apply_lo_ra_collection_qwen_image = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            loras=loras,
            transformer=transformer,
        )

        apply_lo_ra_collection_qwen_image.additional_properties = d
        return apply_lo_ra_collection_qwen_image

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
