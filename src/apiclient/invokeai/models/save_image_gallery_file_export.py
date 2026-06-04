from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.save_image_gallery_file_export_file_format import SaveImageGalleryFileExportFileFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.image_field import ImageField
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="SaveImageGalleryFileExport")


@_attrs_define
class SaveImageGalleryFileExport:
    """Saves an image to the gallery (like the standard Save Image node) AND additionally exports a copy
    to the filesystem with a custom filename.

    Filename pattern: {prefix}{uuid}{suffix}.{file_format}
    - The UUID is the same UUID used for the gallery entry, so the exported file can be matched to the gallery item.
    - The gallery entry itself always uses the plain UUID (prefix/suffix apply only to the exported file on disk).
    - Board and Metadata inputs behave exactly like the standard Save Image node.
    - The export target is restricted to (subfolders of) the InvokeAI outputs folder — absolute paths are rejected.

    Example: prefix="hero_", suffix="_final", file_format="png" → "hero_<uuid>_final.png"

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['save_image_to_file']):  Default: 'save_image_to_file'.
            board (BoardField | None | Unset): The board to save the image to
            metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: False.
            image (ImageField | None | Unset): The image to save and export
            output_directory (str | Unset): Target subdirectory (relative to the configured InvokeAI outputs folder) for the
                exported file. Leave empty to use the outputs folder directly. Example: 'my-exports' → <outputs>/my-exports/.
                Nested paths like 'exports/2026' are allowed. Absolute paths and path traversal ('..') are not allowed for
                security reasons. The directory is created automatically if it doesn't exist. Default: ''.
            prefix (str | Unset): Text prepended to the UUID in the exported filename. Example: 'portrait_' →
                'portrait_<uuid>.png' Default: ''.
            suffix (str | Unset): Text appended to the UUID (before the extension). Example: '_v2' → '<uuid>_v2.png'
                Default: ''.
            file_format (SaveImageGalleryFileExportFileFormat | Unset): File format for the exported file. PNG is lossless;
                JPG/WEBP are lossy and respect 'quality'. Default: SaveImageGalleryFileExportFileFormat.PNG.
            quality (int | Unset): Compression quality for JPG and WEBP (1-100, higher = better quality, larger file).
                Ignored for PNG. Default: 95.
    """

    id: str
    type_: Literal["save_image_to_file"] = "save_image_to_file"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = False
    image: ImageField | None | Unset = UNSET
    output_directory: str | Unset = ""
    prefix: str | Unset = ""
    suffix: str | Unset = ""
    file_format: SaveImageGalleryFileExportFileFormat | Unset = SaveImageGalleryFileExportFileFormat.PNG
    quality: int | Unset = 95
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

        output_directory = self.output_directory

        prefix = self.prefix

        suffix = self.suffix

        file_format: str | Unset = UNSET
        if not isinstance(self.file_format, Unset):
            file_format = self.file_format.value

        quality = self.quality

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
        if output_directory is not UNSET:
            field_dict["output_directory"] = output_directory
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if file_format is not UNSET:
            field_dict["file_format"] = file_format
        if quality is not UNSET:
            field_dict["quality"] = quality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.image_field import ImageField
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["save_image_to_file"], d.pop("type"))
        if type_ != "save_image_to_file":
            raise ValueError(f"type must match const 'save_image_to_file', got '{type_}'")

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

        output_directory = d.pop("output_directory", UNSET)

        prefix = d.pop("prefix", UNSET)

        suffix = d.pop("suffix", UNSET)

        _file_format = d.pop("file_format", UNSET)
        file_format: SaveImageGalleryFileExportFileFormat | Unset
        if isinstance(_file_format, Unset):
            file_format = UNSET
        else:
            file_format = SaveImageGalleryFileExportFileFormat(_file_format)

        quality = d.pop("quality", UNSET)

        save_image_gallery_file_export = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            output_directory=output_directory,
            prefix=prefix,
            suffix=suffix,
            file_format=file_format,
            quality=quality,
        )

        save_image_gallery_file_export.additional_properties = d
        return save_image_gallery_file_export

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
