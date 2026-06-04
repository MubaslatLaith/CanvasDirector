from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_model_panel_control import ExternalModelPanelControl


T = TypeVar("T", bound="ExternalModelPanelSchema")


@_attrs_define
class ExternalModelPanelSchema:
    """
    Attributes:
        prompts (list[ExternalModelPanelControl] | Unset):
        image (list[ExternalModelPanelControl] | Unset):
        generation (list[ExternalModelPanelControl] | Unset):
    """

    prompts: list[ExternalModelPanelControl] | Unset = UNSET
    image: list[ExternalModelPanelControl] | Unset = UNSET
    generation: list[ExternalModelPanelControl] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prompts, Unset):
            prompts = []
            for prompts_item_data in self.prompts:
                prompts_item = prompts_item_data.to_dict()
                prompts.append(prompts_item)

        image: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = []
            for image_item_data in self.image:
                image_item = image_item_data.to_dict()
                image.append(image_item)

        generation: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.generation, Unset):
            generation = []
            for generation_item_data in self.generation:
                generation_item = generation_item_data.to_dict()
                generation.append(generation_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if prompts is not UNSET:
            field_dict["prompts"] = prompts
        if image is not UNSET:
            field_dict["image"] = image
        if generation is not UNSET:
            field_dict["generation"] = generation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_model_panel_control import ExternalModelPanelControl

        d = dict(src_dict)
        _prompts = d.pop("prompts", UNSET)
        prompts: list[ExternalModelPanelControl] | Unset = UNSET
        if _prompts is not UNSET:
            prompts = []
            for prompts_item_data in _prompts:
                prompts_item = ExternalModelPanelControl.from_dict(prompts_item_data)

                prompts.append(prompts_item)

        _image = d.pop("image", UNSET)
        image: list[ExternalModelPanelControl] | Unset = UNSET
        if _image is not UNSET:
            image = []
            for image_item_data in _image:
                image_item = ExternalModelPanelControl.from_dict(image_item_data)

                image.append(image_item)

        _generation = d.pop("generation", UNSET)
        generation: list[ExternalModelPanelControl] | Unset = UNSET
        if _generation is not UNSET:
            generation = []
            for generation_item_data in _generation:
                generation_item = ExternalModelPanelControl.from_dict(generation_item_data)

                generation.append(generation_item)

        external_model_panel_schema = cls(
            prompts=prompts,
            image=image,
            generation=generation,
        )

        return external_model_panel_schema
