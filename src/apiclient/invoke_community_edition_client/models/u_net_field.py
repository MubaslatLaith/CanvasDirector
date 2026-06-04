from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.free_u_config import FreeUConfig
    from ..models.lo_ra_field import LoRAField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="UNetField")


@_attrs_define
class UNetField:
    """
    Attributes:
        unet (ModelIdentifierField):
        scheduler (ModelIdentifierField):
        loras (list[LoRAField]): LoRAs to apply on model loading
        seamless_axes (list[str] | Unset): Axes("x" and "y") to which apply seamless
        freeu_config (FreeUConfig | None | Unset): FreeU configuration
    """

    unet: ModelIdentifierField
    scheduler: ModelIdentifierField
    loras: list[LoRAField]
    seamless_axes: list[str] | Unset = UNSET
    freeu_config: FreeUConfig | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.free_u_config import FreeUConfig

        unet = self.unet.to_dict()

        scheduler = self.scheduler.to_dict()

        loras = []
        for loras_item_data in self.loras:
            loras_item = loras_item_data.to_dict()
            loras.append(loras_item)

        seamless_axes: list[str] | Unset = UNSET
        if not isinstance(self.seamless_axes, Unset):
            seamless_axes = self.seamless_axes

        freeu_config: dict[str, Any] | None | Unset
        if isinstance(self.freeu_config, Unset):
            freeu_config = UNSET
        elif isinstance(self.freeu_config, FreeUConfig):
            freeu_config = self.freeu_config.to_dict()
        else:
            freeu_config = self.freeu_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unet": unet,
                "scheduler": scheduler,
                "loras": loras,
            }
        )
        if seamless_axes is not UNSET:
            field_dict["seamless_axes"] = seamless_axes
        if freeu_config is not UNSET:
            field_dict["freeu_config"] = freeu_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_u_config import FreeUConfig
        from ..models.lo_ra_field import LoRAField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        unet = ModelIdentifierField.from_dict(d.pop("unet"))

        scheduler = ModelIdentifierField.from_dict(d.pop("scheduler"))

        loras = []
        _loras = d.pop("loras")
        for loras_item_data in _loras:
            loras_item = LoRAField.from_dict(loras_item_data)

            loras.append(loras_item)

        seamless_axes = cast(list[str], d.pop("seamless_axes", UNSET))

        def _parse_freeu_config(data: object) -> FreeUConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                freeu_config_type_0 = FreeUConfig.from_dict(data)

                return freeu_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FreeUConfig | None | Unset, data)

        freeu_config = _parse_freeu_config(d.pop("freeu_config", UNSET))

        u_net_field = cls(
            unet=unet,
            scheduler=scheduler,
            loras=loras,
            seamless_axes=seamless_axes,
            freeu_config=freeu_config,
        )

        u_net_field.additional_properties = d
        return u_net_field

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
