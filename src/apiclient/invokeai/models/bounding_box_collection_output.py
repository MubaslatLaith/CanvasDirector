from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bounding_box_field import BoundingBoxField


T = TypeVar("T", bound="BoundingBoxCollectionOutput")


@_attrs_define
class BoundingBoxCollectionOutput:
    """Base class for nodes that output a collection of bounding boxes

    Attributes:
        collection (list[BoundingBoxField]): The output bounding boxes.
        type_ (Literal['bounding_box_collection_output']):  Default: 'bounding_box_collection_output'.
    """

    collection: list[BoundingBoxField]
    type_: Literal["bounding_box_collection_output"] = "bounding_box_collection_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection = []
        for collection_item_data in self.collection:
            collection_item = collection_item_data.to_dict()
            collection.append(collection_item)

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
        from ..models.bounding_box_field import BoundingBoxField

        d = dict(src_dict)
        collection = []
        _collection = d.pop("collection")
        for collection_item_data in _collection:
            collection_item = BoundingBoxField.from_dict(collection_item_data)

            collection.append(collection_item)

        type_ = cast(Literal["bounding_box_collection_output"], d.pop("type"))
        if type_ != "bounding_box_collection_output":
            raise ValueError(f"type must match const 'bounding_box_collection_output', got '{type_}'")

        bounding_box_collection_output = cls(
            collection=collection,
            type_=type_,
        )

        bounding_box_collection_output.additional_properties = d
        return bounding_box_collection_output

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
