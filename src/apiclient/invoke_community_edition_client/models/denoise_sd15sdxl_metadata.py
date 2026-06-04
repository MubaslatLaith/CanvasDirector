from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.denoise_sd15sdxl_metadata_scheduler import DenoiseSD15SDXLMetadataScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditioning_field import ConditioningField
    from ..models.control_field import ControlField
    from ..models.denoise_mask_field import DenoiseMaskField
    from ..models.ip_adapter_field import IPAdapterField
    from ..models.latents_field import LatentsField
    from ..models.metadata_field import MetadataField
    from ..models.t2i_adapter_field import T2IAdapterField
    from ..models.u_net_field import UNetField


T = TypeVar("T", bound="DenoiseSD15SDXLMetadata")


@_attrs_define
class DenoiseSD15SDXLMetadata:
    """
    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['denoise_latents_meta']):  Default: 'denoise_latents_meta'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        positive_conditioning (ConditioningField | list[ConditioningField] | None | Unset): Positive conditioning tensor
        negative_conditioning (ConditioningField | list[ConditioningField] | None | Unset): Negative conditioning tensor
        noise (LatentsField | None | Unset): Noise tensor
        steps (int | Unset): Number of steps to run Default: 10.
        cfg_scale (float | list[float] | Unset): Classifier-Free Guidance scale Default: 7.5.
        denoising_start (float | Unset): When to start denoising, expressed a percentage of total steps Default: 0.0.
        denoising_end (float | Unset): When to stop denoising, expressed a percentage of total steps Default: 1.0.
        scheduler (DenoiseSD15SDXLMetadataScheduler | Unset): Scheduler to use during inference Default:
            DenoiseSD15SDXLMetadataScheduler.EULER.
        unet (None | UNetField | Unset): UNet (scheduler, LoRAs)
        control (ControlField | list[ControlField] | None | Unset):
        ip_adapter (IPAdapterField | list[IPAdapterField] | None | Unset): IP-Adapter to apply
        t2i_adapter (list[T2IAdapterField] | None | T2IAdapterField | Unset): T2I-Adapter(s) to apply
        cfg_rescale_multiplier (float | Unset): Rescale multiplier for CFG guidance, used for models trained with zero-
            terminal SNR Default: 0.0.
        latents (LatentsField | None | Unset): Latents tensor
        denoise_mask (DenoiseMaskField | None | Unset): A mask of the region to apply the denoising process to. Values
            of 0.0 represent the regions to be fully denoised, and 1.0 represent the regions to be preserved.
    """

    id: str
    type_: Literal["denoise_latents_meta"] = "denoise_latents_meta"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    positive_conditioning: ConditioningField | list[ConditioningField] | None | Unset = UNSET
    negative_conditioning: ConditioningField | list[ConditioningField] | None | Unset = UNSET
    noise: LatentsField | None | Unset = UNSET
    steps: int | Unset = 10
    cfg_scale: float | list[float] | Unset = 7.5
    denoising_start: float | Unset = 0.0
    denoising_end: float | Unset = 1.0
    scheduler: DenoiseSD15SDXLMetadataScheduler | Unset = DenoiseSD15SDXLMetadataScheduler.EULER
    unet: None | UNetField | Unset = UNSET
    control: ControlField | list[ControlField] | None | Unset = UNSET
    ip_adapter: IPAdapterField | list[IPAdapterField] | None | Unset = UNSET
    t2i_adapter: list[T2IAdapterField] | None | T2IAdapterField | Unset = UNSET
    cfg_rescale_multiplier: float | Unset = 0.0
    latents: LatentsField | None | Unset = UNSET
    denoise_mask: DenoiseMaskField | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditioning_field import ConditioningField
        from ..models.control_field import ControlField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.ip_adapter_field import IPAdapterField
        from ..models.latents_field import LatentsField
        from ..models.metadata_field import MetadataField
        from ..models.t2i_adapter_field import T2IAdapterField
        from ..models.u_net_field import UNetField

        id = self.id

        type_ = self.type_

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, MetadataField):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        positive_conditioning: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.positive_conditioning, Unset):
            positive_conditioning = UNSET
        elif isinstance(self.positive_conditioning, ConditioningField):
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
        elif isinstance(self.negative_conditioning, ConditioningField):
            negative_conditioning = self.negative_conditioning.to_dict()
        elif isinstance(self.negative_conditioning, list):
            negative_conditioning = []
            for negative_conditioning_type_1_item_data in self.negative_conditioning:
                negative_conditioning_type_1_item = negative_conditioning_type_1_item_data.to_dict()
                negative_conditioning.append(negative_conditioning_type_1_item)

        else:
            negative_conditioning = self.negative_conditioning

        noise: dict[str, Any] | None | Unset
        if isinstance(self.noise, Unset):
            noise = UNSET
        elif isinstance(self.noise, LatentsField):
            noise = self.noise.to_dict()
        else:
            noise = self.noise

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

        t2i_adapter: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.t2i_adapter, Unset):
            t2i_adapter = UNSET
        elif isinstance(self.t2i_adapter, T2IAdapterField):
            t2i_adapter = self.t2i_adapter.to_dict()
        elif isinstance(self.t2i_adapter, list):
            t2i_adapter = []
            for t2i_adapter_type_1_item_data in self.t2i_adapter:
                t2i_adapter_type_1_item = t2i_adapter_type_1_item_data.to_dict()
                t2i_adapter.append(t2i_adapter_type_1_item)

        else:
            t2i_adapter = self.t2i_adapter

        cfg_rescale_multiplier = self.cfg_rescale_multiplier

        latents: dict[str, Any] | None | Unset
        if isinstance(self.latents, Unset):
            latents = UNSET
        elif isinstance(self.latents, LatentsField):
            latents = self.latents.to_dict()
        else:
            latents = self.latents

        denoise_mask: dict[str, Any] | None | Unset
        if isinstance(self.denoise_mask, Unset):
            denoise_mask = UNSET
        elif isinstance(self.denoise_mask, DenoiseMaskField):
            denoise_mask = self.denoise_mask.to_dict()
        else:
            denoise_mask = self.denoise_mask

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
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
        if control is not UNSET:
            field_dict["control"] = control
        if ip_adapter is not UNSET:
            field_dict["ip_adapter"] = ip_adapter
        if t2i_adapter is not UNSET:
            field_dict["t2i_adapter"] = t2i_adapter
        if cfg_rescale_multiplier is not UNSET:
            field_dict["cfg_rescale_multiplier"] = cfg_rescale_multiplier
        if latents is not UNSET:
            field_dict["latents"] = latents
        if denoise_mask is not UNSET:
            field_dict["denoise_mask"] = denoise_mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditioning_field import ConditioningField
        from ..models.control_field import ControlField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.ip_adapter_field import IPAdapterField
        from ..models.latents_field import LatentsField
        from ..models.metadata_field import MetadataField
        from ..models.t2i_adapter_field import T2IAdapterField
        from ..models.u_net_field import UNetField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["denoise_latents_meta"], d.pop("type"))
        if type_ != "denoise_latents_meta":
            raise ValueError(f"type must match const 'denoise_latents_meta', got '{type_}'")

        def _parse_metadata(data: object) -> MetadataField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MetadataField.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataField | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_positive_conditioning(data: object) -> ConditioningField | list[ConditioningField] | None | Unset:
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
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positive_conditioning_type_1 = []
                _positive_conditioning_type_1 = data
                for positive_conditioning_type_1_item_data in _positive_conditioning_type_1:
                    positive_conditioning_type_1_item = ConditioningField.from_dict(
                        positive_conditioning_type_1_item_data
                    )

                    positive_conditioning_type_1.append(positive_conditioning_type_1_item)

                return positive_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditioningField | list[ConditioningField] | None | Unset, data)

        positive_conditioning = _parse_positive_conditioning(d.pop("positive_conditioning", UNSET))

        def _parse_negative_conditioning(data: object) -> ConditioningField | list[ConditioningField] | None | Unset:
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
            try:
                if not isinstance(data, list):
                    raise TypeError()
                negative_conditioning_type_1 = []
                _negative_conditioning_type_1 = data
                for negative_conditioning_type_1_item_data in _negative_conditioning_type_1:
                    negative_conditioning_type_1_item = ConditioningField.from_dict(
                        negative_conditioning_type_1_item_data
                    )

                    negative_conditioning_type_1.append(negative_conditioning_type_1_item)

                return negative_conditioning_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditioningField | list[ConditioningField] | None | Unset, data)

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
        scheduler: DenoiseSD15SDXLMetadataScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = DenoiseSD15SDXLMetadataScheduler(_scheduler)

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

        def _parse_t2i_adapter(data: object) -> list[T2IAdapterField] | None | T2IAdapterField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                t2i_adapter_type_0 = T2IAdapterField.from_dict(data)

                return t2i_adapter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                t2i_adapter_type_1 = []
                _t2i_adapter_type_1 = data
                for t2i_adapter_type_1_item_data in _t2i_adapter_type_1:
                    t2i_adapter_type_1_item = T2IAdapterField.from_dict(t2i_adapter_type_1_item_data)

                    t2i_adapter_type_1.append(t2i_adapter_type_1_item)

                return t2i_adapter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[T2IAdapterField] | None | T2IAdapterField | Unset, data)

        t2i_adapter = _parse_t2i_adapter(d.pop("t2i_adapter", UNSET))

        cfg_rescale_multiplier = d.pop("cfg_rescale_multiplier", UNSET)

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

        denoise_sd15sdxl_metadata = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            positive_conditioning=positive_conditioning,
            negative_conditioning=negative_conditioning,
            noise=noise,
            steps=steps,
            cfg_scale=cfg_scale,
            denoising_start=denoising_start,
            denoising_end=denoising_end,
            scheduler=scheduler,
            unet=unet,
            control=control,
            ip_adapter=ip_adapter,
            t2i_adapter=t2i_adapter,
            cfg_rescale_multiplier=cfg_rescale_multiplier,
            latents=latents,
            denoise_mask=denoise_mask,
        )

        denoise_sd15sdxl_metadata.additional_properties = d
        return denoise_sd15sdxl_metadata

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
