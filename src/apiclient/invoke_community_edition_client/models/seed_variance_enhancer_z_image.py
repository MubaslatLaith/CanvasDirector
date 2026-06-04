from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.z_image_conditioning_field import ZImageConditioningField


T = TypeVar("T", bound="SeedVarianceEnhancerZImage")


@_attrs_define
class SeedVarianceEnhancerZImage:
    """Adds seed-based noise to Z-Image conditioning to increase variance between seeds.

    Z-Image-Turbo can produce relatively similar images with different seeds,
    making it harder to explore variations of a prompt. This node implements
    reproducible, seed-based noise injection into text embeddings to increase
    visual variation while maintaining reproducibility.

    The noise strength is auto-calibrated relative to the embedding's standard
    deviation, ensuring consistent results across different prompts.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['z_image_seed_variance_enhancer']):  Default: 'z_image_seed_variance_enhancer'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            conditioning (None | Unset | ZImageConditioningField): Conditioning tensor
            seed (int | Unset): Seed for reproducible noise generation. Different seeds produce different noise patterns.
                Default: 0.
            strength (float | Unset): Noise strength as multiplier of embedding std. 0=off, 0.1=subtle, 0.5=strong. Default:
                0.1.
            randomize_percent (float | Unset): Percentage of embedding values to add noise to (1-100). Lower values create
                more selective noise patterns. Default: 50.0.
    """

    id: str
    type_: Literal["z_image_seed_variance_enhancer"] = "z_image_seed_variance_enhancer"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    conditioning: None | Unset | ZImageConditioningField = UNSET
    seed: int | Unset = 0
    strength: float | Unset = 0.1
    randomize_percent: float | Unset = 50.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.z_image_conditioning_field import ZImageConditioningField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        conditioning: dict[str, Any] | None | Unset
        if isinstance(self.conditioning, Unset):
            conditioning = UNSET
        elif isinstance(self.conditioning, ZImageConditioningField):
            conditioning = self.conditioning.to_dict()
        else:
            conditioning = self.conditioning

        seed = self.seed

        strength = self.strength

        randomize_percent = self.randomize_percent

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
        if conditioning is not UNSET:
            field_dict["conditioning"] = conditioning
        if seed is not UNSET:
            field_dict["seed"] = seed
        if strength is not UNSET:
            field_dict["strength"] = strength
        if randomize_percent is not UNSET:
            field_dict["randomize_percent"] = randomize_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.z_image_conditioning_field import ZImageConditioningField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["z_image_seed_variance_enhancer"], d.pop("type"))
        if type_ != "z_image_seed_variance_enhancer":
            raise ValueError(f"type must match const 'z_image_seed_variance_enhancer', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_conditioning(data: object) -> None | Unset | ZImageConditioningField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conditioning_type_0 = ZImageConditioningField.from_dict(data)

                return conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ZImageConditioningField, data)

        conditioning = _parse_conditioning(d.pop("conditioning", UNSET))

        seed = d.pop("seed", UNSET)

        strength = d.pop("strength", UNSET)

        randomize_percent = d.pop("randomize_percent", UNSET)

        seed_variance_enhancer_z_image = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            conditioning=conditioning,
            seed=seed,
            strength=strength,
            randomize_percent=randomize_percent,
        )

        seed_variance_enhancer_z_image.additional_properties = d
        return seed_variance_enhancer_z_image

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
