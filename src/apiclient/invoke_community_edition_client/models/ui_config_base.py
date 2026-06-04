from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.classification import Classification

T = TypeVar("T", bound="UIConfigBase")


@_attrs_define
class UIConfigBase:
    """Provides additional node configuration to the UI.
    This is used internally by the @invocation decorator logic. Do not use this directly.

        Attributes:
            tags (list[str] | None): The node's tags
            title (None | str): The node's display name
            category (None | str): The node's category
            version (str): The node's version. Should be a valid semver string e.g. "1.0.0" or "3.8.13".
            node_pack (str): The node pack that this node belongs to, will be 'invokeai' for built-in nodes
            classification (Classification): The classification of an Invocation.
                - `Stable`: The invocation, including its inputs/outputs and internal logic, is stable. You may build workflows
                with it, having confidence that they will not break because of a change in this invocation.
                - `Beta`: The invocation is not yet stable, but is planned to be stable in the future. Workflows built around
                this invocation may break, but we are committed to supporting this invocation long-term.
                - `Prototype`: The invocation is not yet stable and may be removed from the application at any time. Workflows
                built around this invocation may break, and we are *not* committed to supporting this invocation.
                - `Deprecated`: The invocation is deprecated and may be removed in a future version.
                - `Internal`: The invocation is not intended for use by end-users. It may be changed or removed at any time, but
                is exposed for users to play with.
                - `Special`: The invocation is a special case and does not fit into any of the other classifications.
    """

    tags: list[str] | None
    title: None | str
    category: None | str
    version: str
    node_pack: str
    classification: Classification
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | None
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        title: None | str
        title = self.title

        category: None | str
        category = self.category

        version = self.version

        node_pack = self.node_pack

        classification = self.classification.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
                "title": title,
                "category": category,
                "version": version,
                "node_pack": node_pack,
                "classification": classification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_tags(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tags = _parse_tags(d.pop("tags"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        version = d.pop("version")

        node_pack = d.pop("node_pack")

        classification = Classification(d.pop("classification"))

        ui_config_base = cls(
            tags=tags,
            title=title,
            category=category,
            version=version,
            node_pack=node_pack,
            classification=classification,
        )

        ui_config_base.additional_properties = d
        return ui_config_base

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
