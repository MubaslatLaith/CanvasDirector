from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field import MetadataField
    from ..models.t2i_adapter_field import T2IAdapterField


T = TypeVar("T", bound="MetadataToT2IAdapters")


@_attrs_define
class MetadataToT2IAdapters:
    """Extracts a T2I-Adapters value of a label from metadata

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['metadata_to_t2i_adapters']):  Default: 'metadata_to_t2i_adapters'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        t2i_adapter_list (list[T2IAdapterField] | None | T2IAdapterField | Unset): IP-Adapter to apply
    """

    id: str
    type_: Literal["metadata_to_t2i_adapters"] = "metadata_to_t2i_adapters"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    t2i_adapter_list: list[T2IAdapterField] | None | T2IAdapterField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metadata_field import MetadataField
        from ..models.t2i_adapter_field import T2IAdapterField

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

        t2i_adapter_list: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.t2i_adapter_list, Unset):
            t2i_adapter_list = UNSET
        elif isinstance(self.t2i_adapter_list, T2IAdapterField):
            t2i_adapter_list = self.t2i_adapter_list.to_dict()
        elif isinstance(self.t2i_adapter_list, list):
            t2i_adapter_list = []
            for t2i_adapter_list_type_1_item_data in self.t2i_adapter_list:
                t2i_adapter_list_type_1_item = t2i_adapter_list_type_1_item_data.to_dict()
                t2i_adapter_list.append(t2i_adapter_list_type_1_item)

        else:
            t2i_adapter_list = self.t2i_adapter_list

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
        if t2i_adapter_list is not UNSET:
            field_dict["t2i_adapter_list"] = t2i_adapter_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field import MetadataField
        from ..models.t2i_adapter_field import T2IAdapterField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["metadata_to_t2i_adapters"], d.pop("type"))
        if type_ != "metadata_to_t2i_adapters":
            raise ValueError(f"type must match const 'metadata_to_t2i_adapters', got '{type_}'")

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

        def _parse_t2i_adapter_list(data: object) -> list[T2IAdapterField] | None | T2IAdapterField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                t2i_adapter_list_type_0 = T2IAdapterField.from_dict(data)

                return t2i_adapter_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                t2i_adapter_list_type_1 = []
                _t2i_adapter_list_type_1 = data
                for t2i_adapter_list_type_1_item_data in _t2i_adapter_list_type_1:
                    t2i_adapter_list_type_1_item = T2IAdapterField.from_dict(t2i_adapter_list_type_1_item_data)

                    t2i_adapter_list_type_1.append(t2i_adapter_list_type_1_item)

                return t2i_adapter_list_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[T2IAdapterField] | None | T2IAdapterField | Unset, data)

        t2i_adapter_list = _parse_t2i_adapter_list(d.pop("t2i_adapter_list", UNSET))

        metadata_to_t2i_adapters = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            t2i_adapter_list=t2i_adapter_list,
        )

        metadata_to_t2i_adapters.additional_properties = d
        return metadata_to_t2i_adapters

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
