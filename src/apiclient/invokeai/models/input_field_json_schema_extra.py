from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_model_type import BaseModelType
from ..models.clip_variant_type import ClipVariantType
from ..models.field_kind import FieldKind
from ..models.input_ import Input
from ..models.model_format import ModelFormat
from ..models.model_type import ModelType
from ..models.model_variant_type import ModelVariantType
from ..models.ui_component import UIComponent
from ..models.ui_type import UIType

if TYPE_CHECKING:
    from ..models.input_field_json_schema_extra_ui_choice_labels_type_0 import (
        InputFieldJSONSchemaExtraUiChoiceLabelsType0,
    )


T = TypeVar("T", bound="InputFieldJSONSchemaExtra")


@_attrs_define
class InputFieldJSONSchemaExtra:
    """Extra attributes to be added to input fields and their OpenAPI schema. Used during graph execution,
    and by the workflow editor during schema parsing and UI rendering.

        Attributes:
            input_ (Input): The type of input a field accepts.
                - `Input.Direct`: The field must have its value provided directly, when the invocation and field       are
                instantiated.
                - `Input.Connection`: The field must have its value provided by a connection.
                - `Input.Any`: The field may have its value provided either directly or by a connection.
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
            orig_required (bool):  Default: True.
            default (Any | None):
            orig_default (Any | None):
            ui_hidden (bool):  Default: False.
            ui_type (None | UIType):
            ui_component (None | UIComponent):
            ui_order (int | None):
            ui_choice_labels (InputFieldJSONSchemaExtraUiChoiceLabelsType0 | None):
            ui_model_base (list[BaseModelType] | None):
            ui_model_type (list[ModelType] | None):
            ui_model_variant (list[ClipVariantType | ModelVariantType] | None):
            ui_model_format (list[ModelFormat] | None):
            ui_model_provider_id (list[str] | None):
    """

    input_: Input
    field_kind: FieldKind
    default: Any | None
    orig_default: Any | None
    ui_type: None | UIType
    ui_component: None | UIComponent
    ui_order: int | None
    ui_choice_labels: InputFieldJSONSchemaExtraUiChoiceLabelsType0 | None
    ui_model_base: list[BaseModelType] | None
    ui_model_type: list[ModelType] | None
    ui_model_variant: list[ClipVariantType | ModelVariantType] | None
    ui_model_format: list[ModelFormat] | None
    ui_model_provider_id: list[str] | None
    orig_required: bool = True
    ui_hidden: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_field_json_schema_extra_ui_choice_labels_type_0 import (
            InputFieldJSONSchemaExtraUiChoiceLabelsType0,
        )

        input_ = self.input_.value

        field_kind = self.field_kind.value

        orig_required = self.orig_required

        default: Any | None
        default = self.default

        orig_default: Any | None
        orig_default = self.orig_default

        ui_hidden = self.ui_hidden

        ui_type: None | str
        if isinstance(self.ui_type, UIType):
            ui_type = self.ui_type.value
        else:
            ui_type = self.ui_type

        ui_component: None | str
        if isinstance(self.ui_component, UIComponent):
            ui_component = self.ui_component.value
        else:
            ui_component = self.ui_component

        ui_order: int | None
        ui_order = self.ui_order

        ui_choice_labels: dict[str, Any] | None
        if isinstance(self.ui_choice_labels, InputFieldJSONSchemaExtraUiChoiceLabelsType0):
            ui_choice_labels = self.ui_choice_labels.to_dict()
        else:
            ui_choice_labels = self.ui_choice_labels

        ui_model_base: list[str] | None
        if isinstance(self.ui_model_base, list):
            ui_model_base = []
            for ui_model_base_type_0_item_data in self.ui_model_base:
                ui_model_base_type_0_item = ui_model_base_type_0_item_data.value
                ui_model_base.append(ui_model_base_type_0_item)

        else:
            ui_model_base = self.ui_model_base

        ui_model_type: list[str] | None
        if isinstance(self.ui_model_type, list):
            ui_model_type = []
            for ui_model_type_type_0_item_data in self.ui_model_type:
                ui_model_type_type_0_item = ui_model_type_type_0_item_data.value
                ui_model_type.append(ui_model_type_type_0_item)

        else:
            ui_model_type = self.ui_model_type

        ui_model_variant: list[str] | None
        if isinstance(self.ui_model_variant, list):
            ui_model_variant = []
            for ui_model_variant_type_0_item_data in self.ui_model_variant:
                ui_model_variant_type_0_item: str
                if isinstance(ui_model_variant_type_0_item_data, ClipVariantType):
                    ui_model_variant_type_0_item = ui_model_variant_type_0_item_data.value
                else:
                    ui_model_variant_type_0_item = ui_model_variant_type_0_item_data.value

                ui_model_variant.append(ui_model_variant_type_0_item)

        else:
            ui_model_variant = self.ui_model_variant

        ui_model_format: list[str] | None
        if isinstance(self.ui_model_format, list):
            ui_model_format = []
            for ui_model_format_type_0_item_data in self.ui_model_format:
                ui_model_format_type_0_item = ui_model_format_type_0_item_data.value
                ui_model_format.append(ui_model_format_type_0_item)

        else:
            ui_model_format = self.ui_model_format

        ui_model_provider_id: list[str] | None
        if isinstance(self.ui_model_provider_id, list):
            ui_model_provider_id = self.ui_model_provider_id

        else:
            ui_model_provider_id = self.ui_model_provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "field_kind": field_kind,
                "orig_required": orig_required,
                "default": default,
                "orig_default": orig_default,
                "ui_hidden": ui_hidden,
                "ui_type": ui_type,
                "ui_component": ui_component,
                "ui_order": ui_order,
                "ui_choice_labels": ui_choice_labels,
                "ui_model_base": ui_model_base,
                "ui_model_type": ui_model_type,
                "ui_model_variant": ui_model_variant,
                "ui_model_format": ui_model_format,
                "ui_model_provider_id": ui_model_provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_field_json_schema_extra_ui_choice_labels_type_0 import (
            InputFieldJSONSchemaExtraUiChoiceLabelsType0,
        )

        d = dict(src_dict)
        input_ = Input(d.pop("input"))

        field_kind = FieldKind(d.pop("field_kind"))

        orig_required = d.pop("orig_required")

        def _parse_default(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        default = _parse_default(d.pop("default"))

        def _parse_orig_default(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        orig_default = _parse_orig_default(d.pop("orig_default"))

        ui_hidden = d.pop("ui_hidden")

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

        def _parse_ui_component(data: object) -> None | UIComponent:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ui_component_type_0 = UIComponent(data)

                return ui_component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UIComponent, data)

        ui_component = _parse_ui_component(d.pop("ui_component"))

        def _parse_ui_order(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ui_order = _parse_ui_order(d.pop("ui_order"))

        def _parse_ui_choice_labels(data: object) -> InputFieldJSONSchemaExtraUiChoiceLabelsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ui_choice_labels_type_0 = InputFieldJSONSchemaExtraUiChoiceLabelsType0.from_dict(data)

                return ui_choice_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InputFieldJSONSchemaExtraUiChoiceLabelsType0 | None, data)

        ui_choice_labels = _parse_ui_choice_labels(d.pop("ui_choice_labels"))

        def _parse_ui_model_base(data: object) -> list[BaseModelType] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ui_model_base_type_0 = []
                _ui_model_base_type_0 = data
                for ui_model_base_type_0_item_data in _ui_model_base_type_0:
                    ui_model_base_type_0_item = BaseModelType(ui_model_base_type_0_item_data)

                    ui_model_base_type_0.append(ui_model_base_type_0_item)

                return ui_model_base_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BaseModelType] | None, data)

        ui_model_base = _parse_ui_model_base(d.pop("ui_model_base"))

        def _parse_ui_model_type(data: object) -> list[ModelType] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ui_model_type_type_0 = []
                _ui_model_type_type_0 = data
                for ui_model_type_type_0_item_data in _ui_model_type_type_0:
                    ui_model_type_type_0_item = ModelType(ui_model_type_type_0_item_data)

                    ui_model_type_type_0.append(ui_model_type_type_0_item)

                return ui_model_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ModelType] | None, data)

        ui_model_type = _parse_ui_model_type(d.pop("ui_model_type"))

        def _parse_ui_model_variant(data: object) -> list[ClipVariantType | ModelVariantType] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ui_model_variant_type_0 = []
                _ui_model_variant_type_0 = data
                for ui_model_variant_type_0_item_data in _ui_model_variant_type_0:

                    def _parse_ui_model_variant_type_0_item(data: object) -> ClipVariantType | ModelVariantType:
                        try:
                            if not isinstance(data, str):
                                raise TypeError()
                            ui_model_variant_type_0_item_type_0 = ClipVariantType(data)

                            return ui_model_variant_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, str):
                            raise TypeError()
                        ui_model_variant_type_0_item_type_1 = ModelVariantType(data)

                        return ui_model_variant_type_0_item_type_1

                    ui_model_variant_type_0_item = _parse_ui_model_variant_type_0_item(
                        ui_model_variant_type_0_item_data
                    )

                    ui_model_variant_type_0.append(ui_model_variant_type_0_item)

                return ui_model_variant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClipVariantType | ModelVariantType] | None, data)

        ui_model_variant = _parse_ui_model_variant(d.pop("ui_model_variant"))

        def _parse_ui_model_format(data: object) -> list[ModelFormat] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ui_model_format_type_0 = []
                _ui_model_format_type_0 = data
                for ui_model_format_type_0_item_data in _ui_model_format_type_0:
                    ui_model_format_type_0_item = ModelFormat(ui_model_format_type_0_item_data)

                    ui_model_format_type_0.append(ui_model_format_type_0_item)

                return ui_model_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ModelFormat] | None, data)

        ui_model_format = _parse_ui_model_format(d.pop("ui_model_format"))

        def _parse_ui_model_provider_id(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ui_model_provider_id_type_0 = cast(list[str], data)

                return ui_model_provider_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        ui_model_provider_id = _parse_ui_model_provider_id(d.pop("ui_model_provider_id"))

        input_field_json_schema_extra = cls(
            input_=input_,
            field_kind=field_kind,
            orig_required=orig_required,
            default=default,
            orig_default=orig_default,
            ui_hidden=ui_hidden,
            ui_type=ui_type,
            ui_component=ui_component,
            ui_order=ui_order,
            ui_choice_labels=ui_choice_labels,
            ui_model_base=ui_model_base,
            ui_model_type=ui_model_type,
            ui_model_variant=ui_model_variant,
            ui_model_format=ui_model_format,
            ui_model_provider_id=ui_model_provider_id,
        )

        input_field_json_schema_extra.additional_properties = d
        return input_field_json_schema_extra

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
