from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integer_math_operation import IntegerMathOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegerMath")


@_attrs_define
class IntegerMath:
    """Performs integer math.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['integer_math']):  Default: 'integer_math'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        operation (IntegerMathOperation | Unset): The operation to perform Default: IntegerMathOperation.ADD.
        a (int | Unset): The first number Default: 1.
        b (int | Unset): The second number Default: 1.
    """

    id: str
    type_: Literal["integer_math"] = "integer_math"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    operation: IntegerMathOperation | Unset = IntegerMathOperation.ADD
    a: int | Unset = 1
    b: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        a = self.a

        b = self.b

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
        if operation is not UNSET:
            field_dict["operation"] = operation
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["integer_math"], d.pop("type"))
        if type_ != "integer_math":
            raise ValueError(f"type must match const 'integer_math', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: IntegerMathOperation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = IntegerMathOperation(_operation)

        a = d.pop("a", UNSET)

        b = d.pop("b", UNSET)

        integer_math = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            operation=operation,
            a=a,
            b=b,
        )

        integer_math.additional_properties = d
        return integer_math

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
