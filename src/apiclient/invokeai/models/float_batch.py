from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.float_batch_batch_group import FloatBatchBatchGroup
from ..types import UNSET, Unset

T = TypeVar("T", bound="FloatBatch")


@_attrs_define
class FloatBatch:
    """Create a batched generation, where the workflow is executed once for each float in the batch.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['float_batch']):  Default: 'float_batch'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        batch_group_id (FloatBatchBatchGroup | Unset): The ID of this batch node's group. If provided, all batch nodes
            in with the same ID will be 'zipped' before execution, and all nodes' collections must be of the same size.
            Default: FloatBatchBatchGroup.NONE.
        floats (list[float] | None | Unset): The floats to batch over
    """

    id: str
    type_: Literal["float_batch"] = "float_batch"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    batch_group_id: FloatBatchBatchGroup | Unset = FloatBatchBatchGroup.NONE
    floats: list[float] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        batch_group_id: str | Unset = UNSET
        if not isinstance(self.batch_group_id, Unset):
            batch_group_id = self.batch_group_id.value

        floats: list[float] | None | Unset
        if isinstance(self.floats, Unset):
            floats = UNSET
        elif isinstance(self.floats, list):
            floats = self.floats

        else:
            floats = self.floats

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
        if floats is not UNSET:
            field_dict["floats"] = floats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["float_batch"], d.pop("type"))
        if type_ != "float_batch":
            raise ValueError(f"type must match const 'float_batch', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _batch_group_id = d.pop("batch_group_id", UNSET)
        batch_group_id: FloatBatchBatchGroup | Unset
        if isinstance(_batch_group_id, Unset):
            batch_group_id = UNSET
        else:
            batch_group_id = FloatBatchBatchGroup(_batch_group_id)

        def _parse_floats(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                floats_type_0 = cast(list[float], data)

                return floats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        floats = _parse_floats(d.pop("floats", UNSET))

        float_batch = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            batch_group_id=batch_group_id,
            floats=floats,
        )

        float_batch.additional_properties = d
        return float_batch

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
