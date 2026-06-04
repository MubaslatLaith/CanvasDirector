from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowAndGraphResponse")


@_attrs_define
class WorkflowAndGraphResponse:
    """
    Attributes:
        workflow (None | str): The workflow used to generate the image, as stringified JSON
        graph (None | str): The graph used to generate the image, as stringified JSON
    """

    workflow: None | str
    graph: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow: None | str
        workflow = self.workflow

        graph: None | str
        graph = self.graph

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflow": workflow,
                "graph": graph,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workflow(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workflow = _parse_workflow(d.pop("workflow"))

        def _parse_graph(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        graph = _parse_graph(d.pop("graph"))

        workflow_and_graph_response = cls(
            workflow=workflow,
            graph=graph,
        )

        workflow_and_graph_response.additional_properties = d
        return workflow_and_graph_response

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
