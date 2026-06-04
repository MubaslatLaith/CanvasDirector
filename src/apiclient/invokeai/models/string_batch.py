from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.string_batch_batch_group import StringBatchBatchGroup
from ..types import UNSET, Unset

T = TypeVar("T", bound="StringBatch")


@_attrs_define
class StringBatch:
    """Create a batched generation, where the workflow is executed once for each string in the batch.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['string_batch']):  Default: 'string_batch'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        batch_group_id (StringBatchBatchGroup | Unset): The ID of this batch node's group. If provided, all batch nodes
            in with the same ID will be 'zipped' before execution, and all nodes' collections must be of the same size.
            Default: StringBatchBatchGroup.NONE.
        strings (list[str] | None | Unset): The strings to batch over
    """

    id: str
    type_: Literal["string_batch"] = "string_batch"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    batch_group_id: StringBatchBatchGroup | Unset = StringBatchBatchGroup.NONE
    strings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        batch_group_id: str | Unset = UNSET
        if not isinstance(self.batch_group_id, Unset):
            batch_group_id = self.batch_group_id.value

        strings: list[str] | None | Unset
        if isinstance(self.strings, Unset):
            strings = UNSET
        elif isinstance(self.strings, list):
            strings = self.strings

        else:
            strings = self.strings

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
        if batch_group_id is not UNSET:
            field_dict["batch_group_id"] = batch_group_id
        if strings is not UNSET:
            field_dict["strings"] = strings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["string_batch"], d.pop("type"))
        if type_ != "string_batch":
            raise ValueError(f"type must match const 'string_batch', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _batch_group_id = d.pop("batch_group_id", UNSET)
        batch_group_id: StringBatchBatchGroup | Unset
        if isinstance(_batch_group_id, Unset):
            batch_group_id = UNSET
        else:
            batch_group_id = StringBatchBatchGroup(_batch_group_id)

        def _parse_strings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                strings_type_0 = cast(list[str], data)

                return strings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        strings = _parse_strings(d.pop("strings", UNSET))

        string_batch = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            batch_group_id=batch_group_id,
            strings=strings,
        )

        string_batch.additional_properties = d
        return string_batch

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
