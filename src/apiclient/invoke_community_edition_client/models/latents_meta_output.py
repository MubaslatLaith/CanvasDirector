from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.latents_field import LatentsField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="LatentsMetaOutput")


@_attrs_define
class LatentsMetaOutput:
    """Latents + metadata

    Attributes:
        metadata (MetadataField): Pydantic model for metadata with custom root of type dict[str, Any].
            Metadata is stored without a strict schema.
        type_ (Literal['latents_meta_output']):  Default: 'latents_meta_output'.
        latents (LatentsField): A latents tensor primitive field
        width (int): Width of output (px)
        height (int): Height of output (px)
    """

    metadata: MetadataField
    latents: LatentsField
    width: int
    height: int
    type_: Literal["latents_meta_output"] = "latents_meta_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        type_ = self.type_

        latents = self.latents.to_dict()

        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "type": type_,
                "latents": latents,
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latents_field import LatentsField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        metadata = MetadataField.from_dict(d.pop("metadata"))

        type_ = cast(Literal["latents_meta_output"], d.pop("type"))
        if type_ != "latents_meta_output":
            raise ValueError(f"type must match const 'latents_meta_output', got '{type_}'")

        latents = LatentsField.from_dict(d.pop("latents"))

        width = d.pop("width")

        height = d.pop("height")

        latents_meta_output = cls(
            metadata=metadata,
            type_=type_,
            latents=latents,
            width=width,
            height=height,
        )

        latents_meta_output.additional_properties = d
        return latents_meta_output

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
