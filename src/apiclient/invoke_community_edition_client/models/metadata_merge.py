from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="MetadataMerge")


@_attrs_define
class MetadataMerge:
    """Merged a collection of MetadataDict into a single MetadataDict.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['merge_metadata']):  Default: 'merge_metadata'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        collection (list[MetadataField] | None | Unset): Collection of Metadata
    """

    id: str
    type_: Literal["merge_metadata"] = "merge_metadata"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    collection: list[MetadataField] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        collection: list[dict[str, Any]] | None | Unset
        if isinstance(self.collection, Unset):
            collection = UNSET
        elif isinstance(self.collection, list):
            collection = []
            for collection_type_0_item_data in self.collection:
                collection_type_0_item = collection_type_0_item_data.to_dict()
                collection.append(collection_type_0_item)

        else:
            collection = self.collection

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
        if collection is not UNSET:
            field_dict["collection"] = collection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["merge_metadata"], d.pop("type"))
        if type_ != "merge_metadata":
            raise ValueError(f"type must match const 'merge_metadata', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_collection(data: object) -> list[MetadataField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collection_type_0 = []
                _collection_type_0 = data
                for collection_type_0_item_data in _collection_type_0:
                    collection_type_0_item = MetadataField.from_dict(collection_type_0_item_data)

                    collection_type_0.append(collection_type_0_item)

                return collection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MetadataField] | None | Unset, data)

        collection = _parse_collection(d.pop("collection", UNSET))

        metadata_merge = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            collection=collection,
        )

        metadata_merge.additional_properties = d
        return metadata_merge

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
