from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_latent_noise_noise_type import CreateLatentNoiseNoiseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLatentNoise")


@_attrs_define
class CreateLatentNoise:
    """Generates latent noise for supported denoiser architectures.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['noise']):  Default: 'noise'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        noise_type (CreateLatentNoiseNoiseType | Unset): Architecture-specific noise type. Default:
            CreateLatentNoiseNoiseType.SD.
        seed (int | Unset): Seed for random number generation Default: 0.
        width (int | Unset): Width of output (px) Default: 512.
        height (int | Unset): Height of output (px) Default: 512.
        use_cpu (bool | Unset): Use CPU for noise generation (for reproducible results across platforms) Default: True.
    """

    id: str
    type_: Literal["noise"] = "noise"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    noise_type: CreateLatentNoiseNoiseType | Unset = CreateLatentNoiseNoiseType.SD
    seed: int | Unset = 0
    width: int | Unset = 512
    height: int | Unset = 512
    use_cpu: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        noise_type: str | Unset = UNSET
        if not isinstance(self.noise_type, Unset):
            noise_type = self.noise_type.value

        seed = self.seed

        width = self.width

        height = self.height

        use_cpu = self.use_cpu

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
        if noise_type is not UNSET:
            field_dict["noise_type"] = noise_type
        if seed is not UNSET:
            field_dict["seed"] = seed
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if use_cpu is not UNSET:
            field_dict["use_cpu"] = use_cpu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["noise"], d.pop("type"))
        if type_ != "noise":
            raise ValueError(f"type must match const 'noise', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _noise_type = d.pop("noise_type", UNSET)
        noise_type: CreateLatentNoiseNoiseType | Unset
        if isinstance(_noise_type, Unset):
            noise_type = UNSET
        else:
            noise_type = CreateLatentNoiseNoiseType(_noise_type)

        seed = d.pop("seed", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        use_cpu = d.pop("use_cpu", UNSET)

        create_latent_noise = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            noise_type=noise_type,
            seed=seed,
            width=width,
            height=height,
            use_cpu=use_cpu,
        )

        create_latent_noise.additional_properties = d
        return create_latent_noise

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
