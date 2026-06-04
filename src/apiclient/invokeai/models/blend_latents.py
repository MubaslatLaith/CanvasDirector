from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.latents_field import LatentsField


T = TypeVar("T", bound="BlendLatents")


@_attrs_define
class BlendLatents:
    """Blend two latents using a given alpha. If a mask is provided, the second latents will be masked before blending.
    Latents must have same size. Masking functionality added by @dwringer.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['lblend']):  Default: 'lblend'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            latents_a (LatentsField | None | Unset): Latents tensor
            latents_b (LatentsField | None | Unset): Latents tensor
            mask (ImageField | None | Unset): Mask for blending in latents B
            alpha (float | Unset): Blending factor. 0.0 = use input A only, 1.0 = use input B only, 0.5 = 50% mix of input A
                and input B. Default: 0.5.
    """

    id: str
    type_: Literal["lblend"] = "lblend"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents_a: LatentsField | None | Unset = UNSET
    latents_b: LatentsField | None | Unset = UNSET
    mask: ImageField | None | Unset = UNSET
    alpha: float | Unset = 0.5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.latents_field import LatentsField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        latents_a: dict[str, Any] | None | Unset
        if isinstance(self.latents_a, Unset):
            latents_a = UNSET
        elif isinstance(self.latents_a, LatentsField):
            latents_a = self.latents_a.to_dict()
        else:
            latents_a = self.latents_a

        latents_b: dict[str, Any] | None | Unset
        if isinstance(self.latents_b, Unset):
            latents_b = UNSET
        elif isinstance(self.latents_b, LatentsField):
            latents_b = self.latents_b.to_dict()
        else:
            latents_b = self.latents_b

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, ImageField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        alpha = self.alpha

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
        if latents_a is not UNSET:
            field_dict["latents_a"] = latents_a
        if latents_b is not UNSET:
            field_dict["latents_b"] = latents_b
        if mask is not UNSET:
            field_dict["mask"] = mask
        if alpha is not UNSET:
            field_dict["alpha"] = alpha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.latents_field import LatentsField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["lblend"], d.pop("type"))
        if type_ != "lblend":
            raise ValueError(f"type must match const 'lblend', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_latents_a(data: object) -> LatentsField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latents_a_type_0 = LatentsField.from_dict(data)

                return latents_a_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LatentsField | None | Unset, data)

        latents_a = _parse_latents_a(d.pop("latents_a", UNSET))

        def _parse_latents_b(data: object) -> LatentsField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latents_b_type_0 = LatentsField.from_dict(data)

                return latents_b_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LatentsField | None | Unset, data)

        latents_b = _parse_latents_b(d.pop("latents_b", UNSET))

        def _parse_mask(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_type_0 = ImageField.from_dict(data)

                return mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))

        alpha = d.pop("alpha", UNSET)

        blend_latents = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            latents_a=latents_a,
            latents_b=latents_b,
            mask=mask,
            alpha=alpha,
        )

        blend_latents.additional_properties = d
        return blend_latents

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
