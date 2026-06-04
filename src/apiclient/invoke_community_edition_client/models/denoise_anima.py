from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.denoise_anima_scheduler import DenoiseAnimaScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anima_conditioning_field import AnimaConditioningField
    from ..models.denoise_mask_field import DenoiseMaskField
    from ..models.latents_field import LatentsField
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="DenoiseAnima")


@_attrs_define
class DenoiseAnima:
    """Run the denoising process with an Anima model.

    Uses rectified flow sampling with shift=3.0 and the Cosmos Predict2 DiT
    backbone with integrated LLM Adapter for text conditioning.

    Supports txt2img, img2img (via latents input), and inpainting (via denoise_mask).

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['anima_denoise']):  Default: 'anima_denoise'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            latents (LatentsField | None | Unset): Latents tensor
            noise (LatentsField | None | Unset): Noise tensor
            denoise_mask (DenoiseMaskField | None | Unset): A mask of the region to apply the denoising process to. Values
                of 0.0 represent the regions to be fully denoised, and 1.0 represent the regions to be preserved.
            denoising_start (float | Unset): When to start denoising, expressed a percentage of total steps Default: 0.0.
            denoising_end (float | Unset): When to stop denoising, expressed a percentage of total steps Default: 1.0.
            add_noise (bool | Unset): Add noise based on denoising start. Default: True.
            transformer (None | TransformerField | Unset): Anima transformer model.
            positive_conditioning (AnimaConditioningField | list[AnimaConditioningField] | None | Unset): Positive
                conditioning tensor
            negative_conditioning (AnimaConditioningField | list[AnimaConditioningField] | None | Unset): Negative
                conditioning tensor
            guidance_scale (float | Unset): Guidance scale for classifier-free guidance. Recommended: 4.0-5.0 for Anima.
                Default: 4.5.
            width (int | Unset): Width of the generated image. Default: 1024.
            height (int | Unset): Height of the generated image. Default: 1024.
            steps (int | Unset): Number of denoising steps. 30 recommended for Anima. Default: 30.
            seed (int | Unset): Randomness seed for reproducibility. Default: 0.
            scheduler (DenoiseAnimaScheduler | Unset): Scheduler (sampler) for the denoising process. Default:
                DenoiseAnimaScheduler.EULER.
    """

    id: str
    type_: Literal["anima_denoise"] = "anima_denoise"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    noise: LatentsField | None | Unset = UNSET
    denoise_mask: DenoiseMaskField | None | Unset = UNSET
    denoising_start: float | Unset = 0.0
    denoising_end: float | Unset = 1.0
    add_noise: bool | Unset = True
    transformer: None | TransformerField | Unset = UNSET
    positive_conditioning: AnimaConditioningField | list[AnimaConditioningField] | None | Unset = UNSET
    negative_conditioning: AnimaConditioningField | list[AnimaConditioningField] | None | Unset = UNSET
    guidance_scale: float | Unset = 4.5
    width: int | Unset = 1024
    height: int | Unset = 1024
    steps: int | Unset = 30
    seed: int | Unset = 0
    scheduler: DenoiseAnimaScheduler | Unset = DenoiseAnimaScheduler.EULER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.anima_conditioning_field import AnimaConditioningField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.latents_field import LatentsField
        from ..models.transformer_field import TransformerField

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
        elif isinstance(self.positive_conditioning, AnimaConditioningField):
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
        elif isinstance(self.negative_conditioning, AnimaConditioningField):
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
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.anima_conditioning_field import AnimaConditioningField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.latents_field import LatentsField
        from ..models.transformer_field import TransformerField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["anima_denoise"], d.pop("type"))
        if type_ != "anima_denoise":
            raise ValueError(f"type must match const 'anima_denoise', got '{type_}'")

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
        ) -> AnimaConditioningField | list[AnimaConditioningField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                positive_conditioning_type_0 = AnimaConditioningField.from_dict(data)

                return positive_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positive_conditioning_type_1 = []
                _positive_conditioning_type_1 = data
                for positive_conditioning_type_1_item_data in _positive_conditioning_type_1:
                    positive_conditioning_type_1_item = AnimaConditioningField.from_dict(
                        positive_conditioning_type_1_item_data
                    )

                    positive_conditioning_type_1.append(positive_conditioning_type_1_item)

                return positive_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnimaConditioningField | list[AnimaConditioningField] | None | Unset, data)

        positive_conditioning = _parse_positive_conditioning(d.pop("positive_conditioning", UNSET))

        def _parse_negative_conditioning(
            data: object,
        ) -> AnimaConditioningField | list[AnimaConditioningField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                negative_conditioning_type_0 = AnimaConditioningField.from_dict(data)

                return negative_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                negative_conditioning_type_1 = []
                _negative_conditioning_type_1 = data
                for negative_conditioning_type_1_item_data in _negative_conditioning_type_1:
                    negative_conditioning_type_1_item = AnimaConditioningField.from_dict(
                        negative_conditioning_type_1_item_data
                    )

                    negative_conditioning_type_1.append(negative_conditioning_type_1_item)

                return negative_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnimaConditioningField | list[AnimaConditioningField] | None | Unset, data)

        negative_conditioning = _parse_negative_conditioning(d.pop("negative_conditioning", UNSET))

        guidance_scale = d.pop("guidance_scale", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        steps = d.pop("steps", UNSET)

        seed = d.pop("seed", UNSET)

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: DenoiseAnimaScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = DenoiseAnimaScheduler(_scheduler)

        denoise_anima = cls(
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
            scheduler=scheduler,
        )

        denoise_anima.additional_properties = d
        return denoise_anima

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
