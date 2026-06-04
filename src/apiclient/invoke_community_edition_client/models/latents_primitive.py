from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.latents_field import LatentsField


T = TypeVar("T", bound="LatentsPrimitive")


@_attrs_define
class LatentsPrimitive:
    """A latents tensor primitive value

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['latents']):  Default: 'latents'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        latents (LatentsField | None | Unset): The latents tensor
    """

    id: str
    type_: Literal["latents"] = "latents"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.latents_field import LatentsField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        latents: dict[str, Any] | None | Unset
        if isinstance(self.latents, Unset):
            latents = UNSET
        elif isinstance(self.latents, LatentsField):
            latents = self.latents.to_dict()
        else:
            latents = self.latents

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
        if latents is not UNSET:
            field_dict["latents"] = latents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latents_field import LatentsField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["latents"], d.pop("type"))
        if type_ != "latents":
            raise ValueError(f"type must match const 'latents', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_latents(data: object) -> LatentsField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latents_type_0 = LatentsField.from_dict(data)

                return latents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LatentsField | None | Unset, data)

        latents = _parse_latents(d.pop("latents", UNSET))

        latents_primitive = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            latents=latents,
        )

        latents_primitive.additional_properties = d
        return latents_primitive

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
