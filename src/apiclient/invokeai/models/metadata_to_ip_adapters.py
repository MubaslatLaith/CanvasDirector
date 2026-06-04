from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_adapter_field import IPAdapterField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="MetadataToIPAdapters")


@_attrs_define
class MetadataToIPAdapters:
    """Extracts a IP-Adapters value of a label from metadata

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['metadata_to_ip_adapters']):  Default: 'metadata_to_ip_adapters'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        ip_adapter_list (IPAdapterField | list[IPAdapterField] | None | Unset): IP-Adapter to apply
    """

    id: str
    type_: Literal["metadata_to_ip_adapters"] = "metadata_to_ip_adapters"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    ip_adapter_list: IPAdapterField | list[IPAdapterField] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ip_adapter_field import IPAdapterField
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

        ip_adapter_list: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.ip_adapter_list, Unset):
            ip_adapter_list = UNSET
        elif isinstance(self.ip_adapter_list, IPAdapterField):
            ip_adapter_list = self.ip_adapter_list.to_dict()
        elif isinstance(self.ip_adapter_list, list):
            ip_adapter_list = []
            for ip_adapter_list_type_1_item_data in self.ip_adapter_list:
                ip_adapter_list_type_1_item = ip_adapter_list_type_1_item_data.to_dict()
                ip_adapter_list.append(ip_adapter_list_type_1_item)

        else:
            ip_adapter_list = self.ip_adapter_list

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
        if ip_adapter_list is not UNSET:
            field_dict["ip_adapter_list"] = ip_adapter_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_adapter_field import IPAdapterField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["metadata_to_ip_adapters"], d.pop("type"))
        if type_ != "metadata_to_ip_adapters":
            raise ValueError(f"type must match const 'metadata_to_ip_adapters', got '{type_}'")

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

        def _parse_ip_adapter_list(data: object) -> IPAdapterField | list[IPAdapterField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ip_adapter_list_type_0 = IPAdapterField.from_dict(data)

                return ip_adapter_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_adapter_list_type_1 = []
                _ip_adapter_list_type_1 = data
                for ip_adapter_list_type_1_item_data in _ip_adapter_list_type_1:
                    ip_adapter_list_type_1_item = IPAdapterField.from_dict(ip_adapter_list_type_1_item_data)

                    ip_adapter_list_type_1.append(ip_adapter_list_type_1_item)

                return ip_adapter_list_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAdapterField | list[IPAdapterField] | None | Unset, data)

        ip_adapter_list = _parse_ip_adapter_list(d.pop("ip_adapter_list", UNSET))

        metadata_to_ip_adapters = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            ip_adapter_list=ip_adapter_list,
        )

        metadata_to_ip_adapters.additional_properties = d
        return metadata_to_ip_adapters

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
