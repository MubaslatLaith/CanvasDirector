from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tiled_multi_diffusion_denoise_sd15sdxl_scheduler import TiledMultiDiffusionDenoiseSD15SDXLScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditioning_field import ConditioningField
    from ..models.control_field import ControlField
    from ..models.latents_field import LatentsField
    from ..models.u_net_field import UNetField


T = TypeVar("T", bound="TiledMultiDiffusionDenoiseSD15SDXL")


@_attrs_define
class TiledMultiDiffusionDenoiseSD15SDXL:
    """Tiled Multi-Diffusion denoising.

    This node handles automatically tiling the input image, and is primarily intended for global refinement of images
    in tiled upscaling workflows. Future Multi-Diffusion nodes should allow the user to specify custom regions with
    different parameters for each region to harness the full power of Multi-Diffusion.

    This node has a similar interface to the `DenoiseLatents` node, but it has a reduced feature set (no IP-Adapter,
    T2I-Adapter, masking, etc.).

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['tiled_multi_diffusion_denoise_latents']):  Default: 'tiled_multi_diffusion_denoise_latents'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            positive_conditioning (ConditioningField | None | Unset): Positive conditioning tensor
            negative_conditioning (ConditioningField | None | Unset): Negative conditioning tensor
            noise (LatentsField | None | Unset): Noise tensor
            latents (LatentsField | None | Unset): Latents tensor
            tile_height (int | Unset): Height of the tiles in image space. Default: 1024.
            tile_width (int | Unset): Width of the tiles in image space. Default: 1024.
            tile_overlap (int | Unset): The overlap between adjacent tiles in pixel space. (Of course, tile merging is
                applied in latent space.) Tiles will be cropped during merging (if necessary) to ensure that they overlap by
                exactly this amount. Default: 32.
            steps (int | Unset): Number of steps to run Default: 18.
            cfg_scale (float | list[float] | Unset): Classifier-Free Guidance scale Default: 6.0.
            denoising_start (float | Unset): When to start denoising, expressed a percentage of total steps Default: 0.0.
            denoising_end (float | Unset): When to stop denoising, expressed a percentage of total steps Default: 1.0.
            scheduler (TiledMultiDiffusionDenoiseSD15SDXLScheduler | Unset): Scheduler to use during inference Default:
                TiledMultiDiffusionDenoiseSD15SDXLScheduler.EULER.
            unet (None | UNetField | Unset): UNet (scheduler, LoRAs)
            cfg_rescale_multiplier (float | Unset): Rescale multiplier for CFG guidance, used for models trained with zero-
                terminal SNR Default: 0.0.
            control (ControlField | list[ControlField] | None | Unset):
    """

    id: str
    type_: Literal["tiled_multi_diffusion_denoise_latents"] = "tiled_multi_diffusion_denoise_latents"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    positive_conditioning: ConditioningField | None | Unset = UNSET
    negative_conditioning: ConditioningField | None | Unset = UNSET
    noise: LatentsField | None | Unset = UNSET
    latents: LatentsField | None | Unset = UNSET
    tile_height: int | Unset = 1024
    tile_width: int | Unset = 1024
    tile_overlap: int | Unset = 32
    steps: int | Unset = 18
    cfg_scale: float | list[float] | Unset = 6.0
    denoising_start: float | Unset = 0.0
    denoising_end: float | Unset = 1.0
    scheduler: TiledMultiDiffusionDenoiseSD15SDXLScheduler | Unset = TiledMultiDiffusionDenoiseSD15SDXLScheduler.EULER
    unet: None | UNetField | Unset = UNSET
    cfg_rescale_multiplier: float | Unset = 0.0
    control: ControlField | list[ControlField] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditioning_field import ConditioningField
        from ..models.control_field import ControlField
        from ..models.latents_field import LatentsField
        from ..models.u_net_field import UNetField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        positive_conditioning: dict[str, Any] | None | Unset
        if isinstance(self.positive_conditioning, Unset):
            positive_conditioning = UNSET
        elif isinstance(self.positive_conditioning, ConditioningField):
            positive_conditioning = self.positive_conditioning.to_dict()
        else:
            positive_conditioning = self.positive_conditioning

        negative_conditioning: dict[str, Any] | None | Unset
        if isinstance(self.negative_conditioning, Unset):
            negative_conditioning = UNSET
        elif isinstance(self.negative_conditioning, ConditioningField):
            negative_conditioning = self.negative_conditioning.to_dict()
        else:
            negative_conditioning = self.negative_conditioning

        noise: dict[str, Any] | None | Unset
        if isinstance(self.noise, Unset):
            noise = UNSET
        elif isinstance(self.noise, LatentsField):
            noise = self.noise.to_dict()
        else:
            noise = self.noise

        latents: dict[str, Any] | None | Unset
        if isinstance(self.latents, Unset):
            latents = UNSET
        elif isinstance(self.latents, LatentsField):
            latents = self.latents.to_dict()
        else:
            latents = self.latents

        tile_height = self.tile_height

        tile_width = self.tile_width

        tile_overlap = self.tile_overlap

        steps = self.steps

        cfg_scale: float | list[float] | Unset
        if isinstance(self.cfg_scale, Unset):
            cfg_scale = UNSET
        elif isinstance(self.cfg_scale, list):
            cfg_scale = self.cfg_scale

        else:
            cfg_scale = self.cfg_scale

        denoising_start = self.denoising_start

        denoising_end = self.denoising_end

        scheduler: str | Unset = UNSET
        if not isinstance(self.scheduler, Unset):
            scheduler = self.scheduler.value

        unet: dict[str, Any] | None | Unset
        if isinstance(self.unet, Unset):
            unet = UNSET
        elif isinstance(self.unet, UNetField):
            unet = self.unet.to_dict()
        else:
            unet = self.unet

        cfg_rescale_multiplier = self.cfg_rescale_multiplier

        control: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.control, Unset):
            control = UNSET
        elif isinstance(self.control, ControlField):
            control = self.control.to_dict()
        elif isinstance(self.control, list):
            control = []
            for control_type_1_item_data in self.control:
                control_type_1_item = control_type_1_item_data.to_dict()
                control.append(control_type_1_item)

        else:
            control = self.control

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
        if positive_conditioning is not UNSET:
            field_dict["positive_conditioning"] = positive_conditioning
        if negative_conditioning is not UNSET:
            field_dict["negative_conditioning"] = negative_conditioning
        if noise is not UNSET:
            field_dict["noise"] = noise
        if latents is not UNSET:
            field_dict["latents"] = latents
        if tile_height is not UNSET:
            field_dict["tile_height"] = tile_height
        if tile_width is not UNSET:
            field_dict["tile_width"] = tile_width
        if tile_overlap is not UNSET:
            field_dict["tile_overlap"] = tile_overlap
        if steps is not UNSET:
            field_dict["steps"] = steps
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if denoising_start is not UNSET:
            field_dict["denoising_start"] = denoising_start
        if denoising_end is not UNSET:
            field_dict["denoising_end"] = denoising_end
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if unet is not UNSET:
            field_dict["unet"] = unet
        if cfg_rescale_multiplier is not UNSET:
            field_dict["cfg_rescale_multiplier"] = cfg_rescale_multiplier
        if control is not UNSET:
            field_dict["control"] = control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditioning_field import ConditioningField
        from ..models.control_field import ControlField
        from ..models.latents_field import LatentsField
        from ..models.u_net_field import UNetField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["tiled_multi_diffusion_denoise_latents"], d.pop("type"))
        if type_ != "tiled_multi_diffusion_denoise_latents":
            raise ValueError(f"type must match const 'tiled_multi_diffusion_denoise_latents', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_positive_conditioning(data: object) -> ConditioningField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                positive_conditioning_type_0 = ConditioningField.from_dict(data)

                return positive_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditioningField | None | Unset, data)

        positive_conditioning = _parse_positive_conditioning(d.pop("positive_conditioning", UNSET))

        def _parse_negative_conditioning(data: object) -> ConditioningField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                negative_conditioning_type_0 = ConditioningField.from_dict(data)

                return negative_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditioningField | None | Unset, data)

        negative_conditioning = _parse_negative_conditioning(d.pop("negative_conditioning", UNSET))

        def _parse_noise(data: object) -> LatentsField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                noise_type_0 = LatentsField.from_dict(data)

                return noise_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LatentsField | None | Unset, data)

        noise = _parse_noise(d.pop("noise", UNSET))

        def _parse_latents(data: object) -> LatentsField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latents_type_0 = LatentsField.from_dict(data)

                return latents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LatentsField | None | Unset, data)

        latents = _parse_latents(d.pop("latents", UNSET))

        tile_height = d.pop("tile_height", UNSET)

        tile_width = d.pop("tile_width", UNSET)

        tile_overlap = d.pop("tile_overlap", UNSET)

        steps = d.pop("steps", UNSET)

        def _parse_cfg_scale(data: object) -> float | list[float] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cfg_scale_type_1 = cast(list[float], data)

                return cfg_scale_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | list[float] | Unset, data)

        cfg_scale = _parse_cfg_scale(d.pop("cfg_scale", UNSET))

        denoising_start = d.pop("denoising_start", UNSET)

        denoising_end = d.pop("denoising_end", UNSET)

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: TiledMultiDiffusionDenoiseSD15SDXLScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = TiledMultiDiffusionDenoiseSD15SDXLScheduler(_scheduler)

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

        cfg_rescale_multiplier = d.pop("cfg_rescale_multiplier", UNSET)

        def _parse_control(data: object) -> ControlField | list[ControlField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_type_0 = ControlField.from_dict(data)

                return control_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_type_1 = []
                _control_type_1 = data
                for control_type_1_item_data in _control_type_1:
                    control_type_1_item = ControlField.from_dict(control_type_1_item_data)

                    control_type_1.append(control_type_1_item)

                return control_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlField | list[ControlField] | None | Unset, data)

        control = _parse_control(d.pop("control", UNSET))

        tiled_multi_diffusion_denoise_sd15sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            positive_conditioning=positive_conditioning,
            negative_conditioning=negative_conditioning,
            noise=noise,
            latents=latents,
            tile_height=tile_height,
            tile_width=tile_width,
            tile_overlap=tile_overlap,
            steps=steps,
            cfg_scale=cfg_scale,
            denoising_start=denoising_start,
            denoising_end=denoising_end,
            scheduler=scheduler,
            unet=unet,
            cfg_rescale_multiplier=cfg_rescale_multiplier,
            control=control,
        )

        tiled_multi_diffusion_denoise_sd15sdxl.additional_properties = d
        return tiled_multi_diffusion_denoise_sd15sdxl

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
