from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lo_ra_field import LoRAField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="MetadataToLoRACollection")


@_attrs_define
class MetadataToLoRACollection:
    """Extracts Lora(s) from metadata into a collection

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['metadata_to_lora_collection']):  Default: 'metadata_to_lora_collection'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        custom_label (str | Unset): Label for this metadata item Default: 'loras'.
        loras (list[LoRAField] | LoRAField | None | Unset): LoRA models and weights. May be a single LoRA or collection.
    """

    id: str
    type_: Literal["metadata_to_lora_collection"] = "metadata_to_lora_collection"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    custom_label: str | Unset = "loras"
    loras: list[LoRAField] | LoRAField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lo_ra_field import LoRAField
        from ..models.metadata_field import MetadataField

        id = self.id

        type_ = self.type_

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, MetadataField):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        custom_label = self.custom_label

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if custom_label is not UNSET:
            field_dict["custom_label"] = custom_label
        if loras is not UNSET:
            field_dict["loras"] = loras

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lo_ra_field import LoRAField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["metadata_to_lora_collection"], d.pop("type"))
        if type_ != "metadata_to_lora_collection":
            raise ValueError(f"type must match const 'metadata_to_lora_collection', got '{type_}'")

        def _parse_metadata(data: object) -> MetadataField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MetadataField.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataField | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        custom_label = d.pop("custom_label", UNSET)

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

        metadata_to_lo_ra_collection = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            custom_label=custom_label,
            loras=loras,
        )

        metadata_to_lo_ra_collection.additional_properties = d
        return metadata_to_lo_ra_collection

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
