from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImagePanelLayout")


@_attrs_define
class ImagePanelLayout:
    """Get the coordinates of a single panel in a grid. (If the full image shape cannot be divided evenly into panels,
    then the grid may not cover the entire image.)

        Attributes:
            id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
            type_ (Literal['image_panel_layout']):  Default: 'image_panel_layout'.
            is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
            use_cache (bool | Unset): Whether or not to use the cache Default: True.
            width (int | None | Unset): The width of the entire grid.
            height (int | None | Unset): The height of the entire grid.
            num_cols (int | Unset): The number of columns in the grid. Default: 1.
            num_rows (int | Unset): The number of rows in the grid. Default: 1.
            panel_col_idx (int | Unset): The column index of the panel to be processed. Default: 0.
            panel_row_idx (int | Unset): The row index of the panel to be processed. Default: 0.
    """

    id: str
    type_: Literal["image_panel_layout"] = "image_panel_layout"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    width: int | None | Unset = UNSET
    height: int | None | Unset = UNSET
    num_cols: int | Unset = 1
    num_rows: int | Unset = 1
    panel_col_idx: int | Unset = 0
    panel_row_idx: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

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

        num_cols = self.num_cols

        num_rows = self.num_rows

        panel_col_idx = self.panel_col_idx

        panel_row_idx = self.panel_row_idx

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
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if num_cols is not UNSET:
            field_dict["num_cols"] = num_cols
        if num_rows is not UNSET:
            field_dict["num_rows"] = num_rows
        if panel_col_idx is not UNSET:
            field_dict["panel_col_idx"] = panel_col_idx
        if panel_row_idx is not UNSET:
            field_dict["panel_row_idx"] = panel_row_idx

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["image_panel_layout"], d.pop("type"))
        if type_ != "image_panel_layout":
            raise ValueError(f"type must match const 'image_panel_layout', got '{type_}'")

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

        num_cols = d.pop("num_cols", UNSET)

        num_rows = d.pop("num_rows", UNSET)

        panel_col_idx = d.pop("panel_col_idx", UNSET)

        panel_row_idx = d.pop("panel_row_idx", UNSET)

        image_panel_layout = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            width=width,
            height=height,
            num_cols=num_cols,
            num_rows=num_rows,
            panel_col_idx=panel_col_idx,
            panel_row_idx=panel_row_idx,
        )

        image_panel_layout.additional_properties = d
        return image_panel_layout

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
