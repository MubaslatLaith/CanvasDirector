from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="If")


@_attrs_define
class If:
    """Selects between two optional inputs based on a boolean condition.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['if']):  Default: 'if'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        condition (bool | Unset): The condition used to select an input Default: False.
        true_input (Any | None | Unset): Selected when the condition is true
        false_input (Any | None | Unset): Selected when the condition is false
    """

    id: str
    type_: Literal["if"] = "if"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    condition: bool | Unset = False
    true_input: Any | None | Unset = UNSET
    false_input: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        condition = self.condition

        true_input: Any | None | Unset
        if isinstance(self.true_input, Unset):
            true_input = UNSET
        else:
            true_input = self.true_input

        false_input: Any | None | Unset
        if isinstance(self.false_input, Unset):
            false_input = UNSET
        else:
            false_input = self.false_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if condition is not UNSET:
            field_dict["condition"] = condition
        if true_input is not UNSET:
            field_dict["true_input"] = true_input
        if false_input is not UNSET:
            field_dict["false_input"] = false_input

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["if"], d.pop("type"))
        if type_ != "if":
            raise ValueError(f"type must match const 'if', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        condition = d.pop("condition", UNSET)

        def _parse_true_input(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        true_input = _parse_true_input(d.pop("true_input", UNSET))

        def _parse_false_input(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        false_input = _parse_false_input(d.pop("false_input", UNSET))

        if_ = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            condition=condition,
            true_input=true_input,
            false_input=false_input,
        )

        if_.additional_properties = d
        return if_

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
