from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_model_type import BaseModelType
from ..models.model_type import ModelType
from ..models.sub_model_type import SubModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelIdentifierField")


@_attrs_define
class ModelIdentifierField:
    """
    Attributes:
        key (str): The model's unique key
        hash_ (str): The model's BLAKE3 hash
        name (str): The model's name
        base (BaseModelType): An enumeration of base model architectures. For example, Stable Diffusion 1.x, Stable
            Diffusion 2.x, FLUX, etc.

            Every model config must have a base architecture type.

            Not all models are associated with a base architecture. For example, CLIP models are their own thing, not
            related
            to any particular model architecture. To simplify internal APIs and make it easier to work with models, we use a
            fallback/null value `BaseModelType.Any` for these models, instead of making the model base optional.
        type_ (ModelType): Model type.
        submodel_type (None | SubModelType | Unset): The submodel to load, if this is a main model
    """

    key: str
    hash_: str
    name: str
    base: BaseModelType
    type_: ModelType
    submodel_type: None | SubModelType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        hash_ = self.hash_

        name = self.name

        base = self.base.value

        type_ = self.type_.value

        submodel_type: None | str | Unset
        if isinstance(self.submodel_type, Unset):
            submodel_type = UNSET
        elif isinstance(self.submodel_type, SubModelType):
            submodel_type = self.submodel_type.value
        else:
            submodel_type = self.submodel_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "hash": hash_,
                "name": name,
                "base": base,
                "type": type_,
            }
        )
        if submodel_type is not UNSET:
            field_dict["submodel_type"] = submodel_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        hash_ = d.pop("hash")

        name = d.pop("name")

        base = BaseModelType(d.pop("base"))

        type_ = ModelType(d.pop("type"))

        def _parse_submodel_type(data: object) -> None | SubModelType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submodel_type_type_0 = SubModelType(data)

                return submodel_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubModelType | Unset, data)

        submodel_type = _parse_submodel_type(d.pop("submodel_type", UNSET))

        model_identifier_field = cls(
            key=key,
            hash_=hash_,
            name=name,
            base=base,
            type_=type_,
            submodel_type=submodel_type,
        )

        model_identifier_field.additional_properties = d
        return model_identifier_field

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
