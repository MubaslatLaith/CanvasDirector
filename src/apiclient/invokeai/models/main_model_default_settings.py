from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.main_model_default_settings_scheduler_type_0 import MainModelDefaultSettingsSchedulerType0
from ..models.main_model_default_settings_vae_precision_type_0 import MainModelDefaultSettingsVaePrecisionType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="MainModelDefaultSettings")


@_attrs_define
class MainModelDefaultSettings:
    """
    Attributes:
        vae (None | str | Unset): Default VAE for this model (model key)
        vae_precision (MainModelDefaultSettingsVaePrecisionType0 | None | Unset): Default VAE precision for this model
        scheduler (MainModelDefaultSettingsSchedulerType0 | None | Unset): Default scheduler for this model
        steps (int | None | Unset): Default number of steps for this model
        cfg_scale (float | None | Unset): Default CFG Scale for this model
        cfg_rescale_multiplier (float | None | Unset): Default CFG Rescale Multiplier for this model
        width (int | None | Unset): Default width for this model
        height (int | None | Unset): Default height for this model
        guidance (float | None | Unset): Default Guidance for this model
        cpu_only (bool | None | Unset): Whether this model should run on CPU only
        fp8_storage (bool | None | Unset): Store weights in FP8 to reduce VRAM usage (~50% savings). Weights are cast to
            compute dtype during inference.
    """

    vae: None | str | Unset = UNSET
    vae_precision: MainModelDefaultSettingsVaePrecisionType0 | None | Unset = UNSET
    scheduler: MainModelDefaultSettingsSchedulerType0 | None | Unset = UNSET
    steps: int | None | Unset = UNSET
    cfg_scale: float | None | Unset = UNSET
    cfg_rescale_multiplier: float | None | Unset = UNSET
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    guidance: float | None | Unset = UNSET
    cpu_only: bool | None | Unset = UNSET
    fp8_storage: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vae: None | str | Unset
        if isinstance(self.vae, Unset):
            vae = UNSET
        else:
            vae = self.vae

        vae_precision: None | str | Unset
        if isinstance(self.vae_precision, Unset):
            vae_precision = UNSET
        elif isinstance(self.vae_precision, MainModelDefaultSettingsVaePrecisionType0):
            vae_precision = self.vae_precision.value
        else:
            vae_precision = self.vae_precision

        scheduler: None | str | Unset
        if isinstance(self.scheduler, Unset):
            scheduler = UNSET
        elif isinstance(self.scheduler, MainModelDefaultSettingsSchedulerType0):
            scheduler = self.scheduler.value
        else:
            scheduler = self.scheduler

        steps: int | None | Unset
        if isinstance(self.steps, Unset):
            steps = UNSET
        else:
            steps = self.steps

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

        guidance: float | None | Unset
        if isinstance(self.guidance, Unset):
            guidance = UNSET
        else:
            guidance = self.guidance

        cpu_only: bool | None | Unset
        if isinstance(self.cpu_only, Unset):
            cpu_only = UNSET
        else:
            cpu_only = self.cpu_only

        fp8_storage: bool | None | Unset
        if isinstance(self.fp8_storage, Unset):
            fp8_storage = UNSET
        else:
            fp8_storage = self.fp8_storage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if vae is not UNSET:
            field_dict["vae"] = vae
        if vae_precision is not UNSET:
            field_dict["vae_precision"] = vae_precision
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if steps is not UNSET:
            field_dict["steps"] = steps
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if cfg_rescale_multiplier is not UNSET:
            field_dict["cfg_rescale_multiplier"] = cfg_rescale_multiplier
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if guidance is not UNSET:
            field_dict["guidance"] = guidance
        if cpu_only is not UNSET:
            field_dict["cpu_only"] = cpu_only
        if fp8_storage is not UNSET:
            field_dict["fp8_storage"] = fp8_storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_vae(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vae = _parse_vae(d.pop("vae", UNSET))

        def _parse_vae_precision(data: object) -> MainModelDefaultSettingsVaePrecisionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vae_precision_type_0 = MainModelDefaultSettingsVaePrecisionType0(data)

                return vae_precision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MainModelDefaultSettingsVaePrecisionType0 | None | Unset, data)

        vae_precision = _parse_vae_precision(d.pop("vae_precision", UNSET))

        def _parse_scheduler(data: object) -> MainModelDefaultSettingsSchedulerType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduler_type_0 = MainModelDefaultSettingsSchedulerType0(data)

                return scheduler_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MainModelDefaultSettingsSchedulerType0 | None | Unset, data)

        scheduler = _parse_scheduler(d.pop("scheduler", UNSET))

        def _parse_steps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        steps = _parse_steps(d.pop("steps", UNSET))

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

        def _parse_guidance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        guidance = _parse_guidance(d.pop("guidance", UNSET))

        def _parse_cpu_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cpu_only = _parse_cpu_only(d.pop("cpu_only", UNSET))

        def _parse_fp8_storage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fp8_storage = _parse_fp8_storage(d.pop("fp8_storage", UNSET))

        main_model_default_settings = cls(
            vae=vae,
            vae_precision=vae_precision,
            scheduler=scheduler,
            steps=steps,
            cfg_scale=cfg_scale,
            cfg_rescale_multiplier=cfg_rescale_multiplier,
            width=width,
            height=height,
            guidance=guidance,
            cpu_only=cpu_only,
            fp8_storage=fp8_storage,
        )

        return main_model_default_settings
