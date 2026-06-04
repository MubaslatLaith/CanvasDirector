from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField


T = TypeVar("T", bound="FluxKontextOutput")


@_attrs_define
class FluxKontextOutput:
    """The conditioning output of a FLUX Kontext invocation.

    Attributes:
        kontext_cond (FluxKontextConditioningField): A conditioning field for FLUX Kontext (reference image).
        type_ (Literal['flux_kontext_output']):  Default: 'flux_kontext_output'.
    """

    kontext_cond: FluxKontextConditioningField
    type_: Literal["flux_kontext_output"] = "flux_kontext_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kontext_cond = self.kontext_cond.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kontext_cond": kontext_cond,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField

        d = dict(src_dict)
        kontext_cond = FluxKontextConditioningField.from_dict(d.pop("kontext_cond"))

        type_ = cast(Literal["flux_kontext_output"], d.pop("type"))
        if type_ != "flux_kontext_output":
            raise ValueError(f"type must match const 'flux_kontext_output', got '{type_}'")

        flux_kontext_output = cls(
            kontext_cond=kontext_cond,
            type_=type_,
        )

        flux_kontext_output.additional_properties = d
        return flux_kontext_output

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
