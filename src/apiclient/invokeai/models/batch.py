from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_datum import BatchDatum
    from ..models.graph import Graph
    from ..models.workflow_without_id import WorkflowWithoutID


T = TypeVar("T", bound="Batch")


@_attrs_define
class Batch:
    """
    Attributes:
        graph (Graph): A validated invocation graph made of nodes and typed edges.
        runs (int): Int stating how many times to iterate through all possible batch indices Default: 1.
        batch_id (str | Unset): The ID of the batch
        origin (None | str | Unset): The origin of this queue item. This data is used by the frontend to determine how
            to handle results.
        destination (None | str | Unset): The origin of this queue item. This data is used by the frontend to determine
            how to handle results
        data (list[list[BatchDatum]] | None | Unset): The batch data collection.
        workflow (None | Unset | WorkflowWithoutID): The workflow to initialize the session with
    """

    graph: Graph
    runs: int = 1
    batch_id: str | Unset = UNSET
    origin: None | str | Unset = UNSET
    destination: None | str | Unset = UNSET
    data: list[list[BatchDatum]] | None | Unset = UNSET
    workflow: None | Unset | WorkflowWithoutID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_without_id import WorkflowWithoutID

        graph = self.graph.to_dict()

        runs = self.runs

        batch_id = self.batch_id

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        destination: None | str | Unset
        if isinstance(self.destination, Unset):
            destination = UNSET
        else:
            destination = self.destination

        data: list[list[dict[str, Any]]] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = []
                for data_type_0_item_item_data in data_type_0_item_data:
                    data_type_0_item_item = data_type_0_item_item_data.to_dict()
                    data_type_0_item.append(data_type_0_item_item)

                data.append(data_type_0_item)

        else:
            data = self.data

        workflow: dict[str, Any] | None | Unset
        if isinstance(self.workflow, Unset):
            workflow = UNSET
        elif isinstance(self.workflow, WorkflowWithoutID):
            workflow = self.workflow.to_dict()
        else:
            workflow = self.workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "graph": graph,
                "runs": runs,
            }
        )
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if origin is not UNSET:
            field_dict["origin"] = origin
        if destination is not UNSET:
            field_dict["destination"] = destination
        if data is not UNSET:
            field_dict["data"] = data
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_datum import BatchDatum
        from ..models.graph import Graph
        from ..models.workflow_without_id import WorkflowWithoutID

        d = dict(src_dict)
        graph = Graph.from_dict(d.pop("graph"))

        runs = d.pop("runs")

        batch_id = d.pop("batch_id", UNSET)

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_destination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination = _parse_destination(d.pop("destination", UNSET))

        def _parse_data(data: object) -> list[list[BatchDatum]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = []
                    _data_type_0_item = data_type_0_item_data
                    for data_type_0_item_item_data in _data_type_0_item:
                        data_type_0_item_item = BatchDatum.from_dict(data_type_0_item_item_data)

                        data_type_0_item.append(data_type_0_item_item)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[BatchDatum]] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_workflow(data: object) -> None | Unset | WorkflowWithoutID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workflow_type_0 = WorkflowWithoutID.from_dict(data)

                return workflow_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowWithoutID, data)

        workflow = _parse_workflow(d.pop("workflow", UNSET))

        batch = cls(
            graph=graph,
            runs=runs,
            batch_id=batch_id,
            origin=origin,
            destination=destination,
            data=data,
            workflow=workflow,
        )

        batch.additional_properties = d
        return batch

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
