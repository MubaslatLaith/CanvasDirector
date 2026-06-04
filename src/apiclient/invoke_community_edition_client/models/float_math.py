from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.float_math_operation import FloatMathOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="FloatMath")


@_attrs_define
class FloatMath:
    """Performs floating point math.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['float_math']):  Default: 'float_math'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        operation (FloatMathOperation | Unset): The operation to perform Default: FloatMathOperation.ADD.
        a (float | Unset): The first number Default: 1.0.
        b (float | Unset): The second number Default: 1.0.
    """

    id: str
    type_: Literal["float_math"] = "float_math"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    operation: FloatMathOperation | Unset = FloatMathOperation.ADD
    a: float | Unset = 1.0
    b: float | Unset = 1.0
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

        type_ = cast(Literal["float_math"], d.pop("type"))
        if type_ != "float_math":
            raise ValueError(f"type must match const 'float_math', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: FloatMathOperation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = FloatMathOperation(_operation)

        a = d.pop("a", UNSET)

        b = d.pop("b", UNSET)

        float_math = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            operation=operation,
            a=a,
            b=b,
        )

        float_math.additional_properties = d
        return float_math

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
