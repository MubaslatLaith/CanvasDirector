from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="MetadataOutput")


@_attrs_define
class MetadataOutput:
    """
    Attributes:
        metadata (MetadataField): Pydantic model for metadata with custom root of type dict[str, Any].
            Metadata is stored without a strict schema.
        type_ (Literal['metadata_output']):  Default: 'metadata_output'.
    """

    metadata: MetadataField
    type_: Literal["metadata_output"] = "metadata_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        metadata = MetadataField.from_dict(d.pop("metadata"))

        type_ = cast(Literal["metadata_output"], d.pop("type"))
        if type_ != "metadata_output":
            raise ValueError(f"type must match const 'metadata_output', got '{type_}'")

        metadata_output = cls(
            metadata=metadata,
            type_=type_,
        )

        metadata_output.additional_properties = d
        return metadata_output

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
