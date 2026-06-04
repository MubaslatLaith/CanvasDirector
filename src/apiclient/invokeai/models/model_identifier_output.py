from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="ModelIdentifierOutput")


@_attrs_define
class ModelIdentifierOutput:
    """Model identifier output

    Attributes:
        model (ModelIdentifierField):
        type_ (Literal['model_identifier_output']):  Default: 'model_identifier_output'.
    """

    model: ModelIdentifierField
    type_: Literal["model_identifier_output"] = "model_identifier_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        model = ModelIdentifierField.from_dict(d.pop("model"))

        type_ = cast(Literal["model_identifier_output"], d.pop("type"))
        if type_ != "model_identifier_output":
            raise ValueError(f"type must match const 'model_identifier_output', got '{type_}'")

        model_identifier_output = cls(
            model=model,
            type_=type_,
        )

        model_identifier_output.additional_properties = d
        return model_identifier_output

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
