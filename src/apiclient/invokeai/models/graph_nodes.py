from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
    from ..models.boolean_collection_primitive import BooleanCollectionPrimitive
    from ..models.boolean_primitive import BooleanPrimitive
    from ..models.bounding_box import BoundingBox
    from ..models.calculate_image_tiles import CalculateImageTiles
    from ..models.calculate_image_tiles_even_split import CalculateImageTilesEvenSplit
    from ..models.calculate_image_tiles_minimum_overlap import CalculateImageTilesMinimumOverlap
    from ..models.canny_edge_detection import CannyEdgeDetection
    from ..models.canvas_output import CanvasOutput
    from ..models.canvas_paste_back import CanvasPasteBack
    from ..models.canvas_v2_mask_and_crop import CanvasV2MaskAndCrop
    from ..models.center_pad_or_crop_image import CenterPadOrCropImage
    from ..models.collect_invocation import CollectInvocation
    from ..models.color_correct import ColorCorrect
    from ..models.color_map import ColorMap
    from ..models.color_primitive import ColorPrimitive
    from ..models.combine_masks import CombineMasks
    from ..models.conditioning_collection_primitive import ConditioningCollectionPrimitive
    from ..models.conditioning_primitive import ConditioningPrimitive
    from ..models.content_shuffle import ContentShuffle
    from ..models.control_lo_raflux import ControlLoRAFLUX
    from ..models.control_net_sd15sd2sdxl import ControlNetSD15SD2SDXL
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
    from ..models.face_off import FaceOff
    from ..models.float_batch import FloatBatch
    from ..models.float_collection_primitive import FloatCollectionPrimitive
    from ..models.float_generator import FloatGenerator
    from ..models.float_math import FloatMath
    from ..models.float_primitive import FloatPrimitive
    from ..models.float_range import FloatRange
    from ..models.float_to_integer import FloatToInteger
    from ..models.flux2_denoise import FLUX2Denoise
    from ..models.flux_control_net import FLUXControlNet
    from ..models.flux_denoise import FLUXDenoise
    from ..models.flux_denoise_metadata import FLUXDenoiseMetadata
    from ..models.flux_fill_conditioning import FLUXFillConditioning
    from ..models.flux_kontext_image_prep import FLUXKontextImagePrep
    from ..models.flux_redux import FLUXRedux
    from ..models.fluxip_adapter import FLUXIPAdapter
    from ..models.gemini_image_generation import GeminiImageGeneration
    from ..models.get_image_mask_bounding_box import GetImageMaskBoundingBox
    from ..models.grounding_dino_text_prompt_object_detection import GroundingDINOTextPromptObjectDetection
    from ..models.hed_edge_detection import HEDEdgeDetection
    from ..models.heuristic_resize import HeuristicResize
    from ..models.ideal_size_sd15sdxl import IdealSizeSD15SDXL
    from ..models.if_ import If
    from ..models.image_batch import ImageBatch
    from ..models.image_collection_primitive import ImageCollectionPrimitive
    from ..models.image_compositor import ImageCompositor
    from ..models.image_dilate_or_erode import ImageDilateOrErode
    from ..models.image_generator import ImageGenerator
    from ..models.image_layer_blend import ImageLayerBlend
    from ..models.image_mask_to_tensor import ImageMaskToTensor
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
    from ..models.integer_collection_primitive import IntegerCollectionPrimitive
    from ..models.integer_generator import IntegerGenerator
    from ..models.integer_math import IntegerMath
    from ..models.integer_primitive import IntegerPrimitive
    from ..models.integer_range import IntegerRange
    from ..models.integer_range_of_size import IntegerRangeOfSize
    from ..models.inverse_lerp_image import InverseLerpImage
    from ..models.invert_tensor_mask import InvertTensorMask
    from ..models.ip_adapter_sd15sdxl import IPAdapterSD15SDXL
    from ..models.iterate_invocation import IterateInvocation
    from ..models.kontext_conditioning_flux import KontextConditioningFLUX
    from ..models.l_la_va_one_vision_vllm import LLaVAOneVisionVLLM
    from ..models.la_ma_infill import LaMaInfill
    from ..models.latents_collection_primitive import LatentsCollectionPrimitive
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
    from ..models.media_pipe_face_detection import MediaPipeFaceDetection
    from ..models.merge_tiles_to_image import MergeTilesToImage
    from ..models.metadata import Metadata
    from ..models.metadata_field_extractor import MetadataFieldExtractor
    from ..models.metadata_from_image import MetadataFromImage
    from ..models.metadata_item import MetadataItem
    from ..models.metadata_item_linked import MetadataItemLinked
    from ..models.metadata_merge import MetadataMerge
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
    from ..models.metadata_to_model import MetadataToModel
    from ..models.metadata_to_scheduler import MetadataToScheduler
    from ..models.metadata_to_sdxl_lo_r_as import MetadataToSDXLLoRAs
    from ..models.metadata_to_sdxl_model import MetadataToSDXLModel
    from ..models.metadata_to_string import MetadataToString
    from ..models.metadata_to_string_collection import MetadataToStringCollection
    from ..models.metadata_to_t2i_adapters import MetadataToT2IAdapters
    from ..models.metadata_to_vae import MetadataToVAE
    from ..models.mlsd_detection import MLSDDetection
    from ..models.multiply_image_channel import MultiplyImageChannel
    from ..models.multiply_images import MultiplyImages
    from ..models.multiply_integers import MultiplyIntegers
    from ..models.normal_map import NormalMap
    from ..models.offset_image_channel import OffsetImageChannel
    from ..models.open_ai_image_generation import OpenAIImageGeneration
    from ..models.open_cv_inpaint import OpenCVInpaint
    from ..models.pair_tile_with_image import PairTileWithImage
    from ..models.paste_image import PasteImage
    from ..models.paste_image_into_bounding_box import PasteImageIntoBoundingBox
    from ..models.patch_match_infill import PatchMatchInfill
    from ..models.pbr_maps import PBRMaps
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
    from ..models.prompt_z_image import PromptZImage
    from ..models.prompts_from_file import PromptsFromFile
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
    from ..models.seed_variance_enhancer_z_image import SeedVarianceEnhancerZImage
    from ..models.seedream_image_generation import SeedreamImageGeneration
    from ..models.segment_anything import SegmentAnything
    from ..models.select_lo_ra import SelectLoRA
    from ..models.show_image import ShowImage
    from ..models.solid_color_infill import SolidColorInfill
    from ..models.string_batch import StringBatch
    from ..models.string_collection_primitive import StringCollectionPrimitive
    from ..models.string_generator import StringGenerator
    from ..models.string_join import StringJoin
    from ..models.string_join_three import StringJoinThree
    from ..models.string_primitive import StringPrimitive
    from ..models.string_replace import StringReplace
    from ..models.string_split import StringSplit
    from ..models.string_split_negative import StringSplitNegative
    from ..models.subtract_integers import SubtractIntegers
    from ..models.t2i_adapter_sd15sdxl import T2IAdapterSD15SDXL
    from ..models.tensor_mask_to_image import TensorMaskToImage
    from ..models.text_llm import TextLLM
    from ..models.tile_infill import TileInfill
    from ..models.tile_to_properties import TileToProperties
    from ..models.tiled_multi_diffusion_denoise_sd15sdxl import TiledMultiDiffusionDenoiseSD15SDXL
    from ..models.unsharp_mask import UnsharpMask
    from ..models.unsharp_mask_oklab import UnsharpMaskOklab
    from ..models.upscale_real_esrgan import UpscaleRealESRGAN
    from ..models.vae_model_sd15sd2sdxlsd3flux import VAEModelSD15SD2SDXLSD3FLUX
    from ..models.z_image_control_net import ZImageControlNet


T = TypeVar("T", bound="GraphNodes")


@_attrs_define
class GraphNodes:
    """The nodes in this graph"""

    additional_properties: dict[
        str,
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
        | ZImageControlNet,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_image_noise import AddImageNoise
        from ..models.add_integers import AddIntegers
        from ..models.add_invisible_watermark import AddInvisibleWatermark
        from ..models.adjust_image_hue import AdjustImageHue
        from ..models.adjust_image_hue_oklch import AdjustImageHueOklch
        from ..models.adjust_image_hue_plus import AdjustImageHuePlus
        from ..models.alibaba_cloud_dash_scope_image_generation import AlibabaCloudDashScopeImageGeneration
        from ..models.alpha_mask_to_tensor import AlphaMaskToTensor
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
        from ..models.boolean_collection_primitive import BooleanCollectionPrimitive
        from ..models.boolean_primitive import BooleanPrimitive
        from ..models.bounding_box import BoundingBox
        from ..models.calculate_image_tiles import CalculateImageTiles
        from ..models.calculate_image_tiles_even_split import CalculateImageTilesEvenSplit
        from ..models.calculate_image_tiles_minimum_overlap import CalculateImageTilesMinimumOverlap
        from ..models.canny_edge_detection import CannyEdgeDetection
        from ..models.canvas_output import CanvasOutput
        from ..models.canvas_paste_back import CanvasPasteBack
        from ..models.canvas_v2_mask_and_crop import CanvasV2MaskAndCrop
        from ..models.center_pad_or_crop_image import CenterPadOrCropImage
        from ..models.collect_invocation import CollectInvocation
        from ..models.color_correct import ColorCorrect
        from ..models.color_map import ColorMap
        from ..models.color_primitive import ColorPrimitive
        from ..models.combine_masks import CombineMasks
        from ..models.conditioning_collection_primitive import ConditioningCollectionPrimitive
        from ..models.conditioning_primitive import ConditioningPrimitive
        from ..models.content_shuffle import ContentShuffle
        from ..models.control_lo_raflux import ControlLoRAFLUX
        from ..models.control_net_sd15sd2sdxl import ControlNetSD15SD2SDXL
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
        from ..models.face_off import FaceOff
        from ..models.float_batch import FloatBatch
        from ..models.float_collection_primitive import FloatCollectionPrimitive
        from ..models.float_generator import FloatGenerator
        from ..models.float_math import FloatMath
        from ..models.float_primitive import FloatPrimitive
        from ..models.float_range import FloatRange
        from ..models.float_to_integer import FloatToInteger
        from ..models.flux2_denoise import FLUX2Denoise
        from ..models.flux_control_net import FLUXControlNet
        from ..models.flux_denoise import FLUXDenoise
        from ..models.flux_denoise_metadata import FLUXDenoiseMetadata
        from ..models.flux_fill_conditioning import FLUXFillConditioning
        from ..models.flux_kontext_image_prep import FLUXKontextImagePrep
        from ..models.flux_redux import FLUXRedux
        from ..models.fluxip_adapter import FLUXIPAdapter
        from ..models.gemini_image_generation import GeminiImageGeneration
        from ..models.get_image_mask_bounding_box import GetImageMaskBoundingBox
        from ..models.grounding_dino_text_prompt_object_detection import GroundingDINOTextPromptObjectDetection
        from ..models.hed_edge_detection import HEDEdgeDetection
        from ..models.heuristic_resize import HeuristicResize
        from ..models.ideal_size_sd15sdxl import IdealSizeSD15SDXL
        from ..models.if_ import If
        from ..models.image_batch import ImageBatch
        from ..models.image_collection_primitive import ImageCollectionPrimitive
        from ..models.image_compositor import ImageCompositor
        from ..models.image_dilate_or_erode import ImageDilateOrErode
        from ..models.image_generator import ImageGenerator
        from ..models.image_layer_blend import ImageLayerBlend
        from ..models.image_mask_to_tensor import ImageMaskToTensor
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
        from ..models.integer_collection_primitive import IntegerCollectionPrimitive
        from ..models.integer_generator import IntegerGenerator
        from ..models.integer_math import IntegerMath
        from ..models.integer_primitive import IntegerPrimitive
        from ..models.integer_range import IntegerRange
        from ..models.integer_range_of_size import IntegerRangeOfSize
        from ..models.inverse_lerp_image import InverseLerpImage
        from ..models.invert_tensor_mask import InvertTensorMask
        from ..models.ip_adapter_sd15sdxl import IPAdapterSD15SDXL
        from ..models.iterate_invocation import IterateInvocation
        from ..models.kontext_conditioning_flux import KontextConditioningFLUX
        from ..models.l_la_va_one_vision_vllm import LLaVAOneVisionVLLM
        from ..models.la_ma_infill import LaMaInfill
        from ..models.latents_collection_primitive import LatentsCollectionPrimitive
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
        from ..models.media_pipe_face_detection import MediaPipeFaceDetection
        from ..models.merge_tiles_to_image import MergeTilesToImage
        from ..models.metadata import Metadata
        from ..models.metadata_field_extractor import MetadataFieldExtractor
        from ..models.metadata_from_image import MetadataFromImage
        from ..models.metadata_item import MetadataItem
        from ..models.metadata_item_linked import MetadataItemLinked
        from ..models.metadata_merge import MetadataMerge
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
        from ..models.metadata_to_model import MetadataToModel
        from ..models.metadata_to_scheduler import MetadataToScheduler
        from ..models.metadata_to_sdxl_lo_r_as import MetadataToSDXLLoRAs
        from ..models.metadata_to_sdxl_model import MetadataToSDXLModel
        from ..models.metadata_to_string import MetadataToString
        from ..models.metadata_to_string_collection import MetadataToStringCollection
        from ..models.metadata_to_t2i_adapters import MetadataToT2IAdapters
        from ..models.metadata_to_vae import MetadataToVAE
        from ..models.mlsd_detection import MLSDDetection
        from ..models.multiply_image_channel import MultiplyImageChannel
        from ..models.multiply_images import MultiplyImages
        from ..models.multiply_integers import MultiplyIntegers
        from ..models.normal_map import NormalMap
        from ..models.offset_image_channel import OffsetImageChannel
        from ..models.open_ai_image_generation import OpenAIImageGeneration
        from ..models.open_cv_inpaint import OpenCVInpaint
        from ..models.pair_tile_with_image import PairTileWithImage
        from ..models.paste_image import PasteImage
        from ..models.paste_image_into_bounding_box import PasteImageIntoBoundingBox
        from ..models.patch_match_infill import PatchMatchInfill
        from ..models.pbr_maps import PBRMaps
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
        from ..models.prompts_from_file import PromptsFromFile
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
        from ..models.seed_variance_enhancer_z_image import SeedVarianceEnhancerZImage
        from ..models.seedream_image_generation import SeedreamImageGeneration
        from ..models.segment_anything import SegmentAnything
        from ..models.select_lo_ra import SelectLoRA
        from ..models.show_image import ShowImage
        from ..models.solid_color_infill import SolidColorInfill
        from ..models.string_batch import StringBatch
        from ..models.string_collection_primitive import StringCollectionPrimitive
        from ..models.string_generator import StringGenerator
        from ..models.string_join import StringJoin
        from ..models.string_join_three import StringJoinThree
        from ..models.string_primitive import StringPrimitive
        from ..models.string_replace import StringReplace
        from ..models.string_split import StringSplit
        from ..models.string_split_negative import StringSplitNegative
        from ..models.subtract_integers import SubtractIntegers
        from ..models.t2i_adapter_sd15sdxl import T2IAdapterSD15SDXL
        from ..models.tensor_mask_to_image import TensorMaskToImage
        from ..models.text_llm import TextLLM
        from ..models.tile_infill import TileInfill
        from ..models.tile_to_properties import TileToProperties
        from ..models.tiled_multi_diffusion_denoise_sd15sdxl import TiledMultiDiffusionDenoiseSD15SDXL
        from ..models.unsharp_mask import UnsharpMask
        from ..models.unsharp_mask_oklab import UnsharpMaskOklab
        from ..models.upscale_real_esrgan import UpscaleRealESRGAN
        from ..models.vae_model_sd15sd2sdxlsd3flux import VAEModelSD15SD2SDXLSD3FLUX
        from ..models.z_image_control_net import ZImageControlNet

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, AddIntegers):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AlibabaCloudDashScopeImageGeneration):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AlphaMaskToTensor):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseAnima):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsAnima):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageAnima):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRACollectionAnima):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRAAnima):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelAnima):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptAnima):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyTensorMaskToImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyMaskToImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BlankImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BlendLatents):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BooleanCollectionPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BooleanPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BoundingBox):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyCLIPSkipSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CV2Infill):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CalculateImageTilesEvenSplit):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CalculateImageTiles):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CalculateImageTilesMinimumOverlap):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CannyEdgeDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CanvasOutput):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CanvasPasteBack):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CanvasV2MaskAndCrop):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CenterPadOrCropImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseCogView4):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsCogView4):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageCogView4):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelCogView4):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptCogView4):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CollectInvocation):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ColorCorrect):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ColorPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ColorMap):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptSD15):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ConditioningCollectionPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ConditioningPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ContentShuffle):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ControlNetSD15SD2SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CoreMetadata):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CreateDenoiseMask):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CreateGradientMask):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CropImageToBoundingBox):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CropLatents):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, OpenCVInpaint):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DWOpenposeDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DecodeInvisibleWatermark):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseSD15SDXLMetadata):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DepthAnythingDepthEstimation):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DivideIntegers):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DynamicPrompt):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, UpscaleRealESRGAN):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ExpandMaskWithFade):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRACollectionFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FaceIdentifier):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FaceMask):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FaceOff):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatBatch):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatCollectionPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatGenerator):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatRange):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatMath):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FloatToInteger):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUX2Denoise):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRACollectionFlux2Klein):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRAFlux2Klein):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelFlux2Klein):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptFlux2Klein):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageFLUX2):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsFLUX2):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ControlLoRAFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUXControlNet):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUXDenoise):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUXDenoiseMetadata):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUXFillConditioning):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUXIPAdapter):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUXKontextImagePrep):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, KontextConditioningFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRAFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, FLUXRedux):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsFLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyFreeUSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, GeminiImageGeneration):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, GetImageMaskBoundingBox):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, GroundingDINOTextPromptObjectDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, HEDEdgeDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, HeuristicResize):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IPAdapterSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IdealSizeSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, If):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageBatch):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BlurImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ExtractImageChannel):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MultiplyImageChannel):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, OffsetImageChannel):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageCollectionPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ConvertImageMode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CropImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageGenerator):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AdjustImageHue):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, InverseLerpImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImagePrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LerpImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageMaskToTensor):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MultiplyImages):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BlurNSFWImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AddImageNoise):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImagePanelLayout):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PasteImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ResizeImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ScaleImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AddInvisibleWatermark):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SolidColorInfill):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PatchMatchInfill):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TileInfill):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerBatch):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerCollectionPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerGenerator):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerMath):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, InvertTensorMask):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AdjustImageHuePlus):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, EquivalentAchromaticLightness):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageLayerBlend):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageCompositor):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageDilateOrErode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, EnhanceImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageValueThresholds):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IterateInvocation):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LaMaInfill):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsCollectionPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LineartAnimeEdgeDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LineartEdgeDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LLaVAOneVisionVLLM):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRACollectionSD15):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRASD15):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SelectLoRA):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MLSDDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelSD15SD2):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CombineMasks):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MaskEdge):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MaskFromAlpha):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MaskFromSegmentedImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TensorMaskToImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MediaPipeFaceDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataMerge):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MergeTilesToImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataFieldExtractor):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataFromImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, Metadata):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataItem):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataItemLinked):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToBoolCollection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToBool):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToControlNets):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToFloatCollection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToFloat):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToIPAdapters):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToIntegerCollection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToInteger):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToLoRACollection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToLoRAs):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToModel):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToSDXLLoRAs):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToSDXLModel):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToScheduler):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToStringCollection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToString):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToT2IAdapters):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MetadataToVAE):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AnyModel):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MultiplyIntegers):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CreateLatentNoise):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, NormalMap):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, UnsharpMaskOklab):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AdjustImageHueOklch):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, OpenAIImageGeneration):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PBRMaps):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PairTileWithImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PasteImageIntoBoundingBox):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PiDiNetEdgeDetection):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptTemplate):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptsFromFile):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseQwenImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsQwenImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageQwenImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRACollectionQwenImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRAQwenImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelQwenImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptQwenImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, RandomFloat):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, RandomInteger):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, RandomRange):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerRange):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerRangeOfSize):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CreateRectangleMask):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ResizeLatents):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, RoundFloat):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseSD3):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsSD3):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageSD3):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptSDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRACollectionSDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRASDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelSDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptSDXLRefiner):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, RefinerModelSDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SaveImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SaveImageGalleryFileExport):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ScaleLatents):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, Scheduler):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelSD3):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, PromptSD3):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplySeamlessSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SeedreamImageGeneration):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SegmentAnything):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ShowImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToImageAutoscale):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringBatch):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringCollectionPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringGenerator):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringPrimitive):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringJoin):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringJoinThree):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringReplace):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringSplit):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, StringSplitNegative):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SubtractIntegers):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, T2IAdapterSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TextLLM):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TileToProperties):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TiledMultiDiffusionDenoiseSD15SDXL):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, UnsharpMask):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, VAEModelSD15SD2SDXLSD3FLUX):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ZImageControlNet):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseZImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, DenoiseZImageMetadata):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ImageToLatentsZImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, LatentsToImageZImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRACollectionZImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ApplyLoRAZImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MainModelZImage):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SeedVarianceEnhancerZImage):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

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
        from ..models.boolean_collection_primitive import BooleanCollectionPrimitive
        from ..models.boolean_primitive import BooleanPrimitive
        from ..models.bounding_box import BoundingBox
        from ..models.calculate_image_tiles import CalculateImageTiles
        from ..models.calculate_image_tiles_even_split import CalculateImageTilesEvenSplit
        from ..models.calculate_image_tiles_minimum_overlap import CalculateImageTilesMinimumOverlap
        from ..models.canny_edge_detection import CannyEdgeDetection
        from ..models.canvas_output import CanvasOutput
        from ..models.canvas_paste_back import CanvasPasteBack
        from ..models.canvas_v2_mask_and_crop import CanvasV2MaskAndCrop
        from ..models.center_pad_or_crop_image import CenterPadOrCropImage
        from ..models.collect_invocation import CollectInvocation
        from ..models.color_correct import ColorCorrect
        from ..models.color_map import ColorMap
        from ..models.color_primitive import ColorPrimitive
        from ..models.combine_masks import CombineMasks
        from ..models.conditioning_collection_primitive import ConditioningCollectionPrimitive
        from ..models.conditioning_primitive import ConditioningPrimitive
        from ..models.content_shuffle import ContentShuffle
        from ..models.control_lo_raflux import ControlLoRAFLUX
        from ..models.control_net_sd15sd2sdxl import ControlNetSD15SD2SDXL
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
        from ..models.face_off import FaceOff
        from ..models.float_batch import FloatBatch
        from ..models.float_collection_primitive import FloatCollectionPrimitive
        from ..models.float_generator import FloatGenerator
        from ..models.float_math import FloatMath
        from ..models.float_primitive import FloatPrimitive
        from ..models.float_range import FloatRange
        from ..models.float_to_integer import FloatToInteger
        from ..models.flux2_denoise import FLUX2Denoise
        from ..models.flux_control_net import FLUXControlNet
        from ..models.flux_denoise import FLUXDenoise
        from ..models.flux_denoise_metadata import FLUXDenoiseMetadata
        from ..models.flux_fill_conditioning import FLUXFillConditioning
        from ..models.flux_kontext_image_prep import FLUXKontextImagePrep
        from ..models.flux_redux import FLUXRedux
        from ..models.fluxip_adapter import FLUXIPAdapter
        from ..models.gemini_image_generation import GeminiImageGeneration
        from ..models.get_image_mask_bounding_box import GetImageMaskBoundingBox
        from ..models.grounding_dino_text_prompt_object_detection import GroundingDINOTextPromptObjectDetection
        from ..models.hed_edge_detection import HEDEdgeDetection
        from ..models.heuristic_resize import HeuristicResize
        from ..models.ideal_size_sd15sdxl import IdealSizeSD15SDXL
        from ..models.if_ import If
        from ..models.image_batch import ImageBatch
        from ..models.image_collection_primitive import ImageCollectionPrimitive
        from ..models.image_compositor import ImageCompositor
        from ..models.image_dilate_or_erode import ImageDilateOrErode
        from ..models.image_generator import ImageGenerator
        from ..models.image_layer_blend import ImageLayerBlend
        from ..models.image_mask_to_tensor import ImageMaskToTensor
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
        from ..models.integer_collection_primitive import IntegerCollectionPrimitive
        from ..models.integer_generator import IntegerGenerator
        from ..models.integer_math import IntegerMath
        from ..models.integer_primitive import IntegerPrimitive
        from ..models.integer_range import IntegerRange
        from ..models.integer_range_of_size import IntegerRangeOfSize
        from ..models.inverse_lerp_image import InverseLerpImage
        from ..models.invert_tensor_mask import InvertTensorMask
        from ..models.ip_adapter_sd15sdxl import IPAdapterSD15SDXL
        from ..models.iterate_invocation import IterateInvocation
        from ..models.kontext_conditioning_flux import KontextConditioningFLUX
        from ..models.l_la_va_one_vision_vllm import LLaVAOneVisionVLLM
        from ..models.la_ma_infill import LaMaInfill
        from ..models.latents_collection_primitive import LatentsCollectionPrimitive
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
        from ..models.media_pipe_face_detection import MediaPipeFaceDetection
        from ..models.merge_tiles_to_image import MergeTilesToImage
        from ..models.metadata import Metadata
        from ..models.metadata_field_extractor import MetadataFieldExtractor
        from ..models.metadata_from_image import MetadataFromImage
        from ..models.metadata_item import MetadataItem
        from ..models.metadata_item_linked import MetadataItemLinked
        from ..models.metadata_merge import MetadataMerge
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
        from ..models.metadata_to_model import MetadataToModel
        from ..models.metadata_to_scheduler import MetadataToScheduler
        from ..models.metadata_to_sdxl_lo_r_as import MetadataToSDXLLoRAs
        from ..models.metadata_to_sdxl_model import MetadataToSDXLModel
        from ..models.metadata_to_string import MetadataToString
        from ..models.metadata_to_string_collection import MetadataToStringCollection
        from ..models.metadata_to_t2i_adapters import MetadataToT2IAdapters
        from ..models.metadata_to_vae import MetadataToVAE
        from ..models.mlsd_detection import MLSDDetection
        from ..models.multiply_image_channel import MultiplyImageChannel
        from ..models.multiply_images import MultiplyImages
        from ..models.multiply_integers import MultiplyIntegers
        from ..models.normal_map import NormalMap
        from ..models.offset_image_channel import OffsetImageChannel
        from ..models.open_ai_image_generation import OpenAIImageGeneration
        from ..models.open_cv_inpaint import OpenCVInpaint
        from ..models.pair_tile_with_image import PairTileWithImage
        from ..models.paste_image import PasteImage
        from ..models.paste_image_into_bounding_box import PasteImageIntoBoundingBox
        from ..models.patch_match_infill import PatchMatchInfill
        from ..models.pbr_maps import PBRMaps
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
        from ..models.prompt_z_image import PromptZImage
        from ..models.prompts_from_file import PromptsFromFile
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
        from ..models.seed_variance_enhancer_z_image import SeedVarianceEnhancerZImage
        from ..models.seedream_image_generation import SeedreamImageGeneration
        from ..models.segment_anything import SegmentAnything
        from ..models.select_lo_ra import SelectLoRA
        from ..models.show_image import ShowImage
        from ..models.solid_color_infill import SolidColorInfill
        from ..models.string_batch import StringBatch
        from ..models.string_collection_primitive import StringCollectionPrimitive
        from ..models.string_generator import StringGenerator
        from ..models.string_join import StringJoin
        from ..models.string_join_three import StringJoinThree
        from ..models.string_primitive import StringPrimitive
        from ..models.string_replace import StringReplace
        from ..models.string_split import StringSplit
        from ..models.string_split_negative import StringSplitNegative
        from ..models.subtract_integers import SubtractIntegers
        from ..models.t2i_adapter_sd15sdxl import T2IAdapterSD15SDXL
        from ..models.tensor_mask_to_image import TensorMaskToImage
        from ..models.text_llm import TextLLM
        from ..models.tile_infill import TileInfill
        from ..models.tile_to_properties import TileToProperties
        from ..models.tiled_multi_diffusion_denoise_sd15sdxl import TiledMultiDiffusionDenoiseSD15SDXL
        from ..models.unsharp_mask import UnsharpMask
        from ..models.unsharp_mask_oklab import UnsharpMaskOklab
        from ..models.upscale_real_esrgan import UpscaleRealESRGAN
        from ..models.vae_model_sd15sd2sdxlsd3flux import VAEModelSD15SD2SDXLSD3FLUX
        from ..models.z_image_control_net import ZImageControlNet

        d = dict(src_dict)
        graph_nodes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
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
                    additional_property_type_0 = AddIntegers.from_dict(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = AlibabaCloudDashScopeImageGeneration.from_dict(data)

                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = AlphaMaskToTensor.from_dict(data)

                    return additional_property_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = DenoiseAnima.from_dict(data)

                    return additional_property_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_4 = ImageToLatentsAnima.from_dict(data)

                    return additional_property_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_5 = LatentsToImageAnima.from_dict(data)

                    return additional_property_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_6 = ApplyLoRACollectionAnima.from_dict(data)

                    return additional_property_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_7 = ApplyLoRAAnima.from_dict(data)

                    return additional_property_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_8 = MainModelAnima.from_dict(data)

                    return additional_property_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_9 = PromptAnima.from_dict(data)

                    return additional_property_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_10 = ApplyTensorMaskToImage.from_dict(data)

                    return additional_property_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_11 = ApplyMaskToImage.from_dict(data)

                    return additional_property_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_12 = BlankImage.from_dict(data)

                    return additional_property_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_13 = BlendLatents.from_dict(data)

                    return additional_property_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_14 = BooleanCollectionPrimitive.from_dict(data)

                    return additional_property_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_15 = BooleanPrimitive.from_dict(data)

                    return additional_property_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_16 = BoundingBox.from_dict(data)

                    return additional_property_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_17 = ApplyCLIPSkipSD15SDXL.from_dict(data)

                    return additional_property_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_18 = CV2Infill.from_dict(data)

                    return additional_property_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_19 = CalculateImageTilesEvenSplit.from_dict(data)

                    return additional_property_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_20 = CalculateImageTiles.from_dict(data)

                    return additional_property_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_21 = CalculateImageTilesMinimumOverlap.from_dict(data)

                    return additional_property_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_22 = CannyEdgeDetection.from_dict(data)

                    return additional_property_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_23 = CanvasOutput.from_dict(data)

                    return additional_property_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_24 = CanvasPasteBack.from_dict(data)

                    return additional_property_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_25 = CanvasV2MaskAndCrop.from_dict(data)

                    return additional_property_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_26 = CenterPadOrCropImage.from_dict(data)

                    return additional_property_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_27 = DenoiseCogView4.from_dict(data)

                    return additional_property_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_28 = ImageToLatentsCogView4.from_dict(data)

                    return additional_property_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_29 = LatentsToImageCogView4.from_dict(data)

                    return additional_property_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_30 = MainModelCogView4.from_dict(data)

                    return additional_property_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_31 = PromptCogView4.from_dict(data)

                    return additional_property_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_32 = CollectInvocation.from_dict(data)

                    return additional_property_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_33 = ColorCorrect.from_dict(data)

                    return additional_property_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_34 = ColorPrimitive.from_dict(data)

                    return additional_property_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_35 = ColorMap.from_dict(data)

                    return additional_property_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_36 = PromptSD15.from_dict(data)

                    return additional_property_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_37 = ConditioningCollectionPrimitive.from_dict(data)

                    return additional_property_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_38 = ConditioningPrimitive.from_dict(data)

                    return additional_property_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_39 = ContentShuffle.from_dict(data)

                    return additional_property_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_40 = ControlNetSD15SD2SDXL.from_dict(data)

                    return additional_property_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_41 = CoreMetadata.from_dict(data)

                    return additional_property_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_42 = CreateDenoiseMask.from_dict(data)

                    return additional_property_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_43 = CreateGradientMask.from_dict(data)

                    return additional_property_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_44 = CropImageToBoundingBox.from_dict(data)

                    return additional_property_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_45 = CropLatents.from_dict(data)

                    return additional_property_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_46 = OpenCVInpaint.from_dict(data)

                    return additional_property_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_47 = DWOpenposeDetection.from_dict(data)

                    return additional_property_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_48 = DecodeInvisibleWatermark.from_dict(data)

                    return additional_property_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_49 = DenoiseSD15SDXL.from_dict(data)

                    return additional_property_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_50 = DenoiseSD15SDXLMetadata.from_dict(data)

                    return additional_property_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_51 = DepthAnythingDepthEstimation.from_dict(data)

                    return additional_property_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_52 = DivideIntegers.from_dict(data)

                    return additional_property_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_53 = DynamicPrompt.from_dict(data)

                    return additional_property_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_54 = UpscaleRealESRGAN.from_dict(data)

                    return additional_property_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_55 = ExpandMaskWithFade.from_dict(data)

                    return additional_property_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_56 = ApplyLoRACollectionFLUX.from_dict(data)

                    return additional_property_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_57 = FaceIdentifier.from_dict(data)

                    return additional_property_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_58 = FaceMask.from_dict(data)

                    return additional_property_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_59 = FaceOff.from_dict(data)

                    return additional_property_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_60 = FloatBatch.from_dict(data)

                    return additional_property_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_61 = FloatCollectionPrimitive.from_dict(data)

                    return additional_property_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_62 = FloatGenerator.from_dict(data)

                    return additional_property_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_63 = FloatPrimitive.from_dict(data)

                    return additional_property_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_64 = FloatRange.from_dict(data)

                    return additional_property_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_65 = FloatMath.from_dict(data)

                    return additional_property_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_66 = FloatToInteger.from_dict(data)

                    return additional_property_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_67 = FLUX2Denoise.from_dict(data)

                    return additional_property_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_68 = ApplyLoRACollectionFlux2Klein.from_dict(data)

                    return additional_property_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_69 = ApplyLoRAFlux2Klein.from_dict(data)

                    return additional_property_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_70 = MainModelFlux2Klein.from_dict(data)

                    return additional_property_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_71 = PromptFlux2Klein.from_dict(data)

                    return additional_property_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_72 = LatentsToImageFLUX2.from_dict(data)

                    return additional_property_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_73 = ImageToLatentsFLUX2.from_dict(data)

                    return additional_property_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_74 = ControlLoRAFLUX.from_dict(data)

                    return additional_property_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_75 = FLUXControlNet.from_dict(data)

                    return additional_property_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_76 = FLUXDenoise.from_dict(data)

                    return additional_property_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_77 = FLUXDenoiseMetadata.from_dict(data)

                    return additional_property_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_78 = FLUXFillConditioning.from_dict(data)

                    return additional_property_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_79 = FLUXIPAdapter.from_dict(data)

                    return additional_property_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_80 = FLUXKontextImagePrep.from_dict(data)

                    return additional_property_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_81 = KontextConditioningFLUX.from_dict(data)

                    return additional_property_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_82 = ApplyLoRAFLUX.from_dict(data)

                    return additional_property_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_83 = MainModelFLUX.from_dict(data)

                    return additional_property_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_84 = FLUXRedux.from_dict(data)

                    return additional_property_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_85 = PromptFLUX.from_dict(data)

                    return additional_property_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_86 = LatentsToImageFLUX.from_dict(data)

                    return additional_property_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_87 = ImageToLatentsFLUX.from_dict(data)

                    return additional_property_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_88 = ApplyFreeUSD15SDXL.from_dict(data)

                    return additional_property_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_89 = GeminiImageGeneration.from_dict(data)

                    return additional_property_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_90 = GetImageMaskBoundingBox.from_dict(data)

                    return additional_property_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_91 = GroundingDINOTextPromptObjectDetection.from_dict(data)

                    return additional_property_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_92 = HEDEdgeDetection.from_dict(data)

                    return additional_property_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_93 = HeuristicResize.from_dict(data)

                    return additional_property_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_94 = IPAdapterSD15SDXL.from_dict(data)

                    return additional_property_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_95 = IdealSizeSD15SDXL.from_dict(data)

                    return additional_property_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_96 = If.from_dict(data)

                    return additional_property_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_97 = ImageBatch.from_dict(data)

                    return additional_property_type_97
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_98 = BlurImage.from_dict(data)

                    return additional_property_type_98
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_99 = ExtractImageChannel.from_dict(data)

                    return additional_property_type_99
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_100 = MultiplyImageChannel.from_dict(data)

                    return additional_property_type_100
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_101 = OffsetImageChannel.from_dict(data)

                    return additional_property_type_101
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_102 = ImageCollectionPrimitive.from_dict(data)

                    return additional_property_type_102
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_103 = ConvertImageMode.from_dict(data)

                    return additional_property_type_103
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_104 = CropImage.from_dict(data)

                    return additional_property_type_104
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_105 = ImageGenerator.from_dict(data)

                    return additional_property_type_105
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_106 = AdjustImageHue.from_dict(data)

                    return additional_property_type_106
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_107 = InverseLerpImage.from_dict(data)

                    return additional_property_type_107
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_108 = ImagePrimitive.from_dict(data)

                    return additional_property_type_108
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_109 = LerpImage.from_dict(data)

                    return additional_property_type_109
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_110 = ImageMaskToTensor.from_dict(data)

                    return additional_property_type_110
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_111 = MultiplyImages.from_dict(data)

                    return additional_property_type_111
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_112 = BlurNSFWImage.from_dict(data)

                    return additional_property_type_112
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_113 = AddImageNoise.from_dict(data)

                    return additional_property_type_113
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_114 = ImagePanelLayout.from_dict(data)

                    return additional_property_type_114
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_115 = PasteImage.from_dict(data)

                    return additional_property_type_115
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_116 = ResizeImage.from_dict(data)

                    return additional_property_type_116
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_117 = ScaleImage.from_dict(data)

                    return additional_property_type_117
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_118 = ImageToLatentsSD15SDXL.from_dict(data)

                    return additional_property_type_118
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_119 = AddInvisibleWatermark.from_dict(data)

                    return additional_property_type_119
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_120 = SolidColorInfill.from_dict(data)

                    return additional_property_type_120
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_121 = PatchMatchInfill.from_dict(data)

                    return additional_property_type_121
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_122 = TileInfill.from_dict(data)

                    return additional_property_type_122
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_123 = IntegerBatch.from_dict(data)

                    return additional_property_type_123
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_124 = IntegerCollectionPrimitive.from_dict(data)

                    return additional_property_type_124
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_125 = IntegerGenerator.from_dict(data)

                    return additional_property_type_125
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_126 = IntegerPrimitive.from_dict(data)

                    return additional_property_type_126
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_127 = IntegerMath.from_dict(data)

                    return additional_property_type_127
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_128 = InvertTensorMask.from_dict(data)

                    return additional_property_type_128
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_129 = AdjustImageHuePlus.from_dict(data)

                    return additional_property_type_129
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_130 = EquivalentAchromaticLightness.from_dict(data)

                    return additional_property_type_130
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_131 = ImageLayerBlend.from_dict(data)

                    return additional_property_type_131
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_132 = ImageCompositor.from_dict(data)

                    return additional_property_type_132
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_133 = ImageDilateOrErode.from_dict(data)

                    return additional_property_type_133
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_134 = EnhanceImage.from_dict(data)

                    return additional_property_type_134
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_135 = ImageValueThresholds.from_dict(data)

                    return additional_property_type_135
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_136 = IterateInvocation.from_dict(data)

                    return additional_property_type_136
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_137 = LaMaInfill.from_dict(data)

                    return additional_property_type_137
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_138 = LatentsCollectionPrimitive.from_dict(data)

                    return additional_property_type_138
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_139 = LatentsPrimitive.from_dict(data)

                    return additional_property_type_139
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_140 = LatentsToImageSD15SDXL.from_dict(data)

                    return additional_property_type_140
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_141 = LineartAnimeEdgeDetection.from_dict(data)

                    return additional_property_type_141
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_142 = LineartEdgeDetection.from_dict(data)

                    return additional_property_type_142
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_143 = LLaVAOneVisionVLLM.from_dict(data)

                    return additional_property_type_143
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_144 = ApplyLoRACollectionSD15.from_dict(data)

                    return additional_property_type_144
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_145 = ApplyLoRASD15.from_dict(data)

                    return additional_property_type_145
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_146 = SelectLoRA.from_dict(data)

                    return additional_property_type_146
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_147 = MLSDDetection.from_dict(data)

                    return additional_property_type_147
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_148 = MainModelSD15SD2.from_dict(data)

                    return additional_property_type_148
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_149 = CombineMasks.from_dict(data)

                    return additional_property_type_149
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_150 = MaskEdge.from_dict(data)

                    return additional_property_type_150
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_151 = MaskFromAlpha.from_dict(data)

                    return additional_property_type_151
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_152 = MaskFromSegmentedImage.from_dict(data)

                    return additional_property_type_152
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_153 = TensorMaskToImage.from_dict(data)

                    return additional_property_type_153
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_154 = MediaPipeFaceDetection.from_dict(data)

                    return additional_property_type_154
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_155 = MetadataMerge.from_dict(data)

                    return additional_property_type_155
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_156 = MergeTilesToImage.from_dict(data)

                    return additional_property_type_156
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_157 = MetadataFieldExtractor.from_dict(data)

                    return additional_property_type_157
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_158 = MetadataFromImage.from_dict(data)

                    return additional_property_type_158
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_159 = Metadata.from_dict(data)

                    return additional_property_type_159
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_160 = MetadataItem.from_dict(data)

                    return additional_property_type_160
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_161 = MetadataItemLinked.from_dict(data)

                    return additional_property_type_161
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_162 = MetadataToBoolCollection.from_dict(data)

                    return additional_property_type_162
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_163 = MetadataToBool.from_dict(data)

                    return additional_property_type_163
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_164 = MetadataToControlNets.from_dict(data)

                    return additional_property_type_164
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_165 = MetadataToFloatCollection.from_dict(data)

                    return additional_property_type_165
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_166 = MetadataToFloat.from_dict(data)

                    return additional_property_type_166
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_167 = MetadataToIPAdapters.from_dict(data)

                    return additional_property_type_167
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_168 = MetadataToIntegerCollection.from_dict(data)

                    return additional_property_type_168
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_169 = MetadataToInteger.from_dict(data)

                    return additional_property_type_169
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_170 = MetadataToLoRACollection.from_dict(data)

                    return additional_property_type_170
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_171 = MetadataToLoRAs.from_dict(data)

                    return additional_property_type_171
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_172 = MetadataToModel.from_dict(data)

                    return additional_property_type_172
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_173 = MetadataToSDXLLoRAs.from_dict(data)

                    return additional_property_type_173
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_174 = MetadataToSDXLModel.from_dict(data)

                    return additional_property_type_174
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_175 = MetadataToScheduler.from_dict(data)

                    return additional_property_type_175
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_176 = MetadataToStringCollection.from_dict(data)

                    return additional_property_type_176
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_177 = MetadataToString.from_dict(data)

                    return additional_property_type_177
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_178 = MetadataToT2IAdapters.from_dict(data)

                    return additional_property_type_178
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_179 = MetadataToVAE.from_dict(data)

                    return additional_property_type_179
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_180 = AnyModel.from_dict(data)

                    return additional_property_type_180
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_181 = MultiplyIntegers.from_dict(data)

                    return additional_property_type_181
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_182 = CreateLatentNoise.from_dict(data)

                    return additional_property_type_182
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_183 = NormalMap.from_dict(data)

                    return additional_property_type_183
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_184 = UnsharpMaskOklab.from_dict(data)

                    return additional_property_type_184
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_185 = AdjustImageHueOklch.from_dict(data)

                    return additional_property_type_185
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_186 = OpenAIImageGeneration.from_dict(data)

                    return additional_property_type_186
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_187 = PBRMaps.from_dict(data)

                    return additional_property_type_187
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_188 = PairTileWithImage.from_dict(data)

                    return additional_property_type_188
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_189 = PasteImageIntoBoundingBox.from_dict(data)

                    return additional_property_type_189
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_190 = PiDiNetEdgeDetection.from_dict(data)

                    return additional_property_type_190
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_191 = PromptTemplate.from_dict(data)

                    return additional_property_type_191
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_192 = PromptsFromFile.from_dict(data)

                    return additional_property_type_192
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_193 = DenoiseQwenImage.from_dict(data)

                    return additional_property_type_193
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_194 = ImageToLatentsQwenImage.from_dict(data)

                    return additional_property_type_194
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_195 = LatentsToImageQwenImage.from_dict(data)

                    return additional_property_type_195
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_196 = ApplyLoRACollectionQwenImage.from_dict(data)

                    return additional_property_type_196
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_197 = ApplyLoRAQwenImage.from_dict(data)

                    return additional_property_type_197
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_198 = MainModelQwenImage.from_dict(data)

                    return additional_property_type_198
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_199 = PromptQwenImage.from_dict(data)

                    return additional_property_type_199
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_200 = RandomFloat.from_dict(data)

                    return additional_property_type_200
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_201 = RandomInteger.from_dict(data)

                    return additional_property_type_201
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_202 = RandomRange.from_dict(data)

                    return additional_property_type_202
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_203 = IntegerRange.from_dict(data)

                    return additional_property_type_203
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_204 = IntegerRangeOfSize.from_dict(data)

                    return additional_property_type_204
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_205 = CreateRectangleMask.from_dict(data)

                    return additional_property_type_205
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_206 = ResizeLatents.from_dict(data)

                    return additional_property_type_206
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_207 = RoundFloat.from_dict(data)

                    return additional_property_type_207
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_208 = DenoiseSD3.from_dict(data)

                    return additional_property_type_208
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_209 = ImageToLatentsSD3.from_dict(data)

                    return additional_property_type_209
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_210 = LatentsToImageSD3.from_dict(data)

                    return additional_property_type_210
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_211 = PromptSDXL.from_dict(data)

                    return additional_property_type_211
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_212 = ApplyLoRACollectionSDXL.from_dict(data)

                    return additional_property_type_212
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_213 = ApplyLoRASDXL.from_dict(data)

                    return additional_property_type_213
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_214 = MainModelSDXL.from_dict(data)

                    return additional_property_type_214
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_215 = PromptSDXLRefiner.from_dict(data)

                    return additional_property_type_215
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_216 = RefinerModelSDXL.from_dict(data)

                    return additional_property_type_216
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_217 = SaveImage.from_dict(data)

                    return additional_property_type_217
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_218 = SaveImageGalleryFileExport.from_dict(data)

                    return additional_property_type_218
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_219 = ScaleLatents.from_dict(data)

                    return additional_property_type_219
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_220 = Scheduler.from_dict(data)

                    return additional_property_type_220
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_221 = MainModelSD3.from_dict(data)

                    return additional_property_type_221
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_222 = PromptSD3.from_dict(data)

                    return additional_property_type_222
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_223 = ApplySeamlessSD15SDXL.from_dict(data)

                    return additional_property_type_223
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_224 = SeedreamImageGeneration.from_dict(data)

                    return additional_property_type_224
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_225 = SegmentAnything.from_dict(data)

                    return additional_property_type_225
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_226 = ShowImage.from_dict(data)

                    return additional_property_type_226
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_227 = ImageToImageAutoscale.from_dict(data)

                    return additional_property_type_227
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_228 = ImageToImage.from_dict(data)

                    return additional_property_type_228
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_229 = StringBatch.from_dict(data)

                    return additional_property_type_229
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_230 = StringCollectionPrimitive.from_dict(data)

                    return additional_property_type_230
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_231 = StringGenerator.from_dict(data)

                    return additional_property_type_231
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_232 = StringPrimitive.from_dict(data)

                    return additional_property_type_232
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_233 = StringJoin.from_dict(data)

                    return additional_property_type_233
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_234 = StringJoinThree.from_dict(data)

                    return additional_property_type_234
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_235 = StringReplace.from_dict(data)

                    return additional_property_type_235
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_236 = StringSplit.from_dict(data)

                    return additional_property_type_236
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_237 = StringSplitNegative.from_dict(data)

                    return additional_property_type_237
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_238 = SubtractIntegers.from_dict(data)

                    return additional_property_type_238
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_239 = T2IAdapterSD15SDXL.from_dict(data)

                    return additional_property_type_239
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_240 = TextLLM.from_dict(data)

                    return additional_property_type_240
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_241 = TileToProperties.from_dict(data)

                    return additional_property_type_241
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_242 = TiledMultiDiffusionDenoiseSD15SDXL.from_dict(data)

                    return additional_property_type_242
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_243 = UnsharpMask.from_dict(data)

                    return additional_property_type_243
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_244 = VAEModelSD15SD2SDXLSD3FLUX.from_dict(data)

                    return additional_property_type_244
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_245 = ZImageControlNet.from_dict(data)

                    return additional_property_type_245
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_246 = DenoiseZImage.from_dict(data)

                    return additional_property_type_246
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_247 = DenoiseZImageMetadata.from_dict(data)

                    return additional_property_type_247
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_248 = ImageToLatentsZImage.from_dict(data)

                    return additional_property_type_248
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_249 = LatentsToImageZImage.from_dict(data)

                    return additional_property_type_249
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_250 = ApplyLoRACollectionZImage.from_dict(data)

                    return additional_property_type_250
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_251 = ApplyLoRAZImage.from_dict(data)

                    return additional_property_type_251
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_252 = MainModelZImage.from_dict(data)

                    return additional_property_type_252
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_253 = SeedVarianceEnhancerZImage.from_dict(data)

                    return additional_property_type_253
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_254 = PromptZImage.from_dict(data)

                return additional_property_type_254

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        graph_nodes.additional_properties = additional_properties
        return graph_nodes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
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
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: AddImageNoise
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
        | ZImageControlNet,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
