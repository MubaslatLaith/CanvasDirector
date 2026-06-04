from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.control_net_recall_parameter import ControlNetRecallParameter
    from ..models.ip_adapter_recall_parameter import IPAdapterRecallParameter
    from ..models.lo_ra_recall_parameter import LoRARecallParameter
    from ..models.reference_image_recall_parameter import ReferenceImageRecallParameter


T = TypeVar("T", bound="RecallParameter")


@_attrs_define
class RecallParameter:
    """Request model for updating recallable parameters.

    Attributes:
        positive_prompt (None | str | Unset): Positive prompt text
        negative_prompt (None | str | Unset): Negative prompt text
        model (None | str | Unset): Main model name/identifier
        refiner_model (None | str | Unset): Refiner model name/identifier
        vae_model (None | str | Unset): VAE model name/identifier
        scheduler (None | str | Unset): Scheduler name
        steps (int | None | Unset): Number of generation steps
        refiner_steps (int | None | Unset): Number of refiner steps
        cfg_scale (float | None | Unset): CFG scale for guidance
        cfg_rescale_multiplier (float | None | Unset): CFG rescale multiplier
        refiner_cfg_scale (float | None | Unset): Refiner CFG scale
        guidance (float | None | Unset): Guidance scale
        width (int | None | Unset): Image width in pixels
        height (int | None | Unset): Image height in pixels
        seed (int | None | Unset): Random seed
        denoise_strength (float | None | Unset): Denoising strength
        refiner_denoise_start (float | None | Unset): Refiner denoising start
        clip_skip (int | None | Unset): CLIP skip layers
        seamless_x (bool | None | Unset): Enable seamless X tiling
        seamless_y (bool | None | Unset): Enable seamless Y tiling
        refiner_positive_aesthetic_score (float | None | Unset): Refiner positive aesthetic score
        refiner_negative_aesthetic_score (float | None | Unset): Refiner negative aesthetic score
        loras (list[LoRARecallParameter] | None | Unset): List of LoRAs with their weights
        control_layers (list[ControlNetRecallParameter] | None | Unset): List of control adapters (ControlNet, T2I
            Adapter, Control LoRA) with their settings
        ip_adapters (list[IPAdapterRecallParameter] | None | Unset): List of IP Adapters with their settings
        reference_images (list[ReferenceImageRecallParameter] | None | Unset): List of model-free reference images for
            architectures that consume reference images directly (FLUX.2 Klein, FLUX Kontext, Qwen Image Edit). The frontend
            picks the correct config type based on the currently-selected main model.
    """

    positive_prompt: None | str | Unset = UNSET
    negative_prompt: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    refiner_model: None | str | Unset = UNSET
    vae_model: None | str | Unset = UNSET
    scheduler: None | str | Unset = UNSET
    steps: int | None | Unset = UNSET
    refiner_steps: int | None | Unset = UNSET
    cfg_scale: float | None | Unset = UNSET
    cfg_rescale_multiplier: float | None | Unset = UNSET
    refiner_cfg_scale: float | None | Unset = UNSET
    guidance: float | None | Unset = UNSET
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    seed: int | None | Unset = UNSET
    denoise_strength: float | None | Unset = UNSET
    refiner_denoise_start: float | None | Unset = UNSET
    clip_skip: int | None | Unset = UNSET
    seamless_x: bool | None | Unset = UNSET
    seamless_y: bool | None | Unset = UNSET
    refiner_positive_aesthetic_score: float | None | Unset = UNSET
    refiner_negative_aesthetic_score: float | None | Unset = UNSET
    loras: list[LoRARecallParameter] | None | Unset = UNSET
    control_layers: list[ControlNetRecallParameter] | None | Unset = UNSET
    ip_adapters: list[IPAdapterRecallParameter] | None | Unset = UNSET
    reference_images: list[ReferenceImageRecallParameter] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        positive_prompt: None | str | Unset
        if isinstance(self.positive_prompt, Unset):
            positive_prompt = UNSET
        else:
            positive_prompt = self.positive_prompt

        negative_prompt: None | str | Unset
        if isinstance(self.negative_prompt, Unset):
            negative_prompt = UNSET
        else:
            negative_prompt = self.negative_prompt

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        refiner_model: None | str | Unset
        if isinstance(self.refiner_model, Unset):
            refiner_model = UNSET
        else:
            refiner_model = self.refiner_model

        vae_model: None | str | Unset
        if isinstance(self.vae_model, Unset):
            vae_model = UNSET
        else:
            vae_model = self.vae_model

        scheduler: None | str | Unset
        if isinstance(self.scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = self.scheduler

        steps: int | None | Unset
        if isinstance(self.steps, Unset):
            steps = UNSET
        else:
            steps = self.steps

        refiner_steps: int | None | Unset
        if isinstance(self.refiner_steps, Unset):
            refiner_steps = UNSET
        else:
            refiner_steps = self.refiner_steps

        cfg_scale: float | None | Unset
        if isinstance(self.cfg_scale, Unset):
            cfg_scale = UNSET
        else:
            cfg_scale = self.cfg_scale

        cfg_rescale_multiplier: float | None | Unset
        if isinstance(self.cfg_rescale_multiplier, Unset):
            cfg_rescale_multiplier = UNSET
        else:
            cfg_rescale_multiplier = self.cfg_rescale_multiplier

        refiner_cfg_scale: float | None | Unset
        if isinstance(self.refiner_cfg_scale, Unset):
            refiner_cfg_scale = UNSET
        else:
            refiner_cfg_scale = self.refiner_cfg_scale

        guidance: float | None | Unset
        if isinstance(self.guidance, Unset):
            guidance = UNSET
        else:
            guidance = self.guidance

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        seed: int | None | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        denoise_strength: float | None | Unset
        if isinstance(self.denoise_strength, Unset):
            denoise_strength = UNSET
        else:
            denoise_strength = self.denoise_strength

        refiner_denoise_start: float | None | Unset
        if isinstance(self.refiner_denoise_start, Unset):
            refiner_denoise_start = UNSET
        else:
            refiner_denoise_start = self.refiner_denoise_start

        clip_skip: int | None | Unset
        if isinstance(self.clip_skip, Unset):
            clip_skip = UNSET
        else:
            clip_skip = self.clip_skip

        seamless_x: bool | None | Unset
        if isinstance(self.seamless_x, Unset):
            seamless_x = UNSET
        else:
            seamless_x = self.seamless_x

        seamless_y: bool | None | Unset
        if isinstance(self.seamless_y, Unset):
            seamless_y = UNSET
        else:
            seamless_y = self.seamless_y

        refiner_positive_aesthetic_score: float | None | Unset
        if isinstance(self.refiner_positive_aesthetic_score, Unset):
            refiner_positive_aesthetic_score = UNSET
        else:
            refiner_positive_aesthetic_score = self.refiner_positive_aesthetic_score

        refiner_negative_aesthetic_score: float | None | Unset
        if isinstance(self.refiner_negative_aesthetic_score, Unset):
            refiner_negative_aesthetic_score = UNSET
        else:
            refiner_negative_aesthetic_score = self.refiner_negative_aesthetic_score

        loras: list[dict[str, Any]] | None | Unset
        if isinstance(self.loras, Unset):
            loras = UNSET
        elif isinstance(self.loras, list):
            loras = []
            for loras_type_0_item_data in self.loras:
                loras_type_0_item = loras_type_0_item_data.to_dict()
                loras.append(loras_type_0_item)

        else:
            loras = self.loras

        control_layers: list[dict[str, Any]] | None | Unset
        if isinstance(self.control_layers, Unset):
            control_layers = UNSET
        elif isinstance(self.control_layers, list):
            control_layers = []
            for control_layers_type_0_item_data in self.control_layers:
                control_layers_type_0_item = control_layers_type_0_item_data.to_dict()
                control_layers.append(control_layers_type_0_item)

        else:
            control_layers = self.control_layers

        ip_adapters: list[dict[str, Any]] | None | Unset
        if isinstance(self.ip_adapters, Unset):
            ip_adapters = UNSET
        elif isinstance(self.ip_adapters, list):
            ip_adapters = []
            for ip_adapters_type_0_item_data in self.ip_adapters:
                ip_adapters_type_0_item = ip_adapters_type_0_item_data.to_dict()
                ip_adapters.append(ip_adapters_type_0_item)

        else:
            ip_adapters = self.ip_adapters

        reference_images: list[dict[str, Any]] | None | Unset
        if isinstance(self.reference_images, Unset):
            reference_images = UNSET
        elif isinstance(self.reference_images, list):
            reference_images = []
            for reference_images_type_0_item_data in self.reference_images:
                reference_images_type_0_item = reference_images_type_0_item_data.to_dict()
                reference_images.append(reference_images_type_0_item)

        else:
            reference_images = self.reference_images

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if positive_prompt is not UNSET:
            field_dict["positive_prompt"] = positive_prompt
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt
        if model is not UNSET:
            field_dict["model"] = model
        if refiner_model is not UNSET:
            field_dict["refiner_model"] = refiner_model
        if vae_model is not UNSET:
            field_dict["vae_model"] = vae_model
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if steps is not UNSET:
            field_dict["steps"] = steps
        if refiner_steps is not UNSET:
            field_dict["refiner_steps"] = refiner_steps
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if cfg_rescale_multiplier is not UNSET:
            field_dict["cfg_rescale_multiplier"] = cfg_rescale_multiplier
        if refiner_cfg_scale is not UNSET:
            field_dict["refiner_cfg_scale"] = refiner_cfg_scale
        if guidance is not UNSET:
            field_dict["guidance"] = guidance
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if seed is not UNSET:
            field_dict["seed"] = seed
        if denoise_strength is not UNSET:
            field_dict["denoise_strength"] = denoise_strength
        if refiner_denoise_start is not UNSET:
            field_dict["refiner_denoise_start"] = refiner_denoise_start
        if clip_skip is not UNSET:
            field_dict["clip_skip"] = clip_skip
        if seamless_x is not UNSET:
            field_dict["seamless_x"] = seamless_x
        if seamless_y is not UNSET:
            field_dict["seamless_y"] = seamless_y
        if refiner_positive_aesthetic_score is not UNSET:
            field_dict["refiner_positive_aesthetic_score"] = refiner_positive_aesthetic_score
        if refiner_negative_aesthetic_score is not UNSET:
            field_dict["refiner_negative_aesthetic_score"] = refiner_negative_aesthetic_score
        if loras is not UNSET:
            field_dict["loras"] = loras
        if control_layers is not UNSET:
            field_dict["control_layers"] = control_layers
        if ip_adapters is not UNSET:
            field_dict["ip_adapters"] = ip_adapters
        if reference_images is not UNSET:
            field_dict["reference_images"] = reference_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_net_recall_parameter import ControlNetRecallParameter
        from ..models.ip_adapter_recall_parameter import IPAdapterRecallParameter
        from ..models.lo_ra_recall_parameter import LoRARecallParameter
        from ..models.reference_image_recall_parameter import ReferenceImageRecallParameter

        d = dict(src_dict)

        def _parse_positive_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        positive_prompt = _parse_positive_prompt(d.pop("positive_prompt", UNSET))

        def _parse_negative_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        negative_prompt = _parse_negative_prompt(d.pop("negative_prompt", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_refiner_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refiner_model = _parse_refiner_model(d.pop("refiner_model", UNSET))

        def _parse_vae_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vae_model = _parse_vae_model(d.pop("vae_model", UNSET))

        def _parse_scheduler(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduler = _parse_scheduler(d.pop("scheduler", UNSET))

        def _parse_steps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))

        def _parse_refiner_steps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        refiner_steps = _parse_refiner_steps(d.pop("refiner_steps", UNSET))

        def _parse_cfg_scale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cfg_scale = _parse_cfg_scale(d.pop("cfg_scale", UNSET))

        def _parse_cfg_rescale_multiplier(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cfg_rescale_multiplier = _parse_cfg_rescale_multiplier(d.pop("cfg_rescale_multiplier", UNSET))

        def _parse_refiner_cfg_scale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refiner_cfg_scale = _parse_refiner_cfg_scale(d.pop("refiner_cfg_scale", UNSET))

        def _parse_guidance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        guidance = _parse_guidance(d.pop("guidance", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_denoise_strength(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        denoise_strength = _parse_denoise_strength(d.pop("denoise_strength", UNSET))

        def _parse_refiner_denoise_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refiner_denoise_start = _parse_refiner_denoise_start(d.pop("refiner_denoise_start", UNSET))

        def _parse_clip_skip(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        clip_skip = _parse_clip_skip(d.pop("clip_skip", UNSET))

        def _parse_seamless_x(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        seamless_x = _parse_seamless_x(d.pop("seamless_x", UNSET))

        def _parse_seamless_y(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        seamless_y = _parse_seamless_y(d.pop("seamless_y", UNSET))

        def _parse_refiner_positive_aesthetic_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refiner_positive_aesthetic_score = _parse_refiner_positive_aesthetic_score(
            d.pop("refiner_positive_aesthetic_score", UNSET)
        )

        def _parse_refiner_negative_aesthetic_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refiner_negative_aesthetic_score = _parse_refiner_negative_aesthetic_score(
            d.pop("refiner_negative_aesthetic_score", UNSET)
        )

        def _parse_loras(data: object) -> list[LoRARecallParameter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                loras_type_0 = []
                _loras_type_0 = data
                for loras_type_0_item_data in _loras_type_0:
                    loras_type_0_item = LoRARecallParameter.from_dict(loras_type_0_item_data)

                    loras_type_0.append(loras_type_0_item)

                return loras_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoRARecallParameter] | None | Unset, data)

        loras = _parse_loras(d.pop("loras", UNSET))

        def _parse_control_layers(data: object) -> list[ControlNetRecallParameter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_layers_type_0 = []
                _control_layers_type_0 = data
                for control_layers_type_0_item_data in _control_layers_type_0:
                    control_layers_type_0_item = ControlNetRecallParameter.from_dict(control_layers_type_0_item_data)

                    control_layers_type_0.append(control_layers_type_0_item)

                return control_layers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ControlNetRecallParameter] | None | Unset, data)

        control_layers = _parse_control_layers(d.pop("control_layers", UNSET))

        def _parse_ip_adapters(data: object) -> list[IPAdapterRecallParameter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_adapters_type_0 = []
                _ip_adapters_type_0 = data
                for ip_adapters_type_0_item_data in _ip_adapters_type_0:
                    ip_adapters_type_0_item = IPAdapterRecallParameter.from_dict(ip_adapters_type_0_item_data)

                    ip_adapters_type_0.append(ip_adapters_type_0_item)

                return ip_adapters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IPAdapterRecallParameter] | None | Unset, data)

        ip_adapters = _parse_ip_adapters(d.pop("ip_adapters", UNSET))

        def _parse_reference_images(data: object) -> list[ReferenceImageRecallParameter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reference_images_type_0 = []
                _reference_images_type_0 = data
                for reference_images_type_0_item_data in _reference_images_type_0:
                    reference_images_type_0_item = ReferenceImageRecallParameter.from_dict(
                        reference_images_type_0_item_data
                    )

                    reference_images_type_0.append(reference_images_type_0_item)

                return reference_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReferenceImageRecallParameter] | None | Unset, data)

        reference_images = _parse_reference_images(d.pop("reference_images", UNSET))

        recall_parameter = cls(
            positive_prompt=positive_prompt,
            negative_prompt=negative_prompt,
            model=model,
            refiner_model=refiner_model,
            vae_model=vae_model,
            scheduler=scheduler,
            steps=steps,
            refiner_steps=refiner_steps,
            cfg_scale=cfg_scale,
            cfg_rescale_multiplier=cfg_rescale_multiplier,
            refiner_cfg_scale=refiner_cfg_scale,
            guidance=guidance,
            width=width,
            height=height,
            seed=seed,
            denoise_strength=denoise_strength,
            refiner_denoise_start=refiner_denoise_start,
            clip_skip=clip_skip,
            seamless_x=seamless_x,
            seamless_y=seamless_y,
            refiner_positive_aesthetic_score=refiner_positive_aesthetic_score,
            refiner_negative_aesthetic_score=refiner_negative_aesthetic_score,
            loras=loras,
            control_layers=control_layers,
            ip_adapters=ip_adapters,
            reference_images=reference_images,
        )

        return recall_parameter
