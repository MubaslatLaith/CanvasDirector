from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_to_float_label import MetadataToFloatLabel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="MetadataToFloat")


@_attrs_define
class MetadataToFloat:
    """Extracts a Float value of a label from metadata

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['metadata_to_float']):  Default: 'metadata_to_float'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        label (MetadataToFloatLabel | Unset): Label for this metadata item Default: MetadataToFloatLabel.VALUE_0.
        custom_label (None | str | Unset): Label for this metadata item
        default_value (float | None | Unset): The default float to use if not found in the metadata
    """

    id: str
    type_: Literal["metadata_to_float"] = "metadata_to_float"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    label: MetadataToFloatLabel | Unset = MetadataToFloatLabel.VALUE_0
    custom_label: None | str | Unset = UNSET
    default_value: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metadata_field import MetadataField

        id = self.id

        type_ = self.type_

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, MetadataField):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        label: str | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.value

        custom_label: None | str | Unset
        if isinstance(self.custom_label, Unset):
            custom_label = UNSET
        else:
            custom_label = self.custom_label

        default_value: float | None | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if label is not UNSET:
            field_dict["label"] = label
        if custom_label is not UNSET:
            field_dict["custom_label"] = custom_label
        if default_value is not UNSET:
            field_dict["default_value"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["metadata_to_float"], d.pop("type"))
        if type_ != "metadata_to_float":
            raise ValueError(f"type must match const 'metadata_to_float', got '{type_}'")

        def _parse_metadata(data: object) -> MetadataField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MetadataField.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataField | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _label = d.pop("label", UNSET)
        label: MetadataToFloatLabel | Unset
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = MetadataToFloatLabel(_label)

        def _parse_custom_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_label = _parse_custom_label(d.pop("custom_label", UNSET))

        def _parse_default_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        metadata_to_float = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            label=label,
            custom_label=custom_label,
            default_value=default_value,
        )

        metadata_to_float.additional_properties = d
        return metadata_to_float

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
