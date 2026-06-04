from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lo_ra_field import LoRAField


T = TypeVar("T", bound="MetadataToLorasCollectionOutput")


@_attrs_define
class MetadataToLorasCollectionOutput:
    """Model loader output

    Attributes:
        lora (list[LoRAField]): Collection of LoRA model and weights
        type_ (Literal['metadata_to_lora_collection_output']):  Default: 'metadata_to_lora_collection_output'.
    """

    lora: list[LoRAField]
    type_: Literal["metadata_to_lora_collection_output"] = "metadata_to_lora_collection_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lora = []
        for lora_item_data in self.lora:
            lora_item = lora_item_data.to_dict()
            lora.append(lora_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lora": lora,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lo_ra_field import LoRAField

        d = dict(src_dict)
        lora = []
        _lora = d.pop("lora")
        for lora_item_data in _lora:
            lora_item = LoRAField.from_dict(lora_item_data)

            lora.append(lora_item)

        type_ = cast(Literal["metadata_to_lora_collection_output"], d.pop("type"))
        if type_ != "metadata_to_lora_collection_output":
            raise ValueError(f"type must match const 'metadata_to_lora_collection_output', got '{type_}'")

        metadata_to_loras_collection_output = cls(
            lora=lora,
            type_=type_,
        )

        metadata_to_loras_collection_output.additional_properties = d
        return metadata_to_loras_collection_output

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
