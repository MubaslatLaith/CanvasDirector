from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_image_noise import AddImageNoise
    from ..models.add_integers import AddIntegers
    from ..models.add_invisible_watermark import AddInvisibleWatermark
    from ..models.adjust_image_hue import AdjustImageHue
    from ..models.adjust_image_hue_oklch import AdjustImageHueOklch
    from ..models.adjust_image_hue_plus import AdjustImageHuePlus
    from ..models.alibaba_cloud_dash_scope_image_generation import AlibabaCloudDashScopeImageGeneration
    from ..models.alpha_mask_to_tensor import AlphaMaskToTensor
    from ..models.anima_conditioning_output import AnimaConditioningOutput
    from ..models.anima_lo_ra_loader_output import AnimaLoRALoaderOutput
    from ..models.anima_model_loader_output import AnimaModelLoaderOutput
    from ..models.any_model import AnyModel
    from ..models.apply_clip_skip_sd15sdxl import ApplyCLIPSkipSD15SDXL
    from ..models.apply_free_usd15sdxl import ApplyFreeUSD15SDXL
    from ..models.apply_lo_ra_anima import ApplyLoRAAnima
    from ..models.apply_lo_ra_collection_anima import ApplyLoRACollectionAnima
    from ..models.apply_lo_ra_collection_flux import ApplyLoRACollectionFLUX
    from ..models.apply_lo_ra_collection_flux_2_klein import ApplyLoRACollectionFlux2Klein
    from ..models.apply_lo_ra_collection_qwen_image import ApplyLoRACollectionQwenImage
    from ..models.apply_lo_ra_collection_sd15 import ApplyLoRACollectionSD15
    from ..models.apply_lo_ra_collection_sdxl import ApplyLoRACollectionSDXL
    from ..models.apply_lo_ra_collection_z_image import ApplyLoRACollectionZImage
    from ..models.apply_lo_ra_flux_2_klein import ApplyLoRAFlux2Klein
    from ..models.apply_lo_ra_qwen_image import ApplyLoRAQwenImage
    from ..models.apply_lo_raflux import ApplyLoRAFLUX
    from ..models.apply_lo_rasd15 import ApplyLoRASD15
    from ..models.apply_lo_rasdxl import ApplyLoRASDXL
    from ..models.apply_lo_raz_image import ApplyLoRAZImage
    from ..models.apply_mask_to_image import ApplyMaskToImage
    from ..models.apply_seamless_sd15sdxl import ApplySeamlessSD15SDXL
    from ..models.apply_tensor_mask_to_image import ApplyTensorMaskToImage
    from ..models.blank_image import BlankImage
    from ..models.blend_latents import BlendLatents
    from ..models.blur_image import BlurImage
    from ..models.blur_nsfw_image import BlurNSFWImage
    from ..models.boolean_collection_output import BooleanCollectionOutput
    from ..models.boolean_collection_primitive import BooleanCollectionPrimitive
    from ..models.boolean_output import BooleanOutput
    from ..models.boolean_primitive import BooleanPrimitive
    from ..models.bounding_box import BoundingBox
    from ..models.bounding_box_collection_output import BoundingBoxCollectionOutput
    from ..models.bounding_box_output import BoundingBoxOutput
    from ..models.calculate_image_tiles import CalculateImageTiles
    from ..models.calculate_image_tiles_even_split import CalculateImageTilesEvenSplit
    from ..models.calculate_image_tiles_minimum_overlap import CalculateImageTilesMinimumOverlap
    from ..models.calculate_image_tiles_output import CalculateImageTilesOutput
    from ..models.canny_edge_detection import CannyEdgeDetection
    from ..models.canvas_output import CanvasOutput
    from ..models.canvas_paste_back import CanvasPasteBack
    from ..models.canvas_v2_mask_and_crop import CanvasV2MaskAndCrop
    from ..models.center_pad_or_crop_image import CenterPadOrCropImage
    from ..models.clip_output import CLIPOutput
    from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
    from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
    from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
    from ..models.collect_invocation import CollectInvocation
    from ..models.collect_invocation_output import CollectInvocationOutput
    from ..models.color_collection_output import ColorCollectionOutput
    from ..models.color_correct import ColorCorrect
    from ..models.color_map import ColorMap
    from ..models.color_output import ColorOutput
    from ..models.color_primitive import ColorPrimitive
    from ..models.combine_masks import CombineMasks
    from ..models.conditioning_collection_output import ConditioningCollectionOutput
    from ..models.conditioning_collection_primitive import ConditioningCollectionPrimitive
    from ..models.conditioning_output import ConditioningOutput
    from ..models.conditioning_primitive import ConditioningPrimitive
    from ..models.content_shuffle import ContentShuffle
    from ..models.control_lo_raflux import ControlLoRAFLUX
    from ..models.control_net_sd15sd2sdxl import ControlNetSD15SD2SDXL
    from ..models.control_output import ControlOutput
    from ..models.convert_image_mode import ConvertImageMode
    from ..models.core_metadata import CoreMetadata
    from ..models.create_denoise_mask import CreateDenoiseMask
    from ..models.create_gradient_mask import CreateGradientMask
    from ..models.create_latent_noise import CreateLatentNoise
    from ..models.create_rectangle_mask import CreateRectangleMask
    from ..models.crop_image import CropImage
    from ..models.crop_image_to_bounding_box import CropImageToBoundingBox
    from ..models.crop_latents import CropLatents
    from ..models.cv2_infill import CV2Infill
    from ..models.decode_invisible_watermark import DecodeInvisibleWatermark
    from ..models.denoise_anima import DenoiseAnima
    from ..models.denoise_cog_view_4 import DenoiseCogView4
    from ..models.denoise_mask_output import DenoiseMaskOutput
    from ..models.denoise_qwen_image import DenoiseQwenImage
    from ..models.denoise_sd3 import DenoiseSD3
    from ..models.denoise_sd15sdxl import DenoiseSD15SDXL
    from ..models.denoise_sd15sdxl_metadata import DenoiseSD15SDXLMetadata
    from ..models.denoise_z_image import DenoiseZImage
    from ..models.denoise_z_image_metadata import DenoiseZImageMetadata
    from ..models.depth_anything_depth_estimation import DepthAnythingDepthEstimation
    from ..models.divide_integers import DivideIntegers
    from ..models.dw_openpose_detection import DWOpenposeDetection
    from ..models.dynamic_prompt import DynamicPrompt
    from ..models.enhance_image import EnhanceImage
    from ..models.equivalent_achromatic_lightness import EquivalentAchromaticLightness
    from ..models.expand_mask_with_fade import ExpandMaskWithFade
    from ..models.extract_image_channel import ExtractImageChannel
    from ..models.face_identifier import FaceIdentifier
    from ..models.face_mask import FaceMask
    from ..models.face_mask_output import FaceMaskOutput
    from ..models.face_off import FaceOff
    from ..models.face_off_output import FaceOffOutput
    from ..models.float_batch import FloatBatch
    from ..models.float_collection_output import FloatCollectionOutput
    from ..models.float_collection_primitive import FloatCollectionPrimitive
    from ..models.float_generator import FloatGenerator
    from ..models.float_generator_output import FloatGeneratorOutput
    from ..models.float_math import FloatMath
    from ..models.float_output import FloatOutput
    from ..models.float_primitive import FloatPrimitive
    from ..models.float_range import FloatRange
    from ..models.float_to_integer import FloatToInteger
    from ..models.flux2_denoise import FLUX2Denoise
    from ..models.flux_2_klein_lo_ra_loader_output import Flux2KleinLoRALoaderOutput
    from ..models.flux_2_klein_model_loader_output import Flux2KleinModelLoaderOutput
    from ..models.flux_conditioning_collection_output import FluxConditioningCollectionOutput
    from ..models.flux_conditioning_output import FluxConditioningOutput
    from ..models.flux_control_lo_ra_loader_output import FluxControlLoRALoaderOutput
    from ..models.flux_control_net import FLUXControlNet
    from ..models.flux_control_net_output import FluxControlNetOutput
    from ..models.flux_denoise import FLUXDenoise
    from ..models.flux_denoise_metadata import FLUXDenoiseMetadata
    from ..models.flux_fill_conditioning import FLUXFillConditioning
    from ..models.flux_fill_output import FluxFillOutput
    from ..models.flux_kontext_image_prep import FLUXKontextImagePrep
    from ..models.flux_kontext_output import FluxKontextOutput
    from ..models.flux_lo_ra_loader_output import FluxLoRALoaderOutput
    from ..models.flux_model_loader_output import FluxModelLoaderOutput
    from ..models.flux_redux import FLUXRedux
    from ..models.flux_redux_output import FluxReduxOutput
    from ..models.fluxip_adapter import FLUXIPAdapter
    from ..models.gemini_image_generation import GeminiImageGeneration
    from ..models.get_image_mask_bounding_box import GetImageMaskBoundingBox
    from ..models.gradient_mask_output import GradientMaskOutput
    from ..models.grounding_dino_text_prompt_object_detection import GroundingDINOTextPromptObjectDetection
    from ..models.hed_edge_detection import HEDEdgeDetection
    from ..models.heuristic_resize import HeuristicResize
    from ..models.ideal_size_output import IdealSizeOutput
    from ..models.ideal_size_sd15sdxl import IdealSizeSD15SDXL
    from ..models.if_ import If
    from ..models.if_invocation_output import IfInvocationOutput
    from ..models.image_batch import ImageBatch
    from ..models.image_collection_output import ImageCollectionOutput
    from ..models.image_collection_primitive import ImageCollectionPrimitive
    from ..models.image_compositor import ImageCompositor
    from ..models.image_dilate_or_erode import ImageDilateOrErode
    from ..models.image_generator import ImageGenerator
    from ..models.image_generator_output import ImageGeneratorOutput
    from ..models.image_layer_blend import ImageLayerBlend
    from ..models.image_mask_to_tensor import ImageMaskToTensor
    from ..models.image_output import ImageOutput
    from ..models.image_panel_coordinate_output import ImagePanelCoordinateOutput
    from ..models.image_panel_layout import ImagePanelLayout
    from ..models.image_primitive import ImagePrimitive
    from ..models.image_to_image import ImageToImage
    from ..models.image_to_image_autoscale import ImageToImageAutoscale
    from ..models.image_to_latents_anima import ImageToLatentsAnima
    from ..models.image_to_latents_cog_view_4 import ImageToLatentsCogView4
    from ..models.image_to_latents_flux import ImageToLatentsFLUX
    from ..models.image_to_latents_flux2 import ImageToLatentsFLUX2
    from ..models.image_to_latents_qwen_image import ImageToLatentsQwenImage
    from ..models.image_to_latents_sd3 import ImageToLatentsSD3
    from ..models.image_to_latents_sd15sdxl import ImageToLatentsSD15SDXL
    from ..models.image_to_latents_z_image import ImageToLatentsZImage
    from ..models.image_value_thresholds import ImageValueThresholds
    from ..models.integer_batch import IntegerBatch
    from ..models.integer_collection_output import IntegerCollectionOutput
    from ..models.integer_collection_primitive import IntegerCollectionPrimitive
    from ..models.integer_generator import IntegerGenerator
    from ..models.integer_generator_output import IntegerGeneratorOutput
    from ..models.integer_math import IntegerMath
    from ..models.integer_output import IntegerOutput
    from ..models.integer_primitive import IntegerPrimitive
    from ..models.integer_range import IntegerRange
    from ..models.integer_range_of_size import IntegerRangeOfSize
    from ..models.inverse_lerp_image import InverseLerpImage
    from ..models.invert_tensor_mask import InvertTensorMask
    from ..models.ip_adapter_output import IPAdapterOutput
    from ..models.ip_adapter_sd15sdxl import IPAdapterSD15SDXL
    from ..models.iterate_invocation import IterateInvocation
    from ..models.iterate_invocation_output import IterateInvocationOutput
    from ..models.kontext_conditioning_flux import KontextConditioningFLUX
    from ..models.l_la_va_one_vision_vllm import LLaVAOneVisionVLLM
    from ..models.la_ma_infill import LaMaInfill
    from ..models.latents_collection_output import LatentsCollectionOutput
    from ..models.latents_collection_primitive import LatentsCollectionPrimitive
    from ..models.latents_meta_output import LatentsMetaOutput
    from ..models.latents_output import LatentsOutput
    from ..models.latents_primitive import LatentsPrimitive
    from ..models.latents_to_image_anima import LatentsToImageAnima
    from ..models.latents_to_image_cog_view_4 import LatentsToImageCogView4
    from ..models.latents_to_image_flux import LatentsToImageFLUX
    from ..models.latents_to_image_flux2 import LatentsToImageFLUX2
    from ..models.latents_to_image_qwen_image import LatentsToImageQwenImage
    from ..models.latents_to_image_sd3 import LatentsToImageSD3
    from ..models.latents_to_image_sd15sdxl import LatentsToImageSD15SDXL
    from ..models.latents_to_image_z_image import LatentsToImageZImage
    from ..models.lerp_image import LerpImage
    from ..models.lineart_anime_edge_detection import LineartAnimeEdgeDetection
    from ..models.lineart_edge_detection import LineartEdgeDetection
    from ..models.lo_ra_loader_output import LoRALoaderOutput
    from ..models.lo_ra_selector_output import LoRASelectorOutput
    from ..models.main_model_anima import MainModelAnima
    from ..models.main_model_cog_view_4 import MainModelCogView4
    from ..models.main_model_flux import MainModelFLUX
    from ..models.main_model_flux_2_klein import MainModelFlux2Klein
    from ..models.main_model_qwen_image import MainModelQwenImage
    from ..models.main_model_sd3 import MainModelSD3
    from ..models.main_model_sd15sd2 import MainModelSD15SD2
    from ..models.main_model_sdxl import MainModelSDXL
    from ..models.main_model_z_image import MainModelZImage
    from ..models.mask_edge import MaskEdge
    from ..models.mask_from_alpha import MaskFromAlpha
    from ..models.mask_from_segmented_image import MaskFromSegmentedImage
    from ..models.mask_output import MaskOutput
    from ..models.md_control_list_output import MDControlListOutput
    from ..models.mdip_adapter_list_output import MDIPAdapterListOutput
    from ..models.mdt2i_adapter_list_output import MDT2IAdapterListOutput
    from ..models.media_pipe_face_detection import MediaPipeFaceDetection
    from ..models.merge_tiles_to_image import MergeTilesToImage
    from ..models.metadata import Metadata
    from ..models.metadata_field_extractor import MetadataFieldExtractor
    from ..models.metadata_from_image import MetadataFromImage
    from ..models.metadata_item import MetadataItem
    from ..models.metadata_item_linked import MetadataItemLinked
    from ..models.metadata_item_output import MetadataItemOutput
    from ..models.metadata_merge import MetadataMerge
    from ..models.metadata_output import MetadataOutput
    from ..models.metadata_to_bool import MetadataToBool
    from ..models.metadata_to_bool_collection import MetadataToBoolCollection
    from ..models.metadata_to_control_nets import MetadataToControlNets
    from ..models.metadata_to_float import MetadataToFloat
    from ..models.metadata_to_float_collection import MetadataToFloatCollection
    from ..models.metadata_to_integer import MetadataToInteger
    from ..models.metadata_to_integer_collection import MetadataToIntegerCollection
    from ..models.metadata_to_ip_adapters import MetadataToIPAdapters
    from ..models.metadata_to_lo_r_as import MetadataToLoRAs
    from ..models.metadata_to_lo_ra_collection import MetadataToLoRACollection
    from ..models.metadata_to_loras_collection_output import MetadataToLorasCollectionOutput
    from ..models.metadata_to_model import MetadataToModel
    from ..models.metadata_to_model_output import MetadataToModelOutput
    from ..models.metadata_to_scheduler import MetadataToScheduler
    from ..models.metadata_to_sdxl_lo_r_as import MetadataToSDXLLoRAs
    from ..models.metadata_to_sdxl_model import MetadataToSDXLModel
    from ..models.metadata_to_sdxl_model_output import MetadataToSDXLModelOutput
    from ..models.metadata_to_string import MetadataToString
    from ..models.metadata_to_string_collection import MetadataToStringCollection
    from ..models.metadata_to_t2i_adapters import MetadataToT2IAdapters
    from ..models.metadata_to_vae import MetadataToVAE
    from ..models.mlsd_detection import MLSDDetection
    from ..models.model_identifier_output import ModelIdentifierOutput
    from ..models.model_loader_output import ModelLoaderOutput
    from ..models.multiply_image_channel import MultiplyImageChannel
    from ..models.multiply_images import MultiplyImages
    from ..models.multiply_integers import MultiplyIntegers
    from ..models.noise_output import NoiseOutput
    from ..models.normal_map import NormalMap
    from ..models.offset_image_channel import OffsetImageChannel
    from ..models.open_ai_image_generation import OpenAIImageGeneration
    from ..models.open_cv_inpaint import OpenCVInpaint
    from ..models.pair_tile_image_output import PairTileImageOutput
    from ..models.pair_tile_with_image import PairTileWithImage
    from ..models.paste_image import PasteImage
    from ..models.paste_image_into_bounding_box import PasteImageIntoBoundingBox
    from ..models.patch_match_infill import PatchMatchInfill
    from ..models.pbr_maps import PBRMaps
    from ..models.pbr_maps_output import PBRMapsOutput
    from ..models.pi_di_net_edge_detection import PiDiNetEdgeDetection
    from ..models.prompt_anima import PromptAnima
    from ..models.prompt_cog_view_4 import PromptCogView4
    from ..models.prompt_flux import PromptFLUX
    from ..models.prompt_flux_2_klein import PromptFlux2Klein
    from ..models.prompt_qwen_image import PromptQwenImage
    from ..models.prompt_sd3 import PromptSD3
    from ..models.prompt_sd15 import PromptSD15
    from ..models.prompt_sdxl import PromptSDXL
    from ..models.prompt_sdxl_refiner import PromptSDXLRefiner
    from ..models.prompt_template import PromptTemplate
    from ..models.prompt_template_output import PromptTemplateOutput
    from ..models.prompt_z_image import PromptZImage
    from ..models.prompts_from_file import PromptsFromFile
    from ..models.qwen_image_conditioning_output import QwenImageConditioningOutput
    from ..models.qwen_image_lo_ra_loader_output import QwenImageLoRALoaderOutput
    from ..models.qwen_image_model_loader_output import QwenImageModelLoaderOutput
    from ..models.random_float import RandomFloat
    from ..models.random_integer import RandomInteger
    from ..models.random_range import RandomRange
    from ..models.refiner_model_sdxl import RefinerModelSDXL
    from ..models.resize_image import ResizeImage
    from ..models.resize_latents import ResizeLatents
    from ..models.round_float import RoundFloat
    from ..models.save_image import SaveImage
    from ..models.save_image_gallery_file_export import SaveImageGalleryFileExport
    from ..models.scale_image import ScaleImage
    from ..models.scale_latents import ScaleLatents
    from ..models.scheduler import Scheduler
    from ..models.scheduler_output import SchedulerOutput
    from ..models.sd3_conditioning_output import SD3ConditioningOutput
    from ..models.sd_3_model_loader_output import Sd3ModelLoaderOutput
    from ..models.sdxl_lo_ra_loader_output import SDXLLoRALoaderOutput
    from ..models.sdxl_model_loader_output import SDXLModelLoaderOutput
    from ..models.sdxl_refiner_model_loader_output import SDXLRefinerModelLoaderOutput
    from ..models.seamless_mode_output import SeamlessModeOutput
    from ..models.seed_variance_enhancer_z_image import SeedVarianceEnhancerZImage
    from ..models.seedream_image_generation import SeedreamImageGeneration
    from ..models.segment_anything import SegmentAnything
    from ..models.select_lo_ra import SelectLoRA
    from ..models.show_image import ShowImage
    from ..models.solid_color_infill import SolidColorInfill
    from ..models.string_2_output import String2Output
    from ..models.string_batch import StringBatch
    from ..models.string_collection_output import StringCollectionOutput
    from ..models.string_collection_primitive import StringCollectionPrimitive
    from ..models.string_generator import StringGenerator
    from ..models.string_generator_output import StringGeneratorOutput
    from ..models.string_join import StringJoin
    from ..models.string_join_three import StringJoinThree
    from ..models.string_output import StringOutput
    from ..models.string_pos_neg_output import StringPosNegOutput
    from ..models.string_primitive import StringPrimitive
    from ..models.string_replace import StringReplace
    from ..models.string_split import StringSplit
    from ..models.string_split_negative import StringSplitNegative
    from ..models.subtract_integers import SubtractIntegers
    from ..models.t2i_adapter_output import T2IAdapterOutput
    from ..models.t2i_adapter_sd15sdxl import T2IAdapterSD15SDXL
    from ..models.tensor_mask_to_image import TensorMaskToImage
    from ..models.text_llm import TextLLM
    from ..models.tile_infill import TileInfill
    from ..models.tile_to_properties import TileToProperties
    from ..models.tile_to_properties_output import TileToPropertiesOutput
    from ..models.tiled_multi_diffusion_denoise_sd15sdxl import TiledMultiDiffusionDenoiseSD15SDXL
    from ..models.u_net_output import UNetOutput
    from ..models.unsharp_mask import UnsharpMask
    from ..models.unsharp_mask_oklab import UnsharpMaskOklab
    from ..models.upscale_real_esrgan import UpscaleRealESRGAN
    from ..models.vae_model_sd15sd2sdxlsd3flux import VAEModelSD15SD2SDXLSD3FLUX
    from ..models.vae_output import VAEOutput
    from ..models.z_image_conditioning_output import ZImageConditioningOutput
    from ..models.z_image_control_net import ZImageControlNet
    from ..models.z_image_control_output import ZImageControlOutput
    from ..models.z_image_lo_ra_loader_output import ZImageLoRALoaderOutput
    from ..models.z_image_model_loader_output import ZImageModelLoaderOutput


T = TypeVar("T", bound="InvocationCompleteEvent")


@_attrs_define
class InvocationCompleteEvent:
    """Event model for invocation_complete

    Attributes:
        timestamp (int): The timestamp of the event
        queue_id (str): The ID of the queue
        item_id (int): The ID of the queue item
        batch_id (str): The ID of the queue batch
        origin (None | str): The origin of the queue item
        destination (None | str): The destination of the queue item
        user_id (str): The ID of the user who created the queue item Default: 'system'.
        session_id (str): The ID of the session (aka graph execution state)
        invocation (AddImageNoise | AddIntegers | AddInvisibleWatermark | AdjustImageHue | AdjustImageHueOklch |
            AdjustImageHuePlus | AlibabaCloudDashScopeImageGeneration | AlphaMaskToTensor | AnyModel | ApplyCLIPSkipSD15SDXL
            | ApplyFreeUSD15SDXL | ApplyLoRAAnima | ApplyLoRACollectionAnima | ApplyLoRACollectionFLUX |
            ApplyLoRACollectionFlux2Klein | ApplyLoRACollectionQwenImage | ApplyLoRACollectionSD15 | ApplyLoRACollectionSDXL
            | ApplyLoRACollectionZImage | ApplyLoRAFLUX | ApplyLoRAFlux2Klein | ApplyLoRAQwenImage | ApplyLoRASD15 |
            ApplyLoRASDXL | ApplyLoRAZImage | ApplyMaskToImage | ApplySeamlessSD15SDXL | ApplyTensorMaskToImage | BlankImage
            | BlendLatents | BlurImage | BlurNSFWImage | BooleanCollectionPrimitive | BooleanPrimitive | BoundingBox |
            CalculateImageTiles | CalculateImageTilesEvenSplit | CalculateImageTilesMinimumOverlap | CannyEdgeDetection |
            CanvasOutput | CanvasPasteBack | CanvasV2MaskAndCrop | CenterPadOrCropImage | CollectInvocation | ColorCorrect |
            ColorMap | ColorPrimitive | CombineMasks | ConditioningCollectionPrimitive | ConditioningPrimitive |
            ContentShuffle | ControlLoRAFLUX | ControlNetSD15SD2SDXL | ConvertImageMode | CoreMetadata | CreateDenoiseMask |
            CreateGradientMask | CreateLatentNoise | CreateRectangleMask | CropImage | CropImageToBoundingBox | CropLatents
            | CV2Infill | DecodeInvisibleWatermark | DenoiseAnima | DenoiseCogView4 | DenoiseQwenImage | DenoiseSD15SDXL |
            DenoiseSD15SDXLMetadata | DenoiseSD3 | DenoiseZImage | DenoiseZImageMetadata | DepthAnythingDepthEstimation |
            DivideIntegers | DWOpenposeDetection | DynamicPrompt | EnhanceImage | EquivalentAchromaticLightness |
            ExpandMaskWithFade | ExtractImageChannel | FaceIdentifier | FaceMask | FaceOff | FloatBatch |
            FloatCollectionPrimitive | FloatGenerator | FloatMath | FloatPrimitive | FloatRange | FloatToInteger |
            FLUX2Denoise | FLUXControlNet | FLUXDenoise | FLUXDenoiseMetadata | FLUXFillConditioning | FLUXIPAdapter |
            FLUXKontextImagePrep | FLUXRedux | GeminiImageGeneration | GetImageMaskBoundingBox |
            GroundingDINOTextPromptObjectDetection | HEDEdgeDetection | HeuristicResize | IdealSizeSD15SDXL | If |
            ImageBatch | ImageCollectionPrimitive | ImageCompositor | ImageDilateOrErode | ImageGenerator | ImageLayerBlend
            | ImageMaskToTensor | ImagePanelLayout | ImagePrimitive | ImageToImage | ImageToImageAutoscale |
            ImageToLatentsAnima | ImageToLatentsCogView4 | ImageToLatentsFLUX | ImageToLatentsFLUX2 |
            ImageToLatentsQwenImage | ImageToLatentsSD15SDXL | ImageToLatentsSD3 | ImageToLatentsZImage |
            ImageValueThresholds | IntegerBatch | IntegerCollectionPrimitive | IntegerGenerator | IntegerMath |
            IntegerPrimitive | IntegerRange | IntegerRangeOfSize | InverseLerpImage | InvertTensorMask | IPAdapterSD15SDXL |
            IterateInvocation | KontextConditioningFLUX | LaMaInfill | LatentsCollectionPrimitive | LatentsPrimitive |
            LatentsToImageAnima | LatentsToImageCogView4 | LatentsToImageFLUX | LatentsToImageFLUX2 |
            LatentsToImageQwenImage | LatentsToImageSD15SDXL | LatentsToImageSD3 | LatentsToImageZImage | LerpImage |
            LineartAnimeEdgeDetection | LineartEdgeDetection | LLaVAOneVisionVLLM | MainModelAnima | MainModelCogView4 |
            MainModelFLUX | MainModelFlux2Klein | MainModelQwenImage | MainModelSD15SD2 | MainModelSD3 | MainModelSDXL |
            MainModelZImage | MaskEdge | MaskFromAlpha | MaskFromSegmentedImage | MediaPipeFaceDetection | MergeTilesToImage
            | Metadata | MetadataFieldExtractor | MetadataFromImage | MetadataItem | MetadataItemLinked | MetadataMerge |
            MetadataToBool | MetadataToBoolCollection | MetadataToControlNets | MetadataToFloat | MetadataToFloatCollection
            | MetadataToInteger | MetadataToIntegerCollection | MetadataToIPAdapters | MetadataToLoRACollection |
            MetadataToLoRAs | MetadataToModel | MetadataToScheduler | MetadataToSDXLLoRAs | MetadataToSDXLModel |
            MetadataToString | MetadataToStringCollection | MetadataToT2IAdapters | MetadataToVAE | MLSDDetection |
            MultiplyImageChannel | MultiplyImages | MultiplyIntegers | NormalMap | OffsetImageChannel |
            OpenAIImageGeneration | OpenCVInpaint | PairTileWithImage | PasteImage | PasteImageIntoBoundingBox |
            PatchMatchInfill | PBRMaps | PiDiNetEdgeDetection | PromptAnima | PromptCogView4 | PromptFLUX | PromptFlux2Klein
            | PromptQwenImage | PromptSD15 | PromptSD3 | PromptSDXL | PromptSDXLRefiner | PromptsFromFile | PromptTemplate |
            PromptZImage | RandomFloat | RandomInteger | RandomRange | RefinerModelSDXL | ResizeImage | ResizeLatents |
            RoundFloat | SaveImage | SaveImageGalleryFileExport | ScaleImage | ScaleLatents | Scheduler |
            SeedreamImageGeneration | SeedVarianceEnhancerZImage | SegmentAnything | SelectLoRA | ShowImage |
            SolidColorInfill | StringBatch | StringCollectionPrimitive | StringGenerator | StringJoin | StringJoinThree |
            StringPrimitive | StringReplace | StringSplit | StringSplitNegative | SubtractIntegers | T2IAdapterSD15SDXL |
            TensorMaskToImage | TextLLM | TiledMultiDiffusionDenoiseSD15SDXL | TileInfill | TileToProperties | UnsharpMask |
            UnsharpMaskOklab | UpscaleRealESRGAN | VAEModelSD15SD2SDXLSD3FLUX | ZImageControlNet): The ID of the invocation
        invocation_source_id (str): The ID of the prepared invocation's source node
        result (AnimaConditioningOutput | AnimaLoRALoaderOutput | AnimaModelLoaderOutput | BooleanCollectionOutput |
            BooleanOutput | BoundingBoxCollectionOutput | BoundingBoxOutput | CalculateImageTilesOutput | CLIPOutput |
            CLIPSkipInvocationOutput | CogView4ConditioningOutput | CogView4ModelLoaderOutput | CollectInvocationOutput |
            ColorCollectionOutput | ColorOutput | ConditioningCollectionOutput | ConditioningOutput | ControlOutput |
            DenoiseMaskOutput | FaceMaskOutput | FaceOffOutput | FloatCollectionOutput | FloatGeneratorOutput | FloatOutput
            | Flux2KleinLoRALoaderOutput | Flux2KleinModelLoaderOutput | FluxConditioningCollectionOutput |
            FluxConditioningOutput | FluxControlLoRALoaderOutput | FluxControlNetOutput | FluxFillOutput | FluxKontextOutput
            | FluxLoRALoaderOutput | FluxModelLoaderOutput | FluxReduxOutput | GradientMaskOutput | IdealSizeOutput |
            IfInvocationOutput | ImageCollectionOutput | ImageGeneratorOutput | ImageOutput | ImagePanelCoordinateOutput |
            IntegerCollectionOutput | IntegerGeneratorOutput | IntegerOutput | IPAdapterOutput | IterateInvocationOutput |
            LatentsCollectionOutput | LatentsMetaOutput | LatentsOutput | LoRALoaderOutput | LoRASelectorOutput | MaskOutput
            | MDControlListOutput | MDIPAdapterListOutput | MDT2IAdapterListOutput | MetadataItemOutput | MetadataOutput |
            MetadataToLorasCollectionOutput | MetadataToModelOutput | MetadataToSDXLModelOutput | ModelIdentifierOutput |
            ModelLoaderOutput | NoiseOutput | PairTileImageOutput | PBRMapsOutput | PromptTemplateOutput |
            QwenImageConditioningOutput | QwenImageLoRALoaderOutput | QwenImageModelLoaderOutput | SchedulerOutput |
            SD3ConditioningOutput | Sd3ModelLoaderOutput | SDXLLoRALoaderOutput | SDXLModelLoaderOutput |
            SDXLRefinerModelLoaderOutput | SeamlessModeOutput | String2Output | StringCollectionOutput |
            StringGeneratorOutput | StringOutput | StringPosNegOutput | T2IAdapterOutput | TileToPropertiesOutput |
            UNetOutput | VAEOutput | ZImageConditioningOutput | ZImageControlOutput | ZImageLoRALoaderOutput |
            ZImageModelLoaderOutput): The result of the invocation
    """

    timestamp: int
    queue_id: str
    item_id: int
    batch_id: str
    origin: None | str
    destination: None | str
    session_id: str
    invocation: (
        AddImageNoise
        | AddIntegers
        | AddInvisibleWatermark
        | AdjustImageHue
        | AdjustImageHueOklch
        | AdjustImageHuePlus
        | AlibabaCloudDashScopeImageGeneration
        | AlphaMaskToTensor
        | AnyModel
        | ApplyCLIPSkipSD15SDXL
        | ApplyFreeUSD15SDXL
        | ApplyLoRAAnima
        | ApplyLoRACollectionAnima
        | ApplyLoRACollectionFLUX
        | ApplyLoRACollectionFlux2Klein
        | ApplyLoRACollectionQwenImage
        | ApplyLoRACollectionSD15
        | ApplyLoRACollectionSDXL
        | ApplyLoRACollectionZImage
        | ApplyLoRAFLUX
        | ApplyLoRAFlux2Klein
        | ApplyLoRAQwenImage
        | ApplyLoRASD15
        | ApplyLoRASDXL
        | ApplyLoRAZImage
        | ApplyMaskToImage
        | ApplySeamlessSD15SDXL
        | ApplyTensorMaskToImage
        | BlankImage
        | BlendLatents
        | BlurImage
        | BlurNSFWImage
        | BooleanCollectionPrimitive
        | BooleanPrimitive
        | BoundingBox
        | CalculateImageTiles
        | CalculateImageTilesEvenSplit
        | CalculateImageTilesMinimumOverlap
        | CannyEdgeDetection
        | CanvasOutput
        | CanvasPasteBack
        | CanvasV2MaskAndCrop
        | CenterPadOrCropImage
        | CollectInvocation
        | ColorCorrect
        | ColorMap
        | ColorPrimitive
        | CombineMasks
        | ConditioningCollectionPrimitive
        | ConditioningPrimitive
        | ContentShuffle
        | ControlLoRAFLUX
        | ControlNetSD15SD2SDXL
        | ConvertImageMode
        | CoreMetadata
        | CreateDenoiseMask
        | CreateGradientMask
        | CreateLatentNoise
        | CreateRectangleMask
        | CropImage
        | CropImageToBoundingBox
        | CropLatents
        | CV2Infill
        | DecodeInvisibleWatermark
        | DenoiseAnima
        | DenoiseCogView4
        | DenoiseQwenImage
        | DenoiseSD15SDXL
        | DenoiseSD15SDXLMetadata
        | DenoiseSD3
        | DenoiseZImage
        | DenoiseZImageMetadata
        | DepthAnythingDepthEstimation
        | DivideIntegers
        | DWOpenposeDetection
        | DynamicPrompt
        | EnhanceImage
        | EquivalentAchromaticLightness
        | ExpandMaskWithFade
        | ExtractImageChannel
        | FaceIdentifier
        | FaceMask
        | FaceOff
        | FloatBatch
        | FloatCollectionPrimitive
        | FloatGenerator
        | FloatMath
        | FloatPrimitive
        | FloatRange
        | FloatToInteger
        | FLUX2Denoise
        | FLUXControlNet
        | FLUXDenoise
        | FLUXDenoiseMetadata
        | FLUXFillConditioning
        | FLUXIPAdapter
        | FLUXKontextImagePrep
        | FLUXRedux
        | GeminiImageGeneration
        | GetImageMaskBoundingBox
        | GroundingDINOTextPromptObjectDetection
        | HEDEdgeDetection
        | HeuristicResize
        | IdealSizeSD15SDXL
        | If
        | ImageBatch
        | ImageCollectionPrimitive
        | ImageCompositor
        | ImageDilateOrErode
        | ImageGenerator
        | ImageLayerBlend
        | ImageMaskToTensor
        | ImagePanelLayout
        | ImagePrimitive
        | ImageToImage
        | ImageToImageAutoscale
        | ImageToLatentsAnima
        | ImageToLatentsCogView4
        | ImageToLatentsFLUX
        | ImageToLatentsFLUX2
        | ImageToLatentsQwenImage
        | ImageToLatentsSD15SDXL
        | ImageToLatentsSD3
        | ImageToLatentsZImage
        | ImageValueThresholds
        | IntegerBatch
        | IntegerCollectionPrimitive
        | IntegerGenerator
        | IntegerMath
        | IntegerPrimitive
        | IntegerRange
        | IntegerRangeOfSize
        | InverseLerpImage
        | InvertTensorMask
        | IPAdapterSD15SDXL
        | IterateInvocation
        | KontextConditioningFLUX
        | LaMaInfill
        | LatentsCollectionPrimitive
        | LatentsPrimitive
        | LatentsToImageAnima
        | LatentsToImageCogView4
        | LatentsToImageFLUX
        | LatentsToImageFLUX2
        | LatentsToImageQwenImage
        | LatentsToImageSD15SDXL
        | LatentsToImageSD3
        | LatentsToImageZImage
        | LerpImage
        | LineartAnimeEdgeDetection
        | LineartEdgeDetection
        | LLaVAOneVisionVLLM
        | MainModelAnima
        | MainModelCogView4
        | MainModelFLUX
        | MainModelFlux2Klein
        | MainModelQwenImage
        | MainModelSD15SD2
        | MainModelSD3
        | MainModelSDXL
        | MainModelZImage
        | MaskEdge
        | MaskFromAlpha
        | MaskFromSegmentedImage
        | MediaPipeFaceDetection
        | MergeTilesToImage
        | Metadata
        | MetadataFieldExtractor
        | MetadataFromImage
        | MetadataItem
        | MetadataItemLinked
        | MetadataMerge
        | MetadataToBool
        | MetadataToBoolCollection
        | MetadataToControlNets
        | MetadataToFloat
        | MetadataToFloatCollection
        | MetadataToInteger
        | MetadataToIntegerCollection
        | MetadataToIPAdapters
        | MetadataToLoRACollection
        | MetadataToLoRAs
        | MetadataToModel
        | MetadataToScheduler
        | MetadataToSDXLLoRAs
        | MetadataToSDXLModel
        | MetadataToString
        | MetadataToStringCollection
        | MetadataToT2IAdapters
        | MetadataToVAE
        | MLSDDetection
        | MultiplyImageChannel
        | MultiplyImages
        | MultiplyIntegers
        | NormalMap
        | OffsetImageChannel
        | OpenAIImageGeneration
        | OpenCVInpaint
        | PairTileWithImage
        | PasteImage
        | PasteImageIntoBoundingBox
        | PatchMatchInfill
        | PBRMaps
        | PiDiNetEdgeDetection
        | PromptAnima
        | PromptCogView4
        | PromptFLUX
        | PromptFlux2Klein
        | PromptQwenImage
        | PromptSD15
        | PromptSD3
        | PromptSDXL
        | PromptSDXLRefiner
        | PromptsFromFile
        | PromptTemplate
        | PromptZImage
        | RandomFloat
        | RandomInteger
        | RandomRange
        | RefinerModelSDXL
        | ResizeImage
        | ResizeLatents
        | RoundFloat
        | SaveImage
        | SaveImageGalleryFileExport
        | ScaleImage
        | ScaleLatents
        | Scheduler
        | SeedreamImageGeneration
        | SeedVarianceEnhancerZImage
        | SegmentAnything
        | SelectLoRA
        | ShowImage
        | SolidColorInfill
        | StringBatch
        | StringCollectionPrimitive
        | StringGenerator
        | StringJoin
        | StringJoinThree
        | StringPrimitive
        | StringReplace
        | StringSplit
        | StringSplitNegative
        | SubtractIntegers
        | T2IAdapterSD15SDXL
        | TensorMaskToImage
        | TextLLM
        | TiledMultiDiffusionDenoiseSD15SDXL
        | TileInfill
        | TileToProperties
        | UnsharpMask
        | UnsharpMaskOklab
        | UpscaleRealESRGAN
        | VAEModelSD15SD2SDXLSD3FLUX
        | ZImageControlNet
    )
    invocation_source_id: str
    result: (
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
    )
    user_id: str = "system"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_image_noise import AddImageNoise
        from ..models.add_integers import AddIntegers
        from ..models.add_invisible_watermark import AddInvisibleWatermark
        from ..models.adjust_image_hue import AdjustImageHue
        from ..models.adjust_image_hue_oklch import AdjustImageHueOklch
        from ..models.adjust_image_hue_plus import AdjustImageHuePlus
        from ..models.alibaba_cloud_dash_scope_image_generation import AlibabaCloudDashScopeImageGeneration
        from ..models.alpha_mask_to_tensor import AlphaMaskToTensor
        from ..models.anima_conditioning_output import AnimaConditioningOutput
        from ..models.anima_lo_ra_loader_output import AnimaLoRALoaderOutput
        from ..models.anima_model_loader_output import AnimaModelLoaderOutput
        from ..models.any_model import AnyModel
        from ..models.apply_clip_skip_sd15sdxl import ApplyCLIPSkipSD15SDXL
        from ..models.apply_free_usd15sdxl import ApplyFreeUSD15SDXL
        from ..models.apply_lo_ra_anima import ApplyLoRAAnima
        from ..models.apply_lo_ra_collection_anima import ApplyLoRACollectionAnima
        from ..models.apply_lo_ra_collection_flux import ApplyLoRACollectionFLUX
        from ..models.apply_lo_ra_collection_flux_2_klein import ApplyLoRACollectionFlux2Klein
        from ..models.apply_lo_ra_collection_qwen_image import ApplyLoRACollectionQwenImage
        from ..models.apply_lo_ra_collection_sd15 import ApplyLoRACollectionSD15
        from ..models.apply_lo_ra_collection_sdxl import ApplyLoRACollectionSDXL
        from ..models.apply_lo_ra_collection_z_image import ApplyLoRACollectionZImage
        from ..models.apply_lo_ra_flux_2_klein import ApplyLoRAFlux2Klein
        from ..models.apply_lo_ra_qwen_image import ApplyLoRAQwenImage
        from ..models.apply_lo_raflux import ApplyLoRAFLUX
        from ..models.apply_lo_rasd15 import ApplyLoRASD15
        from ..models.apply_lo_rasdxl import ApplyLoRASDXL
        from ..models.apply_lo_raz_image import ApplyLoRAZImage
        from ..models.apply_mask_to_image import ApplyMaskToImage
        from ..models.apply_seamless_sd15sdxl import ApplySeamlessSD15SDXL
        from ..models.apply_tensor_mask_to_image import ApplyTensorMaskToImage
        from ..models.blank_image import BlankImage
        from ..models.blend_latents import BlendLatents
        from ..models.blur_image import BlurImage
        from ..models.blur_nsfw_image import BlurNSFWImage
        from ..models.boolean_collection_output import BooleanCollectionOutput
        from ..models.boolean_collection_primitive import BooleanCollectionPrimitive
        from ..models.boolean_output import BooleanOutput
        from ..models.boolean_primitive import BooleanPrimitive
        from ..models.bounding_box import BoundingBox
        from ..models.bounding_box_collection_output import BoundingBoxCollectionOutput
        from ..models.bounding_box_output import BoundingBoxOutput
        from ..models.calculate_image_tiles import CalculateImageTiles
        from ..models.calculate_image_tiles_even_split import CalculateImageTilesEvenSplit
        from ..models.calculate_image_tiles_minimum_overlap import CalculateImageTilesMinimumOverlap
        from ..models.calculate_image_tiles_output import CalculateImageTilesOutput
        from ..models.canny_edge_detection import CannyEdgeDetection
        from ..models.canvas_output import CanvasOutput
        from ..models.canvas_paste_back import CanvasPasteBack
        from ..models.canvas_v2_mask_and_crop import CanvasV2MaskAndCrop
        from ..models.center_pad_or_crop_image import CenterPadOrCropImage
        from ..models.clip_output import CLIPOutput
        from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
        from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
        from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
        from ..models.collect_invocation import CollectInvocation
        from ..models.collect_invocation_output import CollectInvocationOutput
        from ..models.color_collection_output import ColorCollectionOutput
        from ..models.color_correct import ColorCorrect
        from ..models.color_map import ColorMap
        from ..models.color_output import ColorOutput
        from ..models.color_primitive import ColorPrimitive
        from ..models.combine_masks import CombineMasks
        from ..models.conditioning_collection_output import ConditioningCollectionOutput
        from ..models.conditioning_collection_primitive import ConditioningCollectionPrimitive
        from ..models.conditioning_output import ConditioningOutput
        from ..models.conditioning_primitive import ConditioningPrimitive
        from ..models.content_shuffle import ContentShuffle
        from ..models.control_lo_raflux import ControlLoRAFLUX
        from ..models.control_net_sd15sd2sdxl import ControlNetSD15SD2SDXL
        from ..models.control_output import ControlOutput
        from ..models.convert_image_mode import ConvertImageMode
        from ..models.core_metadata import CoreMetadata
        from ..models.create_denoise_mask import CreateDenoiseMask
        from ..models.create_gradient_mask import CreateGradientMask
        from ..models.create_latent_noise import CreateLatentNoise
        from ..models.create_rectangle_mask import CreateRectangleMask
        from ..models.crop_image import CropImage
        from ..models.crop_image_to_bounding_box import CropImageToBoundingBox
        from ..models.crop_latents import CropLatents
        from ..models.cv2_infill import CV2Infill
        from ..models.decode_invisible_watermark import DecodeInvisibleWatermark
        from ..models.denoise_anima import DenoiseAnima
        from ..models.denoise_cog_view_4 import DenoiseCogView4
        from ..models.denoise_mask_output import DenoiseMaskOutput
        from ..models.denoise_qwen_image import DenoiseQwenImage
        from ..models.denoise_sd3 import DenoiseSD3
        from ..models.denoise_sd15sdxl import DenoiseSD15SDXL
        from ..models.denoise_sd15sdxl_metadata import DenoiseSD15SDXLMetadata
        from ..models.denoise_z_image import DenoiseZImage
        from ..models.denoise_z_image_metadata import DenoiseZImageMetadata
        from ..models.depth_anything_depth_estimation import DepthAnythingDepthEstimation
        from ..models.divide_integers import DivideIntegers
        from ..models.dw_openpose_detection import DWOpenposeDetection
        from ..models.dynamic_prompt import DynamicPrompt
        from ..models.enhance_image import EnhanceImage
        from ..models.equivalent_achromatic_lightness import EquivalentAchromaticLightness
        from ..models.expand_mask_with_fade import ExpandMaskWithFade
        from ..models.extract_image_channel import ExtractImageChannel
        from ..models.face_identifier import FaceIdentifier
        from ..models.face_mask import FaceMask
        from ..models.face_mask_output import FaceMaskOutput
        from ..models.face_off import FaceOff
        from ..models.face_off_output import FaceOffOutput
        from ..models.float_batch import FloatBatch
        from ..models.float_collection_output import FloatCollectionOutput
        from ..models.float_collection_primitive import FloatCollectionPrimitive
        from ..models.float_generator import FloatGenerator
        from ..models.float_generator_output import FloatGeneratorOutput
        from ..models.float_math import FloatMath
        from ..models.float_output import FloatOutput
        from ..models.float_primitive import FloatPrimitive
        from ..models.float_range import FloatRange
        from ..models.float_to_integer import FloatToInteger
        from ..models.flux2_denoise import FLUX2Denoise
        from ..models.flux_2_klein_lo_ra_loader_output import Flux2KleinLoRALoaderOutput
        from ..models.flux_2_klein_model_loader_output import Flux2KleinModelLoaderOutput
        from ..models.flux_conditioning_collection_output import FluxConditioningCollectionOutput
        from ..models.flux_conditioning_output import FluxConditioningOutput
        from ..models.flux_control_lo_ra_loader_output import FluxControlLoRALoaderOutput
        from ..models.flux_control_net import FLUXControlNet
        from ..models.flux_control_net_output import FluxControlNetOutput
        from ..models.flux_denoise import FLUXDenoise
        from ..models.flux_denoise_metadata import FLUXDenoiseMetadata
        from ..models.flux_fill_conditioning import FLUXFillConditioning
        from ..models.flux_fill_output import FluxFillOutput
        from ..models.flux_kontext_image_prep import FLUXKontextImagePrep
        from ..models.flux_kontext_output import FluxKontextOutput
        from ..models.flux_lo_ra_loader_output import FluxLoRALoaderOutput
        from ..models.flux_model_loader_output import FluxModelLoaderOutput
        from ..models.flux_redux import FLUXRedux
        from ..models.flux_redux_output import FluxReduxOutput
        from ..models.fluxip_adapter import FLUXIPAdapter
        from ..models.gemini_image_generation import GeminiImageGeneration
        from ..models.get_image_mask_bounding_box import GetImageMaskBoundingBox
        from ..models.gradient_mask_output import GradientMaskOutput
        from ..models.grounding_dino_text_prompt_object_detection import GroundingDINOTextPromptObjectDetection
        from ..models.hed_edge_detection import HEDEdgeDetection
        from ..models.heuristic_resize import HeuristicResize
        from ..models.ideal_size_output import IdealSizeOutput
        from ..models.ideal_size_sd15sdxl import IdealSizeSD15SDXL
        from ..models.if_ import If
        from ..models.if_invocation_output import IfInvocationOutput
        from ..models.image_batch import ImageBatch
        from ..models.image_collection_output import ImageCollectionOutput
        from ..models.image_collection_primitive import ImageCollectionPrimitive
        from ..models.image_compositor import ImageCompositor
        from ..models.image_dilate_or_erode import ImageDilateOrErode
        from ..models.image_generator import ImageGenerator
        from ..models.image_generator_output import ImageGeneratorOutput
        from ..models.image_layer_blend import ImageLayerBlend
        from ..models.image_mask_to_tensor import ImageMaskToTensor
        from ..models.image_output import ImageOutput
        from ..models.image_panel_coordinate_output import ImagePanelCoordinateOutput
        from ..models.image_panel_layout import ImagePanelLayout
        from ..models.image_primitive import ImagePrimitive
        from ..models.image_to_image import ImageToImage
        from ..models.image_to_image_autoscale import ImageToImageAutoscale
        from ..models.image_to_latents_anima import ImageToLatentsAnima
        from ..models.image_to_latents_cog_view_4 import ImageToLatentsCogView4
        from ..models.image_to_latents_flux import ImageToLatentsFLUX
        from ..models.image_to_latents_flux2 import ImageToLatentsFLUX2
        from ..models.image_to_latents_qwen_image import ImageToLatentsQwenImage
        from ..models.image_to_latents_sd3 import ImageToLatentsSD3
        from ..models.image_to_latents_sd15sdxl import ImageToLatentsSD15SDXL
        from ..models.image_to_latents_z_image import ImageToLatentsZImage
        from ..models.image_value_thresholds import ImageValueThresholds
        from ..models.integer_batch import IntegerBatch
        from ..models.integer_collection_output import IntegerCollectionOutput
        from ..models.integer_collection_primitive import IntegerCollectionPrimitive
        from ..models.integer_generator import IntegerGenerator
        from ..models.integer_generator_output import IntegerGeneratorOutput
        from ..models.integer_math import IntegerMath
        from ..models.integer_output import IntegerOutput
        from ..models.integer_primitive import IntegerPrimitive
        from ..models.integer_range import IntegerRange
        from ..models.integer_range_of_size import IntegerRangeOfSize
        from ..models.inverse_lerp_image import InverseLerpImage
        from ..models.invert_tensor_mask import InvertTensorMask
        from ..models.ip_adapter_output import IPAdapterOutput
        from ..models.ip_adapter_sd15sdxl import IPAdapterSD15SDXL
        from ..models.iterate_invocation import IterateInvocation
        from ..models.iterate_invocation_output import IterateInvocationOutput
        from ..models.kontext_conditioning_flux import KontextConditioningFLUX
        from ..models.l_la_va_one_vision_vllm import LLaVAOneVisionVLLM
        from ..models.la_ma_infill import LaMaInfill
        from ..models.latents_collection_output import LatentsCollectionOutput
        from ..models.latents_collection_primitive import LatentsCollectionPrimitive
        from ..models.latents_meta_output import LatentsMetaOutput
        from ..models.latents_output import LatentsOutput
        from ..models.latents_primitive import LatentsPrimitive
        from ..models.latents_to_image_anima import LatentsToImageAnima
        from ..models.latents_to_image_cog_view_4 import LatentsToImageCogView4
        from ..models.latents_to_image_flux import LatentsToImageFLUX
        from ..models.latents_to_image_flux2 import LatentsToImageFLUX2
        from ..models.latents_to_image_qwen_image import LatentsToImageQwenImage
        from ..models.latents_to_image_sd3 import LatentsToImageSD3
        from ..models.latents_to_image_sd15sdxl import LatentsToImageSD15SDXL
        from ..models.latents_to_image_z_image import LatentsToImageZImage
        from ..models.lerp_image import LerpImage
        from ..models.lineart_anime_edge_detection import LineartAnimeEdgeDetection
        from ..models.lineart_edge_detection import LineartEdgeDetection
        from ..models.lo_ra_loader_output import LoRALoaderOutput
        from ..models.lo_ra_selector_output import LoRASelectorOutput
        from ..models.main_model_anima import MainModelAnima
        from ..models.main_model_cog_view_4 import MainModelCogView4
        from ..models.main_model_flux import MainModelFLUX
        from ..models.main_model_flux_2_klein import MainModelFlux2Klein
        from ..models.main_model_qwen_image import MainModelQwenImage
        from ..models.main_model_sd3 import MainModelSD3
        from ..models.main_model_sd15sd2 import MainModelSD15SD2
        from ..models.main_model_sdxl import MainModelSDXL
        from ..models.main_model_z_image import MainModelZImage
        from ..models.mask_edge import MaskEdge
        from ..models.mask_from_alpha import MaskFromAlpha
        from ..models.mask_from_segmented_image import MaskFromSegmentedImage
        from ..models.mask_output import MaskOutput
        from ..models.md_control_list_output import MDControlListOutput
        from ..models.mdip_adapter_list_output import MDIPAdapterListOutput
        from ..models.mdt2i_adapter_list_output import MDT2IAdapterListOutput
        from ..models.media_pipe_face_detection import MediaPipeFaceDetection
        from ..models.merge_tiles_to_image import MergeTilesToImage
        from ..models.metadata import Metadata
        from ..models.metadata_field_extractor import MetadataFieldExtractor
        from ..models.metadata_from_image import MetadataFromImage
        from ..models.metadata_item import MetadataItem
        from ..models.metadata_item_linked import MetadataItemLinked
        from ..models.metadata_item_output import MetadataItemOutput
        from ..models.metadata_merge import MetadataMerge
        from ..models.metadata_output import MetadataOutput
        from ..models.metadata_to_bool import MetadataToBool
        from ..models.metadata_to_bool_collection import MetadataToBoolCollection
        from ..models.metadata_to_control_nets import MetadataToControlNets
        from ..models.metadata_to_float import MetadataToFloat
        from ..models.metadata_to_float_collection import MetadataToFloatCollection
        from ..models.metadata_to_integer import MetadataToInteger
        from ..models.metadata_to_integer_collection import MetadataToIntegerCollection
        from ..models.metadata_to_ip_adapters import MetadataToIPAdapters
        from ..models.metadata_to_lo_r_as import MetadataToLoRAs
        from ..models.metadata_to_lo_ra_collection import MetadataToLoRACollection
        from ..models.metadata_to_loras_collection_output import MetadataToLorasCollectionOutput
        from ..models.metadata_to_model import MetadataToModel
        from ..models.metadata_to_model_output import MetadataToModelOutput
        from ..models.metadata_to_scheduler import MetadataToScheduler
        from ..models.metadata_to_sdxl_lo_r_as import MetadataToSDXLLoRAs
        from ..models.metadata_to_sdxl_model import MetadataToSDXLModel
        from ..models.metadata_to_sdxl_model_output import MetadataToSDXLModelOutput
        from ..models.metadata_to_string import MetadataToString
        from ..models.metadata_to_string_collection import MetadataToStringCollection
        from ..models.metadata_to_t2i_adapters import MetadataToT2IAdapters
        from ..models.metadata_to_vae import MetadataToVAE
        from ..models.mlsd_detection import MLSDDetection
        from ..models.model_identifier_output import ModelIdentifierOutput
        from ..models.model_loader_output import ModelLoaderOutput
        from ..models.multiply_image_channel import MultiplyImageChannel
        from ..models.multiply_images import MultiplyImages
        from ..models.multiply_integers import MultiplyIntegers
        from ..models.noise_output import NoiseOutput
        from ..models.normal_map import NormalMap
        from ..models.offset_image_channel import OffsetImageChannel
        from ..models.open_ai_image_generation import OpenAIImageGeneration
        from ..models.open_cv_inpaint import OpenCVInpaint
        from ..models.pair_tile_image_output import PairTileImageOutput
        from ..models.pair_tile_with_image import PairTileWithImage
        from ..models.paste_image import PasteImage
        from ..models.paste_image_into_bounding_box import PasteImageIntoBoundingBox
        from ..models.patch_match_infill import PatchMatchInfill
        from ..models.pbr_maps import PBRMaps
        from ..models.pbr_maps_output import PBRMapsOutput
        from ..models.pi_di_net_edge_detection import PiDiNetEdgeDetection
        from ..models.prompt_anima import PromptAnima
        from ..models.prompt_cog_view_4 import PromptCogView4
        from ..models.prompt_flux import PromptFLUX
        from ..models.prompt_flux_2_klein import PromptFlux2Klein
        from ..models.prompt_qwen_image import PromptQwenImage
        from ..models.prompt_sd3 import PromptSD3
        from ..models.prompt_sd15 import PromptSD15
        from ..models.prompt_sdxl import PromptSDXL
        from ..models.prompt_sdxl_refiner import PromptSDXLRefiner
        from ..models.prompt_template import PromptTemplate
        from ..models.prompt_template_output import PromptTemplateOutput
        from ..models.prompts_from_file import PromptsFromFile
        from ..models.qwen_image_conditioning_output import QwenImageConditioningOutput
        from ..models.qwen_image_lo_ra_loader_output import QwenImageLoRALoaderOutput
        from ..models.qwen_image_model_loader_output import QwenImageModelLoaderOutput
        from ..models.random_float import RandomFloat
        from ..models.random_integer import RandomInteger
        from ..models.random_range import RandomRange
        from ..models.refiner_model_sdxl import RefinerModelSDXL
        from ..models.resize_image import ResizeImage
        from ..models.resize_latents import ResizeLatents
        from ..models.round_float import RoundFloat
        from ..models.save_image import SaveImage
        from ..models.save_image_gallery_file_export import SaveImageGalleryFileExport
        from ..models.scale_image import ScaleImage
        from ..models.scale_latents import ScaleLatents
        from ..models.scheduler import Scheduler
        from ..models.scheduler_output import SchedulerOutput
        from ..models.sd3_conditioning_output import SD3ConditioningOutput
        from ..models.sd_3_model_loader_output import Sd3ModelLoaderOutput
        from ..models.sdxl_lo_ra_loader_output import SDXLLoRALoaderOutput
        from ..models.sdxl_model_loader_output import SDXLModelLoaderOutput
        from ..models.sdxl_refiner_model_loader_output import SDXLRefinerModelLoaderOutput
        from ..models.seamless_mode_output import SeamlessModeOutput
        from ..models.seed_variance_enhancer_z_image import SeedVarianceEnhancerZImage
        from ..models.seedream_image_generation import SeedreamImageGeneration
        from ..models.segment_anything import SegmentAnything
        from ..models.select_lo_ra import SelectLoRA
        from ..models.show_image import ShowImage
        from ..models.solid_color_infill import SolidColorInfill
        from ..models.string_2_output import String2Output
        from ..models.string_batch import StringBatch
        from ..models.string_collection_output import StringCollectionOutput
        from ..models.string_collection_primitive import StringCollectionPrimitive
        from ..models.string_generator import StringGenerator
        from ..models.string_generator_output import StringGeneratorOutput
        from ..models.string_join import StringJoin
        from ..models.string_join_three import StringJoinThree
        from ..models.string_output import StringOutput
        from ..models.string_pos_neg_output import StringPosNegOutput
        from ..models.string_primitive import StringPrimitive
        from ..models.string_replace import StringReplace
        from ..models.string_split import StringSplit
        from ..models.string_split_negative import StringSplitNegative
        from ..models.subtract_integers import SubtractIntegers
        from ..models.t2i_adapter_output import T2IAdapterOutput
        from ..models.t2i_adapter_sd15sdxl import T2IAdapterSD15SDXL
        from ..models.tensor_mask_to_image import TensorMaskToImage
        from ..models.text_llm import TextLLM
        from ..models.tile_infill import TileInfill
        from ..models.tile_to_properties import TileToProperties
        from ..models.tile_to_properties_output import TileToPropertiesOutput
        from ..models.tiled_multi_diffusion_denoise_sd15sdxl import TiledMultiDiffusionDenoiseSD15SDXL
        from ..models.u_net_output import UNetOutput
        from ..models.unsharp_mask import UnsharpMask
        from ..models.unsharp_mask_oklab import UnsharpMaskOklab
        from ..models.upscale_real_esrgan import UpscaleRealESRGAN
        from ..models.vae_model_sd15sd2sdxlsd3flux import VAEModelSD15SD2SDXLSD3FLUX
        from ..models.vae_output import VAEOutput
        from ..models.z_image_conditioning_output import ZImageConditioningOutput
        from ..models.z_image_control_net import ZImageControlNet
        from ..models.z_image_control_output import ZImageControlOutput
        from ..models.z_image_lo_ra_loader_output import ZImageLoRALoaderOutput

        timestamp = self.timestamp

        queue_id = self.queue_id

        item_id = self.item_id

        batch_id = self.batch_id

        origin: None | str
        origin = self.origin

        destination: None | str
        destination = self.destination

        user_id = self.user_id

        session_id = self.session_id

        invocation: dict[str, Any]
        if isinstance(self.invocation, AddIntegers):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AlibabaCloudDashScopeImageGeneration):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AlphaMaskToTensor):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseAnima):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsAnima):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageAnima):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRACollectionAnima):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRAAnima):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelAnima):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptAnima):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyTensorMaskToImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyMaskToImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, BlankImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, BlendLatents):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, BooleanCollectionPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, BooleanPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, BoundingBox):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyCLIPSkipSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CV2Infill):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CalculateImageTilesEvenSplit):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CalculateImageTiles):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CalculateImageTilesMinimumOverlap):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CannyEdgeDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CanvasOutput):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CanvasPasteBack):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CanvasV2MaskAndCrop):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CenterPadOrCropImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseCogView4):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsCogView4):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageCogView4):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelCogView4):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptCogView4):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CollectInvocation):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ColorCorrect):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ColorPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ColorMap):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptSD15):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ConditioningCollectionPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ConditioningPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ContentShuffle):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ControlNetSD15SD2SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CoreMetadata):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CreateDenoiseMask):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CreateGradientMask):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CropImageToBoundingBox):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CropLatents):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, OpenCVInpaint):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DWOpenposeDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DecodeInvisibleWatermark):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseSD15SDXLMetadata):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DepthAnythingDepthEstimation):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DivideIntegers):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DynamicPrompt):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, UpscaleRealESRGAN):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ExpandMaskWithFade):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRACollectionFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FaceIdentifier):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FaceMask):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FaceOff):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FloatBatch):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FloatCollectionPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FloatGenerator):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FloatPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FloatRange):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FloatMath):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FloatToInteger):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUX2Denoise):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRACollectionFlux2Klein):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRAFlux2Klein):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelFlux2Klein):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptFlux2Klein):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageFLUX2):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsFLUX2):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ControlLoRAFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUXControlNet):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUXDenoise):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUXDenoiseMetadata):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUXFillConditioning):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUXIPAdapter):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUXKontextImagePrep):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, KontextConditioningFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRAFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, FLUXRedux):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsFLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyFreeUSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, GeminiImageGeneration):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, GetImageMaskBoundingBox):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, GroundingDINOTextPromptObjectDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, HEDEdgeDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, HeuristicResize):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IPAdapterSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IdealSizeSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, If):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageBatch):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, BlurImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ExtractImageChannel):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MultiplyImageChannel):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, OffsetImageChannel):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageCollectionPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ConvertImageMode):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CropImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageGenerator):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AdjustImageHue):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, InverseLerpImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImagePrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LerpImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageMaskToTensor):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MultiplyImages):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, BlurNSFWImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AddImageNoise):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImagePanelLayout):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PasteImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ResizeImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ScaleImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AddInvisibleWatermark):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SolidColorInfill):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PatchMatchInfill):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, TileInfill):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IntegerBatch):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IntegerCollectionPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IntegerGenerator):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IntegerPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IntegerMath):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, InvertTensorMask):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AdjustImageHuePlus):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, EquivalentAchromaticLightness):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageLayerBlend):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageCompositor):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageDilateOrErode):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, EnhanceImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageValueThresholds):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IterateInvocation):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LaMaInfill):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsCollectionPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LineartAnimeEdgeDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LineartEdgeDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LLaVAOneVisionVLLM):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRACollectionSD15):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRASD15):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SelectLoRA):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MLSDDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelSD15SD2):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CombineMasks):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MaskEdge):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MaskFromAlpha):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MaskFromSegmentedImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, TensorMaskToImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MediaPipeFaceDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataMerge):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MergeTilesToImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataFieldExtractor):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataFromImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, Metadata):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataItem):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataItemLinked):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToBoolCollection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToBool):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToControlNets):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToFloatCollection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToFloat):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToIPAdapters):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToIntegerCollection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToInteger):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToLoRACollection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToLoRAs):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToModel):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToSDXLLoRAs):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToSDXLModel):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToScheduler):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToStringCollection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToString):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToT2IAdapters):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MetadataToVAE):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AnyModel):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MultiplyIntegers):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CreateLatentNoise):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, NormalMap):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, UnsharpMaskOklab):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, AdjustImageHueOklch):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, OpenAIImageGeneration):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PBRMaps):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PairTileWithImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PasteImageIntoBoundingBox):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PiDiNetEdgeDetection):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptTemplate):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptsFromFile):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseQwenImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsQwenImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageQwenImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRACollectionQwenImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRAQwenImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelQwenImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptQwenImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, RandomFloat):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, RandomInteger):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, RandomRange):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IntegerRange):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, IntegerRangeOfSize):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, CreateRectangleMask):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ResizeLatents):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, RoundFloat):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseSD3):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsSD3):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageSD3):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptSDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRACollectionSDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRASDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelSDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptSDXLRefiner):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, RefinerModelSDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SaveImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SaveImageGalleryFileExport):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ScaleLatents):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, Scheduler):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelSD3):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, PromptSD3):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplySeamlessSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SeedreamImageGeneration):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SegmentAnything):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ShowImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToImageAutoscale):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringBatch):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringCollectionPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringGenerator):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringPrimitive):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringJoin):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringJoinThree):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringReplace):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringSplit):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, StringSplitNegative):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SubtractIntegers):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, T2IAdapterSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, TextLLM):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, TileToProperties):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, TiledMultiDiffusionDenoiseSD15SDXL):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, UnsharpMask):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, VAEModelSD15SD2SDXLSD3FLUX):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ZImageControlNet):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseZImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, DenoiseZImageMetadata):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ImageToLatentsZImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, LatentsToImageZImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRACollectionZImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, ApplyLoRAZImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, MainModelZImage):
            invocation = self.invocation.to_dict()
        elif isinstance(self.invocation, SeedVarianceEnhancerZImage):
            invocation = self.invocation.to_dict()
        else:
            invocation = self.invocation.to_dict()

        invocation_source_id = self.invocation_source_id

        result: dict[str, Any]
        if isinstance(self.result, AnimaConditioningOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, AnimaLoRALoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, AnimaModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, BooleanCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, BooleanOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, BoundingBoxCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, BoundingBoxOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, CLIPOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, CLIPSkipInvocationOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, CalculateImageTilesOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, CogView4ConditioningOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, CogView4ModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, CollectInvocationOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ColorCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ColorOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ConditioningCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ConditioningOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ControlOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, DenoiseMaskOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FaceMaskOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FaceOffOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FloatCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FloatGeneratorOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FloatOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, Flux2KleinLoRALoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, Flux2KleinModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxConditioningCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxConditioningOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxControlLoRALoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxControlNetOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxFillOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxKontextOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxLoRALoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, FluxReduxOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, GradientMaskOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, IPAdapterOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, IdealSizeOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, IfInvocationOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ImageCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ImageGeneratorOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ImageOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ImagePanelCoordinateOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, IntegerCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, IntegerGeneratorOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, IntegerOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, IterateInvocationOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, LatentsCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, LatentsMetaOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, LatentsOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, LoRALoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, LoRASelectorOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MDControlListOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MDIPAdapterListOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MDT2IAdapterListOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MaskOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MetadataItemOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MetadataOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MetadataToLorasCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MetadataToModelOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, MetadataToSDXLModelOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ModelIdentifierOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, NoiseOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, PBRMapsOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, PairTileImageOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, PromptTemplateOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, QwenImageConditioningOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, QwenImageLoRALoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, QwenImageModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, SD3ConditioningOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, SDXLLoRALoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, SDXLModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, SDXLRefinerModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, SchedulerOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, Sd3ModelLoaderOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, SeamlessModeOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, String2Output):
            result = self.result.to_dict()
        elif isinstance(self.result, StringCollectionOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, StringGeneratorOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, StringOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, StringPosNegOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, T2IAdapterOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, TileToPropertiesOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, UNetOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, VAEOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ZImageConditioningOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ZImageControlOutput):
            result = self.result.to_dict()
        elif isinstance(self.result, ZImageLoRALoaderOutput):
            result = self.result.to_dict()
        else:
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "queue_id": queue_id,
                "item_id": item_id,
                "batch_id": batch_id,
                "origin": origin,
                "destination": destination,
                "user_id": user_id,
                "session_id": session_id,
                "invocation": invocation,
                "invocation_source_id": invocation_source_id,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_image_noise import AddImageNoise
        from ..models.add_integers import AddIntegers
        from ..models.add_invisible_watermark import AddInvisibleWatermark
        from ..models.adjust_image_hue import AdjustImageHue
        from ..models.adjust_image_hue_oklch import AdjustImageHueOklch
        from ..models.adjust_image_hue_plus import AdjustImageHuePlus
        from ..models.alibaba_cloud_dash_scope_image_generation import AlibabaCloudDashScopeImageGeneration
        from ..models.alpha_mask_to_tensor import AlphaMaskToTensor
        from ..models.anima_conditioning_output import AnimaConditioningOutput
        from ..models.anima_lo_ra_loader_output import AnimaLoRALoaderOutput
        from ..models.anima_model_loader_output import AnimaModelLoaderOutput
        from ..models.any_model import AnyModel
        from ..models.apply_clip_skip_sd15sdxl import ApplyCLIPSkipSD15SDXL
        from ..models.apply_free_usd15sdxl import ApplyFreeUSD15SDXL
        from ..models.apply_lo_ra_anima import ApplyLoRAAnima
        from ..models.apply_lo_ra_collection_anima import ApplyLoRACollectionAnima
        from ..models.apply_lo_ra_collection_flux import ApplyLoRACollectionFLUX
        from ..models.apply_lo_ra_collection_flux_2_klein import ApplyLoRACollectionFlux2Klein
        from ..models.apply_lo_ra_collection_qwen_image import ApplyLoRACollectionQwenImage
        from ..models.apply_lo_ra_collection_sd15 import ApplyLoRACollectionSD15
        from ..models.apply_lo_ra_collection_sdxl import ApplyLoRACollectionSDXL
        from ..models.apply_lo_ra_collection_z_image import ApplyLoRACollectionZImage
        from ..models.apply_lo_ra_flux_2_klein import ApplyLoRAFlux2Klein
        from ..models.apply_lo_ra_qwen_image import ApplyLoRAQwenImage
        from ..models.apply_lo_raflux import ApplyLoRAFLUX
        from ..models.apply_lo_rasd15 import ApplyLoRASD15
        from ..models.apply_lo_rasdxl import ApplyLoRASDXL
        from ..models.apply_lo_raz_image import ApplyLoRAZImage
        from ..models.apply_mask_to_image import ApplyMaskToImage
        from ..models.apply_seamless_sd15sdxl import ApplySeamlessSD15SDXL
        from ..models.apply_tensor_mask_to_image import ApplyTensorMaskToImage
        from ..models.blank_image import BlankImage
        from ..models.blend_latents import BlendLatents
        from ..models.blur_image import BlurImage
        from ..models.blur_nsfw_image import BlurNSFWImage
        from ..models.boolean_collection_output import BooleanCollectionOutput
        from ..models.boolean_collection_primitive import BooleanCollectionPrimitive
        from ..models.boolean_output import BooleanOutput
        from ..models.boolean_primitive import BooleanPrimitive
        from ..models.bounding_box import BoundingBox
        from ..models.bounding_box_collection_output import BoundingBoxCollectionOutput
        from ..models.bounding_box_output import BoundingBoxOutput
        from ..models.calculate_image_tiles import CalculateImageTiles
        from ..models.calculate_image_tiles_even_split import CalculateImageTilesEvenSplit
        from ..models.calculate_image_tiles_minimum_overlap import CalculateImageTilesMinimumOverlap
        from ..models.calculate_image_tiles_output import CalculateImageTilesOutput
        from ..models.canny_edge_detection import CannyEdgeDetection
        from ..models.canvas_output import CanvasOutput
        from ..models.canvas_paste_back import CanvasPasteBack
        from ..models.canvas_v2_mask_and_crop import CanvasV2MaskAndCrop
        from ..models.center_pad_or_crop_image import CenterPadOrCropImage
        from ..models.clip_output import CLIPOutput
        from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
        from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
        from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
        from ..models.collect_invocation import CollectInvocation
        from ..models.collect_invocation_output import CollectInvocationOutput
        from ..models.color_collection_output import ColorCollectionOutput
        from ..models.color_correct import ColorCorrect
        from ..models.color_map import ColorMap
        from ..models.color_output import ColorOutput
        from ..models.color_primitive import ColorPrimitive
        from ..models.combine_masks import CombineMasks
        from ..models.conditioning_collection_output import ConditioningCollectionOutput
        from ..models.conditioning_collection_primitive import ConditioningCollectionPrimitive
        from ..models.conditioning_output import ConditioningOutput
        from ..models.conditioning_primitive import ConditioningPrimitive
        from ..models.content_shuffle import ContentShuffle
        from ..models.control_lo_raflux import ControlLoRAFLUX
        from ..models.control_net_sd15sd2sdxl import ControlNetSD15SD2SDXL
        from ..models.control_output import ControlOutput
        from ..models.convert_image_mode import ConvertImageMode
        from ..models.core_metadata import CoreMetadata
        from ..models.create_denoise_mask import CreateDenoiseMask
        from ..models.create_gradient_mask import CreateGradientMask
        from ..models.create_latent_noise import CreateLatentNoise
        from ..models.create_rectangle_mask import CreateRectangleMask
        from ..models.crop_image import CropImage
        from ..models.crop_image_to_bounding_box import CropImageToBoundingBox
        from ..models.crop_latents import CropLatents
        from ..models.cv2_infill import CV2Infill
        from ..models.decode_invisible_watermark import DecodeInvisibleWatermark
        from ..models.denoise_anima import DenoiseAnima
        from ..models.denoise_cog_view_4 import DenoiseCogView4
        from ..models.denoise_mask_output import DenoiseMaskOutput
        from ..models.denoise_qwen_image import DenoiseQwenImage
        from ..models.denoise_sd3 import DenoiseSD3
        from ..models.denoise_sd15sdxl import DenoiseSD15SDXL
        from ..models.denoise_sd15sdxl_metadata import DenoiseSD15SDXLMetadata
        from ..models.denoise_z_image import DenoiseZImage
        from ..models.denoise_z_image_metadata import DenoiseZImageMetadata
        from ..models.depth_anything_depth_estimation import DepthAnythingDepthEstimation
        from ..models.divide_integers import DivideIntegers
        from ..models.dw_openpose_detection import DWOpenposeDetection
        from ..models.dynamic_prompt import DynamicPrompt
        from ..models.enhance_image import EnhanceImage
        from ..models.equivalent_achromatic_lightness import EquivalentAchromaticLightness
        from ..models.expand_mask_with_fade import ExpandMaskWithFade
        from ..models.extract_image_channel import ExtractImageChannel
        from ..models.face_identifier import FaceIdentifier
        from ..models.face_mask import FaceMask
        from ..models.face_mask_output import FaceMaskOutput
        from ..models.face_off import FaceOff
        from ..models.face_off_output import FaceOffOutput
        from ..models.float_batch import FloatBatch
        from ..models.float_collection_output import FloatCollectionOutput
        from ..models.float_collection_primitive import FloatCollectionPrimitive
        from ..models.float_generator import FloatGenerator
        from ..models.float_generator_output import FloatGeneratorOutput
        from ..models.float_math import FloatMath
        from ..models.float_output import FloatOutput
        from ..models.float_primitive import FloatPrimitive
        from ..models.float_range import FloatRange
        from ..models.float_to_integer import FloatToInteger
        from ..models.flux2_denoise import FLUX2Denoise
        from ..models.flux_2_klein_lo_ra_loader_output import Flux2KleinLoRALoaderOutput
        from ..models.flux_2_klein_model_loader_output import Flux2KleinModelLoaderOutput
        from ..models.flux_conditioning_collection_output import FluxConditioningCollectionOutput
        from ..models.flux_conditioning_output import FluxConditioningOutput
        from ..models.flux_control_lo_ra_loader_output import FluxControlLoRALoaderOutput
        from ..models.flux_control_net import FLUXControlNet
        from ..models.flux_control_net_output import FluxControlNetOutput
        from ..models.flux_denoise import FLUXDenoise
        from ..models.flux_denoise_metadata import FLUXDenoiseMetadata
        from ..models.flux_fill_conditioning import FLUXFillConditioning
        from ..models.flux_fill_output import FluxFillOutput
        from ..models.flux_kontext_image_prep import FLUXKontextImagePrep
        from ..models.flux_kontext_output import FluxKontextOutput
        from ..models.flux_lo_ra_loader_output import FluxLoRALoaderOutput
        from ..models.flux_model_loader_output import FluxModelLoaderOutput
        from ..models.flux_redux import FLUXRedux
        from ..models.flux_redux_output import FluxReduxOutput
        from ..models.fluxip_adapter import FLUXIPAdapter
        from ..models.gemini_image_generation import GeminiImageGeneration
        from ..models.get_image_mask_bounding_box import GetImageMaskBoundingBox
        from ..models.gradient_mask_output import GradientMaskOutput
        from ..models.grounding_dino_text_prompt_object_detection import GroundingDINOTextPromptObjectDetection
        from ..models.hed_edge_detection import HEDEdgeDetection
        from ..models.heuristic_resize import HeuristicResize
        from ..models.ideal_size_output import IdealSizeOutput
        from ..models.ideal_size_sd15sdxl import IdealSizeSD15SDXL
        from ..models.if_ import If
        from ..models.if_invocation_output import IfInvocationOutput
        from ..models.image_batch import ImageBatch
        from ..models.image_collection_output import ImageCollectionOutput
        from ..models.image_collection_primitive import ImageCollectionPrimitive
        from ..models.image_compositor import ImageCompositor
        from ..models.image_dilate_or_erode import ImageDilateOrErode
        from ..models.image_generator import ImageGenerator
        from ..models.image_generator_output import ImageGeneratorOutput
        from ..models.image_layer_blend import ImageLayerBlend
        from ..models.image_mask_to_tensor import ImageMaskToTensor
        from ..models.image_output import ImageOutput
        from ..models.image_panel_coordinate_output import ImagePanelCoordinateOutput
        from ..models.image_panel_layout import ImagePanelLayout
        from ..models.image_primitive import ImagePrimitive
        from ..models.image_to_image import ImageToImage
        from ..models.image_to_image_autoscale import ImageToImageAutoscale
        from ..models.image_to_latents_anima import ImageToLatentsAnima
        from ..models.image_to_latents_cog_view_4 import ImageToLatentsCogView4
        from ..models.image_to_latents_flux import ImageToLatentsFLUX
        from ..models.image_to_latents_flux2 import ImageToLatentsFLUX2
        from ..models.image_to_latents_qwen_image import ImageToLatentsQwenImage
        from ..models.image_to_latents_sd3 import ImageToLatentsSD3
        from ..models.image_to_latents_sd15sdxl import ImageToLatentsSD15SDXL
        from ..models.image_to_latents_z_image import ImageToLatentsZImage
        from ..models.image_value_thresholds import ImageValueThresholds
        from ..models.integer_batch import IntegerBatch
        from ..models.integer_collection_output import IntegerCollectionOutput
        from ..models.integer_collection_primitive import IntegerCollectionPrimitive
        from ..models.integer_generator import IntegerGenerator
        from ..models.integer_generator_output import IntegerGeneratorOutput
        from ..models.integer_math import IntegerMath
        from ..models.integer_output import IntegerOutput
        from ..models.integer_primitive import IntegerPrimitive
        from ..models.integer_range import IntegerRange
        from ..models.integer_range_of_size import IntegerRangeOfSize
        from ..models.inverse_lerp_image import InverseLerpImage
        from ..models.invert_tensor_mask import InvertTensorMask
        from ..models.ip_adapter_output import IPAdapterOutput
        from ..models.ip_adapter_sd15sdxl import IPAdapterSD15SDXL
        from ..models.iterate_invocation import IterateInvocation
        from ..models.iterate_invocation_output import IterateInvocationOutput
        from ..models.kontext_conditioning_flux import KontextConditioningFLUX
        from ..models.l_la_va_one_vision_vllm import LLaVAOneVisionVLLM
        from ..models.la_ma_infill import LaMaInfill
        from ..models.latents_collection_output import LatentsCollectionOutput
        from ..models.latents_collection_primitive import LatentsCollectionPrimitive
        from ..models.latents_meta_output import LatentsMetaOutput
        from ..models.latents_output import LatentsOutput
        from ..models.latents_primitive import LatentsPrimitive
        from ..models.latents_to_image_anima import LatentsToImageAnima
        from ..models.latents_to_image_cog_view_4 import LatentsToImageCogView4
        from ..models.latents_to_image_flux import LatentsToImageFLUX
        from ..models.latents_to_image_flux2 import LatentsToImageFLUX2
        from ..models.latents_to_image_qwen_image import LatentsToImageQwenImage
        from ..models.latents_to_image_sd3 import LatentsToImageSD3
        from ..models.latents_to_image_sd15sdxl import LatentsToImageSD15SDXL
        from ..models.latents_to_image_z_image import LatentsToImageZImage
        from ..models.lerp_image import LerpImage
        from ..models.lineart_anime_edge_detection import LineartAnimeEdgeDetection
        from ..models.lineart_edge_detection import LineartEdgeDetection
        from ..models.lo_ra_loader_output import LoRALoaderOutput
        from ..models.lo_ra_selector_output import LoRASelectorOutput
        from ..models.main_model_anima import MainModelAnima
        from ..models.main_model_cog_view_4 import MainModelCogView4
        from ..models.main_model_flux import MainModelFLUX
        from ..models.main_model_flux_2_klein import MainModelFlux2Klein
        from ..models.main_model_qwen_image import MainModelQwenImage
        from ..models.main_model_sd3 import MainModelSD3
        from ..models.main_model_sd15sd2 import MainModelSD15SD2
        from ..models.main_model_sdxl import MainModelSDXL
        from ..models.main_model_z_image import MainModelZImage
        from ..models.mask_edge import MaskEdge
        from ..models.mask_from_alpha import MaskFromAlpha
        from ..models.mask_from_segmented_image import MaskFromSegmentedImage
        from ..models.mask_output import MaskOutput
        from ..models.md_control_list_output import MDControlListOutput
        from ..models.mdip_adapter_list_output import MDIPAdapterListOutput
        from ..models.mdt2i_adapter_list_output import MDT2IAdapterListOutput
        from ..models.media_pipe_face_detection import MediaPipeFaceDetection
        from ..models.merge_tiles_to_image import MergeTilesToImage
        from ..models.metadata import Metadata
        from ..models.metadata_field_extractor import MetadataFieldExtractor
        from ..models.metadata_from_image import MetadataFromImage
        from ..models.metadata_item import MetadataItem
        from ..models.metadata_item_linked import MetadataItemLinked
        from ..models.metadata_item_output import MetadataItemOutput
        from ..models.metadata_merge import MetadataMerge
        from ..models.metadata_output import MetadataOutput
        from ..models.metadata_to_bool import MetadataToBool
        from ..models.metadata_to_bool_collection import MetadataToBoolCollection
        from ..models.metadata_to_control_nets import MetadataToControlNets
        from ..models.metadata_to_float import MetadataToFloat
        from ..models.metadata_to_float_collection import MetadataToFloatCollection
        from ..models.metadata_to_integer import MetadataToInteger
        from ..models.metadata_to_integer_collection import MetadataToIntegerCollection
        from ..models.metadata_to_ip_adapters import MetadataToIPAdapters
        from ..models.metadata_to_lo_r_as import MetadataToLoRAs
        from ..models.metadata_to_lo_ra_collection import MetadataToLoRACollection
        from ..models.metadata_to_loras_collection_output import MetadataToLorasCollectionOutput
        from ..models.metadata_to_model import MetadataToModel
        from ..models.metadata_to_model_output import MetadataToModelOutput
        from ..models.metadata_to_scheduler import MetadataToScheduler
        from ..models.metadata_to_sdxl_lo_r_as import MetadataToSDXLLoRAs
        from ..models.metadata_to_sdxl_model import MetadataToSDXLModel
        from ..models.metadata_to_sdxl_model_output import MetadataToSDXLModelOutput
        from ..models.metadata_to_string import MetadataToString
        from ..models.metadata_to_string_collection import MetadataToStringCollection
        from ..models.metadata_to_t2i_adapters import MetadataToT2IAdapters
        from ..models.metadata_to_vae import MetadataToVAE
        from ..models.mlsd_detection import MLSDDetection
        from ..models.model_identifier_output import ModelIdentifierOutput
        from ..models.model_loader_output import ModelLoaderOutput
        from ..models.multiply_image_channel import MultiplyImageChannel
        from ..models.multiply_images import MultiplyImages
        from ..models.multiply_integers import MultiplyIntegers
        from ..models.noise_output import NoiseOutput
        from ..models.normal_map import NormalMap
        from ..models.offset_image_channel import OffsetImageChannel
        from ..models.open_ai_image_generation import OpenAIImageGeneration
        from ..models.open_cv_inpaint import OpenCVInpaint
        from ..models.pair_tile_image_output import PairTileImageOutput
        from ..models.pair_tile_with_image import PairTileWithImage
        from ..models.paste_image import PasteImage
        from ..models.paste_image_into_bounding_box import PasteImageIntoBoundingBox
        from ..models.patch_match_infill import PatchMatchInfill
        from ..models.pbr_maps import PBRMaps
        from ..models.pbr_maps_output import PBRMapsOutput
        from ..models.pi_di_net_edge_detection import PiDiNetEdgeDetection
        from ..models.prompt_anima import PromptAnima
        from ..models.prompt_cog_view_4 import PromptCogView4
        from ..models.prompt_flux import PromptFLUX
        from ..models.prompt_flux_2_klein import PromptFlux2Klein
        from ..models.prompt_qwen_image import PromptQwenImage
        from ..models.prompt_sd3 import PromptSD3
        from ..models.prompt_sd15 import PromptSD15
        from ..models.prompt_sdxl import PromptSDXL
        from ..models.prompt_sdxl_refiner import PromptSDXLRefiner
        from ..models.prompt_template import PromptTemplate
        from ..models.prompt_template_output import PromptTemplateOutput
        from ..models.prompt_z_image import PromptZImage
        from ..models.prompts_from_file import PromptsFromFile
        from ..models.qwen_image_conditioning_output import QwenImageConditioningOutput
        from ..models.qwen_image_lo_ra_loader_output import QwenImageLoRALoaderOutput
        from ..models.qwen_image_model_loader_output import QwenImageModelLoaderOutput
        from ..models.random_float import RandomFloat
        from ..models.random_integer import RandomInteger
        from ..models.random_range import RandomRange
        from ..models.refiner_model_sdxl import RefinerModelSDXL
        from ..models.resize_image import ResizeImage
        from ..models.resize_latents import ResizeLatents
        from ..models.round_float import RoundFloat
        from ..models.save_image import SaveImage
        from ..models.save_image_gallery_file_export import SaveImageGalleryFileExport
        from ..models.scale_image import ScaleImage
        from ..models.scale_latents import ScaleLatents
        from ..models.scheduler import Scheduler
        from ..models.scheduler_output import SchedulerOutput
        from ..models.sd3_conditioning_output import SD3ConditioningOutput
        from ..models.sd_3_model_loader_output import Sd3ModelLoaderOutput
        from ..models.sdxl_lo_ra_loader_output import SDXLLoRALoaderOutput
        from ..models.sdxl_model_loader_output import SDXLModelLoaderOutput
        from ..models.sdxl_refiner_model_loader_output import SDXLRefinerModelLoaderOutput
        from ..models.seamless_mode_output import SeamlessModeOutput
        from ..models.seed_variance_enhancer_z_image import SeedVarianceEnhancerZImage
        from ..models.seedream_image_generation import SeedreamImageGeneration
        from ..models.segment_anything import SegmentAnything
        from ..models.select_lo_ra import SelectLoRA
        from ..models.show_image import ShowImage
        from ..models.solid_color_infill import SolidColorInfill
        from ..models.string_2_output import String2Output
        from ..models.string_batch import StringBatch
        from ..models.string_collection_output import StringCollectionOutput
        from ..models.string_collection_primitive import StringCollectionPrimitive
        from ..models.string_generator import StringGenerator
        from ..models.string_generator_output import StringGeneratorOutput
        from ..models.string_join import StringJoin
        from ..models.string_join_three import StringJoinThree
        from ..models.string_output import StringOutput
        from ..models.string_pos_neg_output import StringPosNegOutput
        from ..models.string_primitive import StringPrimitive
        from ..models.string_replace import StringReplace
        from ..models.string_split import StringSplit
        from ..models.string_split_negative import StringSplitNegative
        from ..models.subtract_integers import SubtractIntegers
        from ..models.t2i_adapter_output import T2IAdapterOutput
        from ..models.t2i_adapter_sd15sdxl import T2IAdapterSD15SDXL
        from ..models.tensor_mask_to_image import TensorMaskToImage
        from ..models.text_llm import TextLLM
        from ..models.tile_infill import TileInfill
        from ..models.tile_to_properties import TileToProperties
        from ..models.tile_to_properties_output import TileToPropertiesOutput
        from ..models.tiled_multi_diffusion_denoise_sd15sdxl import TiledMultiDiffusionDenoiseSD15SDXL
        from ..models.u_net_output import UNetOutput
        from ..models.unsharp_mask import UnsharpMask
        from ..models.unsharp_mask_oklab import UnsharpMaskOklab
        from ..models.upscale_real_esrgan import UpscaleRealESRGAN
        from ..models.vae_model_sd15sd2sdxlsd3flux import VAEModelSD15SD2SDXLSD3FLUX
        from ..models.vae_output import VAEOutput
        from ..models.z_image_conditioning_output import ZImageConditioningOutput
        from ..models.z_image_control_net import ZImageControlNet
        from ..models.z_image_control_output import ZImageControlOutput
        from ..models.z_image_lo_ra_loader_output import ZImageLoRALoaderOutput
        from ..models.z_image_model_loader_output import ZImageModelLoaderOutput

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        queue_id = d.pop("queue_id")

        item_id = d.pop("item_id")

        batch_id = d.pop("batch_id")

        def _parse_origin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        origin = _parse_origin(d.pop("origin"))

        def _parse_destination(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        destination = _parse_destination(d.pop("destination"))

        user_id = d.pop("user_id")

        session_id = d.pop("session_id")

        def _parse_invocation(
            data: object,
        ) -> (
            AddImageNoise
            | AddIntegers
            | AddInvisibleWatermark
            | AdjustImageHue
            | AdjustImageHueOklch
            | AdjustImageHuePlus
            | AlibabaCloudDashScopeImageGeneration
            | AlphaMaskToTensor
            | AnyModel
            | ApplyCLIPSkipSD15SDXL
            | ApplyFreeUSD15SDXL
            | ApplyLoRAAnima
            | ApplyLoRACollectionAnima
            | ApplyLoRACollectionFLUX
            | ApplyLoRACollectionFlux2Klein
            | ApplyLoRACollectionQwenImage
            | ApplyLoRACollectionSD15
            | ApplyLoRACollectionSDXL
            | ApplyLoRACollectionZImage
            | ApplyLoRAFLUX
            | ApplyLoRAFlux2Klein
            | ApplyLoRAQwenImage
            | ApplyLoRASD15
            | ApplyLoRASDXL
            | ApplyLoRAZImage
            | ApplyMaskToImage
            | ApplySeamlessSD15SDXL
            | ApplyTensorMaskToImage
            | BlankImage
            | BlendLatents
            | BlurImage
            | BlurNSFWImage
            | BooleanCollectionPrimitive
            | BooleanPrimitive
            | BoundingBox
            | CalculateImageTiles
            | CalculateImageTilesEvenSplit
            | CalculateImageTilesMinimumOverlap
            | CannyEdgeDetection
            | CanvasOutput
            | CanvasPasteBack
            | CanvasV2MaskAndCrop
            | CenterPadOrCropImage
            | CollectInvocation
            | ColorCorrect
            | ColorMap
            | ColorPrimitive
            | CombineMasks
            | ConditioningCollectionPrimitive
            | ConditioningPrimitive
            | ContentShuffle
            | ControlLoRAFLUX
            | ControlNetSD15SD2SDXL
            | ConvertImageMode
            | CoreMetadata
            | CreateDenoiseMask
            | CreateGradientMask
            | CreateLatentNoise
            | CreateRectangleMask
            | CropImage
            | CropImageToBoundingBox
            | CropLatents
            | CV2Infill
            | DecodeInvisibleWatermark
            | DenoiseAnima
            | DenoiseCogView4
            | DenoiseQwenImage
            | DenoiseSD15SDXL
            | DenoiseSD15SDXLMetadata
            | DenoiseSD3
            | DenoiseZImage
            | DenoiseZImageMetadata
            | DepthAnythingDepthEstimation
            | DivideIntegers
            | DWOpenposeDetection
            | DynamicPrompt
            | EnhanceImage
            | EquivalentAchromaticLightness
            | ExpandMaskWithFade
            | ExtractImageChannel
            | FaceIdentifier
            | FaceMask
            | FaceOff
            | FloatBatch
            | FloatCollectionPrimitive
            | FloatGenerator
            | FloatMath
            | FloatPrimitive
            | FloatRange
            | FloatToInteger
            | FLUX2Denoise
            | FLUXControlNet
            | FLUXDenoise
            | FLUXDenoiseMetadata
            | FLUXFillConditioning
            | FLUXIPAdapter
            | FLUXKontextImagePrep
            | FLUXRedux
            | GeminiImageGeneration
            | GetImageMaskBoundingBox
            | GroundingDINOTextPromptObjectDetection
            | HEDEdgeDetection
            | HeuristicResize
            | IdealSizeSD15SDXL
            | If
            | ImageBatch
            | ImageCollectionPrimitive
            | ImageCompositor
            | ImageDilateOrErode
            | ImageGenerator
            | ImageLayerBlend
            | ImageMaskToTensor
            | ImagePanelLayout
            | ImagePrimitive
            | ImageToImage
            | ImageToImageAutoscale
            | ImageToLatentsAnima
            | ImageToLatentsCogView4
            | ImageToLatentsFLUX
            | ImageToLatentsFLUX2
            | ImageToLatentsQwenImage
            | ImageToLatentsSD15SDXL
            | ImageToLatentsSD3
            | ImageToLatentsZImage
            | ImageValueThresholds
            | IntegerBatch
            | IntegerCollectionPrimitive
            | IntegerGenerator
            | IntegerMath
            | IntegerPrimitive
            | IntegerRange
            | IntegerRangeOfSize
            | InverseLerpImage
            | InvertTensorMask
            | IPAdapterSD15SDXL
            | IterateInvocation
            | KontextConditioningFLUX
            | LaMaInfill
            | LatentsCollectionPrimitive
            | LatentsPrimitive
            | LatentsToImageAnima
            | LatentsToImageCogView4
            | LatentsToImageFLUX
            | LatentsToImageFLUX2
            | LatentsToImageQwenImage
            | LatentsToImageSD15SDXL
            | LatentsToImageSD3
            | LatentsToImageZImage
            | LerpImage
            | LineartAnimeEdgeDetection
            | LineartEdgeDetection
            | LLaVAOneVisionVLLM
            | MainModelAnima
            | MainModelCogView4
            | MainModelFLUX
            | MainModelFlux2Klein
            | MainModelQwenImage
            | MainModelSD15SD2
            | MainModelSD3
            | MainModelSDXL
            | MainModelZImage
            | MaskEdge
            | MaskFromAlpha
            | MaskFromSegmentedImage
            | MediaPipeFaceDetection
            | MergeTilesToImage
            | Metadata
            | MetadataFieldExtractor
            | MetadataFromImage
            | MetadataItem
            | MetadataItemLinked
            | MetadataMerge
            | MetadataToBool
            | MetadataToBoolCollection
            | MetadataToControlNets
            | MetadataToFloat
            | MetadataToFloatCollection
            | MetadataToInteger
            | MetadataToIntegerCollection
            | MetadataToIPAdapters
            | MetadataToLoRACollection
            | MetadataToLoRAs
            | MetadataToModel
            | MetadataToScheduler
            | MetadataToSDXLLoRAs
            | MetadataToSDXLModel
            | MetadataToString
            | MetadataToStringCollection
            | MetadataToT2IAdapters
            | MetadataToVAE
            | MLSDDetection
            | MultiplyImageChannel
            | MultiplyImages
            | MultiplyIntegers
            | NormalMap
            | OffsetImageChannel
            | OpenAIImageGeneration
            | OpenCVInpaint
            | PairTileWithImage
            | PasteImage
            | PasteImageIntoBoundingBox
            | PatchMatchInfill
            | PBRMaps
            | PiDiNetEdgeDetection
            | PromptAnima
            | PromptCogView4
            | PromptFLUX
            | PromptFlux2Klein
            | PromptQwenImage
            | PromptSD15
            | PromptSD3
            | PromptSDXL
            | PromptSDXLRefiner
            | PromptsFromFile
            | PromptTemplate
            | PromptZImage
            | RandomFloat
            | RandomInteger
            | RandomRange
            | RefinerModelSDXL
            | ResizeImage
            | ResizeLatents
            | RoundFloat
            | SaveImage
            | SaveImageGalleryFileExport
            | ScaleImage
            | ScaleLatents
            | Scheduler
            | SeedreamImageGeneration
            | SeedVarianceEnhancerZImage
            | SegmentAnything
            | SelectLoRA
            | ShowImage
            | SolidColorInfill
            | StringBatch
            | StringCollectionPrimitive
            | StringGenerator
            | StringJoin
            | StringJoinThree
            | StringPrimitive
            | StringReplace
            | StringSplit
            | StringSplitNegative
            | SubtractIntegers
            | T2IAdapterSD15SDXL
            | TensorMaskToImage
            | TextLLM
            | TiledMultiDiffusionDenoiseSD15SDXL
            | TileInfill
            | TileToProperties
            | UnsharpMask
            | UnsharpMaskOklab
            | UpscaleRealESRGAN
            | VAEModelSD15SD2SDXLSD3FLUX
            | ZImageControlNet
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_0 = AddIntegers.from_dict(data)

                return invocation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_1 = AlibabaCloudDashScopeImageGeneration.from_dict(data)

                return invocation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_2 = AlphaMaskToTensor.from_dict(data)

                return invocation_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_3 = DenoiseAnima.from_dict(data)

                return invocation_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_4 = ImageToLatentsAnima.from_dict(data)

                return invocation_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_5 = LatentsToImageAnima.from_dict(data)

                return invocation_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_6 = ApplyLoRACollectionAnima.from_dict(data)

                return invocation_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_7 = ApplyLoRAAnima.from_dict(data)

                return invocation_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_8 = MainModelAnima.from_dict(data)

                return invocation_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_9 = PromptAnima.from_dict(data)

                return invocation_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_10 = ApplyTensorMaskToImage.from_dict(data)

                return invocation_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_11 = ApplyMaskToImage.from_dict(data)

                return invocation_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_12 = BlankImage.from_dict(data)

                return invocation_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_13 = BlendLatents.from_dict(data)

                return invocation_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_14 = BooleanCollectionPrimitive.from_dict(data)

                return invocation_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_15 = BooleanPrimitive.from_dict(data)

                return invocation_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_16 = BoundingBox.from_dict(data)

                return invocation_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_17 = ApplyCLIPSkipSD15SDXL.from_dict(data)

                return invocation_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_18 = CV2Infill.from_dict(data)

                return invocation_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_19 = CalculateImageTilesEvenSplit.from_dict(data)

                return invocation_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_20 = CalculateImageTiles.from_dict(data)

                return invocation_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_21 = CalculateImageTilesMinimumOverlap.from_dict(data)

                return invocation_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_22 = CannyEdgeDetection.from_dict(data)

                return invocation_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_23 = CanvasOutput.from_dict(data)

                return invocation_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_24 = CanvasPasteBack.from_dict(data)

                return invocation_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_25 = CanvasV2MaskAndCrop.from_dict(data)

                return invocation_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_26 = CenterPadOrCropImage.from_dict(data)

                return invocation_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_27 = DenoiseCogView4.from_dict(data)

                return invocation_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_28 = ImageToLatentsCogView4.from_dict(data)

                return invocation_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_29 = LatentsToImageCogView4.from_dict(data)

                return invocation_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_30 = MainModelCogView4.from_dict(data)

                return invocation_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_31 = PromptCogView4.from_dict(data)

                return invocation_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_32 = CollectInvocation.from_dict(data)

                return invocation_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_33 = ColorCorrect.from_dict(data)

                return invocation_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_34 = ColorPrimitive.from_dict(data)

                return invocation_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_35 = ColorMap.from_dict(data)

                return invocation_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_36 = PromptSD15.from_dict(data)

                return invocation_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_37 = ConditioningCollectionPrimitive.from_dict(data)

                return invocation_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_38 = ConditioningPrimitive.from_dict(data)

                return invocation_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_39 = ContentShuffle.from_dict(data)

                return invocation_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_40 = ControlNetSD15SD2SDXL.from_dict(data)

                return invocation_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_41 = CoreMetadata.from_dict(data)

                return invocation_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_42 = CreateDenoiseMask.from_dict(data)

                return invocation_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_43 = CreateGradientMask.from_dict(data)

                return invocation_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_44 = CropImageToBoundingBox.from_dict(data)

                return invocation_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_45 = CropLatents.from_dict(data)

                return invocation_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_46 = OpenCVInpaint.from_dict(data)

                return invocation_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_47 = DWOpenposeDetection.from_dict(data)

                return invocation_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_48 = DecodeInvisibleWatermark.from_dict(data)

                return invocation_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_49 = DenoiseSD15SDXL.from_dict(data)

                return invocation_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_50 = DenoiseSD15SDXLMetadata.from_dict(data)

                return invocation_type_50
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_51 = DepthAnythingDepthEstimation.from_dict(data)

                return invocation_type_51
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_52 = DivideIntegers.from_dict(data)

                return invocation_type_52
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_53 = DynamicPrompt.from_dict(data)

                return invocation_type_53
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_54 = UpscaleRealESRGAN.from_dict(data)

                return invocation_type_54
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_55 = ExpandMaskWithFade.from_dict(data)

                return invocation_type_55
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_56 = ApplyLoRACollectionFLUX.from_dict(data)

                return invocation_type_56
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_57 = FaceIdentifier.from_dict(data)

                return invocation_type_57
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_58 = FaceMask.from_dict(data)

                return invocation_type_58
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_59 = FaceOff.from_dict(data)

                return invocation_type_59
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_60 = FloatBatch.from_dict(data)

                return invocation_type_60
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_61 = FloatCollectionPrimitive.from_dict(data)

                return invocation_type_61
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_62 = FloatGenerator.from_dict(data)

                return invocation_type_62
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_63 = FloatPrimitive.from_dict(data)

                return invocation_type_63
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_64 = FloatRange.from_dict(data)

                return invocation_type_64
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_65 = FloatMath.from_dict(data)

                return invocation_type_65
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_66 = FloatToInteger.from_dict(data)

                return invocation_type_66
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_67 = FLUX2Denoise.from_dict(data)

                return invocation_type_67
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_68 = ApplyLoRACollectionFlux2Klein.from_dict(data)

                return invocation_type_68
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_69 = ApplyLoRAFlux2Klein.from_dict(data)

                return invocation_type_69
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_70 = MainModelFlux2Klein.from_dict(data)

                return invocation_type_70
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_71 = PromptFlux2Klein.from_dict(data)

                return invocation_type_71
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_72 = LatentsToImageFLUX2.from_dict(data)

                return invocation_type_72
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_73 = ImageToLatentsFLUX2.from_dict(data)

                return invocation_type_73
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_74 = ControlLoRAFLUX.from_dict(data)

                return invocation_type_74
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_75 = FLUXControlNet.from_dict(data)

                return invocation_type_75
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_76 = FLUXDenoise.from_dict(data)

                return invocation_type_76
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_77 = FLUXDenoiseMetadata.from_dict(data)

                return invocation_type_77
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_78 = FLUXFillConditioning.from_dict(data)

                return invocation_type_78
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_79 = FLUXIPAdapter.from_dict(data)

                return invocation_type_79
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_80 = FLUXKontextImagePrep.from_dict(data)

                return invocation_type_80
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_81 = KontextConditioningFLUX.from_dict(data)

                return invocation_type_81
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_82 = ApplyLoRAFLUX.from_dict(data)

                return invocation_type_82
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_83 = MainModelFLUX.from_dict(data)

                return invocation_type_83
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_84 = FLUXRedux.from_dict(data)

                return invocation_type_84
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_85 = PromptFLUX.from_dict(data)

                return invocation_type_85
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_86 = LatentsToImageFLUX.from_dict(data)

                return invocation_type_86
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_87 = ImageToLatentsFLUX.from_dict(data)

                return invocation_type_87
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_88 = ApplyFreeUSD15SDXL.from_dict(data)

                return invocation_type_88
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_89 = GeminiImageGeneration.from_dict(data)

                return invocation_type_89
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_90 = GetImageMaskBoundingBox.from_dict(data)

                return invocation_type_90
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_91 = GroundingDINOTextPromptObjectDetection.from_dict(data)

                return invocation_type_91
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_92 = HEDEdgeDetection.from_dict(data)

                return invocation_type_92
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_93 = HeuristicResize.from_dict(data)

                return invocation_type_93
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_94 = IPAdapterSD15SDXL.from_dict(data)

                return invocation_type_94
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_95 = IdealSizeSD15SDXL.from_dict(data)

                return invocation_type_95
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_96 = If.from_dict(data)

                return invocation_type_96
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_97 = ImageBatch.from_dict(data)

                return invocation_type_97
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_98 = BlurImage.from_dict(data)

                return invocation_type_98
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_99 = ExtractImageChannel.from_dict(data)

                return invocation_type_99
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_100 = MultiplyImageChannel.from_dict(data)

                return invocation_type_100
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_101 = OffsetImageChannel.from_dict(data)

                return invocation_type_101
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_102 = ImageCollectionPrimitive.from_dict(data)

                return invocation_type_102
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_103 = ConvertImageMode.from_dict(data)

                return invocation_type_103
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_104 = CropImage.from_dict(data)

                return invocation_type_104
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_105 = ImageGenerator.from_dict(data)

                return invocation_type_105
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_106 = AdjustImageHue.from_dict(data)

                return invocation_type_106
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_107 = InverseLerpImage.from_dict(data)

                return invocation_type_107
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_108 = ImagePrimitive.from_dict(data)

                return invocation_type_108
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_109 = LerpImage.from_dict(data)

                return invocation_type_109
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_110 = ImageMaskToTensor.from_dict(data)

                return invocation_type_110
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_111 = MultiplyImages.from_dict(data)

                return invocation_type_111
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_112 = BlurNSFWImage.from_dict(data)

                return invocation_type_112
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_113 = AddImageNoise.from_dict(data)

                return invocation_type_113
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_114 = ImagePanelLayout.from_dict(data)

                return invocation_type_114
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_115 = PasteImage.from_dict(data)

                return invocation_type_115
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_116 = ResizeImage.from_dict(data)

                return invocation_type_116
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_117 = ScaleImage.from_dict(data)

                return invocation_type_117
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_118 = ImageToLatentsSD15SDXL.from_dict(data)

                return invocation_type_118
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_119 = AddInvisibleWatermark.from_dict(data)

                return invocation_type_119
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_120 = SolidColorInfill.from_dict(data)

                return invocation_type_120
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_121 = PatchMatchInfill.from_dict(data)

                return invocation_type_121
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_122 = TileInfill.from_dict(data)

                return invocation_type_122
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_123 = IntegerBatch.from_dict(data)

                return invocation_type_123
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_124 = IntegerCollectionPrimitive.from_dict(data)

                return invocation_type_124
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_125 = IntegerGenerator.from_dict(data)

                return invocation_type_125
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_126 = IntegerPrimitive.from_dict(data)

                return invocation_type_126
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_127 = IntegerMath.from_dict(data)

                return invocation_type_127
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_128 = InvertTensorMask.from_dict(data)

                return invocation_type_128
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_129 = AdjustImageHuePlus.from_dict(data)

                return invocation_type_129
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_130 = EquivalentAchromaticLightness.from_dict(data)

                return invocation_type_130
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_131 = ImageLayerBlend.from_dict(data)

                return invocation_type_131
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_132 = ImageCompositor.from_dict(data)

                return invocation_type_132
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_133 = ImageDilateOrErode.from_dict(data)

                return invocation_type_133
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_134 = EnhanceImage.from_dict(data)

                return invocation_type_134
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_135 = ImageValueThresholds.from_dict(data)

                return invocation_type_135
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_136 = IterateInvocation.from_dict(data)

                return invocation_type_136
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_137 = LaMaInfill.from_dict(data)

                return invocation_type_137
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_138 = LatentsCollectionPrimitive.from_dict(data)

                return invocation_type_138
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_139 = LatentsPrimitive.from_dict(data)

                return invocation_type_139
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_140 = LatentsToImageSD15SDXL.from_dict(data)

                return invocation_type_140
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_141 = LineartAnimeEdgeDetection.from_dict(data)

                return invocation_type_141
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_142 = LineartEdgeDetection.from_dict(data)

                return invocation_type_142
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_143 = LLaVAOneVisionVLLM.from_dict(data)

                return invocation_type_143
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_144 = ApplyLoRACollectionSD15.from_dict(data)

                return invocation_type_144
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_145 = ApplyLoRASD15.from_dict(data)

                return invocation_type_145
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_146 = SelectLoRA.from_dict(data)

                return invocation_type_146
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_147 = MLSDDetection.from_dict(data)

                return invocation_type_147
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_148 = MainModelSD15SD2.from_dict(data)

                return invocation_type_148
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_149 = CombineMasks.from_dict(data)

                return invocation_type_149
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_150 = MaskEdge.from_dict(data)

                return invocation_type_150
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_151 = MaskFromAlpha.from_dict(data)

                return invocation_type_151
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_152 = MaskFromSegmentedImage.from_dict(data)

                return invocation_type_152
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_153 = TensorMaskToImage.from_dict(data)

                return invocation_type_153
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_154 = MediaPipeFaceDetection.from_dict(data)

                return invocation_type_154
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_155 = MetadataMerge.from_dict(data)

                return invocation_type_155
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_156 = MergeTilesToImage.from_dict(data)

                return invocation_type_156
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_157 = MetadataFieldExtractor.from_dict(data)

                return invocation_type_157
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_158 = MetadataFromImage.from_dict(data)

                return invocation_type_158
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_159 = Metadata.from_dict(data)

                return invocation_type_159
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_160 = MetadataItem.from_dict(data)

                return invocation_type_160
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_161 = MetadataItemLinked.from_dict(data)

                return invocation_type_161
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_162 = MetadataToBoolCollection.from_dict(data)

                return invocation_type_162
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_163 = MetadataToBool.from_dict(data)

                return invocation_type_163
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_164 = MetadataToControlNets.from_dict(data)

                return invocation_type_164
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_165 = MetadataToFloatCollection.from_dict(data)

                return invocation_type_165
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_166 = MetadataToFloat.from_dict(data)

                return invocation_type_166
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_167 = MetadataToIPAdapters.from_dict(data)

                return invocation_type_167
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_168 = MetadataToIntegerCollection.from_dict(data)

                return invocation_type_168
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_169 = MetadataToInteger.from_dict(data)

                return invocation_type_169
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_170 = MetadataToLoRACollection.from_dict(data)

                return invocation_type_170
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_171 = MetadataToLoRAs.from_dict(data)

                return invocation_type_171
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_172 = MetadataToModel.from_dict(data)

                return invocation_type_172
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_173 = MetadataToSDXLLoRAs.from_dict(data)

                return invocation_type_173
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_174 = MetadataToSDXLModel.from_dict(data)

                return invocation_type_174
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_175 = MetadataToScheduler.from_dict(data)

                return invocation_type_175
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_176 = MetadataToStringCollection.from_dict(data)

                return invocation_type_176
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_177 = MetadataToString.from_dict(data)

                return invocation_type_177
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_178 = MetadataToT2IAdapters.from_dict(data)

                return invocation_type_178
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_179 = MetadataToVAE.from_dict(data)

                return invocation_type_179
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_180 = AnyModel.from_dict(data)

                return invocation_type_180
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_181 = MultiplyIntegers.from_dict(data)

                return invocation_type_181
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_182 = CreateLatentNoise.from_dict(data)

                return invocation_type_182
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_183 = NormalMap.from_dict(data)

                return invocation_type_183
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_184 = UnsharpMaskOklab.from_dict(data)

                return invocation_type_184
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_185 = AdjustImageHueOklch.from_dict(data)

                return invocation_type_185
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_186 = OpenAIImageGeneration.from_dict(data)

                return invocation_type_186
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_187 = PBRMaps.from_dict(data)

                return invocation_type_187
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_188 = PairTileWithImage.from_dict(data)

                return invocation_type_188
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_189 = PasteImageIntoBoundingBox.from_dict(data)

                return invocation_type_189
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_190 = PiDiNetEdgeDetection.from_dict(data)

                return invocation_type_190
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_191 = PromptTemplate.from_dict(data)

                return invocation_type_191
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_192 = PromptsFromFile.from_dict(data)

                return invocation_type_192
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_193 = DenoiseQwenImage.from_dict(data)

                return invocation_type_193
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_194 = ImageToLatentsQwenImage.from_dict(data)

                return invocation_type_194
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_195 = LatentsToImageQwenImage.from_dict(data)

                return invocation_type_195
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_196 = ApplyLoRACollectionQwenImage.from_dict(data)

                return invocation_type_196
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_197 = ApplyLoRAQwenImage.from_dict(data)

                return invocation_type_197
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_198 = MainModelQwenImage.from_dict(data)

                return invocation_type_198
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_199 = PromptQwenImage.from_dict(data)

                return invocation_type_199
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_200 = RandomFloat.from_dict(data)

                return invocation_type_200
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_201 = RandomInteger.from_dict(data)

                return invocation_type_201
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_202 = RandomRange.from_dict(data)

                return invocation_type_202
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_203 = IntegerRange.from_dict(data)

                return invocation_type_203
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_204 = IntegerRangeOfSize.from_dict(data)

                return invocation_type_204
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_205 = CreateRectangleMask.from_dict(data)

                return invocation_type_205
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_206 = ResizeLatents.from_dict(data)

                return invocation_type_206
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_207 = RoundFloat.from_dict(data)

                return invocation_type_207
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_208 = DenoiseSD3.from_dict(data)

                return invocation_type_208
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_209 = ImageToLatentsSD3.from_dict(data)

                return invocation_type_209
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_210 = LatentsToImageSD3.from_dict(data)

                return invocation_type_210
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_211 = PromptSDXL.from_dict(data)

                return invocation_type_211
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_212 = ApplyLoRACollectionSDXL.from_dict(data)

                return invocation_type_212
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_213 = ApplyLoRASDXL.from_dict(data)

                return invocation_type_213
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_214 = MainModelSDXL.from_dict(data)

                return invocation_type_214
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_215 = PromptSDXLRefiner.from_dict(data)

                return invocation_type_215
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_216 = RefinerModelSDXL.from_dict(data)

                return invocation_type_216
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_217 = SaveImage.from_dict(data)

                return invocation_type_217
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_218 = SaveImageGalleryFileExport.from_dict(data)

                return invocation_type_218
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_219 = ScaleLatents.from_dict(data)

                return invocation_type_219
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_220 = Scheduler.from_dict(data)

                return invocation_type_220
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_221 = MainModelSD3.from_dict(data)

                return invocation_type_221
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_222 = PromptSD3.from_dict(data)

                return invocation_type_222
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_223 = ApplySeamlessSD15SDXL.from_dict(data)

                return invocation_type_223
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_224 = SeedreamImageGeneration.from_dict(data)

                return invocation_type_224
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_225 = SegmentAnything.from_dict(data)

                return invocation_type_225
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_226 = ShowImage.from_dict(data)

                return invocation_type_226
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_227 = ImageToImageAutoscale.from_dict(data)

                return invocation_type_227
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_228 = ImageToImage.from_dict(data)

                return invocation_type_228
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_229 = StringBatch.from_dict(data)

                return invocation_type_229
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_230 = StringCollectionPrimitive.from_dict(data)

                return invocation_type_230
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_231 = StringGenerator.from_dict(data)

                return invocation_type_231
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_232 = StringPrimitive.from_dict(data)

                return invocation_type_232
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_233 = StringJoin.from_dict(data)

                return invocation_type_233
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_234 = StringJoinThree.from_dict(data)

                return invocation_type_234
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_235 = StringReplace.from_dict(data)

                return invocation_type_235
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_236 = StringSplit.from_dict(data)

                return invocation_type_236
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_237 = StringSplitNegative.from_dict(data)

                return invocation_type_237
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_238 = SubtractIntegers.from_dict(data)

                return invocation_type_238
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_239 = T2IAdapterSD15SDXL.from_dict(data)

                return invocation_type_239
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_240 = TextLLM.from_dict(data)

                return invocation_type_240
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_241 = TileToProperties.from_dict(data)

                return invocation_type_241
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_242 = TiledMultiDiffusionDenoiseSD15SDXL.from_dict(data)

                return invocation_type_242
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_243 = UnsharpMask.from_dict(data)

                return invocation_type_243
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_244 = VAEModelSD15SD2SDXLSD3FLUX.from_dict(data)

                return invocation_type_244
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_245 = ZImageControlNet.from_dict(data)

                return invocation_type_245
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_246 = DenoiseZImage.from_dict(data)

                return invocation_type_246
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_247 = DenoiseZImageMetadata.from_dict(data)

                return invocation_type_247
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_248 = ImageToLatentsZImage.from_dict(data)

                return invocation_type_248
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_249 = LatentsToImageZImage.from_dict(data)

                return invocation_type_249
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_250 = ApplyLoRACollectionZImage.from_dict(data)

                return invocation_type_250
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_251 = ApplyLoRAZImage.from_dict(data)

                return invocation_type_251
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_252 = MainModelZImage.from_dict(data)

                return invocation_type_252
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invocation_type_253 = SeedVarianceEnhancerZImage.from_dict(data)

                return invocation_type_253
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            invocation_type_254 = PromptZImage.from_dict(data)

            return invocation_type_254

        invocation = _parse_invocation(d.pop("invocation"))

        invocation_source_id = d.pop("invocation_source_id")

        def _parse_result(
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
                result_type_0 = AnimaConditioningOutput.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_1 = AnimaLoRALoaderOutput.from_dict(data)

                return result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_2 = AnimaModelLoaderOutput.from_dict(data)

                return result_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_3 = BooleanCollectionOutput.from_dict(data)

                return result_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_4 = BooleanOutput.from_dict(data)

                return result_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_5 = BoundingBoxCollectionOutput.from_dict(data)

                return result_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_6 = BoundingBoxOutput.from_dict(data)

                return result_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_7 = CLIPOutput.from_dict(data)

                return result_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_8 = CLIPSkipInvocationOutput.from_dict(data)

                return result_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_9 = CalculateImageTilesOutput.from_dict(data)

                return result_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_10 = CogView4ConditioningOutput.from_dict(data)

                return result_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_11 = CogView4ModelLoaderOutput.from_dict(data)

                return result_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_12 = CollectInvocationOutput.from_dict(data)

                return result_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_13 = ColorCollectionOutput.from_dict(data)

                return result_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_14 = ColorOutput.from_dict(data)

                return result_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_15 = ConditioningCollectionOutput.from_dict(data)

                return result_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_16 = ConditioningOutput.from_dict(data)

                return result_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_17 = ControlOutput.from_dict(data)

                return result_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_18 = DenoiseMaskOutput.from_dict(data)

                return result_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_19 = FaceMaskOutput.from_dict(data)

                return result_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_20 = FaceOffOutput.from_dict(data)

                return result_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_21 = FloatCollectionOutput.from_dict(data)

                return result_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_22 = FloatGeneratorOutput.from_dict(data)

                return result_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_23 = FloatOutput.from_dict(data)

                return result_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_24 = Flux2KleinLoRALoaderOutput.from_dict(data)

                return result_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_25 = Flux2KleinModelLoaderOutput.from_dict(data)

                return result_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_26 = FluxConditioningCollectionOutput.from_dict(data)

                return result_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_27 = FluxConditioningOutput.from_dict(data)

                return result_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_28 = FluxControlLoRALoaderOutput.from_dict(data)

                return result_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_29 = FluxControlNetOutput.from_dict(data)

                return result_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_30 = FluxFillOutput.from_dict(data)

                return result_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_31 = FluxKontextOutput.from_dict(data)

                return result_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_32 = FluxLoRALoaderOutput.from_dict(data)

                return result_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_33 = FluxModelLoaderOutput.from_dict(data)

                return result_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_34 = FluxReduxOutput.from_dict(data)

                return result_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_35 = GradientMaskOutput.from_dict(data)

                return result_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_36 = IPAdapterOutput.from_dict(data)

                return result_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_37 = IdealSizeOutput.from_dict(data)

                return result_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_38 = IfInvocationOutput.from_dict(data)

                return result_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_39 = ImageCollectionOutput.from_dict(data)

                return result_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_40 = ImageGeneratorOutput.from_dict(data)

                return result_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_41 = ImageOutput.from_dict(data)

                return result_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_42 = ImagePanelCoordinateOutput.from_dict(data)

                return result_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_43 = IntegerCollectionOutput.from_dict(data)

                return result_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_44 = IntegerGeneratorOutput.from_dict(data)

                return result_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_45 = IntegerOutput.from_dict(data)

                return result_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_46 = IterateInvocationOutput.from_dict(data)

                return result_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_47 = LatentsCollectionOutput.from_dict(data)

                return result_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_48 = LatentsMetaOutput.from_dict(data)

                return result_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_49 = LatentsOutput.from_dict(data)

                return result_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_50 = LoRALoaderOutput.from_dict(data)

                return result_type_50
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_51 = LoRASelectorOutput.from_dict(data)

                return result_type_51
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_52 = MDControlListOutput.from_dict(data)

                return result_type_52
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_53 = MDIPAdapterListOutput.from_dict(data)

                return result_type_53
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_54 = MDT2IAdapterListOutput.from_dict(data)

                return result_type_54
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_55 = MaskOutput.from_dict(data)

                return result_type_55
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_56 = MetadataItemOutput.from_dict(data)

                return result_type_56
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_57 = MetadataOutput.from_dict(data)

                return result_type_57
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_58 = MetadataToLorasCollectionOutput.from_dict(data)

                return result_type_58
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_59 = MetadataToModelOutput.from_dict(data)

                return result_type_59
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_60 = MetadataToSDXLModelOutput.from_dict(data)

                return result_type_60
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_61 = ModelIdentifierOutput.from_dict(data)

                return result_type_61
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_62 = ModelLoaderOutput.from_dict(data)

                return result_type_62
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_63 = NoiseOutput.from_dict(data)

                return result_type_63
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_64 = PBRMapsOutput.from_dict(data)

                return result_type_64
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_65 = PairTileImageOutput.from_dict(data)

                return result_type_65
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_66 = PromptTemplateOutput.from_dict(data)

                return result_type_66
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_67 = QwenImageConditioningOutput.from_dict(data)

                return result_type_67
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_68 = QwenImageLoRALoaderOutput.from_dict(data)

                return result_type_68
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_69 = QwenImageModelLoaderOutput.from_dict(data)

                return result_type_69
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_70 = SD3ConditioningOutput.from_dict(data)

                return result_type_70
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_71 = SDXLLoRALoaderOutput.from_dict(data)

                return result_type_71
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_72 = SDXLModelLoaderOutput.from_dict(data)

                return result_type_72
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_73 = SDXLRefinerModelLoaderOutput.from_dict(data)

                return result_type_73
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_74 = SchedulerOutput.from_dict(data)

                return result_type_74
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_75 = Sd3ModelLoaderOutput.from_dict(data)

                return result_type_75
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_76 = SeamlessModeOutput.from_dict(data)

                return result_type_76
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_77 = String2Output.from_dict(data)

                return result_type_77
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_78 = StringCollectionOutput.from_dict(data)

                return result_type_78
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_79 = StringGeneratorOutput.from_dict(data)

                return result_type_79
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_80 = StringOutput.from_dict(data)

                return result_type_80
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_81 = StringPosNegOutput.from_dict(data)

                return result_type_81
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_82 = T2IAdapterOutput.from_dict(data)

                return result_type_82
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_83 = TileToPropertiesOutput.from_dict(data)

                return result_type_83
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_84 = UNetOutput.from_dict(data)

                return result_type_84
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_85 = VAEOutput.from_dict(data)

                return result_type_85
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_86 = ZImageConditioningOutput.from_dict(data)

                return result_type_86
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_87 = ZImageControlOutput.from_dict(data)

                return result_type_87
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_88 = ZImageLoRALoaderOutput.from_dict(data)

                return result_type_88
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            result_type_89 = ZImageModelLoaderOutput.from_dict(data)

            return result_type_89

        result = _parse_result(d.pop("result"))

        invocation_complete_event = cls(
            timestamp=timestamp,
            queue_id=queue_id,
            item_id=item_id,
            batch_id=batch_id,
            origin=origin,
            destination=destination,
            user_id=user_id,
            session_id=session_id,
            invocation=invocation,
            invocation_source_id=invocation_source_id,
            result=result,
        )

        invocation_complete_event.additional_properties = d
        return invocation_complete_event

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
