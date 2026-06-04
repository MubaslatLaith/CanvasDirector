from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flux_redux_conditioning_field import FluxReduxConditioningField


T = TypeVar("T", bound="FluxReduxOutput")


@_attrs_define
class FluxReduxOutput:
    """The conditioning output of a FLUX Redux invocation.

    Attributes:
        redux_cond (FluxReduxConditioningField): A FLUX Redux conditioning tensor primitive value
        type_ (Literal['flux_redux_output']):  Default: 'flux_redux_output'.
    """

    redux_cond: FluxReduxConditioningField
    type_: Literal["flux_redux_output"] = "flux_redux_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redux_cond = self.redux_cond.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redux_cond": redux_cond,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flux_redux_conditioning_field import FluxReduxConditioningField

        d = dict(src_dict)
        redux_cond = FluxReduxConditioningField.from_dict(d.pop("redux_cond"))

        type_ = cast(Literal["flux_redux_output"], d.pop("type"))
        if type_ != "flux_redux_output":
            raise ValueError(f"type must match const 'flux_redux_output', got '{type_}'")

        flux_redux_output = cls(
            redux_cond=redux_cond,
            type_=type_,
        )

        flux_redux_output.additional_properties = d
        return flux_redux_output

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
