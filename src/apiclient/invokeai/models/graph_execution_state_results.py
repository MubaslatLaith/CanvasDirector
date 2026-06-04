from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.anima_conditioning_output import AnimaConditioningOutput
    from ..models.anima_lo_ra_loader_output import AnimaLoRALoaderOutput
    from ..models.anima_model_loader_output import AnimaModelLoaderOutput
    from ..models.boolean_collection_output import BooleanCollectionOutput
    from ..models.boolean_output import BooleanOutput
    from ..models.bounding_box_collection_output import BoundingBoxCollectionOutput
    from ..models.bounding_box_output import BoundingBoxOutput
    from ..models.calculate_image_tiles_output import CalculateImageTilesOutput
    from ..models.clip_output import CLIPOutput
    from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
    from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
    from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
    from ..models.collect_invocation_output import CollectInvocationOutput
    from ..models.color_collection_output import ColorCollectionOutput
    from ..models.color_output import ColorOutput
    from ..models.conditioning_collection_output import ConditioningCollectionOutput
    from ..models.conditioning_output import ConditioningOutput
    from ..models.control_output import ControlOutput
    from ..models.denoise_mask_output import DenoiseMaskOutput
    from ..models.face_mask_output import FaceMaskOutput
    from ..models.face_off_output import FaceOffOutput
    from ..models.float_collection_output import FloatCollectionOutput
    from ..models.float_generator_output import FloatGeneratorOutput
    from ..models.float_output import FloatOutput
    from ..models.flux_2_klein_lo_ra_loader_output import Flux2KleinLoRALoaderOutput
    from ..models.flux_2_klein_model_loader_output import Flux2KleinModelLoaderOutput
    from ..models.flux_conditioning_collection_output import FluxConditioningCollectionOutput
    from ..models.flux_conditioning_output import FluxConditioningOutput
    from ..models.flux_control_lo_ra_loader_output import FluxControlLoRALoaderOutput
    from ..models.flux_control_net_output import FluxControlNetOutput
    from ..models.flux_fill_output import FluxFillOutput
    from ..models.flux_kontext_output import FluxKontextOutput
    from ..models.flux_lo_ra_loader_output import FluxLoRALoaderOutput
    from ..models.flux_model_loader_output import FluxModelLoaderOutput
    from ..models.flux_redux_output import FluxReduxOutput
    from ..models.gradient_mask_output import GradientMaskOutput
    from ..models.ideal_size_output import IdealSizeOutput
    from ..models.if_invocation_output import IfInvocationOutput
    from ..models.image_collection_output import ImageCollectionOutput
    from ..models.image_generator_output import ImageGeneratorOutput
    from ..models.image_output import ImageOutput
    from ..models.image_panel_coordinate_output import ImagePanelCoordinateOutput
    from ..models.integer_collection_output import IntegerCollectionOutput
    from ..models.integer_generator_output import IntegerGeneratorOutput
    from ..models.integer_output import IntegerOutput
    from ..models.ip_adapter_output import IPAdapterOutput
    from ..models.iterate_invocation_output import IterateInvocationOutput
    from ..models.latents_collection_output import LatentsCollectionOutput
    from ..models.latents_meta_output import LatentsMetaOutput
    from ..models.latents_output import LatentsOutput
    from ..models.lo_ra_loader_output import LoRALoaderOutput
    from ..models.lo_ra_selector_output import LoRASelectorOutput
    from ..models.mask_output import MaskOutput
    from ..models.md_control_list_output import MDControlListOutput
    from ..models.mdip_adapter_list_output import MDIPAdapterListOutput
    from ..models.mdt2i_adapter_list_output import MDT2IAdapterListOutput
    from ..models.metadata_item_output import MetadataItemOutput
    from ..models.metadata_output import MetadataOutput
    from ..models.metadata_to_loras_collection_output import MetadataToLorasCollectionOutput
    from ..models.metadata_to_model_output import MetadataToModelOutput
    from ..models.metadata_to_sdxl_model_output import MetadataToSDXLModelOutput
    from ..models.model_identifier_output import ModelIdentifierOutput
    from ..models.model_loader_output import ModelLoaderOutput
    from ..models.noise_output import NoiseOutput
    from ..models.pair_tile_image_output import PairTileImageOutput
    from ..models.pbr_maps_output import PBRMapsOutput
    from ..models.prompt_template_output import PromptTemplateOutput
    from ..models.qwen_image_conditioning_output import QwenImageConditioningOutput
    from ..models.qwen_image_lo_ra_loader_output import QwenImageLoRALoaderOutput
    from ..models.qwen_image_model_loader_output import QwenImageModelLoaderOutput
    from ..models.scheduler_output import SchedulerOutput
    from ..models.sd3_conditioning_output import SD3ConditioningOutput
    from ..models.sd_3_model_loader_output import Sd3ModelLoaderOutput
    from ..models.sdxl_lo_ra_loader_output import SDXLLoRALoaderOutput
    from ..models.sdxl_model_loader_output import SDXLModelLoaderOutput
    from ..models.sdxl_refiner_model_loader_output import SDXLRefinerModelLoaderOutput
    from ..models.seamless_mode_output import SeamlessModeOutput
    from ..models.string_2_output import String2Output
    from ..models.string_collection_output import StringCollectionOutput
    from ..models.string_generator_output import StringGeneratorOutput
    from ..models.string_output import StringOutput
    from ..models.string_pos_neg_output import StringPosNegOutput
    from ..models.t2i_adapter_output import T2IAdapterOutput
    from ..models.tile_to_properties_output import TileToPropertiesOutput
    from ..models.u_net_output import UNetOutput
    from ..models.vae_output import VAEOutput
    from ..models.z_image_conditioning_output import ZImageConditioningOutput
    from ..models.z_image_control_output import ZImageControlOutput
    from ..models.z_image_lo_ra_loader_output import ZImageLoRALoaderOutput
    from ..models.z_image_model_loader_output import ZImageModelLoaderOutput


T = TypeVar("T", bound="GraphExecutionStateResults")


@_attrs_define
class GraphExecutionStateResults:
    """The results of node executions"""

    additional_properties: dict[
        str,
        AnimaConditioningOutput
        | AnimaLoRALoaderOutput
        | AnimaModelLoaderOutput
        | BooleanCollectionOutput
        | BooleanOutput
        | BoundingBoxCollectionOutput
        | BoundingBoxOutput
        | CalculateImageTilesOutput
        | CLIPOutput
        | CLIPSkipInvocationOutput
        | CogView4ConditioningOutput
        | CogView4ModelLoaderOutput
        | CollectInvocationOutput
        | ColorCollectionOutput
        | ColorOutput
        | ConditioningCollectionOutput
        | ConditioningOutput
        | ControlOutput
        | DenoiseMaskOutput
        | FaceMaskOutput
        | FaceOffOutput
        | FloatCollectionOutput
        | FloatGeneratorOutput
        | FloatOutput
        | Flux2KleinLoRALoaderOutput
        | Flux2KleinModelLoaderOutput
        | FluxConditioningCollectionOutput
        | FluxConditioningOutput
        | FluxControlLoRALoaderOutput
        | FluxControlNetOutput
        | FluxFillOutput
        | FluxKontextOutput
        | FluxLoRALoaderOutput
        | FluxModelLoaderOutput
        | FluxReduxOutput
        | GradientMaskOutput
        | IdealSizeOutput
        | IfInvocationOutput
        | ImageCollectionOutput
        | ImageGeneratorOutput
        | ImageOutput
        | ImagePanelCoordinateOutput
        | IntegerCollectionOutput
        | IntegerGeneratorOutput
        | IntegerOutput
        | IPAdapterOutput
        | IterateInvocationOutput
        | LatentsCollectionOutput
        | LatentsMetaOutput
        | LatentsOutput
        | LoRALoaderOutput
        | LoRASelectorOutput
        | MaskOutput
        | MDControlListOutput
        | MDIPAdapterListOutput
        | MDT2IAdapterListOutput
        | MetadataItemOutput
        | MetadataOutput
        | MetadataToLorasCollectionOutput
        | MetadataToModelOutput
        | MetadataToSDXLModelOutput
        | ModelIdentifierOutput
        | ModelLoaderOutput
        | NoiseOutput
        | PairTileImageOutput
        | PBRMapsOutput
        | PromptTemplateOutput
        | QwenImageConditioningOutput
        | QwenImageLoRALoaderOutput
        | QwenImageModelLoaderOutput
        | SchedulerOutput
        | SD3ConditioningOutput
        | Sd3ModelLoaderOutput
        | SDXLLoRALoaderOutput
        | SDXLModelLoaderOutput
        | SDXLRefinerModelLoaderOutput
        | SeamlessModeOutput
        | String2Output
        | StringCollectionOutput
        | StringGeneratorOutput
        | StringOutput
        | StringPosNegOutput
        | T2IAdapterOutput
        | TileToPropertiesOutput
        | UNetOutput
        | VAEOutput
        | ZImageConditioningOutput
        | ZImageControlOutput
        | ZImageLoRALoaderOutput
        | ZImageModelLoaderOutput,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.anima_conditioning_output import AnimaConditioningOutput
        from ..models.anima_lo_ra_loader_output import AnimaLoRALoaderOutput
        from ..models.anima_model_loader_output import AnimaModelLoaderOutput
        from ..models.boolean_collection_output import BooleanCollectionOutput
        from ..models.boolean_output import BooleanOutput
        from ..models.bounding_box_collection_output import BoundingBoxCollectionOutput
        from ..models.bounding_box_output import BoundingBoxOutput
        from ..models.calculate_image_tiles_output import CalculateImageTilesOutput
        from ..models.clip_output import CLIPOutput
        from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
        from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
        from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
        from ..models.collect_invocation_output import CollectInvocationOutput
        from ..models.color_collection_output import ColorCollectionOutput
        from ..models.color_output import ColorOutput
        from ..models.conditioning_collection_output import ConditioningCollectionOutput
        from ..models.conditioning_output import ConditioningOutput
        from ..models.control_output import ControlOutput
        from ..models.denoise_mask_output import DenoiseMaskOutput
        from ..models.face_mask_output import FaceMaskOutput
        from ..models.face_off_output import FaceOffOutput
        from ..models.float_collection_output import FloatCollectionOutput
        from ..models.float_generator_output import FloatGeneratorOutput
        from ..models.float_output import FloatOutput
        from ..models.flux_2_klein_lo_ra_loader_output import Flux2KleinLoRALoaderOutput
        from ..models.flux_2_klein_model_loader_output import Flux2KleinModelLoaderOutput
        from ..models.flux_conditioning_collection_output import FluxConditioningCollectionOutput
        from ..models.flux_conditioning_output import FluxConditioningOutput
        from ..models.flux_control_lo_ra_loader_output import FluxControlLoRALoaderOutput
        from ..models.flux_control_net_output import FluxControlNetOutput
        from ..models.flux_fill_output import FluxFillOutput
        from ..models.flux_kontext_output import FluxKontextOutput
        from ..models.flux_lo_ra_loader_output import FluxLoRALoaderOutput
        from ..models.flux_model_loader_output import FluxModelLoaderOutput
        from ..models.flux_redux_output import FluxReduxOutput
        from ..models.gradient_mask_output import GradientMaskOutput
        from ..models.ideal_size_output import IdealSizeOutput
        from ..models.if_invocation_output import IfInvocationOutput
        from ..models.image_collection_output import ImageCollectionOutput
        from ..models.image_generator_output import ImageGeneratorOutput
        from ..models.image_output import ImageOutput
        from ..models.image_panel_coordinate_output import ImagePanelCoordinateOutput
        from ..models.integer_collection_output import IntegerCollectionOutput
        from ..models.integer_generator_output import IntegerGeneratorOutput
        from ..models.integer_output import IntegerOutput
        from ..models.ip_adapter_output import IPAdapterOutput
        from ..models.iterate_invocation_output import IterateInvocationOutput
        from ..models.latents_collection_output import LatentsCollectionOutput
        from ..models.latents_meta_output import LatentsMetaOutput
        from ..models.latents_output import LatentsOutput
        from ..models.lo_ra_loader_output import LoRALoaderOutput
        from ..models.lo_ra_selector_output import LoRASelectorOutput
        from ..models.mask_output import MaskOutput
        from ..models.md_control_list_output import MDControlListOutput
        from ..models.mdip_adapter_list_output import MDIPAdapterListOutput
        from ..models.mdt2i_adapter_list_output import MDT2IAdapterListOutput
        from ..models.metadata_item_output import MetadataItemOutput
        from ..models.metadata_output import MetadataOutput
        from ..models.metadata_to_loras_collection_output import MetadataToLorasCollectionOutput
        from ..models.metadata_to_model_output import MetadataToModelOutput
        from ..models.metadata_to_sdxl_model_output import MetadataToSDXLModelOutput
        from ..models.model_identifier_output import ModelIdentifierOutput
        from ..models.model_loader_output import ModelLoaderOutput
        from ..models.noise_output import NoiseOutput
        from ..models.pair_tile_image_output import PairTileImageOutput
        from ..models.pbr_maps_output import PBRMapsOutput
        from ..models.prompt_template_output import PromptTemplateOutput
        from ..models.qwen_image_conditioning_output import QwenImageConditioningOutput
        from ..models.qwen_image_lo_ra_loader_output import QwenImageLoRALoaderOutput
        from ..models.qwen_image_model_loader_output import QwenImageModelLoaderOutput
        from ..models.scheduler_output import SchedulerOutput
        from ..models.sd3_conditioning_output import SD3ConditioningOutput
        from ..models.sd_3_model_loader_output import Sd3ModelLoaderOutput
        from ..models.sdxl_lo_ra_loader_output import SDXLLoRALoaderOutput
        from ..models.sdxl_model_loader_output import SDXLModelLoaderOutput
        from ..models.sdxl_refiner_model_loader_output import SDXLRefinerModelLoaderOutput
        from ..models.seamless_mode_output import SeamlessModeOutput
        from ..models.string_2_output import String2Output
        from ..models.string_collection_output import StringCollectionOutput
        from ..models.string_generator_output import StringGeneratorOutput
        from ..models.string_output import StringOutput
        from ..models.string_pos_neg_output import StringPosNegOutput
        from ..models.t2i_adapter_output import T2IAdapterOutput
        from ..models.tile_to_properties_output import TileToPropertiesOutput
        from ..models.u_net_output import UNetOutput
        from ..models.vae_output import VAEOutput
        from ..models.z_image_conditioning_output import ZImageConditioningOutput
        from ..models.z_image_control_output import ZImageControlOutput
        from ..models.z_image_lo_ra_loader_output import ZImageLoRALoaderOutput

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, AnimaConditioningOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AnimaLoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AnimaModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BooleanCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BooleanOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BoundingBoxCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BoundingBoxOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CLIPOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CLIPSkipInvocationOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CalculateImageTilesOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CogView4ConditioningOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CogView4ModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CollectInvocationOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ColorCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ColorOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ConditioningCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ConditioningOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ControlOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseMaskOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FaceMaskOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FaceOffOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatGeneratorOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, Flux2KleinLoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, Flux2KleinModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxConditioningCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxConditioningOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxControlLoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxControlNetOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxFillOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxKontextOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxLoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FluxReduxOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, GradientMaskOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IPAdapterOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IdealSizeOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IfInvocationOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageGeneratorOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImagePanelCoordinateOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerGeneratorOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IterateInvocationOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsMetaOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LoRASelectorOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MDControlListOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MDIPAdapterListOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MDT2IAdapterListOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MaskOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataItemOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToLorasCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToModelOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToSDXLModelOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ModelIdentifierOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, NoiseOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PBRMapsOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PairTileImageOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptTemplateOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, QwenImageConditioningOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, QwenImageLoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, QwenImageModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SD3ConditioningOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SDXLLoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SDXLModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SDXLRefinerModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SchedulerOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, Sd3ModelLoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SeamlessModeOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, String2Output):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringCollectionOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringGeneratorOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringPosNegOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, T2IAdapterOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TileToPropertiesOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, UNetOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, VAEOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ZImageConditioningOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ZImageControlOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ZImageLoRALoaderOutput):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.anima_conditioning_output import AnimaConditioningOutput
        from ..models.anima_lo_ra_loader_output import AnimaLoRALoaderOutput
        from ..models.anima_model_loader_output import AnimaModelLoaderOutput
        from ..models.boolean_collection_output import BooleanCollectionOutput
        from ..models.boolean_output import BooleanOutput
        from ..models.bounding_box_collection_output import BoundingBoxCollectionOutput
        from ..models.bounding_box_output import BoundingBoxOutput
        from ..models.calculate_image_tiles_output import CalculateImageTilesOutput
        from ..models.clip_output import CLIPOutput
        from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
        from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
        from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
        from ..models.collect_invocation_output import CollectInvocationOutput
        from ..models.color_collection_output import ColorCollectionOutput
        from ..models.color_output import ColorOutput
        from ..models.conditioning_collection_output import ConditioningCollectionOutput
        from ..models.conditioning_output import ConditioningOutput
        from ..models.control_output import ControlOutput
        from ..models.denoise_mask_output import DenoiseMaskOutput
        from ..models.face_mask_output import FaceMaskOutput
        from ..models.face_off_output import FaceOffOutput
        from ..models.float_collection_output import FloatCollectionOutput
        from ..models.float_generator_output import FloatGeneratorOutput
        from ..models.float_output import FloatOutput
        from ..models.flux_2_klein_lo_ra_loader_output import Flux2KleinLoRALoaderOutput
        from ..models.flux_2_klein_model_loader_output import Flux2KleinModelLoaderOutput
        from ..models.flux_conditioning_collection_output import FluxConditioningCollectionOutput
        from ..models.flux_conditioning_output import FluxConditioningOutput
        from ..models.flux_control_lo_ra_loader_output import FluxControlLoRALoaderOutput
        from ..models.flux_control_net_output import FluxControlNetOutput
        from ..models.flux_fill_output import FluxFillOutput
        from ..models.flux_kontext_output import FluxKontextOutput
        from ..models.flux_lo_ra_loader_output import FluxLoRALoaderOutput
        from ..models.flux_model_loader_output import FluxModelLoaderOutput
        from ..models.flux_redux_output import FluxReduxOutput
        from ..models.gradient_mask_output import GradientMaskOutput
        from ..models.ideal_size_output import IdealSizeOutput
        from ..models.if_invocation_output import IfInvocationOutput
        from ..models.image_collection_output import ImageCollectionOutput
        from ..models.image_generator_output import ImageGeneratorOutput
        from ..models.image_output import ImageOutput
        from ..models.image_panel_coordinate_output import ImagePanelCoordinateOutput
        from ..models.integer_collection_output import IntegerCollectionOutput
        from ..models.integer_generator_output import IntegerGeneratorOutput
        from ..models.integer_output import IntegerOutput
        from ..models.ip_adapter_output import IPAdapterOutput
        from ..models.iterate_invocation_output import IterateInvocationOutput
        from ..models.latents_collection_output import LatentsCollectionOutput
        from ..models.latents_meta_output import LatentsMetaOutput
        from ..models.latents_output import LatentsOutput
        from ..models.lo_ra_loader_output import LoRALoaderOutput
        from ..models.lo_ra_selector_output import LoRASelectorOutput
        from ..models.mask_output import MaskOutput
        from ..models.md_control_list_output import MDControlListOutput
        from ..models.mdip_adapter_list_output import MDIPAdapterListOutput
        from ..models.mdt2i_adapter_list_output import MDT2IAdapterListOutput
        from ..models.metadata_item_output import MetadataItemOutput
        from ..models.metadata_output import MetadataOutput
        from ..models.metadata_to_loras_collection_output import MetadataToLorasCollectionOutput
        from ..models.metadata_to_model_output import MetadataToModelOutput
        from ..models.metadata_to_sdxl_model_output import MetadataToSDXLModelOutput
        from ..models.model_identifier_output import ModelIdentifierOutput
        from ..models.model_loader_output import ModelLoaderOutput
        from ..models.noise_output import NoiseOutput
        from ..models.pair_tile_image_output import PairTileImageOutput
        from ..models.pbr_maps_output import PBRMapsOutput
        from ..models.prompt_template_output import PromptTemplateOutput
        from ..models.qwen_image_conditioning_output import QwenImageConditioningOutput
        from ..models.qwen_image_lo_ra_loader_output import QwenImageLoRALoaderOutput
        from ..models.qwen_image_model_loader_output import QwenImageModelLoaderOutput
        from ..models.scheduler_output import SchedulerOutput
        from ..models.sd3_conditioning_output import SD3ConditioningOutput
        from ..models.sd_3_model_loader_output import Sd3ModelLoaderOutput
        from ..models.sdxl_lo_ra_loader_output import SDXLLoRALoaderOutput
        from ..models.sdxl_model_loader_output import SDXLModelLoaderOutput
        from ..models.sdxl_refiner_model_loader_output import SDXLRefinerModelLoaderOutput
        from ..models.seamless_mode_output import SeamlessModeOutput
        from ..models.string_2_output import String2Output
        from ..models.string_collection_output import StringCollectionOutput
        from ..models.string_generator_output import StringGeneratorOutput
        from ..models.string_output import StringOutput
        from ..models.string_pos_neg_output import StringPosNegOutput
        from ..models.t2i_adapter_output import T2IAdapterOutput
        from ..models.tile_to_properties_output import TileToPropertiesOutput
        from ..models.u_net_output import UNetOutput
        from ..models.vae_output import VAEOutput
        from ..models.z_image_conditioning_output import ZImageConditioningOutput
        from ..models.z_image_control_output import ZImageControlOutput
        from ..models.z_image_lo_ra_loader_output import ZImageLoRALoaderOutput
        from ..models.z_image_model_loader_output import ZImageModelLoaderOutput

        d = dict(src_dict)
        graph_execution_state_results = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                AnimaConditioningOutput
                | AnimaLoRALoaderOutput
                | AnimaModelLoaderOutput
                | BooleanCollectionOutput
                | BooleanOutput
                | BoundingBoxCollectionOutput
                | BoundingBoxOutput
                | CalculateImageTilesOutput
                | CLIPOutput
                | CLIPSkipInvocationOutput
                | CogView4ConditioningOutput
                | CogView4ModelLoaderOutput
                | CollectInvocationOutput
                | ColorCollectionOutput
                | ColorOutput
                | ConditioningCollectionOutput
                | ConditioningOutput
                | ControlOutput
                | DenoiseMaskOutput
                | FaceMaskOutput
                | FaceOffOutput
                | FloatCollectionOutput
                | FloatGeneratorOutput
                | FloatOutput
                | Flux2KleinLoRALoaderOutput
                | Flux2KleinModelLoaderOutput
                | FluxConditioningCollectionOutput
                | FluxConditioningOutput
                | FluxControlLoRALoaderOutput
                | FluxControlNetOutput
                | FluxFillOutput
                | FluxKontextOutput
                | FluxLoRALoaderOutput
                | FluxModelLoaderOutput
                | FluxReduxOutput
                | GradientMaskOutput
                | IdealSizeOutput
                | IfInvocationOutput
                | ImageCollectionOutput
                | ImageGeneratorOutput
                | ImageOutput
                | ImagePanelCoordinateOutput
                | IntegerCollectionOutput
                | IntegerGeneratorOutput
                | IntegerOutput
                | IPAdapterOutput
                | IterateInvocationOutput
                | LatentsCollectionOutput
                | LatentsMetaOutput
                | LatentsOutput
                | LoRALoaderOutput
                | LoRASelectorOutput
                | MaskOutput
                | MDControlListOutput
                | MDIPAdapterListOutput
                | MDT2IAdapterListOutput
                | MetadataItemOutput
                | MetadataOutput
                | MetadataToLorasCollectionOutput
                | MetadataToModelOutput
                | MetadataToSDXLModelOutput
                | ModelIdentifierOutput
                | ModelLoaderOutput
                | NoiseOutput
                | PairTileImageOutput
                | PBRMapsOutput
                | PromptTemplateOutput
                | QwenImageConditioningOutput
                | QwenImageLoRALoaderOutput
                | QwenImageModelLoaderOutput
                | SchedulerOutput
                | SD3ConditioningOutput
                | Sd3ModelLoaderOutput
                | SDXLLoRALoaderOutput
                | SDXLModelLoaderOutput
                | SDXLRefinerModelLoaderOutput
                | SeamlessModeOutput
                | String2Output
                | StringCollectionOutput
                | StringGeneratorOutput
                | StringOutput
                | StringPosNegOutput
                | T2IAdapterOutput
                | TileToPropertiesOutput
                | UNetOutput
                | VAEOutput
                | ZImageConditioningOutput
                | ZImageControlOutput
                | ZImageLoRALoaderOutput
                | ZImageModelLoaderOutput
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = AnimaConditioningOutput.from_dict(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = AnimaLoRALoaderOutput.from_dict(data)

                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = AnimaModelLoaderOutput.from_dict(data)

                    return additional_property_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = BooleanCollectionOutput.from_dict(data)

                    return additional_property_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_4 = BooleanOutput.from_dict(data)

                    return additional_property_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_5 = BoundingBoxCollectionOutput.from_dict(data)

                    return additional_property_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_6 = BoundingBoxOutput.from_dict(data)

                    return additional_property_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_7 = CLIPOutput.from_dict(data)

                    return additional_property_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_8 = CLIPSkipInvocationOutput.from_dict(data)

                    return additional_property_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_9 = CalculateImageTilesOutput.from_dict(data)

                    return additional_property_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_10 = CogView4ConditioningOutput.from_dict(data)

                    return additional_property_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_11 = CogView4ModelLoaderOutput.from_dict(data)

                    return additional_property_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_12 = CollectInvocationOutput.from_dict(data)

                    return additional_property_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_13 = ColorCollectionOutput.from_dict(data)

                    return additional_property_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_14 = ColorOutput.from_dict(data)

                    return additional_property_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_15 = ConditioningCollectionOutput.from_dict(data)

                    return additional_property_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_16 = ConditioningOutput.from_dict(data)

                    return additional_property_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_17 = ControlOutput.from_dict(data)

                    return additional_property_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_18 = DenoiseMaskOutput.from_dict(data)

                    return additional_property_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_19 = FaceMaskOutput.from_dict(data)

                    return additional_property_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_20 = FaceOffOutput.from_dict(data)

                    return additional_property_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_21 = FloatCollectionOutput.from_dict(data)

                    return additional_property_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_22 = FloatGeneratorOutput.from_dict(data)

                    return additional_property_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_23 = FloatOutput.from_dict(data)

                    return additional_property_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_24 = Flux2KleinLoRALoaderOutput.from_dict(data)

                    return additional_property_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_25 = Flux2KleinModelLoaderOutput.from_dict(data)

                    return additional_property_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_26 = FluxConditioningCollectionOutput.from_dict(data)

                    return additional_property_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_27 = FluxConditioningOutput.from_dict(data)

                    return additional_property_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_28 = FluxControlLoRALoaderOutput.from_dict(data)

                    return additional_property_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_29 = FluxControlNetOutput.from_dict(data)

                    return additional_property_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_30 = FluxFillOutput.from_dict(data)

                    return additional_property_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_31 = FluxKontextOutput.from_dict(data)

                    return additional_property_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_32 = FluxLoRALoaderOutput.from_dict(data)

                    return additional_property_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_33 = FluxModelLoaderOutput.from_dict(data)

                    return additional_property_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_34 = FluxReduxOutput.from_dict(data)

                    return additional_property_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_35 = GradientMaskOutput.from_dict(data)

                    return additional_property_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_36 = IPAdapterOutput.from_dict(data)

                    return additional_property_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_37 = IdealSizeOutput.from_dict(data)

                    return additional_property_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_38 = IfInvocationOutput.from_dict(data)

                    return additional_property_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_39 = ImageCollectionOutput.from_dict(data)

                    return additional_property_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_40 = ImageGeneratorOutput.from_dict(data)

                    return additional_property_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_41 = ImageOutput.from_dict(data)

                    return additional_property_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_42 = ImagePanelCoordinateOutput.from_dict(data)

                    return additional_property_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_43 = IntegerCollectionOutput.from_dict(data)

                    return additional_property_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_44 = IntegerGeneratorOutput.from_dict(data)

                    return additional_property_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_45 = IntegerOutput.from_dict(data)

                    return additional_property_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_46 = IterateInvocationOutput.from_dict(data)

                    return additional_property_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_47 = LatentsCollectionOutput.from_dict(data)

                    return additional_property_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_48 = LatentsMetaOutput.from_dict(data)

                    return additional_property_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_49 = LatentsOutput.from_dict(data)

                    return additional_property_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_50 = LoRALoaderOutput.from_dict(data)

                    return additional_property_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_51 = LoRASelectorOutput.from_dict(data)

                    return additional_property_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_52 = MDControlListOutput.from_dict(data)

                    return additional_property_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_53 = MDIPAdapterListOutput.from_dict(data)

                    return additional_property_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_54 = MDT2IAdapterListOutput.from_dict(data)

                    return additional_property_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_55 = MaskOutput.from_dict(data)

                    return additional_property_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_56 = MetadataItemOutput.from_dict(data)

                    return additional_property_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_57 = MetadataOutput.from_dict(data)

                    return additional_property_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_58 = MetadataToLorasCollectionOutput.from_dict(data)

                    return additional_property_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_59 = MetadataToModelOutput.from_dict(data)

                    return additional_property_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_60 = MetadataToSDXLModelOutput.from_dict(data)

                    return additional_property_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_61 = ModelIdentifierOutput.from_dict(data)

                    return additional_property_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_62 = ModelLoaderOutput.from_dict(data)

                    return additional_property_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_63 = NoiseOutput.from_dict(data)

                    return additional_property_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_64 = PBRMapsOutput.from_dict(data)

                    return additional_property_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_65 = PairTileImageOutput.from_dict(data)

                    return additional_property_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_66 = PromptTemplateOutput.from_dict(data)

                    return additional_property_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_67 = QwenImageConditioningOutput.from_dict(data)

                    return additional_property_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_68 = QwenImageLoRALoaderOutput.from_dict(data)

                    return additional_property_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_69 = QwenImageModelLoaderOutput.from_dict(data)

                    return additional_property_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_70 = SD3ConditioningOutput.from_dict(data)

                    return additional_property_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_71 = SDXLLoRALoaderOutput.from_dict(data)

                    return additional_property_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_72 = SDXLModelLoaderOutput.from_dict(data)

                    return additional_property_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_73 = SDXLRefinerModelLoaderOutput.from_dict(data)

                    return additional_property_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_74 = SchedulerOutput.from_dict(data)

                    return additional_property_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_75 = Sd3ModelLoaderOutput.from_dict(data)

                    return additional_property_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_76 = SeamlessModeOutput.from_dict(data)

                    return additional_property_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_77 = String2Output.from_dict(data)

                    return additional_property_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_78 = StringCollectionOutput.from_dict(data)

                    return additional_property_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_79 = StringGeneratorOutput.from_dict(data)

                    return additional_property_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_80 = StringOutput.from_dict(data)

                    return additional_property_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_81 = StringPosNegOutput.from_dict(data)

                    return additional_property_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_82 = T2IAdapterOutput.from_dict(data)

                    return additional_property_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_83 = TileToPropertiesOutput.from_dict(data)

                    return additional_property_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_84 = UNetOutput.from_dict(data)

                    return additional_property_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_85 = VAEOutput.from_dict(data)

                    return additional_property_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_86 = ZImageConditioningOutput.from_dict(data)

                    return additional_property_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_87 = ZImageControlOutput.from_dict(data)

                    return additional_property_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_88 = ZImageLoRALoaderOutput.from_dict(data)

                    return additional_property_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_89 = ZImageModelLoaderOutput.from_dict(data)

                return additional_property_type_89

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        graph_execution_state_results.additional_properties = additional_properties
        return graph_execution_state_results

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> (
        AnimaConditioningOutput
        | AnimaLoRALoaderOutput
        | AnimaModelLoaderOutput
        | BooleanCollectionOutput
        | BooleanOutput
        | BoundingBoxCollectionOutput
        | BoundingBoxOutput
        | CalculateImageTilesOutput
        | CLIPOutput
        | CLIPSkipInvocationOutput
        | CogView4ConditioningOutput
        | CogView4ModelLoaderOutput
        | CollectInvocationOutput
        | ColorCollectionOutput
        | ColorOutput
        | ConditioningCollectionOutput
        | ConditioningOutput
        | ControlOutput
        | DenoiseMaskOutput
        | FaceMaskOutput
        | FaceOffOutput
        | FloatCollectionOutput
        | FloatGeneratorOutput
        | FloatOutput
        | Flux2KleinLoRALoaderOutput
        | Flux2KleinModelLoaderOutput
        | FluxConditioningCollectionOutput
        | FluxConditioningOutput
        | FluxControlLoRALoaderOutput
        | FluxControlNetOutput
        | FluxFillOutput
        | FluxKontextOutput
        | FluxLoRALoaderOutput
        | FluxModelLoaderOutput
        | FluxReduxOutput
        | GradientMaskOutput
        | IdealSizeOutput
        | IfInvocationOutput
        | ImageCollectionOutput
        | ImageGeneratorOutput
        | ImageOutput
        | ImagePanelCoordinateOutput
        | IntegerCollectionOutput
        | IntegerGeneratorOutput
        | IntegerOutput
        | IPAdapterOutput
        | IterateInvocationOutput
        | LatentsCollectionOutput
        | LatentsMetaOutput
        | LatentsOutput
        | LoRALoaderOutput
        | LoRASelectorOutput
        | MaskOutput
        | MDControlListOutput
        | MDIPAdapterListOutput
        | MDT2IAdapterListOutput
        | MetadataItemOutput
        | MetadataOutput
        | MetadataToLorasCollectionOutput
        | MetadataToModelOutput
        | MetadataToSDXLModelOutput
        | ModelIdentifierOutput
        | ModelLoaderOutput
        | NoiseOutput
        | PairTileImageOutput
        | PBRMapsOutput
        | PromptTemplateOutput
        | QwenImageConditioningOutput
        | QwenImageLoRALoaderOutput
        | QwenImageModelLoaderOutput
        | SchedulerOutput
        | SD3ConditioningOutput
        | Sd3ModelLoaderOutput
        | SDXLLoRALoaderOutput
        | SDXLModelLoaderOutput
        | SDXLRefinerModelLoaderOutput
        | SeamlessModeOutput
        | String2Output
        | StringCollectionOutput
        | StringGeneratorOutput
        | StringOutput
        | StringPosNegOutput
        | T2IAdapterOutput
        | TileToPropertiesOutput
        | UNetOutput
        | VAEOutput
        | ZImageConditioningOutput
        | ZImageControlOutput
        | ZImageLoRALoaderOutput
        | ZImageModelLoaderOutput
    ):
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: AnimaConditioningOutput
        | AnimaLoRALoaderOutput
        | AnimaModelLoaderOutput
        | BooleanCollectionOutput
        | BooleanOutput
        | BoundingBoxCollectionOutput
        | BoundingBoxOutput
        | CalculateImageTilesOutput
        | CLIPOutput
        | CLIPSkipInvocationOutput
        | CogView4ConditioningOutput
        | CogView4ModelLoaderOutput
        | CollectInvocationOutput
        | ColorCollectionOutput
        | ColorOutput
        | ConditioningCollectionOutput
        | ConditioningOutput
        | ControlOutput
        | DenoiseMaskOutput
        | FaceMaskOutput
        | FaceOffOutput
        | FloatCollectionOutput
        | FloatGeneratorOutput
        | FloatOutput
        | Flux2KleinLoRALoaderOutput
        | Flux2KleinModelLoaderOutput
        | FluxConditioningCollectionOutput
        | FluxConditioningOutput
        | FluxControlLoRALoaderOutput
        | FluxControlNetOutput
        | FluxFillOutput
        | FluxKontextOutput
        | FluxLoRALoaderOutput
        | FluxModelLoaderOutput
        | FluxReduxOutput
        | GradientMaskOutput
        | IdealSizeOutput
        | IfInvocationOutput
        | ImageCollectionOutput
        | ImageGeneratorOutput
        | ImageOutput
        | ImagePanelCoordinateOutput
        | IntegerCollectionOutput
        | IntegerGeneratorOutput
        | IntegerOutput
        | IPAdapterOutput
        | IterateInvocationOutput
        | LatentsCollectionOutput
        | LatentsMetaOutput
        | LatentsOutput
        | LoRALoaderOutput
        | LoRASelectorOutput
        | MaskOutput
        | MDControlListOutput
        | MDIPAdapterListOutput
        | MDT2IAdapterListOutput
        | MetadataItemOutput
        | MetadataOutput
        | MetadataToLorasCollectionOutput
        | MetadataToModelOutput
        | MetadataToSDXLModelOutput
        | ModelIdentifierOutput
        | ModelLoaderOutput
        | NoiseOutput
        | PairTileImageOutput
        | PBRMapsOutput
        | PromptTemplateOutput
        | QwenImageConditioningOutput
        | QwenImageLoRALoaderOutput
        | QwenImageModelLoaderOutput
        | SchedulerOutput
        | SD3ConditioningOutput
        | Sd3ModelLoaderOutput
        | SDXLLoRALoaderOutput
        | SDXLModelLoaderOutput
        | SDXLRefinerModelLoaderOutput
        | SeamlessModeOutput
        | String2Output
        | StringCollectionOutput
        | StringGeneratorOutput
        | StringOutput
        | StringPosNegOutput
        | T2IAdapterOutput
        | TileToPropertiesOutput
        | UNetOutput
        | VAEOutput
        | ZImageConditioningOutput
        | ZImageControlOutput
        | ZImageLoRALoaderOutput
        | ZImageModelLoaderOutput,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
