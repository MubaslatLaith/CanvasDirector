from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="ImageToImageAutoscale")


@_attrs_define
class ImageToImageAutoscale:
    """Run any spandrel image-to-image model (https://github.com/chaiNNer-org/spandrel) until the target scale is reached.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['spandrel_image_to_image_autoscale']):  Default: 'spandrel_image_to_image_autoscale'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The input image
        image_to_image_model (ModelIdentifierField | None | Unset): Image-to-Image model
        tile_size (int | Unset): The tile size for tiled image-to-image. Set to 0 to disable tiling. Default: 512.
        scale (float | Unset): The final scale of the output image. If the model does not upscale the image, this will
            be ignored. Default: 4.0.
        fit_to_multiple_of_8 (bool | Unset): If true, the output image will be resized to the nearest multiple of 8 in
            both dimensions. Default: False.
    """

    id: str
    type_: Literal["spandrel_image_to_image_autoscale"] = "spandrel_image_to_image_autoscale"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    image_to_image_model: ModelIdentifierField | None | Unset = UNSET
    tile_size: int | Unset = 512
    scale: float | Unset = 4.0
    fit_to_multiple_of_8: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField
        from ..models.model_identifier_field import ModelIdentifierField

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

        image_to_image_model: dict[str, Any] | None | Unset
        if isinstance(self.image_to_image_model, Unset):
            image_to_image_model = UNSET
        elif isinstance(self.image_to_image_model, ModelIdentifierField):
            image_to_image_model = self.image_to_image_model.to_dict()
        else:
            image_to_image_model = self.image_to_image_model

        tile_size = self.tile_size

        scale = self.scale

        fit_to_multiple_of_8 = self.fit_to_multiple_of_8

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
        if image_to_image_model is not UNSET:
            field_dict["image_to_image_model"] = image_to_image_model
        if tile_size is not UNSET:
            field_dict["tile_size"] = tile_size
        if scale is not UNSET:
            field_dict["scale"] = scale
        if fit_to_multiple_of_8 is not UNSET:
            field_dict["fit_to_multiple_of_8"] = fit_to_multiple_of_8

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["spandrel_image_to_image_autoscale"], d.pop("type"))
        if type_ != "spandrel_image_to_image_autoscale":
            raise ValueError(f"type must match const 'spandrel_image_to_image_autoscale', got '{type_}'")

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

        def _parse_image_to_image_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_to_image_model_type_0 = ModelIdentifierField.from_dict(data)

                return image_to_image_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        image_to_image_model = _parse_image_to_image_model(d.pop("image_to_image_model", UNSET))

        tile_size = d.pop("tile_size", UNSET)

        scale = d.pop("scale", UNSET)

        fit_to_multiple_of_8 = d.pop("fit_to_multiple_of_8", UNSET)

        image_to_image_autoscale = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            image_to_image_model=image_to_image_model,
            tile_size=tile_size,
            scale=scale,
            fit_to_multiple_of_8=fit_to_multiple_of_8,
        )

        image_to_image_autoscale.additional_properties = d
        return image_to_image_autoscale

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
