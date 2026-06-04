from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge import Edge
    from ..models.graph_nodes import GraphNodes


T = TypeVar("T", bound="Graph")


@_attrs_define
class Graph:
    """A validated invocation graph made of nodes and typed edges.

    Attributes:
        id (str | Unset): The id of this graph
        nodes (GraphNodes | Unset): The nodes in this graph
        edges (list[Edge] | Unset): The connections between nodes and their fields in this graph
    """

    id: str | Unset = UNSET
    nodes: GraphNodes | Unset = UNSET
    edges: list[Edge] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if edges is not UNSET:
            field_dict["edges"] = edges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge import Edge
        from ..models.graph_nodes import GraphNodes

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _nodes = d.pop("nodes", UNSET)
        nodes: GraphNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = GraphNodes.from_dict(_nodes)

        _edges = d.pop("edges", UNSET)
        edges: list[Edge] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = Edge.from_dict(edges_item_data)

                edges.append(edges_item)

        graph = cls(
            id=id,
            nodes=nodes,
            edges=edges,
        )

        graph.additional_properties = d
        return graph

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
