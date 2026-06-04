from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditioning_field import ConditioningField


T = TypeVar("T", bound="ConditioningCollectionPrimitive")


@_attrs_define
class ConditioningCollectionPrimitive:
    """A collection of conditioning tensor primitive values

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['conditioning_collection']):  Default: 'conditioning_collection'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        collection (list[ConditioningField] | Unset): The collection of conditioning tensors
    """

    id: str
    type_: Literal["conditioning_collection"] = "conditioning_collection"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    collection: list[ConditioningField] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        collection: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collection, Unset):
            collection = []
            for collection_item_data in self.collection:
                collection_item = collection_item_data.to_dict()
                collection.append(collection_item)

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
        from ..models.conditioning_field import ConditioningField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["conditioning_collection"], d.pop("type"))
        if type_ != "conditioning_collection":
            raise ValueError(f"type must match const 'conditioning_collection', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _collection = d.pop("collection", UNSET)
        collection: list[ConditioningField] | Unset = UNSET
        if _collection is not UNSET:
            collection = []
            for collection_item_data in _collection:
                collection_item = ConditioningField.from_dict(collection_item_data)

                collection.append(collection_item)

        conditioning_collection_primitive = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            collection=collection,
        )

        conditioning_collection_primitive.additional_properties = d
        return conditioning_collection_primitive

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
