from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.u_net_field import UNetField


T = TypeVar("T", bound="IdealSizeSD15SDXL")


@_attrs_define
class IdealSizeSD15SDXL:
    """Calculates the ideal size for generation to avoid duplication

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['ideal_size']):  Default: 'ideal_size'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        width (int | Unset): Final image width Default: 1024.
        height (int | Unset): Final image height Default: 576.
        unet (None | UNetField | Unset): UNet (scheduler, LoRAs)
        multiplier (float | Unset): Amount to multiply the model's dimensions by when calculating the ideal size (may
            result in initial generation artifacts if too large) Default: 1.0.
    """

    id: str
    type_: Literal["ideal_size"] = "ideal_size"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    width: int | Unset = 1024
    height: int | Unset = 576
    unet: None | UNetField | Unset = UNSET
    multiplier: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.u_net_field import UNetField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        width = self.width

        height = self.height

        unet: dict[str, Any] | None | Unset
        if isinstance(self.unet, Unset):
            unet = UNSET
        elif isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        multiplier = self.multiplier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if unet is not UNSET:
            field_dict["unet"] = unet
        if multiplier is not UNSET:
            field_dict["multiplier"] = multiplier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_net_field import UNetField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["ideal_size"], d.pop("type"))
        if type_ != "ideal_size":
            raise ValueError(f"type must match const 'ideal_size', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        def _parse_unet(data: object) -> None | UNetField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unet_type_0 = UNetField.from_dict(data)

                return unet_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UNetField | Unset, data)

        unet = _parse_unet(d.pop("unet", UNSET))

        multiplier = d.pop("multiplier", UNSET)

        ideal_size_sd15sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            width=width,
            height=height,
            unet=unet,
            multiplier=multiplier,
        )

        ideal_size_sd15sdxl.additional_properties = d
        return ideal_size_sd15sdxl

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
