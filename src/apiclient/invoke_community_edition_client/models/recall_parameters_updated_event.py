from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recall_parameters_updated_event_parameters import RecallParametersUpdatedEventParameters


T = TypeVar("T", bound="RecallParametersUpdatedEvent")


@_attrs_define
class RecallParametersUpdatedEvent:
    """Event model for recall_parameters_updated

    Attributes:
        timestamp (int): The timestamp of the event
        queue_id (str): The ID of the queue
        user_id (str): The ID of the user whose recall parameters were updated
        parameters (RecallParametersUpdatedEventParameters): The recall parameters that were updated
    """

    timestamp: int
    queue_id: str
    user_id: str
    parameters: RecallParametersUpdatedEventParameters
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        queue_id = self.queue_id

        user_id = self.user_id

        parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "queue_id": queue_id,
                "user_id": user_id,
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recall_parameters_updated_event_parameters import RecallParametersUpdatedEventParameters

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        queue_id = d.pop("queue_id")

        user_id = d.pop("user_id")

        parameters = RecallParametersUpdatedEventParameters.from_dict(d.pop("parameters"))

        recall_parameters_updated_event = cls(
            timestamp=timestamp,
            queue_id=queue_id,
            user_id=user_id,
            parameters=parameters,
        )

        recall_parameters_updated_event.additional_properties = d
        return recall_parameters_updated_event

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
