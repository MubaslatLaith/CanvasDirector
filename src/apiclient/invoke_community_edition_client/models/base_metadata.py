from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseMetadata")


@_attrs_define
class BaseMetadata:
    """Adds typing data for discriminated union.

    Attributes:
        name (str): model's name
        type_ (Literal['basemetadata'] | Unset):  Default: 'basemetadata'.
    """

    name: str
    type_: Literal["basemetadata"] | Unset = "basemetadata"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["basemetadata"] | Unset, d.pop("type", UNSET))
        if type_ != "basemetadata" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'basemetadata', got '{type_}'")

        base_metadata = cls(
            name=name,
            type_=type_,
        )

        base_metadata.additional_properties = d
        return base_metadata

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
