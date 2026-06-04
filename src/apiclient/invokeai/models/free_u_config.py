from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FreeUConfig")


@_attrs_define
class FreeUConfig:
    """Configuration for the FreeU hyperparameters.
    - https://huggingface.co/docs/diffusers/main/en/using-diffusers/freeu
    - https://github.com/ChenyangSi/FreeU

        Attributes:
            s1 (float): Scaling factor for stage 1 to attenuate the contributions of the skip features. This is done to
                mitigate the "oversmoothing effect" in the enhanced denoising process.
            s2 (float): Scaling factor for stage 2 to attenuate the contributions of the skip features. This is done to
                mitigate the "oversmoothing effect" in the enhanced denoising process.
            b1 (float): Scaling factor for stage 1 to amplify the contributions of backbone features.
            b2 (float): Scaling factor for stage 2 to amplify the contributions of backbone features.
    """

    s1: float
    s2: float
    b1: float
    b2: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s1 = self.s1

        s2 = self.s2

        b1 = self.b1

        b2 = self.b2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s1": s1,
                "s2": s2,
                "b1": b1,
                "b2": b2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        s1 = d.pop("s1")

        s2 = d.pop("s2")

        b1 = d.pop("b1")

        b2 = d.pop("b2")

        free_u_config = cls(
            s1=s1,
            s2=s2,
            b1=b1,
            b2=b2,
        )

        free_u_config.additional_properties = d
        return free_u_config

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
