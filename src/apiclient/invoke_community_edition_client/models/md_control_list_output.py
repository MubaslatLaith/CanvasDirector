from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.control_field import ControlField


T = TypeVar("T", bound="MDControlListOutput")


@_attrs_define
class MDControlListOutput:
    """
    Attributes:
        control_list (ControlField | list[ControlField] | None): ControlNet(s) to apply
        type_ (Literal['md_control_list_output']):  Default: 'md_control_list_output'.
    """

    control_list: ControlField | list[ControlField] | None
    type_: Literal["md_control_list_output"] = "md_control_list_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_field import ControlField

        control_list: dict[str, Any] | list[dict[str, Any]] | None
        if isinstance(self.control_list, ControlField):
            control_list = self.control_list.to_dict()
        elif isinstance(self.control_list, list):
            control_list = []
            for control_list_type_1_item_data in self.control_list:
                control_list_type_1_item = control_list_type_1_item_data.to_dict()
                control_list.append(control_list_type_1_item)

        else:
            control_list = self.control_list

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "control_list": control_list,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_field import ControlField

        d = dict(src_dict)

        def _parse_control_list(data: object) -> ControlField | list[ControlField] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_list_type_0 = ControlField.from_dict(data)

                return control_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_list_type_1 = []
                _control_list_type_1 = data
                for control_list_type_1_item_data in _control_list_type_1:
                    control_list_type_1_item = ControlField.from_dict(control_list_type_1_item_data)

                    control_list_type_1.append(control_list_type_1_item)

                return control_list_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlField | list[ControlField] | None, data)

        control_list = _parse_control_list(d.pop("control_list"))

        type_ = cast(Literal["md_control_list_output"], d.pop("type"))
        if type_ != "md_control_list_output":
            raise ValueError(f"type must match const 'md_control_list_output', got '{type_}'")

        md_control_list_output = cls(
            control_list=control_list,
            type_=type_,
        )

        md_control_list_output.additional_properties = d
        return md_control_list_output

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
