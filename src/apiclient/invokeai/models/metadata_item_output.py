from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_item_field import MetadataItemField


T = TypeVar("T", bound="MetadataItemOutput")


@_attrs_define
class MetadataItemOutput:
    """Metadata Item Output

    Attributes:
        item (MetadataItemField):
        type_ (Literal['metadata_item_output']):  Default: 'metadata_item_output'.
    """

    item: MetadataItemField
    type_: Literal["metadata_item_output"] = "metadata_item_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item = self.item.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item": item,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_item_field import MetadataItemField

        d = dict(src_dict)
        item = MetadataItemField.from_dict(d.pop("item"))

        type_ = cast(Literal["metadata_item_output"], d.pop("type"))
        if type_ != "metadata_item_output":
            raise ValueError(f"type must match const 'metadata_item_output', got '{type_}'")

        metadata_item_output = cls(
            item=item,
            type_=type_,
        )

        metadata_item_output.additional_properties = d
        return metadata_item_output

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
