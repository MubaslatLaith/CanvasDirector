from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.external_model_source import ExternalModelSource
    from ..models.hf_model_source import HFModelSource
    from ..models.local_model_source import LocalModelSource
    from ..models.url_model_source import URLModelSource


T = TypeVar("T", bound="ModelInstallCancelledEvent")


@_attrs_define
class ModelInstallCancelledEvent:
    """Event model for model_install_cancelled

    Attributes:
        timestamp (int): The timestamp of the event
        id (int): The ID of the install job
        source (ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource): Source of the model; local
            path, repo_id or url
    """

    timestamp: int
    id: int
    source: ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hf_model_source import HFModelSource
        from ..models.local_model_source import LocalModelSource
        from ..models.url_model_source import URLModelSource

        timestamp = self.timestamp

        id = self.id

        source: dict[str, Any]
        if isinstance(self.source, LocalModelSource):
            source = self.source.to_dict()
        elif isinstance(self.source, HFModelSource):
            source = self.source.to_dict()
        elif isinstance(self.source, URLModelSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "id": id,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_model_source import ExternalModelSource
        from ..models.hf_model_source import HFModelSource
        from ..models.local_model_source import LocalModelSource
        from ..models.url_model_source import URLModelSource

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        id = d.pop("id")

        def _parse_source(data: object) -> ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = LocalModelSource.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_1 = HFModelSource.from_dict(data)

                return source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_2 = URLModelSource.from_dict(data)

                return source_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            source_type_3 = ExternalModelSource.from_dict(data)

            return source_type_3

        source = _parse_source(d.pop("source"))

        model_install_cancelled_event = cls(
            timestamp=timestamp,
            id=id,
            source=source,
        )

        model_install_cancelled_event.additional_properties = d
        return model_install_cancelled_event

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
