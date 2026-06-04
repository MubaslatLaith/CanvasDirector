from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.core_metadata_generation_mode_type_0 import CoreMetadataGenerationModeType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.control_net_metadata_field import ControlNetMetadataField
    from ..models.ip_adapter_metadata_field import IPAdapterMetadataField
    from ..models.lo_ra_metadata_field import LoRAMetadataField
    from ..models.model_identifier_field import ModelIdentifierField
    from ..models.t2i_adapter_metadata_field import T2IAdapterMetadataField


T = TypeVar("T", bound="CoreMetadata")


@_attrs_define
class CoreMetadata:
    """Used internally by Invoke to collect metadata for generations.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['core_metadata']):  Default: 'core_metadata'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        generation_mode (CoreMetadataGenerationModeType0 | None | Unset): The generation mode that output this image
        positive_prompt (None | str | Unset): The positive prompt parameter
        negative_prompt (None | str | Unset): The negative prompt parameter
        width (int | None | Unset): The width parameter
        height (int | None | Unset): The height parameter
        seed (int | None | Unset): The seed used for noise generation
        rand_device (None | str | Unset): The device used for random number generation
        cfg_scale (float | None | Unset): The classifier-free guidance scale parameter
        cfg_rescale_multiplier (float | None | Unset): Rescale multiplier for CFG guidance, used for models trained with
            zero-terminal SNR
        steps (int | None | Unset): The number of steps used for inference
        scheduler (None | str | Unset): The scheduler used for inference
        seamless_x (bool | None | Unset): Whether seamless tiling was used on the X axis
        seamless_y (bool | None | Unset): Whether seamless tiling was used on the Y axis
        clip_skip (int | None | Unset): The number of skipped CLIP layers
        model (ModelIdentifierField | None | Unset): The main model used for inference
        controlnets (list[ControlNetMetadataField] | None | Unset): The ControlNets used for inference
        ip_adapters (list[IPAdapterMetadataField] | None | Unset): The IP Adapters used for inference
        t_2_i_adapters (list[T2IAdapterMetadataField] | None | Unset): The IP Adapters used for inference
        loras (list[LoRAMetadataField] | None | Unset): The LoRAs used for inference
        strength (float | None | Unset): The strength used for latents-to-latents
        init_image (None | str | Unset): The name of the initial image
        vae (ModelIdentifierField | None | Unset): The VAE used for decoding, if the main model's default was not used
        qwen3_encoder (ModelIdentifierField | None | Unset): The Qwen3 text encoder model used for Z-Image inference
        hrf_enabled (bool | None | Unset): Whether or not high resolution fix was enabled.
        hrf_method (None | str | Unset): The high resolution fix upscale method.
        hrf_strength (float | None | Unset): The high resolution fix img2img strength used in the upscale pass.
        positive_style_prompt (None | str | Unset): The positive style prompt parameter
        negative_style_prompt (None | str | Unset): The negative style prompt parameter
        refiner_model (ModelIdentifierField | None | Unset): The SDXL Refiner model used
        refiner_cfg_scale (float | None | Unset): The classifier-free guidance scale parameter used for the refiner
        refiner_steps (int | None | Unset): The number of steps used for the refiner
        refiner_scheduler (None | str | Unset): The scheduler used for the refiner
        refiner_positive_aesthetic_score (float | None | Unset): The aesthetic score used for the refiner
        refiner_negative_aesthetic_score (float | None | Unset): The aesthetic score used for the refiner
        refiner_start (float | None | Unset): The start value used for refiner denoising
    """

    id: str
    type_: Literal["core_metadata"] = "core_metadata"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    generation_mode: CoreMetadataGenerationModeType0 | None | Unset = UNSET
    positive_prompt: None | str | Unset = UNSET
    negative_prompt: None | str | Unset = UNSET
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    seed: int | None | Unset = UNSET
    rand_device: None | str | Unset = UNSET
    cfg_scale: float | None | Unset = UNSET
    cfg_rescale_multiplier: float | None | Unset = UNSET
    steps: int | None | Unset = UNSET
    scheduler: None | str | Unset = UNSET
    seamless_x: bool | None | Unset = UNSET
    seamless_y: bool | None | Unset = UNSET
    clip_skip: int | None | Unset = UNSET
    model: ModelIdentifierField | None | Unset = UNSET
    controlnets: list[ControlNetMetadataField] | None | Unset = UNSET
    ip_adapters: list[IPAdapterMetadataField] | None | Unset = UNSET
    t_2_i_adapters: list[T2IAdapterMetadataField] | None | Unset = UNSET
    loras: list[LoRAMetadataField] | None | Unset = UNSET
    strength: float | None | Unset = UNSET
    init_image: None | str | Unset = UNSET
    vae: ModelIdentifierField | None | Unset = UNSET
    qwen3_encoder: ModelIdentifierField | None | Unset = UNSET
    hrf_enabled: bool | None | Unset = UNSET
    hrf_method: None | str | Unset = UNSET
    hrf_strength: float | None | Unset = UNSET
    positive_style_prompt: None | str | Unset = UNSET
    negative_style_prompt: None | str | Unset = UNSET
    refiner_model: ModelIdentifierField | None | Unset = UNSET
    refiner_cfg_scale: float | None | Unset = UNSET
    refiner_steps: int | None | Unset = UNSET
    refiner_scheduler: None | str | Unset = UNSET
    refiner_positive_aesthetic_score: float | None | Unset = UNSET
    refiner_negative_aesthetic_score: float | None | Unset = UNSET
    refiner_start: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_identifier_field import ModelIdentifierField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        generation_mode: None | str | Unset
        if isinstance(self.generation_mode, Unset):
            generation_mode = UNSET
        elif isinstance(self.generation_mode, CoreMetadataGenerationModeType0):
            generation_mode = self.generation_mode.value
        else:
            generation_mode = self.generation_mode

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

        rand_device: None | str | Unset
        if isinstance(self.rand_device, Unset):
            rand_device = UNSET
        else:
            rand_device = self.rand_device

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

        steps: int | None | Unset
        if isinstance(self.steps, Unset):
            steps = UNSET
        else:
            steps = self.steps

        scheduler: None | str | Unset
        if isinstance(self.scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = self.scheduler

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

        clip_skip: int | None | Unset
        if isinstance(self.clip_skip, Unset):
            clip_skip = UNSET
        else:
            clip_skip = self.clip_skip

        model: dict[str, Any] | None | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ModelIdentifierField):
            model = self.model.to_dict()
        else:
            model = self.model

        controlnets: list[dict[str, Any]] | None | Unset
        if isinstance(self.controlnets, Unset):
            controlnets = UNSET
        elif isinstance(self.controlnets, list):
            controlnets = []
            for controlnets_type_0_item_data in self.controlnets:
                controlnets_type_0_item = controlnets_type_0_item_data.to_dict()
                controlnets.append(controlnets_type_0_item)

        else:
            controlnets = self.controlnets

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

        t_2_i_adapters: list[dict[str, Any]] | None | Unset
        if isinstance(self.t_2_i_adapters, Unset):
            t_2_i_adapters = UNSET
        elif isinstance(self.t_2_i_adapters, list):
            t_2_i_adapters = []
            for t_2_i_adapters_type_0_item_data in self.t_2_i_adapters:
                t_2_i_adapters_type_0_item = t_2_i_adapters_type_0_item_data.to_dict()
                t_2_i_adapters.append(t_2_i_adapters_type_0_item)

        else:
            t_2_i_adapters = self.t_2_i_adapters

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

        strength: float | None | Unset
        if isinstance(self.strength, Unset):
            strength = UNSET
        else:
            strength = self.strength

        init_image: None | str | Unset
        if isinstance(self.init_image, Unset):
            init_image = UNSET
        else:
            init_image = self.init_image

        vae: dict[str, Any] | None | Unset
        if isinstance(self.vae, Unset):
            vae = UNSET
        elif isinstance(self.vae, ModelIdentifierField):
            vae = self.vae.to_dict()
        else:
            vae = self.vae

        qwen3_encoder: dict[str, Any] | None | Unset
        if isinstance(self.qwen3_encoder, Unset):
            qwen3_encoder = UNSET
        elif isinstance(self.qwen3_encoder, ModelIdentifierField):
            qwen3_encoder = self.qwen3_encoder.to_dict()
        else:
            qwen3_encoder = self.qwen3_encoder

        hrf_enabled: bool | None | Unset
        if isinstance(self.hrf_enabled, Unset):
            hrf_enabled = UNSET
        else:
            hrf_enabled = self.hrf_enabled

        hrf_method: None | str | Unset
        if isinstance(self.hrf_method, Unset):
            hrf_method = UNSET
        else:
            hrf_method = self.hrf_method

        hrf_strength: float | None | Unset
        if isinstance(self.hrf_strength, Unset):
            hrf_strength = UNSET
        else:
            hrf_strength = self.hrf_strength

        positive_style_prompt: None | str | Unset
        if isinstance(self.positive_style_prompt, Unset):
            positive_style_prompt = UNSET
        else:
            positive_style_prompt = self.positive_style_prompt

        negative_style_prompt: None | str | Unset
        if isinstance(self.negative_style_prompt, Unset):
            negative_style_prompt = UNSET
        else:
            negative_style_prompt = self.negative_style_prompt

        refiner_model: dict[str, Any] | None | Unset
        if isinstance(self.refiner_model, Unset):
            refiner_model = UNSET
        elif isinstance(self.refiner_model, ModelIdentifierField):
            refiner_model = self.refiner_model.to_dict()
        else:
            refiner_model = self.refiner_model

        refiner_cfg_scale: float | None | Unset
        if isinstance(self.refiner_cfg_scale, Unset):
            refiner_cfg_scale = UNSET
        else:
            refiner_cfg_scale = self.refiner_cfg_scale

        refiner_steps: int | None | Unset
        if isinstance(self.refiner_steps, Unset):
            refiner_steps = UNSET
        else:
            refiner_steps = self.refiner_steps

        refiner_scheduler: None | str | Unset
        if isinstance(self.refiner_scheduler, Unset):
            refiner_scheduler = UNSET
        else:
            refiner_scheduler = self.refiner_scheduler

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

        refiner_start: float | None | Unset
        if isinstance(self.refiner_start, Unset):
            refiner_start = UNSET
        else:
            refiner_start = self.refiner_start

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
        if generation_mode is not UNSET:
            field_dict["generation_mode"] = generation_mode
        if positive_prompt is not UNSET:
            field_dict["positive_prompt"] = positive_prompt
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if seed is not UNSET:
            field_dict["seed"] = seed
        if rand_device is not UNSET:
            field_dict["rand_device"] = rand_device
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if cfg_rescale_multiplier is not UNSET:
            field_dict["cfg_rescale_multiplier"] = cfg_rescale_multiplier
        if steps is not UNSET:
            field_dict["steps"] = steps
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if seamless_x is not UNSET:
            field_dict["seamless_x"] = seamless_x
        if seamless_y is not UNSET:
            field_dict["seamless_y"] = seamless_y
        if clip_skip is not UNSET:
            field_dict["clip_skip"] = clip_skip
        if model is not UNSET:
            field_dict["model"] = model
        if controlnets is not UNSET:
            field_dict["controlnets"] = controlnets
        if ip_adapters is not UNSET:
            field_dict["ipAdapters"] = ip_adapters
        if t_2_i_adapters is not UNSET:
            field_dict["t2iAdapters"] = t_2_i_adapters
        if loras is not UNSET:
            field_dict["loras"] = loras
        if strength is not UNSET:
            field_dict["strength"] = strength
        if init_image is not UNSET:
            field_dict["init_image"] = init_image
        if vae is not UNSET:
            field_dict["vae"] = vae
        if qwen3_encoder is not UNSET:
            field_dict["qwen3_encoder"] = qwen3_encoder
        if hrf_enabled is not UNSET:
            field_dict["hrf_enabled"] = hrf_enabled
        if hrf_method is not UNSET:
            field_dict["hrf_method"] = hrf_method
        if hrf_strength is not UNSET:
            field_dict["hrf_strength"] = hrf_strength
        if positive_style_prompt is not UNSET:
            field_dict["positive_style_prompt"] = positive_style_prompt
        if negative_style_prompt is not UNSET:
            field_dict["negative_style_prompt"] = negative_style_prompt
        if refiner_model is not UNSET:
            field_dict["refiner_model"] = refiner_model
        if refiner_cfg_scale is not UNSET:
            field_dict["refiner_cfg_scale"] = refiner_cfg_scale
        if refiner_steps is not UNSET:
            field_dict["refiner_steps"] = refiner_steps
        if refiner_scheduler is not UNSET:
            field_dict["refiner_scheduler"] = refiner_scheduler
        if refiner_positive_aesthetic_score is not UNSET:
            field_dict["refiner_positive_aesthetic_score"] = refiner_positive_aesthetic_score
        if refiner_negative_aesthetic_score is not UNSET:
            field_dict["refiner_negative_aesthetic_score"] = refiner_negative_aesthetic_score
        if refiner_start is not UNSET:
            field_dict["refiner_start"] = refiner_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.control_net_metadata_field import ControlNetMetadataField
        from ..models.ip_adapter_metadata_field import IPAdapterMetadataField
        from ..models.lo_ra_metadata_field import LoRAMetadataField
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.t2i_adapter_metadata_field import T2IAdapterMetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["core_metadata"], d.pop("type"))
        if type_ != "core_metadata":
            raise ValueError(f"type must match const 'core_metadata', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_generation_mode(data: object) -> CoreMetadataGenerationModeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generation_mode_type_0 = CoreMetadataGenerationModeType0(data)

                return generation_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CoreMetadataGenerationModeType0 | None | Unset, data)

        generation_mode = _parse_generation_mode(d.pop("generation_mode", UNSET))

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

        def _parse_rand_device(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rand_device = _parse_rand_device(d.pop("rand_device", UNSET))

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

        def _parse_steps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))

        def _parse_scheduler(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduler = _parse_scheduler(d.pop("scheduler", UNSET))

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

        def _parse_clip_skip(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        clip_skip = _parse_clip_skip(d.pop("clip_skip", UNSET))

        def _parse_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_0 = ModelIdentifierField.from_dict(data)

                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_controlnets(data: object) -> list[ControlNetMetadataField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                controlnets_type_0 = []
                _controlnets_type_0 = data
                for controlnets_type_0_item_data in _controlnets_type_0:
                    controlnets_type_0_item = ControlNetMetadataField.from_dict(controlnets_type_0_item_data)

                    controlnets_type_0.append(controlnets_type_0_item)

                return controlnets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ControlNetMetadataField] | None | Unset, data)

        controlnets = _parse_controlnets(d.pop("controlnets", UNSET))

        def _parse_ip_adapters(data: object) -> list[IPAdapterMetadataField] | None | Unset:
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
                    ip_adapters_type_0_item = IPAdapterMetadataField.from_dict(ip_adapters_type_0_item_data)

                    ip_adapters_type_0.append(ip_adapters_type_0_item)

                return ip_adapters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IPAdapterMetadataField] | None | Unset, data)

        ip_adapters = _parse_ip_adapters(d.pop("ipAdapters", UNSET))

        def _parse_t_2_i_adapters(data: object) -> list[T2IAdapterMetadataField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                t_2_i_adapters_type_0 = []
                _t_2_i_adapters_type_0 = data
                for t_2_i_adapters_type_0_item_data in _t_2_i_adapters_type_0:
                    t_2_i_adapters_type_0_item = T2IAdapterMetadataField.from_dict(t_2_i_adapters_type_0_item_data)

                    t_2_i_adapters_type_0.append(t_2_i_adapters_type_0_item)

                return t_2_i_adapters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[T2IAdapterMetadataField] | None | Unset, data)

        t_2_i_adapters = _parse_t_2_i_adapters(d.pop("t2iAdapters", UNSET))

        def _parse_loras(data: object) -> list[LoRAMetadataField] | None | Unset:
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
                    loras_type_0_item = LoRAMetadataField.from_dict(loras_type_0_item_data)

                    loras_type_0.append(loras_type_0_item)

                return loras_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoRAMetadataField] | None | Unset, data)

        loras = _parse_loras(d.pop("loras", UNSET))

        def _parse_strength(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        strength = _parse_strength(d.pop("strength", UNSET))

        def _parse_init_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        init_image = _parse_init_image(d.pop("init_image", UNSET))

        def _parse_vae(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vae_type_0 = ModelIdentifierField.from_dict(data)

                return vae_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        vae = _parse_vae(d.pop("vae", UNSET))

        def _parse_qwen3_encoder(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qwen3_encoder_type_0 = ModelIdentifierField.from_dict(data)

                return qwen3_encoder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        qwen3_encoder = _parse_qwen3_encoder(d.pop("qwen3_encoder", UNSET))

        def _parse_hrf_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hrf_enabled = _parse_hrf_enabled(d.pop("hrf_enabled", UNSET))

        def _parse_hrf_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hrf_method = _parse_hrf_method(d.pop("hrf_method", UNSET))

        def _parse_hrf_strength(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hrf_strength = _parse_hrf_strength(d.pop("hrf_strength", UNSET))

        def _parse_positive_style_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        positive_style_prompt = _parse_positive_style_prompt(d.pop("positive_style_prompt", UNSET))

        def _parse_negative_style_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        negative_style_prompt = _parse_negative_style_prompt(d.pop("negative_style_prompt", UNSET))

        def _parse_refiner_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                refiner_model_type_0 = ModelIdentifierField.from_dict(data)

                return refiner_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        refiner_model = _parse_refiner_model(d.pop("refiner_model", UNSET))

        def _parse_refiner_cfg_scale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refiner_cfg_scale = _parse_refiner_cfg_scale(d.pop("refiner_cfg_scale", UNSET))

        def _parse_refiner_steps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        refiner_steps = _parse_refiner_steps(d.pop("refiner_steps", UNSET))

        def _parse_refiner_scheduler(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refiner_scheduler = _parse_refiner_scheduler(d.pop("refiner_scheduler", UNSET))

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

        def _parse_refiner_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refiner_start = _parse_refiner_start(d.pop("refiner_start", UNSET))

        core_metadata = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            generation_mode=generation_mode,
            positive_prompt=positive_prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            seed=seed,
            rand_device=rand_device,
            cfg_scale=cfg_scale,
            cfg_rescale_multiplier=cfg_rescale_multiplier,
            steps=steps,
            scheduler=scheduler,
            seamless_x=seamless_x,
            seamless_y=seamless_y,
            clip_skip=clip_skip,
            model=model,
            controlnets=controlnets,
            ip_adapters=ip_adapters,
            t_2_i_adapters=t_2_i_adapters,
            loras=loras,
            strength=strength,
            init_image=init_image,
            vae=vae,
            qwen3_encoder=qwen3_encoder,
            hrf_enabled=hrf_enabled,
            hrf_method=hrf_method,
            hrf_strength=hrf_strength,
            positive_style_prompt=positive_style_prompt,
            negative_style_prompt=negative_style_prompt,
            refiner_model=refiner_model,
            refiner_cfg_scale=refiner_cfg_scale,
            refiner_steps=refiner_steps,
            refiner_scheduler=refiner_scheduler,
            refiner_positive_aesthetic_score=refiner_positive_aesthetic_score,
            refiner_negative_aesthetic_score=refiner_negative_aesthetic_score,
            refiner_start=refiner_start,
        )

        core_metadata.additional_properties = d
        return core_metadata

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
