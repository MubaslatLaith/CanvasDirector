from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flux_denoise_dype_preset import FLUXDenoiseDypePreset
from ..models.flux_denoise_scheduler import FLUXDenoiseScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.control_lo_ra_field import ControlLoRAField
    from ..models.denoise_mask_field import DenoiseMaskField
    from ..models.flux_conditioning_field import FluxConditioningField
    from ..models.flux_control_net_field import FluxControlNetField
    from ..models.flux_fill_conditioning_field import FluxFillConditioningField
    from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField
    from ..models.flux_redux_conditioning_field import FluxReduxConditioningField
    from ..models.ip_adapter_field import IPAdapterField
    from ..models.latents_field import LatentsField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="FLUXDenoise")


@_attrs_define
class FLUXDenoise:
    """Run denoising process with a FLUX transformer model.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['flux_denoise']):  Default: 'flux_denoise'.
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
        control_lora (ControlLoRAField | None | Unset): Control LoRA model to load
        positive_text_conditioning (FluxConditioningField | list[FluxConditioningField] | None | Unset): Positive
            conditioning tensor
        negative_text_conditioning (FluxConditioningField | list[FluxConditioningField] | None | Unset): Negative
            conditioning tensor. Can be None if cfg_scale is 1.0.
        redux_conditioning (FluxReduxConditioningField | list[FluxReduxConditioningField] | None | Unset): FLUX Redux
            conditioning tensor.
        fill_conditioning (FluxFillConditioningField | None | Unset): FLUX Fill conditioning.
        cfg_scale (float | list[float] | Unset): Classifier-Free Guidance scale Default: 1.0.
        cfg_scale_start_step (int | Unset): Index of the first step to apply cfg_scale. Negative indices count backwards
            from the the last step (e.g. a value of -1 refers to the final step). Default: 0.
        cfg_scale_end_step (int | Unset): Index of the last step to apply cfg_scale. Negative indices count backwards
            from the last step (e.g. a value of -1 refers to the final step). Default: -1.
        width (int | Unset): Width of the generated image. Default: 1024.
        height (int | Unset): Height of the generated image. Default: 1024.
        num_steps (int | Unset): Number of diffusion steps. Recommended values are schnell: 4, dev: 50. Default: 4.
        scheduler (FLUXDenoiseScheduler | Unset): Scheduler (sampler) for the denoising process. 'euler' is fast and
            standard. 'heun' is 2nd-order (better quality, 2x slower). 'lcm' is optimized for few steps. Default:
            FLUXDenoiseScheduler.EULER.
        guidance (float | Unset): The guidance strength. Higher values adhere more strictly to the prompt, and will
            produce less diverse images. FLUX dev only, ignored for schnell. Default: 4.0.
        seed (int | Unset): Randomness seed for reproducibility. Default: 0.
        control (FluxControlNetField | list[FluxControlNetField] | None | Unset): ControlNet models.
        controlnet_vae (None | Unset | VAEField): VAE
        ip_adapter (IPAdapterField | list[IPAdapterField] | None | Unset): IP-Adapter to apply
        kontext_conditioning (FluxKontextConditioningField | list[FluxKontextConditioningField] | None | Unset): FLUX
            Kontext conditioning (reference image).
        dype_preset (FLUXDenoiseDypePreset | Unset): DyPE preset for high-resolution generation. 'auto' enables
            automatically for resolutions > 1536px. 'area' enables automatically based on image area. '4k' uses optimized
            settings for 4K output. Default: FLUXDenoiseDypePreset.OFF.
        dype_scale (float | None | Unset): DyPE magnitude (λs). Higher values = stronger extrapolation. Only used when
            dype_preset is not 'off'.
        dype_exponent (float | None | Unset): DyPE decay speed (λt). Controls transition from low to high frequency
            detail. Only used when dype_preset is not 'off'.
    """

    id: str
    type_: Literal["flux_denoise"] = "flux_denoise"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    noise: LatentsField | None | Unset = UNSET
    denoise_mask: DenoiseMaskField | None | Unset = UNSET
    denoising_start: float | Unset = 0.0
    denoising_end: float | Unset = 1.0
    add_noise: bool | Unset = True
    transformer: None | TransformerField | Unset = UNSET
    control_lora: ControlLoRAField | None | Unset = UNSET
    positive_text_conditioning: FluxConditioningField | list[FluxConditioningField] | None | Unset = UNSET
    negative_text_conditioning: FluxConditioningField | list[FluxConditioningField] | None | Unset = UNSET
    redux_conditioning: FluxReduxConditioningField | list[FluxReduxConditioningField] | None | Unset = UNSET
    fill_conditioning: FluxFillConditioningField | None | Unset = UNSET
    cfg_scale: float | list[float] | Unset = 1.0
    cfg_scale_start_step: int | Unset = 0
    cfg_scale_end_step: int | Unset = -1
    width: int | Unset = 1024
    height: int | Unset = 1024
    num_steps: int | Unset = 4
    scheduler: FLUXDenoiseScheduler | Unset = FLUXDenoiseScheduler.EULER
    guidance: float | Unset = 4.0
    seed: int | Unset = 0
    control: FluxControlNetField | list[FluxControlNetField] | None | Unset = UNSET
    controlnet_vae: None | Unset | VAEField = UNSET
    ip_adapter: IPAdapterField | list[IPAdapterField] | None | Unset = UNSET
    kontext_conditioning: FluxKontextConditioningField | list[FluxKontextConditioningField] | None | Unset = UNSET
    dype_preset: FLUXDenoiseDypePreset | Unset = FLUXDenoiseDypePreset.OFF
    dype_scale: float | None | Unset = UNSET
    dype_exponent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.control_lo_ra_field import ControlLoRAField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.flux_conditioning_field import FluxConditioningField
        from ..models.flux_control_net_field import FluxControlNetField
        from ..models.flux_fill_conditioning_field import FluxFillConditioningField
        from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField
        from ..models.flux_redux_conditioning_field import FluxReduxConditioningField
        from ..models.ip_adapter_field import IPAdapterField
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

        control_lora: dict[str, Any] | None | Unset
        if isinstance(self.control_lora, Unset):
            control_lora = UNSET
        elif isinstance(self.control_lora, ControlLoRAField):
            control_lora = self.control_lora.to_dict()
        else:
            control_lora = self.control_lora

        positive_text_conditioning: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.positive_text_conditioning, Unset):
            positive_text_conditioning = UNSET
        elif isinstance(self.positive_text_conditioning, FluxConditioningField):
            positive_text_conditioning = self.positive_text_conditioning.to_dict()
        elif isinstance(self.positive_text_conditioning, list):
            positive_text_conditioning = []
            for positive_text_conditioning_type_1_item_data in self.positive_text_conditioning:
                positive_text_conditioning_type_1_item = positive_text_conditioning_type_1_item_data.to_dict()
                positive_text_conditioning.append(positive_text_conditioning_type_1_item)

        else:
            positive_text_conditioning = self.positive_text_conditioning

        negative_text_conditioning: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.negative_text_conditioning, Unset):
            negative_text_conditioning = UNSET
        elif isinstance(self.negative_text_conditioning, FluxConditioningField):
            negative_text_conditioning = self.negative_text_conditioning.to_dict()
        elif isinstance(self.negative_text_conditioning, list):
            negative_text_conditioning = []
            for negative_text_conditioning_type_1_item_data in self.negative_text_conditioning:
                negative_text_conditioning_type_1_item = negative_text_conditioning_type_1_item_data.to_dict()
                negative_text_conditioning.append(negative_text_conditioning_type_1_item)

        else:
            negative_text_conditioning = self.negative_text_conditioning

        redux_conditioning: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.redux_conditioning, Unset):
            redux_conditioning = UNSET
        elif isinstance(self.redux_conditioning, FluxReduxConditioningField):
            redux_conditioning = self.redux_conditioning.to_dict()
        elif isinstance(self.redux_conditioning, list):
            redux_conditioning = []
            for redux_conditioning_type_1_item_data in self.redux_conditioning:
                redux_conditioning_type_1_item = redux_conditioning_type_1_item_data.to_dict()
                redux_conditioning.append(redux_conditioning_type_1_item)

        else:
            redux_conditioning = self.redux_conditioning

        fill_conditioning: dict[str, Any] | None | Unset
        if isinstance(self.fill_conditioning, Unset):
            fill_conditioning = UNSET
        elif isinstance(self.fill_conditioning, FluxFillConditioningField):
            fill_conditioning = self.fill_conditioning.to_dict()
        else:
            fill_conditioning = self.fill_conditioning

        cfg_scale: float | list[float] | Unset
        if isinstance(self.cfg_scale, Unset):
            cfg_scale = UNSET
        elif isinstance(self.cfg_scale, list):
            cfg_scale = self.cfg_scale

        else:
            cfg_scale = self.cfg_scale

        cfg_scale_start_step = self.cfg_scale_start_step

        cfg_scale_end_step = self.cfg_scale_end_step

        width = self.width

        height = self.height

        num_steps = self.num_steps

        scheduler: str | Unset = UNSET
        if not isinstance(self.scheduler, Unset):
            scheduler = self.scheduler.value

        guidance = self.guidance

        seed = self.seed

        control: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.control, Unset):
            control = UNSET
        elif isinstance(self.control, FluxControlNetField):
            control = self.control.to_dict()
        elif isinstance(self.control, list):
            control = []
            for control_type_1_item_data in self.control:
                control_type_1_item = control_type_1_item_data.to_dict()
                control.append(control_type_1_item)

        else:
            control = self.control

        controlnet_vae: dict[str, Any] | None | Unset
        if isinstance(self.controlnet_vae, Unset):
            controlnet_vae = UNSET
        elif isinstance(self.controlnet_vae, VAEField):
            controlnet_vae = self.controlnet_vae.to_dict()
        else:
            controlnet_vae = self.controlnet_vae

        ip_adapter: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.ip_adapter, Unset):
            ip_adapter = UNSET
        elif isinstance(self.ip_adapter, IPAdapterField):
            ip_adapter = self.ip_adapter.to_dict()
        elif isinstance(self.ip_adapter, list):
            ip_adapter = []
            for ip_adapter_type_1_item_data in self.ip_adapter:
                ip_adapter_type_1_item = ip_adapter_type_1_item_data.to_dict()
                ip_adapter.append(ip_adapter_type_1_item)

        else:
            ip_adapter = self.ip_adapter

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

        dype_preset: str | Unset = UNSET
        if not isinstance(self.dype_preset, Unset):
            dype_preset = self.dype_preset.value

        dype_scale: float | None | Unset
        if isinstance(self.dype_scale, Unset):
            dype_scale = UNSET
        else:
            dype_scale = self.dype_scale

        dype_exponent: float | None | Unset
        if isinstance(self.dype_exponent, Unset):
            dype_exponent = UNSET
        else:
            dype_exponent = self.dype_exponent

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
        if control_lora is not UNSET:
            field_dict["control_lora"] = control_lora
        if positive_text_conditioning is not UNSET:
            field_dict["positive_text_conditioning"] = positive_text_conditioning
        if negative_text_conditioning is not UNSET:
            field_dict["negative_text_conditioning"] = negative_text_conditioning
        if redux_conditioning is not UNSET:
            field_dict["redux_conditioning"] = redux_conditioning
        if fill_conditioning is not UNSET:
            field_dict["fill_conditioning"] = fill_conditioning
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if cfg_scale_start_step is not UNSET:
            field_dict["cfg_scale_start_step"] = cfg_scale_start_step
        if cfg_scale_end_step is not UNSET:
            field_dict["cfg_scale_end_step"] = cfg_scale_end_step
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if num_steps is not UNSET:
            field_dict["num_steps"] = num_steps
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if guidance is not UNSET:
            field_dict["guidance"] = guidance
        if seed is not UNSET:
            field_dict["seed"] = seed
        if control is not UNSET:
            field_dict["control"] = control
        if controlnet_vae is not UNSET:
            field_dict["controlnet_vae"] = controlnet_vae
        if ip_adapter is not UNSET:
            field_dict["ip_adapter"] = ip_adapter
        if kontext_conditioning is not UNSET:
            field_dict["kontext_conditioning"] = kontext_conditioning
        if dype_preset is not UNSET:
            field_dict["dype_preset"] = dype_preset
        if dype_scale is not UNSET:
            field_dict["dype_scale"] = dype_scale
        if dype_exponent is not UNSET:
            field_dict["dype_exponent"] = dype_exponent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_lo_ra_field import ControlLoRAField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.flux_conditioning_field import FluxConditioningField
        from ..models.flux_control_net_field import FluxControlNetField
        from ..models.flux_fill_conditioning_field import FluxFillConditioningField
        from ..models.flux_kontext_conditioning_field import FluxKontextConditioningField
        from ..models.flux_redux_conditioning_field import FluxReduxConditioningField
        from ..models.ip_adapter_field import IPAdapterField
        from ..models.latents_field import LatentsField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux_denoise"], d.pop("type"))
        if type_ != "flux_denoise":
            raise ValueError(f"type must match const 'flux_denoise', got '{type_}'")

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

        def _parse_control_lora(data: object) -> ControlLoRAField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_lora_type_0 = ControlLoRAField.from_dict(data)

                return control_lora_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ControlLoRAField | None | Unset, data)

        control_lora = _parse_control_lora(d.pop("control_lora", UNSET))

        def _parse_positive_text_conditioning(
            data: object,
        ) -> FluxConditioningField | list[FluxConditioningField] | None | Unset:
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
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positive_text_conditioning_type_1 = []
                _positive_text_conditioning_type_1 = data
                for positive_text_conditioning_type_1_item_data in _positive_text_conditioning_type_1:
                    positive_text_conditioning_type_1_item = FluxConditioningField.from_dict(
                        positive_text_conditioning_type_1_item_data
                    )

                    positive_text_conditioning_type_1.append(positive_text_conditioning_type_1_item)

                return positive_text_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxConditioningField | list[FluxConditioningField] | None | Unset, data)

        positive_text_conditioning = _parse_positive_text_conditioning(d.pop("positive_text_conditioning", UNSET))

        def _parse_negative_text_conditioning(
            data: object,
        ) -> FluxConditioningField | list[FluxConditioningField] | None | Unset:
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
            try:
                if not isinstance(data, list):
                    raise TypeError()
                negative_text_conditioning_type_1 = []
                _negative_text_conditioning_type_1 = data
                for negative_text_conditioning_type_1_item_data in _negative_text_conditioning_type_1:
                    negative_text_conditioning_type_1_item = FluxConditioningField.from_dict(
                        negative_text_conditioning_type_1_item_data
                    )

                    negative_text_conditioning_type_1.append(negative_text_conditioning_type_1_item)

                return negative_text_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxConditioningField | list[FluxConditioningField] | None | Unset, data)

        negative_text_conditioning = _parse_negative_text_conditioning(d.pop("negative_text_conditioning", UNSET))

        def _parse_redux_conditioning(
            data: object,
        ) -> FluxReduxConditioningField | list[FluxReduxConditioningField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                redux_conditioning_type_0 = FluxReduxConditioningField.from_dict(data)

                return redux_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                redux_conditioning_type_1 = []
                _redux_conditioning_type_1 = data
                for redux_conditioning_type_1_item_data in _redux_conditioning_type_1:
                    redux_conditioning_type_1_item = FluxReduxConditioningField.from_dict(
                        redux_conditioning_type_1_item_data
                    )

                    redux_conditioning_type_1.append(redux_conditioning_type_1_item)

                return redux_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxReduxConditioningField | list[FluxReduxConditioningField] | None | Unset, data)

        redux_conditioning = _parse_redux_conditioning(d.pop("redux_conditioning", UNSET))

        def _parse_fill_conditioning(data: object) -> FluxFillConditioningField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fill_conditioning_type_0 = FluxFillConditioningField.from_dict(data)

                return fill_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxFillConditioningField | None | Unset, data)

        fill_conditioning = _parse_fill_conditioning(d.pop("fill_conditioning", UNSET))

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

        cfg_scale_start_step = d.pop("cfg_scale_start_step", UNSET)

        cfg_scale_end_step = d.pop("cfg_scale_end_step", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        num_steps = d.pop("num_steps", UNSET)

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: FLUXDenoiseScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = FLUXDenoiseScheduler(_scheduler)

        guidance = d.pop("guidance", UNSET)

        seed = d.pop("seed", UNSET)

        def _parse_control(data: object) -> FluxControlNetField | list[FluxControlNetField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_type_0 = FluxControlNetField.from_dict(data)

                return control_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_type_1 = []
                _control_type_1 = data
                for control_type_1_item_data in _control_type_1:
                    control_type_1_item = FluxControlNetField.from_dict(control_type_1_item_data)

                    control_type_1.append(control_type_1_item)

                return control_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FluxControlNetField | list[FluxControlNetField] | None | Unset, data)

        control = _parse_control(d.pop("control", UNSET))

        def _parse_controlnet_vae(data: object) -> None | Unset | VAEField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                controlnet_vae_type_0 = VAEField.from_dict(data)

                return controlnet_vae_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VAEField, data)

        controlnet_vae = _parse_controlnet_vae(d.pop("controlnet_vae", UNSET))

        def _parse_ip_adapter(data: object) -> IPAdapterField | list[IPAdapterField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ip_adapter_type_0 = IPAdapterField.from_dict(data)

                return ip_adapter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_adapter_type_1 = []
                _ip_adapter_type_1 = data
                for ip_adapter_type_1_item_data in _ip_adapter_type_1:
                    ip_adapter_type_1_item = IPAdapterField.from_dict(ip_adapter_type_1_item_data)

                    ip_adapter_type_1.append(ip_adapter_type_1_item)

                return ip_adapter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAdapterField | list[IPAdapterField] | None | Unset, data)

        ip_adapter = _parse_ip_adapter(d.pop("ip_adapter", UNSET))

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

        _dype_preset = d.pop("dype_preset", UNSET)
        dype_preset: FLUXDenoiseDypePreset | Unset
        if isinstance(_dype_preset, Unset):
            dype_preset = UNSET
        else:
            dype_preset = FLUXDenoiseDypePreset(_dype_preset)

        def _parse_dype_scale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dype_scale = _parse_dype_scale(d.pop("dype_scale", UNSET))

        def _parse_dype_exponent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dype_exponent = _parse_dype_exponent(d.pop("dype_exponent", UNSET))

        flux_denoise = cls(
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
            control_lora=control_lora,
            positive_text_conditioning=positive_text_conditioning,
            negative_text_conditioning=negative_text_conditioning,
            redux_conditioning=redux_conditioning,
            fill_conditioning=fill_conditioning,
            cfg_scale=cfg_scale,
            cfg_scale_start_step=cfg_scale_start_step,
            cfg_scale_end_step=cfg_scale_end_step,
            width=width,
            height=height,
            num_steps=num_steps,
            scheduler=scheduler,
            guidance=guidance,
            seed=seed,
            control=control,
            controlnet_vae=controlnet_vae,
            ip_adapter=ip_adapter,
            kontext_conditioning=kontext_conditioning,
            dype_preset=dype_preset,
            dype_scale=dype_scale,
            dype_exponent=dype_exponent,
        )

        flux_denoise.additional_properties = d
        return flux_denoise

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
