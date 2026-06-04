from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_gradient_mask_coherence_mode import CreateGradientMaskCoherenceMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.u_net_field import UNetField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="CreateGradientMask")


@_attrs_define
class CreateGradientMask:
    """Creates mask for denoising.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['create_gradient_mask']):  Default: 'create_gradient_mask'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        mask (ImageField | None | Unset): Image which will be masked
        edge_radius (int | Unset): How far to expand the edges of the mask Default: 16.
        coherence_mode (CreateGradientMaskCoherenceMode | Unset):  Default:
            CreateGradientMaskCoherenceMode.GAUSSIAN_BLUR.
        minimum_denoise (float | Unset): Minimum denoise level for the coherence region Default: 0.0.
        image (ImageField | None | Unset): OPTIONAL: Only connect for specialized Inpainting models, masked_latents will
            be generated from the image with the VAE
        unet (None | UNetField | Unset): OPTIONAL: If the Unet is a specialized Inpainting model, masked_latents will be
            generated from the image with the VAE
        vae (None | Unset | VAEField): OPTIONAL: Only connect for specialized Inpainting models, masked_latents will be
            generated from the image with the VAE
        tiled (bool | Unset): Processing using overlapping tiles (reduce memory consumption) Default: False.
        fp32 (bool | Unset): Whether or not to use full float32 precision Default: False.
    """

    id: str
    type_: Literal["create_gradient_mask"] = "create_gradient_mask"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    mask: ImageField | None | Unset = UNSET
    edge_radius: int | Unset = 16
    coherence_mode: CreateGradientMaskCoherenceMode | Unset = CreateGradientMaskCoherenceMode.GAUSSIAN_BLUR
    minimum_denoise: float | Unset = 0.0
    image: ImageField | None | Unset = UNSET
    unet: None | UNetField | Unset = UNSET
    vae: None | Unset | VAEField = UNSET
    tiled: bool | Unset = False
    fp32: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, ImageField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        edge_radius = self.edge_radius

        coherence_mode: str | Unset = UNSET
        if not isinstance(self.coherence_mode, Unset):
            coherence_mode = self.coherence_mode.value

        minimum_denoise = self.minimum_denoise

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        unet: dict[str, Any] | None | Unset
        if isinstance(self.unet, Unset):
            unet = UNSET
        elif isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        vae: dict[str, Any] | None | Unset
        if isinstance(self.vae, Unset):
            vae = UNSET
        elif isinstance(self.vae, VAEField):
            vae = self.vae.to_dict()
        else:
            vae = self.vae

        tiled = self.tiled

        fp32 = self.fp32

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
        if mask is not UNSET:
            field_dict["mask"] = mask
        if edge_radius is not UNSET:
            field_dict["edge_radius"] = edge_radius
        if coherence_mode is not UNSET:
            field_dict["coherence_mode"] = coherence_mode
        if minimum_denoise is not UNSET:
            field_dict["minimum_denoise"] = minimum_denoise
        if image is not UNSET:
            field_dict["image"] = image
        if unet is not UNSET:
            field_dict["unet"] = unet
        if vae is not UNSET:
            field_dict["vae"] = vae
        if tiled is not UNSET:
            field_dict["tiled"] = tiled
        if fp32 is not UNSET:
            field_dict["fp32"] = fp32

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.u_net_field import UNetField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["create_gradient_mask"], d.pop("type"))
        if type_ != "create_gradient_mask":
            raise ValueError(f"type must match const 'create_gradient_mask', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_mask(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_type_0 = ImageField.from_dict(data)

                return mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))

        edge_radius = d.pop("edge_radius", UNSET)

        _coherence_mode = d.pop("coherence_mode", UNSET)
        coherence_mode: CreateGradientMaskCoherenceMode | Unset
        if isinstance(_coherence_mode, Unset):
            coherence_mode = UNSET
        else:
            coherence_mode = CreateGradientMaskCoherenceMode(_coherence_mode)

        minimum_denoise = d.pop("minimum_denoise", UNSET)

        def _parse_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = ImageField.from_dict(data)

                return image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

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

        def _parse_vae(data: object) -> None | Unset | VAEField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vae_type_0 = VAEField.from_dict(data)

                return vae_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VAEField, data)

        vae = _parse_vae(d.pop("vae", UNSET))

        tiled = d.pop("tiled", UNSET)

        fp32 = d.pop("fp32", UNSET)

        create_gradient_mask = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            mask=mask,
            edge_radius=edge_radius,
            coherence_mode=coherence_mode,
            minimum_denoise=minimum_denoise,
            image=image,
            unet=unet,
            vae=vae,
            tiled=tiled,
            fp32=fp32,
        )

        create_gradient_mask.additional_properties = d
        return create_gradient_mask

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
