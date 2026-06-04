from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="AnimaConditioningField")


@_attrs_define
class AnimaConditioningField:
    """An Anima conditioning tensor primitive value.

    Anima conditioning contains Qwen3 0.6B hidden states and T5-XXL token IDs,
    which are combined by the LLM Adapter inside the transformer.

        Attributes:
            conditioning_name (str): The name of conditioning tensor
            mask (None | TensorField | Unset): The mask associated with this conditioning tensor for regional prompting.
                Excluded regions should be set to False, included regions should be set to True.
    """

    conditioning_name: str
    mask: None | TensorField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tensor_field import TensorField

        conditioning_name = self.conditioning_name

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, TensorField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditioning_name": conditioning_name,
            }
        )
        if mask is not UNSET:
            field_dict["mask"] = mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tensor_field import TensorField

        d = dict(src_dict)
        conditioning_name = d.pop("conditioning_name")

        def _parse_mask(data: object) -> None | TensorField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_type_0 = TensorField.from_dict(data)

                return mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TensorField | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))

        anima_conditioning_field = cls(
            conditioning_name=conditioning_name,
            mask=mask,
        )

        anima_conditioning_field.additional_properties = d
        return anima_conditioning_field

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
