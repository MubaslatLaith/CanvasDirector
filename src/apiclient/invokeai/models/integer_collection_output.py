from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegerCollectionOutput")


@_attrs_define
class IntegerCollectionOutput:
    """Base class for nodes that output a collection of integers

    Attributes:
        collection (list[int]): The int collection
        type_ (Literal['integer_collection_output']):  Default: 'integer_collection_output'.
    """

    collection: list[int]
    type_: Literal["integer_collection_output"] = "integer_collection_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection = self.collection

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection": collection,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection = cast(list[int], d.pop("collection"))

        type_ = cast(Literal["integer_collection_output"], d.pop("type"))
        if type_ != "integer_collection_output":
            raise ValueError(f"type must match const 'integer_collection_output', got '{type_}'")

        integer_collection_output = cls(
            collection=collection,
            type_=type_,
        )

        integer_collection_output.additional_properties = d
        return integer_collection_output

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
