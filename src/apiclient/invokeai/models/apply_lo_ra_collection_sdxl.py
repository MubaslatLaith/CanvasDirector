from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.lo_ra_field import LoRAField
    from ..models.u_net_field import UNetField


T = TypeVar("T", bound="ApplyLoRACollectionSDXL")


@_attrs_define
class ApplyLoRACollectionSDXL:
    """Applies a collection of SDXL LoRAs to the provided UNet and CLIP models.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['sdxl_lora_collection_loader']):  Default: 'sdxl_lora_collection_loader'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        loras (list[LoRAField] | LoRAField | None | Unset): LoRA models and weights. May be a single LoRA or collection.
        unet (None | UNetField | Unset): UNet (scheduler, LoRAs)
        clip (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        clip2 (CLIPField | None | Unset): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
    """

    id: str
    type_: Literal["sdxl_lora_collection_loader"] = "sdxl_lora_collection_loader"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    loras: list[LoRAField] | LoRAField | None | Unset = UNSET
    unet: None | UNetField | Unset = UNSET
    clip: CLIPField | None | Unset = UNSET
    clip2: CLIPField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField
        from ..models.lo_ra_field import LoRAField
        from ..models.u_net_field import UNetField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        loras: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.loras, Unset):
            loras = UNSET
        elif isinstance(self.loras, LoRAField):
            loras = self.loras.to_dict()
        elif isinstance(self.loras, list):
            loras = []
            for loras_type_1_item_data in self.loras:
                loras_type_1_item = loras_type_1_item_data.to_dict()
                loras.append(loras_type_1_item)

        else:
            loras = self.loras

        unet: dict[str, Any] | None | Unset
        if isinstance(self.unet, Unset):
            unet = UNSET
        elif isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        clip: dict[str, Any] | None | Unset
        if isinstance(self.clip, Unset):
            clip = UNSET
        elif isinstance(self.clip, CLIPField):
            clip = self.clip.to_dict()
        else:
            clip = self.clip

        clip2: dict[str, Any] | None | Unset
        if isinstance(self.clip2, Unset):
            clip2 = UNSET
        elif isinstance(self.clip2, CLIPField):
            clip2 = self.clip2.to_dict()
        else:
            clip2 = self.clip2

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
        if loras is not UNSET:
            field_dict["loras"] = loras
        if unet is not UNSET:
            field_dict["unet"] = unet
        if clip is not UNSET:
            field_dict["clip"] = clip
        if clip2 is not UNSET:
            field_dict["clip2"] = clip2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.lo_ra_field import LoRAField
        from ..models.u_net_field import UNetField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["sdxl_lora_collection_loader"], d.pop("type"))
        if type_ != "sdxl_lora_collection_loader":
            raise ValueError(f"type must match const 'sdxl_lora_collection_loader', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_loras(data: object) -> list[LoRAField] | LoRAField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                loras_type_0 = LoRAField.from_dict(data)

                return loras_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                loras_type_1 = []
                _loras_type_1 = data
                for loras_type_1_item_data in _loras_type_1:
                    loras_type_1_item = LoRAField.from_dict(loras_type_1_item_data)

                    loras_type_1.append(loras_type_1_item)

                return loras_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoRAField] | LoRAField | None | Unset, data)

        loras = _parse_loras(d.pop("loras", UNSET))

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

        def _parse_clip(data: object) -> CLIPField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_type_0 = CLIPField.from_dict(data)

                return clip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None | Unset, data)

        clip = _parse_clip(d.pop("clip", UNSET))

        def _parse_clip2(data: object) -> CLIPField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip2_type_0 = CLIPField.from_dict(data)

                return clip2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None | Unset, data)

        clip2 = _parse_clip2(d.pop("clip2", UNSET))

        apply_lo_ra_collection_sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            loras=loras,
            unet=unet,
            clip=clip,
            clip2=clip2,
        )

        apply_lo_ra_collection_sdxl.additional_properties = d
        return apply_lo_ra_collection_sdxl

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
