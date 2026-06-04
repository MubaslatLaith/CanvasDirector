from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.segment_anything_mask_filter import SegmentAnythingMaskFilter
from ..models.segment_anything_model_type_0 import SegmentAnythingModelType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bounding_box_field import BoundingBoxField
    from ..models.image_field import ImageField
    from ..models.sam_points_field import SAMPointsField


T = TypeVar("T", bound="SegmentAnything")


@_attrs_define
class SegmentAnything:
    """Runs a Segment Anything Model (SAM or SAM2).

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['segment_anything']):  Default: 'segment_anything'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        model (None | SegmentAnythingModelType0 | Unset): The Segment Anything model to use (SAM or SAM2).
        image (ImageField | None | Unset): The image to segment.
        bounding_boxes (list[BoundingBoxField] | None | Unset): The bounding boxes to prompt the model with.
        point_lists (list[SAMPointsField] | None | Unset): The list of point lists to prompt the model with. Each list
            of points represents a single object.
        apply_polygon_refinement (bool | Unset): Whether to apply polygon refinement to the masks. This will smooth the
            edges of the masks slightly and ensure that each mask consists of a single closed polygon (before merging).
            Default: True.
        mask_filter (SegmentAnythingMaskFilter | Unset): The filtering to apply to the detected masks before merging
            them into a final output. Default: SegmentAnythingMaskFilter.ALL.
    """

    id: str
    type_: Literal["segment_anything"] = "segment_anything"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    model: None | SegmentAnythingModelType0 | Unset = UNSET
    image: ImageField | None | Unset = UNSET
    bounding_boxes: list[BoundingBoxField] | None | Unset = UNSET
    point_lists: list[SAMPointsField] | None | Unset = UNSET
    apply_polygon_refinement: bool | Unset = True
    mask_filter: SegmentAnythingMaskFilter | Unset = SegmentAnythingMaskFilter.ALL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, SegmentAnythingModelType0):
            model = self.model.value
        else:
            model = self.model

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        bounding_boxes: list[dict[str, Any]] | None | Unset
        if isinstance(self.bounding_boxes, Unset):
            bounding_boxes = UNSET
        elif isinstance(self.bounding_boxes, list):
            bounding_boxes = []
            for bounding_boxes_type_0_item_data in self.bounding_boxes:
                bounding_boxes_type_0_item = bounding_boxes_type_0_item_data.to_dict()
                bounding_boxes.append(bounding_boxes_type_0_item)

        else:
            bounding_boxes = self.bounding_boxes

        point_lists: list[dict[str, Any]] | None | Unset
        if isinstance(self.point_lists, Unset):
            point_lists = UNSET
        elif isinstance(self.point_lists, list):
            point_lists = []
            for point_lists_type_0_item_data in self.point_lists:
                point_lists_type_0_item = point_lists_type_0_item_data.to_dict()
                point_lists.append(point_lists_type_0_item)

        else:
            point_lists = self.point_lists

        apply_polygon_refinement = self.apply_polygon_refinement

        mask_filter: str | Unset = UNSET
        if not isinstance(self.mask_filter, Unset):
            mask_filter = self.mask_filter.value

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
        if model is not UNSET:
            field_dict["model"] = model
        if image is not UNSET:
            field_dict["image"] = image
        if bounding_boxes is not UNSET:
            field_dict["bounding_boxes"] = bounding_boxes
        if point_lists is not UNSET:
            field_dict["point_lists"] = point_lists
        if apply_polygon_refinement is not UNSET:
            field_dict["apply_polygon_refinement"] = apply_polygon_refinement
        if mask_filter is not UNSET:
            field_dict["mask_filter"] = mask_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bounding_box_field import BoundingBoxField
        from ..models.image_field import ImageField
        from ..models.sam_points_field import SAMPointsField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["segment_anything"], d.pop("type"))
        if type_ != "segment_anything":
            raise ValueError(f"type must match const 'segment_anything', got '{type_}'")

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_model(data: object) -> None | SegmentAnythingModelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_0 = SegmentAnythingModelType0(data)

                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentAnythingModelType0 | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

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

        def _parse_bounding_boxes(data: object) -> list[BoundingBoxField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bounding_boxes_type_0 = []
                _bounding_boxes_type_0 = data
                for bounding_boxes_type_0_item_data in _bounding_boxes_type_0:
                    bounding_boxes_type_0_item = BoundingBoxField.from_dict(bounding_boxes_type_0_item_data)

                    bounding_boxes_type_0.append(bounding_boxes_type_0_item)

                return bounding_boxes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BoundingBoxField] | None | Unset, data)

        bounding_boxes = _parse_bounding_boxes(d.pop("bounding_boxes", UNSET))

        def _parse_point_lists(data: object) -> list[SAMPointsField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                point_lists_type_0 = []
                _point_lists_type_0 = data
                for point_lists_type_0_item_data in _point_lists_type_0:
                    point_lists_type_0_item = SAMPointsField.from_dict(point_lists_type_0_item_data)

                    point_lists_type_0.append(point_lists_type_0_item)

                return point_lists_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SAMPointsField] | None | Unset, data)

        point_lists = _parse_point_lists(d.pop("point_lists", UNSET))

        apply_polygon_refinement = d.pop("apply_polygon_refinement", UNSET)

        _mask_filter = d.pop("mask_filter", UNSET)
        mask_filter: SegmentAnythingMaskFilter | Unset
        if isinstance(_mask_filter, Unset):
            mask_filter = UNSET
        else:
            mask_filter = SegmentAnythingMaskFilter(_mask_filter)

        segment_anything = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            model=model,
            image=image,
            bounding_boxes=bounding_boxes,
            point_lists=point_lists,
            apply_polygon_refinement=apply_polygon_refinement,
            mask_filter=mask_filter,
        )

        segment_anything.additional_properties = d
        return segment_anything

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
