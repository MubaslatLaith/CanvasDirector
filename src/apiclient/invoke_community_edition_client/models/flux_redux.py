from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flux_redux_downsampling_function import FLUXReduxDownsamplingFunction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_field import ImageField
    from ..models.model_identifier_field import ModelIdentifierField
    from ..models.tensor_field import TensorField


T = TypeVar("T", bound="FLUXRedux")


@_attrs_define
class FLUXRedux:
    """Runs a FLUX Redux model to generate a conditioning tensor.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['flux_redux']):  Default: 'flux_redux'.
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        image (ImageField | None | Unset): The FLUX Redux image prompt.
        mask (None | TensorField | Unset): The bool mask associated with this FLUX Redux image prompt. Excluded regions
            should be set to False, included regions should be set to True.
        redux_model (ModelIdentifierField | None | Unset): The FLUX Redux model to use.
        downsampling_factor (int | Unset): Redux Downsampling Factor (1-9) Default: 1.
        downsampling_function (FLUXReduxDownsamplingFunction | Unset): Redux Downsampling Function Default:
            FLUXReduxDownsamplingFunction.AREA.
        weight (float | Unset): Redux weight (0.0-1.0) Default: 1.0.
    """

    id: str
    type_: Literal["flux_redux"] = "flux_redux"
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    image: ImageField | None | Unset = UNSET
    mask: None | TensorField | Unset = UNSET
    redux_model: ModelIdentifierField | None | Unset = UNSET
    downsampling_factor: int | Unset = 1
    downsampling_function: FLUXReduxDownsamplingFunction | Unset = FLUXReduxDownsamplingFunction.AREA
    weight: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.tensor_field import TensorField

        id = self.id

        type_ = self.type_

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ImageField):
            image = self.image.to_dict()
        else:
            image = self.image

        mask: dict[str, Any] | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        elif isinstance(self.mask, TensorField):
            mask = self.mask.to_dict()
        else:
            mask = self.mask

        redux_model: dict[str, Any] | None | Unset
        if isinstance(self.redux_model, Unset):
            redux_model = UNSET
        elif isinstance(self.redux_model, ModelIdentifierField):
            redux_model = self.redux_model.to_dict()
        else:
            redux_model = self.redux_model

        downsampling_factor = self.downsampling_factor

        downsampling_function: str | Unset = UNSET
        if not isinstance(self.downsampling_function, Unset):
            downsampling_function = self.downsampling_function.value

        weight = self.weight

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
        if image is not UNSET:
            field_dict["image"] = image
        if mask is not UNSET:
            field_dict["mask"] = mask
        if redux_model is not UNSET:
            field_dict["redux_model"] = redux_model
        if downsampling_factor is not UNSET:
            field_dict["downsampling_factor"] = downsampling_factor
        if downsampling_function is not UNSET:
            field_dict["downsampling_function"] = downsampling_function
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_field import ImageField
        from ..models.model_identifier_field import ModelIdentifierField
        from ..models.tensor_field import TensorField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["flux_redux"], d.pop("type"))
        if type_ != "flux_redux":
            raise ValueError(f"type must match const 'flux_redux', got '{type_}'")

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

        def _parse_mask(data: object) -> None | TensorField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mask_type_0 = TensorField.from_dict(data)

                return mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TensorField | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))

        def _parse_redux_model(data: object) -> ModelIdentifierField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                redux_model_type_0 = ModelIdentifierField.from_dict(data)

                return redux_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelIdentifierField | None | Unset, data)

        redux_model = _parse_redux_model(d.pop("redux_model", UNSET))

        downsampling_factor = d.pop("downsampling_factor", UNSET)

        _downsampling_function = d.pop("downsampling_function", UNSET)
        downsampling_function: FLUXReduxDownsamplingFunction | Unset
        if isinstance(_downsampling_function, Unset):
            downsampling_function = UNSET
        else:
            downsampling_function = FLUXReduxDownsamplingFunction(_downsampling_function)

        weight = d.pop("weight", UNSET)

        flux_redux = cls(
            id=id,
            type_=type_,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            image=image,
            mask=mask,
            redux_model=redux_model,
            downsampling_factor=downsampling_factor,
            downsampling_function=downsampling_function,
            weight=weight,
        )

        flux_redux.additional_properties = d
        return flux_redux

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
