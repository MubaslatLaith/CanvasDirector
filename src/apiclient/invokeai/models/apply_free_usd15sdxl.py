from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.u_net_field import UNetField


T = TypeVar("T", bound="ApplyFreeUSD15SDXL")


@_attrs_define
class ApplyFreeUSD15SDXL:
    """Applies FreeU to the UNet. Suggested values (b1/b2/s1/s2):

    SD1.5: 1.2/1.4/0.9/0.2,
    SD2: 1.1/1.2/0.9/0.2,
    SDXL: 1.1/1.2/0.6/0.4,

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['freeu']):  Default: 'freeu'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            unet (None | UNetField | Unset): UNet (scheduler, LoRAs)
            b1 (float | Unset): Scaling factor for stage 1 to amplify the contributions of backbone features. Default: 1.2.
            b2 (float | Unset): Scaling factor for stage 2 to amplify the contributions of backbone features. Default: 1.4.
            s1 (float | Unset): Scaling factor for stage 1 to attenuate the contributions of the skip features. This is done
                to mitigate the "oversmoothing effect" in the enhanced denoising process. Default: 0.9.
            s2 (float | Unset): Scaling factor for stage 2 to attenuate the contributions of the skip features. This is done
                to mitigate the "oversmoothing effect" in the enhanced denoising process. Default: 0.2.
    """

    id: str
    type_: Literal["freeu"] = "freeu"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    unet: None | UNetField | Unset = UNSET
    b1: float | Unset = 1.2
    b2: float | Unset = 1.4
    s1: float | Unset = 0.9
    s2: float | Unset = 0.2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.u_net_field import UNetField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        unet: dict[str, Any] | None | Unset
        if isinstance(self.unet, Unset):
            unet = UNSET
        elif isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        b1 = self.b1

        b2 = self.b2

        s1 = self.s1

        s2 = self.s2

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
        if unet is not UNSET:
            field_dict["unet"] = unet
        if b1 is not UNSET:
            field_dict["b1"] = b1
        if b2 is not UNSET:
            field_dict["b2"] = b2
        if s1 is not UNSET:
            field_dict["s1"] = s1
        if s2 is not UNSET:
            field_dict["s2"] = s2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_net_field import UNetField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["freeu"], d.pop("type"))
        if type_ != "freeu":
            raise ValueError(f"type must match const 'freeu', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

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

        b1 = d.pop("b1", UNSET)

        b2 = d.pop("b2", UNSET)

        s1 = d.pop("s1", UNSET)

        s2 = d.pop("s2", UNSET)

        apply_free_usd15sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            unet=unet,
            b1=b1,
            b2=b2,
            s1=s1,
            s2=s2,
        )

        apply_free_usd15sdxl.additional_properties = d
        return apply_free_usd15sdxl

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
