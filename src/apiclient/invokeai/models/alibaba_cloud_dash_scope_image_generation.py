from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alibaba_cloud_dash_scope_image_generation_mode import AlibabaCloudDashScopeImageGenerationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField
    from ..models.model_identifier_field import ModelIdentifierField


T = TypeVar("T", bound="AlibabaCloudDashScopeImageGeneration")


@_attrs_define
class AlibabaCloudDashScopeImageGeneration:
    """Generate images using an Alibaba Cloud DashScope external model.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['alibabacloud_image_generation']):  Default: 'alibabacloud_image_generation'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        model (ModelIdentifierField | None | Unset): Main model (UNet, VAE, CLIP) to load
        mode (AlibabaCloudDashScopeImageGenerationMode | Unset): Generation mode. Not all modes are supported by every
            model; unsupported modes raise at runtime. Default: AlibabaCloudDashScopeImageGenerationMode.TXT2IMG.
        prompt (None | str | Unset): Prompt
        seed (int | None | Unset): Seed for random number generation
        num_images (int | Unset): Number of images to generate Default: 1.
        width (int | Unset): Width of output (px) Default: 1024.
        height (int | Unset): Height of output (px) Default: 1024.
        image_size (None | str | Unset): Image size preset (e.g. 1K, 2K, 4K)
        init_image (ImageField | None | Unset): Init image for img2img/inpaint
        mask_image (ImageField | None | Unset): Mask image for inpaint
        reference_images (list[ImageField] | Unset): Reference images
    """

    id: str
    type_: Literal["alibabacloud_image_generation"] = "alibabacloud_image_generation"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    model: ModelIdentifierField | None | Unset = UNSET
    mode: AlibabaCloudDashScopeImageGenerationMode | Unset = AlibabaCloudDashScopeImageGenerationMode.TXT2IMG
    prompt: None | str | Unset = UNSET
    seed: int | None | Unset = UNSET
    num_images: int | Unset = 1
    width: int | Unset = 1024
    height: int | Unset = 1024
    image_size: None | str | Unset = UNSET
    init_image: ImageField | None | Unset = UNSET
    mask_image: ImageField | None | Unset = UNSET
    reference_images: list[ImageField] | Unset = UNSET
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

        model: dict[str, Any] | None | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ModelIdentifierField):
            model = self.model.to_dict()
        else:
            model = self.model

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        seed: int | None | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        num_images = self.num_images

        width = self.width

        height = self.height

        image_size: None | str | Unset
        if isinstance(self.image_size, Unset):
            image_size = UNSET
        else:
            image_size = self.image_size

        init_image: dict[str, Any] | None | Unset
        if isinstance(self.init_image, Unset):
            init_image = UNSET
        elif isinstance(self.init_image, ImageField):
            init_image = self.init_image.to_dict()
        else:
            init_image = self.init_image

        mask_image: dict[str, Any] | None | Unset
        if isinstance(self.mask_image, Unset):
            mask_image = UNSET
        elif isinstance(self.mask_image, ImageField):
            mask_image = self.mask_image.to_dict()
        else:
            mask_image = self.mask_image

        reference_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reference_images, Unset):
            reference_images = []
            for reference_images_item_data in self.reference_images:
                reference_images_item = reference_images_item_data.to_dict()
                reference_images.append(reference_images_item)

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
        if model is not UNSET:
            field_dict["model"] = model
        if mode is not UNSET:
            field_dict["mode"] = mode
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if seed is not UNSET:
            field_dict["seed"] = seed
        if num_images is not UNSET:
            field_dict["num_images"] = num_images
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if image_size is not UNSET:
            field_dict["image_size"] = image_size
        if init_image is not UNSET:
            field_dict["init_image"] = init_image
        if mask_image is not UNSET:
            field_dict["mask_image"] = mask_image
        if reference_images is not UNSET:
            field_dict["reference_images"] = reference_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField
        from ..models.model_identifier_field import ModelIdentifierField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["alibabacloud_image_generation"], d.pop("type"))
        if type_ != "alibabacloud_image_generation":
            raise ValueError(f"type must match const 'alibabacloud_image_generation', got '{type_}'")

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

        def _parse_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_0 = ModelIdentifierField.from_dict(data)

                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: AlibabaCloudDashScopeImageGenerationMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AlibabaCloudDashScopeImageGenerationMode(_mode)

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))

        num_images = d.pop("num_images", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        def _parse_image_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_size = _parse_image_size(d.pop("image_size", UNSET))

        def _parse_init_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                init_image_type_0 = ImageField.from_dict(data)

                return init_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        init_image = _parse_init_image(d.pop("init_image", UNSET))

        def _parse_mask_image(data: object) -> ImageField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_image_type_0 = ImageField.from_dict(data)

                return mask_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageField | None | Unset, data)

        mask_image = _parse_mask_image(d.pop("mask_image", UNSET))

        _reference_images = d.pop("reference_images", UNSET)
        reference_images: list[ImageField] | Unset = UNSET
        if _reference_images is not UNSET:
            reference_images = []
            for reference_images_item_data in _reference_images:
                reference_images_item = ImageField.from_dict(reference_images_item_data)

                reference_images.append(reference_images_item)

        alibaba_cloud_dash_scope_image_generation = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            model=model,
            mode=mode,
            prompt=prompt,
            seed=seed,
            num_images=num_images,
            width=width,
            height=height,
            image_size=image_size,
            init_image=init_image,
            mask_image=mask_image,
            reference_images=reference_images,
        )

        alibaba_cloud_dash_scope_image_generation.additional_properties = d
        return alibaba_cloud_dash_scope_image_generation

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
