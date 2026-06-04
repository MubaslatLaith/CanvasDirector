from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_field import MetadataField


T = TypeVar("T", bound="CreateRectangleMask")


@_attrs_define
class CreateRectangleMask:
    """Create a rectangular mask.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['rectangle_mask']):  Default: 'rectangle_mask'.
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        width (int | None | Unset): The width of the entire mask.
        height (int | None | Unset): The height of the entire mask.
        x_left (int | None | Unset): The left x-coordinate of the rectangular masked region (inclusive).
        y_top (int | None | Unset): The top y-coordinate of the rectangular masked region (inclusive).
        rectangle_width (int | None | Unset): The width of the rectangular masked region.
        rectangle_height (int | None | Unset): The height of the rectangular masked region.
    """

    id: str
    type_: Literal["rectangle_mask"] = "rectangle_mask"
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    x_left: int | None | Unset = UNSET
    y_top: int | None | Unset = UNSET
    rectangle_width: int | None | Unset = UNSET
    rectangle_height: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        x_left: int | None | Unset
        if isinstance(self.x_left, Unset):
            x_left = UNSET
        else:
            x_left = self.x_left

        y_top: int | None | Unset
        if isinstance(self.y_top, Unset):
            y_top = UNSET
        else:
            y_top = self.y_top

        rectangle_width: int | None | Unset
        if isinstance(self.rectangle_width, Unset):
            rectangle_width = UNSET
        else:
            rectangle_width = self.rectangle_width

        rectangle_height: int | None | Unset
        if isinstance(self.rectangle_height, Unset):
            rectangle_height = UNSET
        else:
            rectangle_height = self.rectangle_height

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
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if x_left is not UNSET:
            field_dict["x_left"] = x_left
        if y_top is not UNSET:
            field_dict["y_top"] = y_top
        if rectangle_width is not UNSET:
            field_dict["rectangle_width"] = rectangle_width
        if rectangle_height is not UNSET:
            field_dict["rectangle_height"] = rectangle_height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_field import MetadataField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["rectangle_mask"], d.pop("type"))
        if type_ != "rectangle_mask":
            raise ValueError(f"type must match const 'rectangle_mask', got '{type_}'")

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

        def _parse_x_left(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        x_left = _parse_x_left(d.pop("x_left", UNSET))

        def _parse_y_top(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y_top = _parse_y_top(d.pop("y_top", UNSET))

        def _parse_rectangle_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rectangle_width = _parse_rectangle_width(d.pop("rectangle_width", UNSET))

        def _parse_rectangle_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rectangle_height = _parse_rectangle_height(d.pop("rectangle_height", UNSET))

        create_rectangle_mask = cls(
            id=id,
            type_=type_,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            width=width,
            height=height,
            x_left=x_left,
            y_top=y_top,
            rectangle_width=rectangle_width,
            rectangle_height=rectangle_height,
        )

        create_rectangle_mask.additional_properties = d
        return create_rectangle_mask

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
