from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_dilate_or_erode_mode import ImageDilateOrErodeMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="ImageDilateOrErode")


@_attrs_define
class ImageDilateOrErode:
    """Dilate (expand) or erode (contract) an image. Originally created by @dwringer

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['invokeai_img_dilate_erode']):  Default: 'invokeai_img_dilate_erode'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The image from which to create a mask
        lightness_only (bool | Unset): If true, only applies to image lightness (CIELa*b*) Default: False.
        radius_w (int | Unset): Width (in pixels) by which to dilate(expand) or erode (contract) the image Default: 4.
        radius_h (int | Unset): Height (in pixels) by which to dilate(expand) or erode (contract) the image Default: 4.
        mode (ImageDilateOrErodeMode | Unset): How to operate on the image Default: ImageDilateOrErodeMode.DILATE.
    """

    id: str
    type_: Literal["invokeai_img_dilate_erode"] = "invokeai_img_dilate_erode"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    lightness_only: bool | Unset = False
    radius_w: int | Unset = 4
    radius_h: int | Unset = 4
    mode: ImageDilateOrErodeMode | Unset = ImageDilateOrErodeMode.DILATE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

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

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        lightness_only = self.lightness_only

        radius_w = self.radius_w

        radius_h = self.radius_h

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

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
        if image is not UNSET:
            field_dict["image"] = image
        if lightness_only is not UNSET:
            field_dict["lightness_only"] = lightness_only
        if radius_w is not UNSET:
            field_dict["radius_w"] = radius_w
        if radius_h is not UNSET:
            field_dict["radius_h"] = radius_h
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["invokeai_img_dilate_erode"], d.pop("type"))
        if type_ != "invokeai_img_dilate_erode":
            raise ValueError(f"type must match const 'invokeai_img_dilate_erode', got '{type_}'")

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

        lightness_only = d.pop("lightness_only", UNSET)

        radius_w = d.pop("radius_w", UNSET)

        radius_h = d.pop("radius_h", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: ImageDilateOrErodeMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ImageDilateOrErodeMode(_mode)

        image_dilate_or_erode = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            lightness_only=lightness_only,
            radius_w=radius_w,
            radius_h=radius_h,
            mode=mode,
        )

        image_dilate_or_erode.additional_properties = d
        return image_dilate_or_erode

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
