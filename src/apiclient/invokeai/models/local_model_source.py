from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalModelSource")


@_attrs_define
class LocalModelSource:
    """A local file or directory path.

    Attributes:
        path (str):
        inplace (bool | None | Unset):  Default: False.
        type_ (Literal['local'] | Unset):  Default: 'local'.
    """

    path: str
    inplace: bool | None | Unset = False
    type_: Literal["local"] | Unset = "local"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path: str
        path = self.path

        inplace: bool | None | Unset
        if isinstance(self.inplace, Unset):
            inplace = UNSET
        else:
            inplace = self.inplace

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if inplace is not UNSET:
            field_dict["inplace"] = inplace
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_path(data: object) -> str:
            return cast(str, data)

        path = _parse_path(d.pop("path"))

        def _parse_inplace(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inplace = _parse_inplace(d.pop("inplace", UNSET))

        type_ = cast(Literal["local"] | Unset, d.pop("type", UNSET))
        if type_ != "local" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'local', got '{type_}'")

        local_model_source = cls(
            path=path,
            inplace=inplace,
            type_=type_,
        )

        local_model_source.additional_properties = d
        return local_model_source

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
