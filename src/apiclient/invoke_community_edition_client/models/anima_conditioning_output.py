from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.anima_conditioning_field import AnimaConditioningField


T = TypeVar("T", bound="AnimaConditioningOutput")


@_attrs_define
class AnimaConditioningOutput:
    """Base class for nodes that output an Anima text conditioning tensor.

    Attributes:
        conditioning (AnimaConditioningField): An Anima conditioning tensor primitive value.

            Anima conditioning contains Qwen3 0.6B hidden states and T5-XXL token IDs,
            which are combined by the LLM Adapter inside the transformer.
        type_ (Literal['anima_conditioning_output']):  Default: 'anima_conditioning_output'.
    """

    conditioning: AnimaConditioningField
    type_: Literal["anima_conditioning_output"] = "anima_conditioning_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditioning = self.conditioning.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditioning": conditioning,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.anima_conditioning_field import AnimaConditioningField

        d = dict(src_dict)
        conditioning = AnimaConditioningField.from_dict(d.pop("conditioning"))

        type_ = cast(Literal["anima_conditioning_output"], d.pop("type"))
        if type_ != "anima_conditioning_output":
            raise ValueError(f"type must match const 'anima_conditioning_output', got '{type_}'")

        anima_conditioning_output = cls(
            conditioning=conditioning,
            type_=type_,
        )

        anima_conditioning_output.additional_properties = d
        return anima_conditioning_output

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
