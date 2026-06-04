from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.denoise_z_image_scheduler import DenoiseZImageScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.denoise_mask_field import DenoiseMaskField
    from ..models.latents_field import LatentsField
    from ..models.transformer_field import TransformerField
    from ..models.vae_field import VAEField
    from ..models.z_image_conditioning_field import ZImageConditioningField
    from ..models.z_image_control_field import ZImageControlField


T = TypeVar("T", bound="DenoiseZImage")


@_attrs_define
class DenoiseZImage:
    """Run the denoising process with a Z-Image model.

    Supports regional prompting by connecting multiple conditioning inputs with masks.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['z_image_denoise']):  Default: 'z_image_denoise'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            latents (LatentsField | None | Unset): Latents tensor
            noise (LatentsField | None | Unset): Noise tensor
            denoise_mask (DenoiseMaskField | None | Unset): A mask of the region to apply the denoising process to. Values
                of 0.0 represent the regions to be fully denoised, and 1.0 represent the regions to be preserved.
            denoising_start (float | Unset): When to start denoising, expressed a percentage of total steps Default: 0.0.
            denoising_end (float | Unset): When to stop denoising, expressed a percentage of total steps Default: 1.0.
            add_noise (bool | Unset): Add noise based on denoising start. Default: True.
            transformer (None | TransformerField | Unset): Z-Image model (Transformer) to load
            positive_conditioning (list[ZImageConditioningField] | None | Unset | ZImageConditioningField): Positive
                conditioning tensor
            negative_conditioning (list[ZImageConditioningField] | None | Unset | ZImageConditioningField): Negative
                conditioning tensor
            guidance_scale (float | Unset): Guidance scale for classifier-free guidance. 1.0 = no CFG (recommended for
                Z-Image-Turbo). Values > 1.0 amplify guidance. Default: 1.0.
            width (int | Unset): Width of the generated image. Default: 1024.
            height (int | Unset): Height of the generated image. Default: 1024.
            steps (int | Unset): Number of denoising steps. 8 recommended for Z-Image-Turbo. Default: 8.
            seed (int | Unset): Randomness seed for reproducibility. Default: 0.
            control (None | Unset | ZImageControlField): Z-Image control conditioning for spatial control (Canny, HED,
                Depth, Pose, MLSD).
            vae (None | Unset | VAEField): VAE Required for control conditioning.
            shift (float | None | Unset): Override the timestep shift (mu) for the sigma schedule. Leave blank to auto-
                calculate based on image dimensions (recommended). Lower values (~0.5) produce less noise shifting, higher
                values (~1.15) produce more.
            scheduler (DenoiseZImageScheduler | Unset): Scheduler (sampler) for the denoising process. Euler is the default
                and recommended. Heun is 2nd-order (better quality, 2x slower). LCM works with Turbo only (not Base). Default:
                DenoiseZImageScheduler.EULER.
    """

    id: str
    type_: Literal["z_image_denoise"] = "z_image_denoise"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    noise: LatentsField | None | Unset = UNSET
    denoise_mask: DenoiseMaskField | None | Unset = UNSET
    denoising_start: float | Unset = 0.0
    denoising_end: float | Unset = 1.0
    add_noise: bool | Unset = True
    transformer: None | TransformerField | Unset = UNSET
    positive_conditioning: list[ZImageConditioningField] | None | Unset | ZImageConditioningField = UNSET
    negative_conditioning: list[ZImageConditioningField] | None | Unset | ZImageConditioningField = UNSET
    guidance_scale: float | Unset = 1.0
    width: int | Unset = 1024
    height: int | Unset = 1024
    steps: int | Unset = 8
    seed: int | Unset = 0
    control: None | Unset | ZImageControlField = UNSET
    vae: None | Unset | VAEField = UNSET
    shift: float | None | Unset = UNSET
    scheduler: DenoiseZImageScheduler | Unset = DenoiseZImageScheduler.EULER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.latents_field import LatentsField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField
        from ..models.z_image_conditioning_field import ZImageConditioningField
        from ..models.z_image_control_field import ZImageControlField

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

        positive_conditioning: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.positive_conditioning, Unset):
            positive_conditioning = UNSET
        elif isinstance(self.positive_conditioning, ZImageConditioningField):
            positive_conditioning = self.positive_conditioning.to_dict()
        elif isinstance(self.positive_conditioning, list):
            positive_conditioning = []
            for positive_conditioning_type_1_item_data in self.positive_conditioning:
                positive_conditioning_type_1_item = positive_conditioning_type_1_item_data.to_dict()
                positive_conditioning.append(positive_conditioning_type_1_item)

        else:
            positive_conditioning = self.positive_conditioning

        negative_conditioning: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.negative_conditioning, Unset):
            negative_conditioning = UNSET
        elif isinstance(self.negative_conditioning, ZImageConditioningField):
            negative_conditioning = self.negative_conditioning.to_dict()
        elif isinstance(self.negative_conditioning, list):
            negative_conditioning = []
            for negative_conditioning_type_1_item_data in self.negative_conditioning:
                negative_conditioning_type_1_item = negative_conditioning_type_1_item_data.to_dict()
                negative_conditioning.append(negative_conditioning_type_1_item)

        else:
            negative_conditioning = self.negative_conditioning

        guidance_scale = self.guidance_scale

        width = self.width

        height = self.height

        steps = self.steps

        seed = self.seed

        control: dict[str, Any] | None | Unset
        if isinstance(self.control, Unset):
            control = UNSET
        elif isinstance(self.control, ZImageControlField):
            control = self.control.to_dict()
        else:
            control = self.control

        vae: dict[str, Any] | None | Unset
        if isinstance(self.vae, Unset):
            vae = UNSET
        elif isinstance(self.vae, VAEField):
            vae = self.vae.to_dict()
        else:
            vae = self.vae

        shift: float | None | Unset
        if isinstance(self.shift, Unset):
            shift = UNSET
        else:
            shift = self.shift

        scheduler: str | Unset = UNSET
        if not isinstance(self.scheduler, Unset):
            scheduler = self.scheduler.value

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
        if positive_conditioning is not UNSET:
            field_dict["positive_conditioning"] = positive_conditioning
        if negative_conditioning is not UNSET:
            field_dict["negative_conditioning"] = negative_conditioning
        if guidance_scale is not UNSET:
            field_dict["guidance_scale"] = guidance_scale
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if steps is not UNSET:
            field_dict["steps"] = steps
        if seed is not UNSET:
            field_dict["seed"] = seed
        if control is not UNSET:
            field_dict["control"] = control
        if vae is not UNSET:
            field_dict["vae"] = vae
        if shift is not UNSET:
            field_dict["shift"] = shift
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.latents_field import LatentsField
        from ..models.transformer_field import TransformerField
        from ..models.vae_field import VAEField
        from ..models.z_image_conditioning_field import ZImageConditioningField
        from ..models.z_image_control_field import ZImageControlField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["z_image_denoise"], d.pop("type"))
        if type_ != "z_image_denoise":
            raise ValueError(f"type must match const 'z_image_denoise', got '{type_}'")

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

        def _parse_positive_conditioning(
            data: object,
        ) -> list[ZImageConditioningField] | None | Unset | ZImageConditioningField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                positive_conditioning_type_0 = ZImageConditioningField.from_dict(data)

                return positive_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positive_conditioning_type_1 = []
                _positive_conditioning_type_1 = data
                for positive_conditioning_type_1_item_data in _positive_conditioning_type_1:
                    positive_conditioning_type_1_item = ZImageConditioningField.from_dict(
                        positive_conditioning_type_1_item_data
                    )

                    positive_conditioning_type_1.append(positive_conditioning_type_1_item)

                return positive_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ZImageConditioningField] | None | Unset | ZImageConditioningField, data)

        positive_conditioning = _parse_positive_conditioning(d.pop("positive_conditioning", UNSET))

        def _parse_negative_conditioning(
            data: object,
        ) -> list[ZImageConditioningField] | None | Unset | ZImageConditioningField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                negative_conditioning_type_0 = ZImageConditioningField.from_dict(data)

                return negative_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                negative_conditioning_type_1 = []
                _negative_conditioning_type_1 = data
                for negative_conditioning_type_1_item_data in _negative_conditioning_type_1:
                    negative_conditioning_type_1_item = ZImageConditioningField.from_dict(
                        negative_conditioning_type_1_item_data
                    )

                    negative_conditioning_type_1.append(negative_conditioning_type_1_item)

                return negative_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ZImageConditioningField] | None | Unset | ZImageConditioningField, data)

        negative_conditioning = _parse_negative_conditioning(d.pop("negative_conditioning", UNSET))

        guidance_scale = d.pop("guidance_scale", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        steps = d.pop("steps", UNSET)

        seed = d.pop("seed", UNSET)

        def _parse_control(data: object) -> None | Unset | ZImageControlField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_type_0 = ZImageControlField.from_dict(data)

                return control_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ZImageControlField, data)

        control = _parse_control(d.pop("control", UNSET))

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

        def _parse_shift(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shift = _parse_shift(d.pop("shift", UNSET))

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: DenoiseZImageScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = DenoiseZImageScheduler(_scheduler)

        denoise_z_image = cls(
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
            positive_conditioning=positive_conditioning,
            negative_conditioning=negative_conditioning,
            guidance_scale=guidance_scale,
            width=width,
            height=height,
            steps=steps,
            seed=seed,
            control=control,
            vae=vae,
            shift=shift,
            scheduler=scheduler,
        )

        denoise_z_image.additional_properties = d
        return denoise_z_image

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
