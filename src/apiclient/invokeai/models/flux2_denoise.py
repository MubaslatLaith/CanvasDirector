from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flux2_denoise_scheduler import FLUX2DenoiseScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.denoise_mask_field import DenoiseMaskField
    from ..models.flux_conditioning_field import FluxConditioningField
    from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField
    from ..models.latents_field import LatentsField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="FLUX2Denoise")


@_attrs_define
class FLUX2Denoise:
    """Run denoising process with a FLUX.2 Klein transformer model.

    This node is designed for FLUX.2 Klein models which use Qwen3 as the text encoder.
    It does not support ControlNet, IP-Adapters, or regional prompting.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['flux2_denoise']):  Default: 'flux2_denoise'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            latents (LatentsField | None | Unset): Latents tensor
            noise (LatentsField | None | Unset): Noise tensor
            denoise_mask (DenoiseMaskField | None | Unset): A mask of the region to apply the denoising process to. Values
                of 0.0 represent the regions to be fully denoised, and 1.0 represent the regions to be preserved.
            denoising_start (float | Unset): When to start denoising, expressed a percentage of total steps Default: 0.0.
            denoising_end (float | Unset): When to stop denoising, expressed a percentage of total steps Default: 1.0.
            add_noise (bool | Unset): Add noise based on denoising start. Default: True.
            transformer (None | TransformerField | Unset): Flux model (Transformer) to load
            positive_text_conditioning (FluxConditioningField | None | Unset): Positive conditioning tensor
            negative_text_conditioning (FluxConditioningField | None | Unset): Negative conditioning tensor. Can be None if
                cfg_scale is 1.0.
            guidance (float | Unset): Guidance strength for distilled guidance-embedding models. Inert for all current
                FLUX.2 Klein variants (their guidance_embeds weights are absent/zero); kept for node-graph compatibility and
                future guidance-embedded models. Default: 4.0.
            cfg_scale (float | Unset): Classifier-Free Guidance scale Default: 1.0.
            width (int | Unset): Width of the generated image. Default: 1024.
            height (int | Unset): Height of the generated image. Default: 1024.
            num_steps (int | Unset): Number of diffusion steps. Use 4 for distilled models, 28+ for base models. Default: 4.
            scheduler (FLUX2DenoiseScheduler | Unset): Scheduler (sampler) for the denoising process. 'euler' is fast and
                standard. 'heun' is 2nd-order (better quality, 2x slower). 'lcm' is optimized for few steps. Default:
                FLUX2DenoiseScheduler.EULER.
            seed (int | Unset): Randomness seed for reproducibility. Default: 0.
            vae (None | Unset | VAEField): FLUX.2 VAE model (required for BN statistics).
            kontext_conditioning (FluxKontextConditioningField | list[FluxKontextConditioningField] | None | Unset): FLUX
                Kontext conditioning (reference images for multi-reference image editing).
    """

    id: str
    type_: Literal["flux2_denoise"] = "flux2_denoise"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    noise: LatentsField | None | Unset = UNSET
    denoise_mask: DenoiseMaskField | None | Unset = UNSET
    denoising_start: float | Unset = 0.0
    denoising_end: float | Unset = 1.0
    add_noise: bool | Unset = True
    transformer: None | TransformerField | Unset = UNSET
    positive_text_conditioning: FluxConditioningField | None | Unset = UNSET
    negative_text_conditioning: FluxConditioningField | None | Unset = UNSET
    guidance: float | Unset = 4.0
    cfg_scale: float | Unset = 1.0
    width: int | Unset = 1024
    height: int | Unset = 1024
    num_steps: int | Unset = 4
    scheduler: FLUX2DenoiseScheduler | Unset = FLUX2DenoiseScheduler.EULER
    seed: int | Unset = 0
    vae: None | Unset | VAEField = UNSET
    kontext_conditioning: FluxKontextConditioningField | list[FluxKontextConditioningField] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.flux_conditioning_field import FluxConditioningField
        from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField
        from ..models.latents_field import LatentsField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        latents: dict[str, Any] | None | Unset
        if isinstance(self.latents, Unset):
            latents = UNSET
        elif isinstance(self.latents, LatentsField):
            latents = self.latents.to_dict()
        else:
            latents = self.latents

        noise: dict[str, Any] | None | Unset
        if isinstance(self.noise, Unset):
            noise = UNSET
        elif isinstance(self.noise, LatentsField):
            noise = self.noise.to_dict()
        else:
            noise = self.noise

        denoise_mask: dict[str, Any] | None | Unset
        if isinstance(self.denoise_mask, Unset):
            denoise_mask = UNSET
        elif isinstance(self.denoise_mask, DenoiseMaskField):
            denoise_mask = self.denoise_mask.to_dict()
        else:
            denoise_mask = self.denoise_mask

        denoising_start = self.denoising_start

        denoising_end = self.denoising_end

        add_noise = self.add_noise

        transformer: dict[str, Any] | None | Unset
        if isinstance(self.transformer, Unset):
            transformer = UNSET
        elif isinstance(self.transformer, TransformerField):
            transformer = self.transformer.to_dict()
        else:
            transformer = self.transformer

        positive_text_conditioning: dict[str, Any] | None | Unset
        if isinstance(self.positive_text_conditioning, Unset):
            positive_text_conditioning = UNSET
        elif isinstance(self.positive_text_conditioning, FluxConditioningField):
            positive_text_conditioning = self.positive_text_conditioning.to_dict()
        else:
            positive_text_conditioning = self.positive_text_conditioning

        negative_text_conditioning: dict[str, Any] | None | Unset
        if isinstance(self.negative_text_conditioning, Unset):
            negative_text_conditioning = UNSET
        elif isinstance(self.negative_text_conditioning, FluxConditioningField):
            negative_text_conditioning = self.negative_text_conditioning.to_dict()
        else:
            negative_text_conditioning = self.negative_text_conditioning

        guidance = self.guidance

        cfg_scale = self.cfg_scale

        width = self.width

        height = self.height

        num_steps = self.num_steps

        scheduler: str | Unset = UNSET
        if not isinstance(self.scheduler, Unset):
            scheduler = self.scheduler.value

        seed = self.seed

        vae: dict[str, Any] | None | Unset
        if isinstance(self.vae, Unset):
            vae = UNSET
        elif isinstance(self.vae, VAEField):
            vae = self.vae.to_dict()
        else:
            vae = self.vae

        kontext_conditioning: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.kontext_conditioning, Unset):
            kontext_conditioning = UNSET
        elif isinstance(self.kontext_conditioning, FluxKontextConditioningField):
            kontext_conditioning = self.kontext_conditioning.to_dict()
        elif isinstance(self.kontext_conditioning, list):
            kontext_conditioning = []
            for kontext_conditioning_type_1_item_data in self.kontext_conditioning:
                kontext_conditioning_type_1_item = kontext_conditioning_type_1_item_data.to_dict()
                kontext_conditioning.append(kontext_conditioning_type_1_item)

        else:
            kontext_conditioning = self.kontext_conditioning

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
        if latents is not UNSET:
            field_dict["latents"] = latents
        if noise is not UNSET:
            field_dict["noise"] = noise
        if denoise_mask is not UNSET:
            field_dict["denoise_mask"] = denoise_mask
        if denoising_start is not UNSET:
            field_dict["denoising_start"] = denoising_start
        if denoising_end is not UNSET:
            field_dict["denoising_end"] = denoising_end
        if add_noise is not UNSET:
            field_dict["add_noise"] = add_noise
        if transformer is not UNSET:
            field_dict["transformer"] = transformer
        if positive_text_conditioning is not UNSET:
            field_dict["positive_text_conditioning"] = positive_text_conditioning
        if negative_text_conditioning is not UNSET:
            field_dict["negative_text_conditioning"] = negative_text_conditioning
        if guidance is not UNSET:
            field_dict["guidance"] = guidance
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if num_steps is not UNSET:
            field_dict["num_steps"] = num_steps
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if seed is not UNSET:
            field_dict["seed"] = seed
        if vae is not UNSET:
            field_dict["vae"] = vae
        if kontext_conditioning is not UNSET:
            field_dict["kontext_conditioning"] = kontext_conditioning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.flux_conditioning_field import FluxConditioningField
        from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField
        from ..models.latents_field import LatentsField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux2_denoise"], d.pop("type"))
        if type_ != "flux2_denoise":
            raise ValueError(f"type must match const 'flux2_denoise', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

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

        def _parse_denoise_mask(data: object) -> DenoiseMaskField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                denoise_mask_type_0 = DenoiseMaskField.from_dict(data)

                return denoise_mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DenoiseMaskField | None | Unset, data)

        denoise_mask = _parse_denoise_mask(d.pop("denoise_mask", UNSET))

        denoising_start = d.pop("denoising_start", UNSET)

        denoising_end = d.pop("denoising_end", UNSET)

        add_noise = d.pop("add_noise", UNSET)

        def _parse_transformer(data: object) -> None | TransformerField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transformer_type_0 = TransformerField.from_dict(data)

                return transformer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransformerField | Unset, data)

        transformer = _parse_transformer(d.pop("transformer", UNSET))

        def _parse_positive_text_conditioning(data: object) -> FluxConditioningField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                positive_text_conditioning_type_0 = FluxConditioningField.from_dict(data)

                return positive_text_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxConditioningField | None | Unset, data)

        positive_text_conditioning = _parse_positive_text_conditioning(d.pop("positive_text_conditioning", UNSET))

        def _parse_negative_text_conditioning(data: object) -> FluxConditioningField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                negative_text_conditioning_type_0 = FluxConditioningField.from_dict(data)

                return negative_text_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxConditioningField | None | Unset, data)

        negative_text_conditioning = _parse_negative_text_conditioning(d.pop("negative_text_conditioning", UNSET))

        guidance = d.pop("guidance", UNSET)

        cfg_scale = d.pop("cfg_scale", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        num_steps = d.pop("num_steps", UNSET)

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: FLUX2DenoiseScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = FLUX2DenoiseScheduler(_scheduler)

        seed = d.pop("seed", UNSET)

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

        def _parse_kontext_conditioning(
            data: object,
        ) -> FluxKontextConditioningField | list[FluxKontextConditioningField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kontext_conditioning_type_0 = FluxKontextConditioningField.from_dict(data)

                return kontext_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kontext_conditioning_type_1 = []
                _kontext_conditioning_type_1 = data
                for kontext_conditioning_type_1_item_data in _kontext_conditioning_type_1:
                    kontext_conditioning_type_1_item = FluxKontextConditioningField.from_dict(
                        kontext_conditioning_type_1_item_data
                    )

                    kontext_conditioning_type_1.append(kontext_conditioning_type_1_item)

                return kontext_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxKontextConditioningField | list[FluxKontextConditioningField] | None | Unset, data)

        kontext_conditioning = _parse_kontext_conditioning(d.pop("kontext_conditioning", UNSET))

        flux2_denoise = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            latents=latents,
            noise=noise,
            denoise_mask=denoise_mask,
            denoising_start=denoising_start,
            denoising_end=denoising_end,
            add_noise=add_noise,
            transformer=transformer,
            positive_text_conditioning=positive_text_conditioning,
            negative_text_conditioning=negative_text_conditioning,
            guidance=guidance,
            cfg_scale=cfg_scale,
            width=width,
            height=height,
            num_steps=num_steps,
            scheduler=scheduler,
            seed=seed,
            vae=vae,
            kontext_conditioning=kontext_conditioning,
        )

        flux2_denoise.additional_properties = d
        return flux2_denoise

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
