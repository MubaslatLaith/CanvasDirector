from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph import Graph
    from ..models.graph_execution_state_errors import GraphExecutionStateErrors
    from ..models.graph_execution_state_indegree import GraphExecutionStateIndegree
    from ..models.graph_execution_state_prepared_source_mapping import GraphExecutionStatePreparedSourceMapping
    from ..models.graph_execution_state_results import GraphExecutionStateResults
    from ..models.graph_execution_state_source_prepared_mapping import GraphExecutionStateSourcePreparedMapping


T = TypeVar("T", bound="GraphExecutionState")


@_attrs_define
class GraphExecutionState:
    """Tracks source-graph expansion, execution progress, and runtime results.

    Attributes:
        id (str): The id of the execution state
        graph (Graph): A validated invocation graph made of nodes and typed edges.
        execution_graph (Graph): A validated invocation graph made of nodes and typed edges.
        executed (list[str]): The set of node ids that have been executed
        executed_history (list[str]): The list of node ids that have been executed, in order of execution
        results (GraphExecutionStateResults): The results of node executions
        errors (GraphExecutionStateErrors): Errors raised when executing nodes
        prepared_source_mapping (GraphExecutionStatePreparedSourceMapping): The map of prepared nodes to original graph
            nodes
        source_prepared_mapping (GraphExecutionStateSourcePreparedMapping): The map of original graph nodes to prepared
            nodes
        ready_order (list[str] | Unset):
        indegree (GraphExecutionStateIndegree | Unset): Remaining unmet input count for exec nodes
    """

    id: str
    graph: Graph
    execution_graph: Graph
    executed: list[str]
    executed_history: list[str]
    results: GraphExecutionStateResults
    errors: GraphExecutionStateErrors
    prepared_source_mapping: GraphExecutionStatePreparedSourceMapping
    source_prepared_mapping: GraphExecutionStateSourcePreparedMapping
    ready_order: list[str] | Unset = UNSET
    indegree: GraphExecutionStateIndegree | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        graph = self.graph.to_dict()

        execution_graph = self.execution_graph.to_dict()

        executed = self.executed

        executed_history = self.executed_history

        results = self.results.to_dict()

        errors = self.errors.to_dict()

        prepared_source_mapping = self.prepared_source_mapping.to_dict()

        source_prepared_mapping = self.source_prepared_mapping.to_dict()

        ready_order: list[str] | Unset = UNSET
        if not isinstance(self.ready_order, Unset):
            ready_order = self.ready_order

        indegree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indegree, Unset):
            indegree = self.indegree.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "graph": graph,
                "execution_graph": execution_graph,
                "executed": executed,
                "executed_history": executed_history,
                "results": results,
                "errors": errors,
                "prepared_source_mapping": prepared_source_mapping,
                "source_prepared_mapping": source_prepared_mapping,
            }
        )
        if ready_order is not UNSET:
            field_dict["ready_order"] = ready_order
        if indegree is not UNSET:
            field_dict["indegree"] = indegree

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph import Graph
        from ..models.graph_execution_state_errors import GraphExecutionStateErrors
        from ..models.graph_execution_state_indegree import GraphExecutionStateIndegree
        from ..models.graph_execution_state_prepared_source_mapping import GraphExecutionStatePreparedSourceMapping
        from ..models.graph_execution_state_results import GraphExecutionStateResults
        from ..models.graph_execution_state_source_prepared_mapping import GraphExecutionStateSourcePreparedMapping

        d = dict(src_dict)
        id = d.pop("id")

        graph = Graph.from_dict(d.pop("graph"))

        execution_graph = Graph.from_dict(d.pop("execution_graph"))

        executed = cast(list[str], d.pop("executed"))

        executed_history = cast(list[str], d.pop("executed_history"))

        results = GraphExecutionStateResults.from_dict(d.pop("results"))

        errors = GraphExecutionStateErrors.from_dict(d.pop("errors"))

        prepared_source_mapping = GraphExecutionStatePreparedSourceMapping.from_dict(d.pop("prepared_source_mapping"))

        source_prepared_mapping = GraphExecutionStateSourcePreparedMapping.from_dict(d.pop("source_prepared_mapping"))

        ready_order = cast(list[str], d.pop("ready_order", UNSET))

        _indegree = d.pop("indegree", UNSET)
        indegree: GraphExecutionStateIndegree | Unset
        if isinstance(_indegree, Unset):
            indegree = UNSET
        else:
            indegree = GraphExecutionStateIndegree.from_dict(_indegree)

        graph_execution_state = cls(
            id=id,
            graph=graph,
            execution_graph=execution_graph,
            executed=executed,
            executed_history=executed_history,
            results=results,
            errors=errors,
            prepared_source_mapping=prepared_source_mapping,
            source_prepared_mapping=source_prepared_mapping,
            ready_order=ready_order,
            indegree=indegree,
        )

        graph_execution_state.additional_properties = d
        return graph_execution_state

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
