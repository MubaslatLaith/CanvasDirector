from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.latents_field import LatentsField


T = TypeVar("T", bound="CropLatents")


@_attrs_define
class CropLatents:
    """Crops a latent-space tensor to a box specified in image-space. The box dimensions and coordinates must be
    divisible by the latent scale factor of 8.

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['crop_latents']):  Default: 'crop_latents'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            latents (LatentsField | None | Unset): Latents tensor
            x (int | None | Unset): The left x coordinate (in px) of the crop rectangle in image space. This value will be
                converted to a dimension in latent space.
            y (int | None | Unset): The top y coordinate (in px) of the crop rectangle in image space. This value will be
                converted to a dimension in latent space.
            width (int | None | Unset): The width (in px) of the crop rectangle in image space. This value will be converted
                to a dimension in latent space.
            height (int | None | Unset): The height (in px) of the crop rectangle in image space. This value will be
                converted to a dimension in latent space.
    """

    id: str
    type_: Literal["crop_latents"] = "crop_latents"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    x: int | None | Unset = UNSET
    y: int | None | Unset = UNSET
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
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

        x: int | None | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: int | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

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
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latents_field import LatentsField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["crop_latents"], d.pop("type"))
        if type_ != "crop_latents":
            raise ValueError(f"type must match const 'crop_latents', got '{type_}'")

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

        def _parse_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        x = _parse_x(d.pop("x", UNSET))

        def _parse_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y = _parse_y(d.pop("y", UNSET))

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

        crop_latents = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            latents=latents,
            x=x,
            y=y,
            width=width,
            height=height,
        )

        crop_latents.additional_properties = d
        return crop_latents

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
