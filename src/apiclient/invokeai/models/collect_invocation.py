from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectInvocation")


@_attrs_define
class CollectInvocation:
    """Collects values into a collection

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['collect']):  Default: 'collect'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        item (Any | None | Unset): The item to collect (all inputs must be of the same type)
        collection (list[Any] | Unset): An optional collection to append to
    """

    id: str
    type_: Literal["collect"] = "collect"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    item: Any | None | Unset = UNSET
    collection: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        item: Any | None | Unset
        if isinstance(self.item, Unset):
            item = UNSET
        else:
            item = self.item

        collection: list[Any] | Unset = UNSET
        if not isinstance(self.collection, Unset):
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
        if item is not UNSET:
            field_dict["item"] = item
        if collection is not UNSET:
            field_dict["collection"] = collection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["collect"], d.pop("type"))
        if type_ != "collect":
            raise ValueError(f"type must match const 'collect', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_item(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        item = _parse_item(d.pop("item", UNSET))

        collection = cast(list[Any], d.pop("collection", UNSET))

        collect_invocation = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            item=item,
            collection=collection,
        )

        collect_invocation.additional_properties = d
        return collect_invocation

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
