from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="CenterPadOrCropImage")


@_attrs_define
class CenterPadOrCropImage:
    """Pad or crop an image's sides from the center by specified pixels. Positive values are outside of the image.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['img_pad_crop']):  Default: 'img_pad_crop'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The image to crop
        left (int | Unset): Number of pixels to pad/crop from the left (negative values crop inwards, positive values
            pad outwards) Default: 0.
        right (int | Unset): Number of pixels to pad/crop from the right (negative values crop inwards, positive values
            pad outwards) Default: 0.
        top (int | Unset): Number of pixels to pad/crop from the top (negative values crop inwards, positive values pad
            outwards) Default: 0.
        bottom (int | Unset): Number of pixels to pad/crop from the bottom (negative values crop inwards, positive
            values pad outwards) Default: 0.
    """

    id: str
    type_: Literal["img_pad_crop"] = "img_pad_crop"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    left: int | Unset = 0
    right: int | Unset = 0
    top: int | Unset = 0
    bottom: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField

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

        left = self.left

        right = self.right

        top = self.top

        bottom = self.bottom

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
        if left is not UNSET:
            field_dict["left"] = left
        if right is not UNSET:
            field_dict["right"] = right
        if top is not UNSET:
            field_dict["top"] = top
        if bottom is not UNSET:
            field_dict["bottom"] = bottom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["img_pad_crop"], d.pop("type"))
        if type_ != "img_pad_crop":
            raise ValueError(f"type must match const 'img_pad_crop', got '{type_}'")

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

        left = d.pop("left", UNSET)

        right = d.pop("right", UNSET)

        top = d.pop("top", UNSET)

        bottom = d.pop("bottom", UNSET)

        center_pad_or_crop_image = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            left=left,
            right=right,
            top=top,
            bottom=bottom,
        )

        center_pad_or_crop_image.additional_properties = d
        return center_pad_or_crop_image

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
