from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exposed_field import ExposedField
    from ..models.workflow_meta import WorkflowMeta
    from ..models.workflow_without_id_edges_item import WorkflowWithoutIDEdgesItem
    from ..models.workflow_without_id_form_type_0 import WorkflowWithoutIDFormType0
    from ..models.workflow_without_id_nodes_item import WorkflowWithoutIDNodesItem


T = TypeVar("T", bound="WorkflowWithoutID")


@_attrs_define
class WorkflowWithoutID:
    """
    Attributes:
        name (str): The name of the workflow.
        author (str): The author of the workflow.
        description (str): The description of the workflow.
        version (str): The version of the workflow.
        contact (str): The contact of the workflow.
        tags (str): The tags of the workflow.
        notes (str): The notes of the workflow.
        exposed_fields (list[ExposedField]): The exposed fields of the workflow.
        meta (WorkflowMeta):
        nodes (list[WorkflowWithoutIDNodesItem]): The nodes of the workflow.
        edges (list[WorkflowWithoutIDEdgesItem]): The edges of the workflow.
        form (None | Unset | WorkflowWithoutIDFormType0): The form of the workflow.
    """

    name: str
    author: str
    description: str
    version: str
    contact: str
    tags: str
    notes: str
    exposed_fields: list[ExposedField]
    meta: WorkflowMeta
    nodes: list[WorkflowWithoutIDNodesItem]
    edges: list[WorkflowWithoutIDEdgesItem]
    form: None | Unset | WorkflowWithoutIDFormType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_without_id_form_type_0 import WorkflowWithoutIDFormType0

        name = self.name

        author = self.author

        description = self.description

        version = self.version

        contact = self.contact

        tags = self.tags

        notes = self.notes

        exposed_fields = []
        for exposed_fields_item_data in self.exposed_fields:
            exposed_fields_item = exposed_fields_item_data.to_dict()
            exposed_fields.append(exposed_fields_item)

        meta = self.meta.to_dict()

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)

        form: dict[str, Any] | None | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        elif isinstance(self.form, WorkflowWithoutIDFormType0):
            form = self.form.to_dict()
        else:
            form = self.form

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "author": author,
                "description": description,
                "version": version,
                "contact": contact,
                "tags": tags,
                "notes": notes,
                "exposedFields": exposed_fields,
                "meta": meta,
                "nodes": nodes,
                "edges": edges,
            }
        )
        if form is not UNSET:
            field_dict["form"] = form

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exposed_field import ExposedField
        from ..models.workflow_meta import WorkflowMeta
        from ..models.workflow_without_id_edges_item import WorkflowWithoutIDEdgesItem
        from ..models.workflow_without_id_form_type_0 import WorkflowWithoutIDFormType0
        from ..models.workflow_without_id_nodes_item import WorkflowWithoutIDNodesItem

        d = dict(src_dict)
        name = d.pop("name")

        author = d.pop("author")

        description = d.pop("description")

        version = d.pop("version")

        contact = d.pop("contact")

        tags = d.pop("tags")

        notes = d.pop("notes")

        exposed_fields = []
        _exposed_fields = d.pop("exposedFields")
        for exposed_fields_item_data in _exposed_fields:
            exposed_fields_item = ExposedField.from_dict(exposed_fields_item_data)

            exposed_fields.append(exposed_fields_item)

        meta = WorkflowMeta.from_dict(d.pop("meta"))

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = WorkflowWithoutIDNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = WorkflowWithoutIDEdgesItem.from_dict(edges_item_data)

            edges.append(edges_item)

        def _parse_form(data: object) -> None | Unset | WorkflowWithoutIDFormType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                form_type_0 = WorkflowWithoutIDFormType0.from_dict(data)

                return form_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowWithoutIDFormType0, data)

        form = _parse_form(d.pop("form", UNSET))

        workflow_without_id = cls(
            name=name,
            author=author,
            description=description,
            version=version,
            contact=contact,
            tags=tags,
            notes=notes,
            exposed_fields=exposed_fields,
            meta=meta,
            nodes=nodes,
            edges=edges,
            form=form,
        )

        workflow_without_id.additional_properties = d
        return workflow_without_id

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
