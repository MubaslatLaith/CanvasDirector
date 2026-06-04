from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_batch_batch_group import ImageBatchBatchGroup
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField


T = TypeVar("T", bound="ImageBatch")


@_attrs_define
class ImageBatch:
    """Create a batched generation, where the workflow is executed once for each image in the batch.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['image_batch']):  Default: 'image_batch'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        batch_group_id (ImageBatchBatchGroup | Unset): The ID of this batch node's group. If provided, all batch nodes
            in with the same ID will be 'zipped' before execution, and all nodes' collections must be of the same size.
            Default: ImageBatchBatchGroup.NONE.
        images (list[ImageField] | None | Unset): The images to batch over
    """

    id: str
    type_: Literal["image_batch"] = "image_batch"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    batch_group_id: ImageBatchBatchGroup | Unset = ImageBatchBatchGroup.NONE
    images: list[ImageField] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        batch_group_id: str | Unset = UNSET
        if not isinstance(self.batch_group_id, Unset):
            batch_group_id = self.batch_group_id.value

        images: list[dict[str, Any]] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

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
        if batch_group_id is not UNSET:
            field_dict["batch_group_id"] = batch_group_id
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["image_batch"], d.pop("type"))
        if type_ != "image_batch":
            raise ValueError(f"type must match const 'image_batch', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        _batch_group_id = d.pop("batch_group_id", UNSET)
        batch_group_id: ImageBatchBatchGroup | Unset
        if isinstance(_batch_group_id, Unset):
            batch_group_id = UNSET
        else:
            batch_group_id = ImageBatchBatchGroup(_batch_group_id)

        def _parse_images(data: object) -> list[ImageField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = ImageField.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageField] | None | Unset, data)

        images = _parse_images(d.pop("images", UNSET))

        image_batch = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            batch_group_id=batch_group_id,
            images=images,
        )

        image_batch.additional_properties = d
        return image_batch

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
