from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IterateInvocationOutput")


@_attrs_define
class IterateInvocationOutput:
    """Used to connect iteration outputs. Will be expanded to a specific output.

    Attributes:
        item (Any): The item being iterated over
        index (int): The index of the item
        total (int): The total number of items
        type_ (Literal['iterate_output']):  Default: 'iterate_output'.
    """

    item: Any
    index: int
    total: int
    type_: Literal["iterate_output"] = "iterate_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item = self.item

        index = self.index

        total = self.total

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item": item,
                "index": index,
                "total": total,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item = d.pop("item")

        index = d.pop("index")

        total = d.pop("total")

        type_ = cast(Literal["iterate_output"], d.pop("type"))
        if type_ != "iterate_output":
            raise ValueError(f"type must match const 'iterate_output', got '{type_}'")

        iterate_invocation_output = cls(
            item=item,
            index=index,
            total=total,
            type_=type_,
        )

        iterate_invocation_output.additional_properties = d
        return iterate_invocation_output

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
