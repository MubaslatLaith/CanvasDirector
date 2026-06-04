from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flux_fill_conditioning_field import FluxFillConditioningField


T = TypeVar("T", bound="FluxFillOutput")


@_attrs_define
class FluxFillOutput:
    """The conditioning output of a FLUX Fill invocation.

    Attributes:
        fill_cond (FluxFillConditioningField): A FLUX Fill conditioning field.
        type_ (Literal['flux_fill_output']):  Default: 'flux_fill_output'.
    """

    fill_cond: FluxFillConditioningField
    type_: Literal["flux_fill_output"] = "flux_fill_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fill_cond = self.fill_cond.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fill_cond": fill_cond,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flux_fill_conditioning_field import FluxFillConditioningField

        d = dict(src_dict)
        fill_cond = FluxFillConditioningField.from_dict(d.pop("fill_cond"))

        type_ = cast(Literal["flux_fill_output"], d.pop("type"))
        if type_ != "flux_fill_output":
            raise ValueError(f"type must match const 'flux_fill_output', got '{type_}'")

        flux_fill_output = cls(
            fill_cond=fill_cond,
            type_=type_,
        )

        flux_fill_output.additional_properties = d
        return flux_fill_output

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
