from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="MainModelCogView4")


@_attrs_define
class MainModelCogView4:
    """Loads a CogView4 base model, outputting its submodels.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        model (ModelIdentifierField):
        type_ (Literal['cogview4_model_loader']):  Default: 'cogview4_model_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
    """

    id: str
    model: ModelIdentifierField
    type_: Literal["cogview4_model_loader"] = "cogview4_model_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model = self.model.to_dict()

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model": model,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        model = ModelIdentifierField.from_dict(d.pop("model"))

        type_ = cast(Literal["cogview4_model_loader"], d.pop("type"))
        if type_ != "cogview4_model_loader":
            raise ValueError(f"type must match const 'cogview4_model_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        main_model_cog_view_4 = cls(
            id=id,
            model=model,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
        )

        main_model_cog_view_4.additional_properties = d
        return main_model_cog_view_4

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
