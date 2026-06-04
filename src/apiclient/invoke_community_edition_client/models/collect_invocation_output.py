from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CollectInvocationOutput")


@_attrs_define
class CollectInvocationOutput:
    """
    Attributes:
        collection (list[Any]): The collection of input items
        type_ (Literal['collect_output']):  Default: 'collect_output'.
    """

    collection: list[Any]
    type_: Literal["collect_output"] = "collect_output"
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
        collection = cast(list[Any], d.pop("collection"))

        type_ = cast(Literal["collect_output"], d.pop("type"))
        if type_ != "collect_output":
            raise ValueError(f"type must match const 'collect_output', got '{type_}'")

        collect_invocation_output = cls(
            collection=collection,
            type_=type_,
        )

        collect_invocation_output.additional_properties = d
        return collect_invocation_output

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
