from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstallNodePackResponse")


@_attrs_define
class InstallNodePackResponse:
    """Response after installing a node pack.

    Attributes:
        name (str): The name of the installed node pack.
        success (bool): Whether the installation was successful.
        message (str): Status message.
        workflows_imported (int | Unset): Number of workflows imported from the pack. Default: 0.
        requires_dependencies (bool | Unset): Whether the pack ships a dependency manifest (requirements.txt or
            pyproject.toml) that the user must install manually following the pack's documentation. Default: False.
        dependency_file (None | str | Unset): Name of the detected dependency manifest file, if any.
    """

    name: str
    success: bool
    message: str
    workflows_imported: int | Unset = 0
    requires_dependencies: bool | Unset = False
    dependency_file: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        success = self.success

        message = self.message

        workflows_imported = self.workflows_imported

        requires_dependencies = self.requires_dependencies

        dependency_file: None | str | Unset
        if isinstance(self.dependency_file, Unset):
            dependency_file = UNSET
        else:
            dependency_file = self.dependency_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "success": success,
                "message": message,
            }
        )
        if workflows_imported is not UNSET:
            field_dict["workflows_imported"] = workflows_imported
        if requires_dependencies is not UNSET:
            field_dict["requires_dependencies"] = requires_dependencies
        if dependency_file is not UNSET:
            field_dict["dependency_file"] = dependency_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        success = d.pop("success")

        message = d.pop("message")

        workflows_imported = d.pop("workflows_imported", UNSET)

        requires_dependencies = d.pop("requires_dependencies", UNSET)

        def _parse_dependency_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dependency_file = _parse_dependency_file(d.pop("dependency_file", UNSET))

        install_node_pack_response = cls(
            name=name,
            success=success,
            message=message,
            workflows_imported=workflows_imported,
            requires_dependencies=requires_dependencies,
            dependency_file=dependency_file,
        )

        install_node_pack_response.additional_properties = d
        return install_node_pack_response

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
