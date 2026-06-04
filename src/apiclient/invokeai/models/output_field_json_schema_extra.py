from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_kind import FieldKind
from ..models.ui_type import UIType

T = TypeVar("T", bound="OutputFieldJSONSchemaExtra")


@_attrs_define
class OutputFieldJSONSchemaExtra:
    """Extra attributes to be added to input fields and their OpenAPI schema. Used by the workflow editor
    during schema parsing and UI rendering.

        Attributes:
            field_kind (FieldKind): The kind of field.
                - `Input`: An input field on a node.
                - `Output`: An output field on a node.
                - `Internal`: A field which is treated as an input, but cannot be used in node definitions. Metadata is
                one example. It is provided to nodes via the WithMetadata class, and we want to reserve the field name
                "metadata" for this on all nodes. `FieldKind` is used to short-circuit the field name validation logic,
                allowing "metadata" for that field.
                - `NodeAttribute`: The field is a node attribute. These are fields which are not inputs or outputs,
                but which are used to store information about the node. For example, the `id` and `type` fields are node
                attributes.

                The presence of this in `json_schema_extra["field_kind"]` is used when initializing node schemas on app
                startup, and when generating the OpenAPI schema for the workflow editor.
            ui_hidden (bool):  Default: False.
            ui_order (int | None):
            ui_type (None | UIType):
    """

    field_kind: FieldKind
    ui_order: int | None
    ui_type: None | UIType
    ui_hidden: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_kind = self.field_kind.value

        ui_hidden = self.ui_hidden

        ui_order: int | None
        ui_order = self.ui_order

        ui_type: None | str
        if isinstance(self.ui_type, UIType):
            ui_type = self.ui_type.value
        else:
            ui_type = self.ui_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_kind": field_kind,
                "ui_hidden": ui_hidden,
                "ui_order": ui_order,
                "ui_type": ui_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_kind = FieldKind(d.pop("field_kind"))

        ui_hidden = d.pop("ui_hidden")

        def _parse_ui_order(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ui_order = _parse_ui_order(d.pop("ui_order"))

        def _parse_ui_type(data: object) -> None | UIType:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ui_type_type_0 = UIType(data)

                return ui_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UIType, data)

        ui_type = _parse_ui_type(d.pop("ui_type"))

        output_field_json_schema_extra = cls(
            field_kind=field_kind,
            ui_hidden=ui_hidden,
            ui_order=ui_order,
            ui_type=ui_type,
        )

        output_field_json_schema_extra.additional_properties = d
        return output_field_json_schema_extra

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
