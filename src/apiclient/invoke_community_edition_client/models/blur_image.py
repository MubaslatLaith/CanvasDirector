from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blur_image_blur_type import BlurImageBlurType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="BlurImage")


@_attrs_define
class BlurImage:
    """Blurs an image

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['img_blur']):  Default: 'img_blur'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The image to blur
        radius (float | Unset): The blur radius Default: 8.0.
        blur_type (BlurImageBlurType | Unset): The type of blur Default: BlurImageBlurType.GAUSSIAN.
    """

    id: str
    type_: Literal["img_blur"] = "img_blur"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    radius: float | Unset = 8.0
    blur_type: BlurImageBlurType | Unset = BlurImageBlurType.GAUSSIAN
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        id = self.id

        type_ = self.type_

        board: dict[str, Any] | None | Unset
        if isinstance(self.board, Unset):
            board = UNSET
        elif isinstance(self.board, BoardField):
            board = self.board.to_dict()
        else:
            board = self.board

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

        radius = self.radius

        blur_type: str | Unset = UNSET
        if not isinstance(self.blur_type, Unset):
            blur_type = self.blur_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if board is not UNSET:
            field_dict["board"] = board
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if image is not UNSET:
            field_dict["image"] = image
        if radius is not UNSET:
            field_dict["radius"] = radius
        if blur_type is not UNSET:
            field_dict["blur_type"] = blur_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["img_blur"], d.pop("type"))
        if type_ != "img_blur":
            raise ValueError(f"type must match const 'img_blur', got '{type_}'")

        def _parse_board(data: object) -> BoardField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                board_type_0 = BoardField.from_dict(data)

                return board_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BoardField | None | Unset, data)

        board = _parse_board(d.pop("board", UNSET))

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

        radius = d.pop("radius", UNSET)

        _blur_type = d.pop("blur_type", UNSET)
        blur_type: BlurImageBlurType | Unset
        if isinstance(_blur_type, Unset):
            blur_type = UNSET
        else:
            blur_type = BlurImageBlurType(_blur_type)

        blur_image = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            radius=radius,
            blur_type=blur_type,
        )

        blur_image.additional_properties = d
        return blur_image

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
