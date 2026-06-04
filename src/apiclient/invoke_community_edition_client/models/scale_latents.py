from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scale_latents_mode import ScaleLatentsMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.latents_field import LatentsField


T = TypeVar("T", bound="ScaleLatents")


@_attrs_define
class ScaleLatents:
    """Scales latents by a given factor.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['lscale']):  Default: 'lscale'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        latents (LatentsField | None | Unset): Latents tensor
        scale_factor (float | None | Unset): The factor by which to scale
        mode (ScaleLatentsMode | Unset): Interpolation mode Default: ScaleLatentsMode.BILINEAR.
        antialias (bool | Unset): Whether or not to apply antialiasing (bilinear or bicubic only) Default: False.
    """

    id: str
    type_: Literal["lscale"] = "lscale"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    scale_factor: float | None | Unset = UNSET
    mode: ScaleLatentsMode | Unset = ScaleLatentsMode.BILINEAR
    antialias: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.latents_field import LatentsField

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

        scale_factor: float | None | Unset
        if isinstance(self.scale_factor, Unset):
            scale_factor = UNSET
        else:
            scale_factor = self.scale_factor

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        antialias = self.antialias

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
        if scale_factor is not UNSET:
            field_dict["scale_factor"] = scale_factor
        if mode is not UNSET:
            field_dict["mode"] = mode
        if antialias is not UNSET:
            field_dict["antialias"] = antialias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latents_field import LatentsField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["lscale"], d.pop("type"))
        if type_ != "lscale":
            raise ValueError(f"type must match const 'lscale', got '{type_}'")

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

        def _parse_scale_factor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        scale_factor = _parse_scale_factor(d.pop("scale_factor", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: ScaleLatentsMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ScaleLatentsMode(_mode)

        antialias = d.pop("antialias", UNSET)

        scale_latents = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            latents=latents,
            scale_factor=scale_factor,
            mode=mode,
            antialias=antialias,
        )

        scale_latents.additional_properties = d
        return scale_latents

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
