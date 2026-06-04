from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_to_latents_sd15sdxl_color_compensation import ImageToLatentsSD15SDXLColorCompensation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.vae_field import VAEField


T = TypeVar("T", bound="ImageToLatentsSD15SDXL")


@_attrs_define
class ImageToLatentsSD15SDXL:
    """Encodes an image into latents.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['i2l']):  Default: 'i2l'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The image to encode
        vae (None | Unset | VAEField): VAE
        tiled (bool | Unset): Processing using overlapping tiles (reduce memory consumption) Default: False.
        tile_size (int | Unset): The tile size for VAE tiling in pixels (image space). If set to 0, the default tile
            size for the model will be used. Larger tile sizes generally produce better results at the cost of higher memory
            usage. Default: 0.
        fp32 (bool | Unset): Whether or not to use full float32 precision Default: False.
        color_compensation (ImageToLatentsSD15SDXLColorCompensation | Unset): Apply VAE scaling compensation when
            encoding images (reduces color drift). Default: ImageToLatentsSD15SDXLColorCompensation.NONE.
    """

    id: str
    type_: Literal["i2l"] = "i2l"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    vae: None | Unset | VAEField = UNSET
    tiled: bool | Unset = False
    tile_size: int | Unset = 0
    fp32: bool | Unset = False
    color_compensation: ImageToLatentsSD15SDXLColorCompensation | Unset = ImageToLatentsSD15SDXLColorCompensation.NONE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.vae_field import VAEField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        vae: dict[str, Any] | None | Unset
        if isinstance(self.vae, Unset):
            vae = UNSET
        elif isinstance(self.vae, VAEField):
            vae = self.vae.to_dict()
        else:
            vae = self.vae

        tiled = self.tiled

        tile_size = self.tile_size

        fp32 = self.fp32

        color_compensation: str | Unset = UNSET
        if not isinstance(self.color_compensation, Unset):
            color_compensation = self.color_compensation.value

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
        if image is not UNSET:
            field_dict["image"] = image
        if vae is not UNSET:
            field_dict["vae"] = vae
        if tiled is not UNSET:
            field_dict["tiled"] = tiled
        if tile_size is not UNSET:
            field_dict["tile_size"] = tile_size
        if fp32 is not UNSET:
            field_dict["fp32"] = fp32
        if color_compensation is not UNSET:
            field_dict["color_compensation"] = color_compensation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.vae_field import VAEField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["i2l"], d.pop("type"))
        if type_ != "i2l":
            raise ValueError(f"type must match const 'i2l', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = ImageField.from_dict(data)

                return image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_vae(data: object) -> None | Unset | VAEField:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vae_type_0 = VAEField.from_dict(data)

                return vae_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VAEField, data)

        vae = _parse_vae(d.pop("vae", UNSET))

        tiled = d.pop("tiled", UNSET)

        tile_size = d.pop("tile_size", UNSET)

        fp32 = d.pop("fp32", UNSET)

        _color_compensation = d.pop("color_compensation", UNSET)
        color_compensation: ImageToLatentsSD15SDXLColorCompensation | Unset
        if isinstance(_color_compensation, Unset):
            color_compensation = UNSET
        else:
            color_compensation = ImageToLatentsSD15SDXLColorCompensation(_color_compensation)

        image_to_latents_sd15sdxl = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            vae=vae,
            tiled=tiled,
            tile_size=tile_size,
            fp32=fp32,
            color_compensation=color_compensation,
        )

        image_to_latents_sd15sdxl.additional_properties = d
        return image_to_latents_sd15sdxl

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
