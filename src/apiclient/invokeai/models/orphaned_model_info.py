from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrphanedModelInfo")


@_attrs_define
class OrphanedModelInfo:
    """Information about an orphaned model directory.

    Attributes:
        path (str): Relative path to the orphaned directory from models root
        absolute_path (str): Absolute path to the orphaned directory
        files (list[str]): List of model files in this directory
        size_bytes (int): Total size of all files in bytes
    """

    path: str
    absolute_path: str
    files: list[str]
    size_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        absolute_path = self.absolute_path

        files = self.files

        size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "absolute_path": absolute_path,
                "files": files,
                "size_bytes": size_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        absolute_path = d.pop("absolute_path")

        files = cast(list[str], d.pop("files"))

        size_bytes = d.pop("size_bytes")

        orphaned_model_info = cls(
            path=path,
            absolute_path=absolute_path,
            files=files,
            size_bytes=size_bytes,
        )

        orphaned_model_info.additional_properties = d
        return orphaned_model_info

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
