from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="FaceMask")


@_attrs_define
class FaceMask:
    """Face mask creation using mediapipe face detection

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['face_mask_detection']):  Default: 'face_mask_detection'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): Image to face detect
        face_ids (str | Unset): Comma-separated list of face ids to mask eg '0,2,7'. Numbered from 0. Leave empty to
            mask all. Find face IDs with FaceIdentifier node. Default: ''.
        minimum_confidence (float | Unset): Minimum confidence for face detection (lower if detection is failing)
            Default: 0.5.
        x_offset (float | Unset): Offset for the X-axis of the face mask Default: 0.0.
        y_offset (float | Unset): Offset for the Y-axis of the face mask Default: 0.0.
        chunk (bool | Unset): Whether to bypass full image face detection and default to image chunking. Chunking will
            occur if no faces are found in the full image. Default: False.
        invert_mask (bool | Unset): Toggle to invert the mask Default: False.
    """

    id: str
    type_: Literal["face_mask_detection"] = "face_mask_detection"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    face_ids: str | Unset = ""
    minimum_confidence: float | Unset = 0.5
    x_offset: float | Unset = 0.0
    y_offset: float | Unset = 0.0
    chunk: bool | Unset = False
    invert_mask: bool | Unset = False
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

        face_ids = self.face_ids

        minimum_confidence = self.minimum_confidence

        x_offset = self.x_offset

        y_offset = self.y_offset

        chunk = self.chunk

        invert_mask = self.invert_mask

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
        if face_ids is not UNSET:
            field_dict["face_ids"] = face_ids
        if minimum_confidence is not UNSET:
            field_dict["minimum_confidence"] = minimum_confidence
        if x_offset is not UNSET:
            field_dict["x_offset"] = x_offset
        if y_offset is not UNSET:
            field_dict["y_offset"] = y_offset
        if chunk is not UNSET:
            field_dict["chunk"] = chunk
        if invert_mask is not UNSET:
            field_dict["invert_mask"] = invert_mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["face_mask_detection"], d.pop("type"))
        if type_ != "face_mask_detection":
            raise ValueError(f"type must match const 'face_mask_detection', got '{type_}'")

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

        face_ids = d.pop("face_ids", UNSET)

        minimum_confidence = d.pop("minimum_confidence", UNSET)

        x_offset = d.pop("x_offset", UNSET)

        y_offset = d.pop("y_offset", UNSET)

        chunk = d.pop("chunk", UNSET)

        invert_mask = d.pop("invert_mask", UNSET)

        face_mask = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            face_ids=face_ids,
            minimum_confidence=minimum_confidence,
            x_offset=x_offset,
            y_offset=y_offset,
            chunk=chunk,
            invert_mask=invert_mask,
        )

        face_mask.additional_properties = d
        return face_mask

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
