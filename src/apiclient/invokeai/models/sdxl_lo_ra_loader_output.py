from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_field import CLIPField
    from ..models.u_net_field import UNetField


T = TypeVar("T", bound="SDXLLoRALoaderOutput")


@_attrs_define
class SDXLLoRALoaderOutput:
    """SDXL LoRA Loader Output

    Attributes:
        unet (None | UNetField): UNet (scheduler, LoRAs)
        clip (CLIPField | None): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        clip2 (CLIPField | None): CLIP (tokenizer, text encoder, LoRAs) and skipped layer count
        type_ (Literal['sdxl_lora_loader_output']):  Default: 'sdxl_lora_loader_output'.
    """

    unet: None | UNetField
    clip: CLIPField | None
    clip2: CLIPField | None
    type_: Literal["sdxl_lora_loader_output"] = "sdxl_lora_loader_output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clip_field import CLIPField
        from ..models.u_net_field import UNetField

        unet: dict[str, Any] | None
        if isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        clip: dict[str, Any] | None
        if isinstance(self.clip, CLIPField):
            clip = self.clip.to_dict()
        else:
            clip = self.clip

        clip2: dict[str, Any] | None
        if isinstance(self.clip2, CLIPField):
            clip2 = self.clip2.to_dict()
        else:
            clip2 = self.clip2

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unet": unet,
                "clip": clip,
                "clip2": clip2,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_field import CLIPField
        from ..models.u_net_field import UNetField

        d = dict(src_dict)

        def _parse_unet(data: object) -> None | UNetField:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unet_type_0 = UNetField.from_dict(data)

                return unet_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UNetField, data)

        unet = _parse_unet(d.pop("unet"))

        def _parse_clip(data: object) -> CLIPField | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_type_0 = CLIPField.from_dict(data)

                return clip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None, data)

        clip = _parse_clip(d.pop("clip"))

        def _parse_clip2(data: object) -> CLIPField | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip2_type_0 = CLIPField.from_dict(data)

                return clip2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIPField | None, data)

        clip2 = _parse_clip2(d.pop("clip2"))

        type_ = cast(Literal["sdxl_lora_loader_output"], d.pop("type"))
        if type_ != "sdxl_lora_loader_output":
            raise ValueError(f"type must match const 'sdxl_lora_loader_output', got '{type_}'")

        sdxl_lo_ra_loader_output = cls(
            unet=unet,
            clip=clip,
            clip2=clip2,
            type_=type_,
        )

        sdxl_lo_ra_loader_output.additional_properties = d
        return sdxl_lo_ra_loader_output

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
