from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="HeuristicResize")


@_attrs_define
class HeuristicResize:
    """Resize an image using a heuristic method. Preserves edge maps.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['heuristic_resize']):  Default: 'heuristic_resize'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The image to resize
        width (int | Unset): The width to resize to (px) Default: 512.
        height (int | Unset): The height to resize to (px) Default: 512.
    """

    id: str
    type_: Literal["heuristic_resize"] = "heuristic_resize"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    width: int | Unset = 512
    height: int | Unset = 512
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

        width = self.width

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
        if image is not UNSET:
            field_dict["image"] = image
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["heuristic_resize"], d.pop("type"))
        if type_ != "heuristic_resize":
            raise ValueError(f"type must match const 'heuristic_resize', got '{type_}'")

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

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        heuristic_resize = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            width=width,
            height=height,
        )

        heuristic_resize.additional_properties = d
        return heuristic_resize

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
