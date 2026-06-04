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
    from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
    from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
    from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
    from ..models.collect_invocation_output import CollectInvocationOutput
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


T = TypeVar("T", bound="InvocationOutputMap")


@_attrs_define
class InvocationOutputMap:
    """
    Attributes:
        add (IntegerOutput): Base class for nodes that output a single integer
        alibabacloud_image_generation (ImageCollectionOutput): Base class for nodes that output a collection of images
        alpha_mask_to_tensor (MaskOutput): A torch mask tensor.
        anima_denoise (LatentsOutput): Base class for nodes that output a single latents tensor
        anima_i2l (LatentsOutput): Base class for nodes that output a single latents tensor
        anima_l2i (ImageOutput): Base class for nodes that output a single image
        anima_lora_collection_loader (AnimaLoRALoaderOutput): Anima LoRA Loader Output
        anima_lora_loader (AnimaLoRALoaderOutput): Anima LoRA Loader Output
        anima_model_loader (AnimaModelLoaderOutput): Anima model loader output.
        anima_text_encoder (AnimaConditioningOutput): Base class for nodes that output an Anima text conditioning
            tensor.
        apply_mask_to_image (ImageOutput): Base class for nodes that output a single image
        apply_tensor_mask_to_image (ImageOutput): Base class for nodes that output a single image
        blank_image (ImageOutput): Base class for nodes that output a single image
        boolean (BooleanOutput): Base class for nodes that output a single boolean
        boolean_collection (BooleanCollectionOutput): Base class for nodes that output a collection of booleans
        bounding_box (BoundingBoxOutput): Base class for nodes that output a single bounding box
        calculate_image_tiles (CalculateImageTilesOutput):
        calculate_image_tiles_even_split (CalculateImageTilesOutput):
        calculate_image_tiles_min_overlap (CalculateImageTilesOutput):
        canny_edge_detection (ImageOutput): Base class for nodes that output a single image
        canvas_output (ImageOutput): Base class for nodes that output a single image
        canvas_paste_back (ImageOutput): Base class for nodes that output a single image
        canvas_v2_mask_and_crop (ImageOutput): Base class for nodes that output a single image
        clip_skip (CLIPSkipInvocationOutput): CLIP skip node output
        cogview4_denoise (LatentsOutput): Base class for nodes that output a single latents tensor
        cogview4_i2l (LatentsOutput): Base class for nodes that output a single latents tensor
        cogview4_l2i (ImageOutput): Base class for nodes that output a single image
        cogview4_model_loader (CogView4ModelLoaderOutput): CogView4 base model loader output.
        cogview4_text_encoder (CogView4ConditioningOutput): Base class for nodes that output a CogView text conditioning
            tensor.
        collect (CollectInvocationOutput):
        color (ColorOutput): Base class for nodes that output a single color
        color_correct (ImageOutput): Base class for nodes that output a single image
        color_map (ImageOutput): Base class for nodes that output a single image
        compel (ConditioningOutput): Base class for nodes that output a single conditioning tensor
        conditioning (ConditioningOutput): Base class for nodes that output a single conditioning tensor
        conditioning_collection (ConditioningCollectionOutput): Base class for nodes that output a collection of
            conditioning tensors
        content_shuffle (ImageOutput): Base class for nodes that output a single image
        controlnet (ControlOutput): node output for ControlNet info
        core_metadata (MetadataOutput):
        create_denoise_mask (DenoiseMaskOutput): Base class for nodes that output a single image
        create_gradient_mask (GradientMaskOutput): Outputs a denoise mask and an image representing the total gradient
            of the mask.
        crop_image_to_bounding_box (ImageOutput): Base class for nodes that output a single image
        crop_latents (LatentsOutput): Base class for nodes that output a single latents tensor
        cv_inpaint (ImageOutput): Base class for nodes that output a single image
        decode_watermark (StringOutput): Base class for nodes that output a single string
        denoise_latents (LatentsOutput): Base class for nodes that output a single latents tensor
        denoise_latents_meta (LatentsMetaOutput): Latents + metadata
        depth_anything_depth_estimation (ImageOutput): Base class for nodes that output a single image
        div (IntegerOutput): Base class for nodes that output a single integer
        dw_openpose_detection (ImageOutput): Base class for nodes that output a single image
        dynamic_prompt (StringCollectionOutput): Base class for nodes that output a collection of strings
        esrgan (ImageOutput): Base class for nodes that output a single image
        expand_mask_with_fade (ImageOutput): Base class for nodes that output a single image
        face_identifier (ImageOutput): Base class for nodes that output a single image
        face_mask_detection (FaceMaskOutput): Base class for FaceMask output
        face_off (FaceOffOutput): Base class for FaceOff Output
        float_ (FloatOutput): Base class for nodes that output a single float
        float_batch (FloatOutput): Base class for nodes that output a single float
        float_collection (FloatCollectionOutput): Base class for nodes that output a collection of floats
        float_generator (FloatGeneratorOutput): Base class for nodes that output a collection of floats
        float_math (FloatOutput): Base class for nodes that output a single float
        float_range (FloatCollectionOutput): Base class for nodes that output a collection of floats
        float_to_int (IntegerOutput): Base class for nodes that output a single integer
        flux2_denoise (LatentsOutput): Base class for nodes that output a single latents tensor
        flux2_klein_lora_collection_loader (Flux2KleinLoRALoaderOutput): FLUX.2 Klein LoRA Loader Output
        flux2_klein_lora_loader (Flux2KleinLoRALoaderOutput): FLUX.2 Klein LoRA Loader Output
        flux2_klein_model_loader (Flux2KleinModelLoaderOutput): Flux2 Klein model loader output.
        flux2_klein_text_encoder (FluxConditioningOutput): Base class for nodes that output a single conditioning tensor
        flux2_vae_decode (ImageOutput): Base class for nodes that output a single image
        flux2_vae_encode (LatentsOutput): Base class for nodes that output a single latents tensor
        flux_control_lora_loader (FluxControlLoRALoaderOutput): Flux Control LoRA Loader Output
        flux_controlnet (FluxControlNetOutput): FLUX ControlNet info
        flux_denoise (LatentsOutput): Base class for nodes that output a single latents tensor
        flux_denoise_meta (LatentsMetaOutput): Latents + metadata
        flux_fill (FluxFillOutput): The conditioning output of a FLUX Fill invocation.
        flux_ip_adapter (IPAdapterOutput):
        flux_kontext (FluxKontextOutput): The conditioning output of a FLUX Kontext invocation.
        flux_kontext_image_prep (ImageOutput): Base class for nodes that output a single image
        flux_lora_collection_loader (FluxLoRALoaderOutput): FLUX LoRA Loader Output
        flux_lora_loader (FluxLoRALoaderOutput): FLUX LoRA Loader Output
        flux_model_loader (FluxModelLoaderOutput): Flux base model loader output
        flux_redux (FluxReduxOutput): The conditioning output of a FLUX Redux invocation.
        flux_text_encoder (FluxConditioningOutput): Base class for nodes that output a single conditioning tensor
        flux_vae_decode (ImageOutput): Base class for nodes that output a single image
        flux_vae_encode (LatentsOutput): Base class for nodes that output a single latents tensor
        freeu (UNetOutput): Base class for invocations that output a UNet field.
        gemini_image_generation (ImageCollectionOutput): Base class for nodes that output a collection of images
        get_image_mask_bounding_box (BoundingBoxOutput): Base class for nodes that output a single bounding box
        grounding_dino (BoundingBoxCollectionOutput): Base class for nodes that output a collection of bounding boxes
        hed_edge_detection (ImageOutput): Base class for nodes that output a single image
        heuristic_resize (ImageOutput): Base class for nodes that output a single image
        i2l (LatentsOutput): Base class for nodes that output a single latents tensor
        ideal_size (IdealSizeOutput): Base class for invocations that output an image
        if_ (IfInvocationOutput):
        image (ImageOutput): Base class for nodes that output a single image
        image_batch (ImageOutput): Base class for nodes that output a single image
        image_collection (ImageCollectionOutput): Base class for nodes that output a collection of images
        image_generator (ImageGeneratorOutput): Base class for nodes that output a collection of boards
        image_mask_to_tensor (MaskOutput): A torch mask tensor.
        image_panel_layout (ImagePanelCoordinateOutput):
        img_blur (ImageOutput): Base class for nodes that output a single image
        img_chan (ImageOutput): Base class for nodes that output a single image
        img_channel_multiply (ImageOutput): Base class for nodes that output a single image
        img_channel_offset (ImageOutput): Base class for nodes that output a single image
        img_conv (ImageOutput): Base class for nodes that output a single image
        img_crop (ImageOutput): Base class for nodes that output a single image
        img_hue_adjust (ImageOutput): Base class for nodes that output a single image
        img_hue_adjust_oklch (ImageOutput): Base class for nodes that output a single image
        img_ilerp (ImageOutput): Base class for nodes that output a single image
        img_lerp (ImageOutput): Base class for nodes that output a single image
        img_mul (ImageOutput): Base class for nodes that output a single image
        img_noise (ImageOutput): Base class for nodes that output a single image
        img_nsfw (ImageOutput): Base class for nodes that output a single image
        img_pad_crop (ImageOutput): Base class for nodes that output a single image
        img_paste (ImageOutput): Base class for nodes that output a single image
        img_resize (ImageOutput): Base class for nodes that output a single image
        img_scale (ImageOutput): Base class for nodes that output a single image
        img_watermark (ImageOutput): Base class for nodes that output a single image
        infill_cv2 (ImageOutput): Base class for nodes that output a single image
        infill_lama (ImageOutput): Base class for nodes that output a single image
        infill_patchmatch (ImageOutput): Base class for nodes that output a single image
        infill_rgba (ImageOutput): Base class for nodes that output a single image
        infill_tile (ImageOutput): Base class for nodes that output a single image
        integer (IntegerOutput): Base class for nodes that output a single integer
        integer_batch (IntegerOutput): Base class for nodes that output a single integer
        integer_collection (IntegerCollectionOutput): Base class for nodes that output a collection of integers
        integer_generator (IntegerGeneratorOutput):
        integer_math (IntegerOutput): Base class for nodes that output a single integer
        invert_tensor_mask (MaskOutput): A torch mask tensor.
        invokeai_ealightness (ImageOutput): Base class for nodes that output a single image
        invokeai_img_blend (ImageOutput): Base class for nodes that output a single image
        invokeai_img_composite (ImageOutput): Base class for nodes that output a single image
        invokeai_img_dilate_erode (ImageOutput): Base class for nodes that output a single image
        invokeai_img_enhance (ImageOutput): Base class for nodes that output a single image
        invokeai_img_hue_adjust_plus (ImageOutput): Base class for nodes that output a single image
        invokeai_img_val_thresholds (ImageOutput): Base class for nodes that output a single image
        ip_adapter (IPAdapterOutput):
        iterate (IterateInvocationOutput): Used to connect iteration outputs. Will be expanded to a specific output.
        l2i (ImageOutput): Base class for nodes that output a single image
        latents (LatentsOutput): Base class for nodes that output a single latents tensor
        latents_collection (LatentsCollectionOutput): Base class for nodes that output a collection of latents tensors
        lblend (LatentsOutput): Base class for nodes that output a single latents tensor
        lineart_anime_edge_detection (ImageOutput): Base class for nodes that output a single image
        lineart_edge_detection (ImageOutput): Base class for nodes that output a single image
        llava_onevision_vllm (StringOutput): Base class for nodes that output a single string
        lora_collection_loader (LoRALoaderOutput): Model loader output
        lora_loader (LoRALoaderOutput): Model loader output
        lora_selector (LoRASelectorOutput): Model loader output
        lresize (LatentsOutput): Base class for nodes that output a single latents tensor
        lscale (LatentsOutput): Base class for nodes that output a single latents tensor
        main_model_loader (ModelLoaderOutput): Model loader output
        mask_combine (ImageOutput): Base class for nodes that output a single image
        mask_edge (ImageOutput): Base class for nodes that output a single image
        mask_from_id (ImageOutput): Base class for nodes that output a single image
        mediapipe_face_detection (ImageOutput): Base class for nodes that output a single image
        merge_metadata (MetadataOutput):
        merge_tiles_to_image (ImageOutput): Base class for nodes that output a single image
        metadata (MetadataOutput):
        metadata_field_extractor (StringOutput): Base class for nodes that output a single string
        metadata_from_image (MetadataOutput):
        metadata_item (MetadataItemOutput): Metadata Item Output
        metadata_item_linked (MetadataOutput):
        metadata_to_bool (BooleanOutput): Base class for nodes that output a single boolean
        metadata_to_bool_collection (BooleanCollectionOutput): Base class for nodes that output a collection of booleans
        metadata_to_controlnets (MDControlListOutput):
        metadata_to_float (FloatOutput): Base class for nodes that output a single float
        metadata_to_float_collection (FloatCollectionOutput): Base class for nodes that output a collection of floats
        metadata_to_integer (IntegerOutput): Base class for nodes that output a single integer
        metadata_to_integer_collection (IntegerCollectionOutput): Base class for nodes that output a collection of
            integers
        metadata_to_ip_adapters (MDIPAdapterListOutput):
        metadata_to_lora_collection (MetadataToLorasCollectionOutput): Model loader output
        metadata_to_loras (LoRALoaderOutput): Model loader output
        metadata_to_model (MetadataToModelOutput): String to main model output
        metadata_to_scheduler (SchedulerOutput):
        metadata_to_sdlx_loras (SDXLLoRALoaderOutput): SDXL LoRA Loader Output
        metadata_to_sdxl_model (MetadataToSDXLModelOutput): String to SDXL main model output
        metadata_to_string (StringOutput): Base class for nodes that output a single string
        metadata_to_string_collection (StringCollectionOutput): Base class for nodes that output a collection of strings
        metadata_to_t2i_adapters (MDT2IAdapterListOutput):
        metadata_to_vae (VAEOutput): Base class for invocations that output a VAE field
        mlsd_detection (ImageOutput): Base class for nodes that output a single image
        model_identifier (ModelIdentifierOutput): Model identifier output
        mul (IntegerOutput): Base class for nodes that output a single integer
        noise (NoiseOutput): Invocation noise output
        normal_map (ImageOutput): Base class for nodes that output a single image
        openai_image_generation (ImageCollectionOutput): Base class for nodes that output a collection of images
        pair_tile_image (PairTileImageOutput):
        paste_image_into_bounding_box (ImageOutput): Base class for nodes that output a single image
        pbr_maps (PBRMapsOutput):
        pidi_edge_detection (ImageOutput): Base class for nodes that output a single image
        prompt_from_file (StringCollectionOutput): Base class for nodes that output a collection of strings
        prompt_template (PromptTemplateOutput): Output for the Prompt Template node
        qwen_image_denoise (LatentsOutput): Base class for nodes that output a single latents tensor
        qwen_image_i2l (LatentsOutput): Base class for nodes that output a single latents tensor
        qwen_image_l2i (ImageOutput): Base class for nodes that output a single image
        qwen_image_lora_collection_loader (QwenImageLoRALoaderOutput): Qwen Image LoRA Loader Output
        qwen_image_lora_loader (QwenImageLoRALoaderOutput): Qwen Image LoRA Loader Output
        qwen_image_model_loader (QwenImageModelLoaderOutput): Qwen Image model loader output.
        qwen_image_text_encoder (QwenImageConditioningOutput): Base class for nodes that output a Qwen Image Edit
            conditioning tensor.
        rand_float (FloatOutput): Base class for nodes that output a single float
        rand_int (IntegerOutput): Base class for nodes that output a single integer
        random_range (IntegerCollectionOutput): Base class for nodes that output a collection of integers
        range_ (IntegerCollectionOutput): Base class for nodes that output a collection of integers
        range_of_size (IntegerCollectionOutput): Base class for nodes that output a collection of integers
        rectangle_mask (MaskOutput): A torch mask tensor.
        round_float (FloatOutput): Base class for nodes that output a single float
        save_image (ImageOutput): Base class for nodes that output a single image
        save_image_to_file (ImageOutput): Base class for nodes that output a single image
        scheduler (SchedulerOutput):
        sd3_denoise (LatentsOutput): Base class for nodes that output a single latents tensor
        sd3_i2l (LatentsOutput): Base class for nodes that output a single latents tensor
        sd3_l2i (ImageOutput): Base class for nodes that output a single image
        sd3_model_loader (Sd3ModelLoaderOutput): SD3 base model loader output.
        sd3_text_encoder (SD3ConditioningOutput): Base class for nodes that output a single SD3 conditioning tensor
        sdxl_compel_prompt (ConditioningOutput): Base class for nodes that output a single conditioning tensor
        sdxl_lora_collection_loader (SDXLLoRALoaderOutput): SDXL LoRA Loader Output
        sdxl_lora_loader (SDXLLoRALoaderOutput): SDXL LoRA Loader Output
        sdxl_model_loader (SDXLModelLoaderOutput): SDXL base model loader output
        sdxl_refiner_compel_prompt (ConditioningOutput): Base class for nodes that output a single conditioning tensor
        sdxl_refiner_model_loader (SDXLRefinerModelLoaderOutput): SDXL refiner model loader output
        seamless (SeamlessModeOutput): Modified Seamless Model output
        seedream_image_generation (ImageCollectionOutput): Base class for nodes that output a collection of images
        segment_anything (MaskOutput): A torch mask tensor.
        show_image (ImageOutput): Base class for nodes that output a single image
        spandrel_image_to_image (ImageOutput): Base class for nodes that output a single image
        spandrel_image_to_image_autoscale (ImageOutput): Base class for nodes that output a single image
        string (StringOutput): Base class for nodes that output a single string
        string_batch (StringOutput): Base class for nodes that output a single string
        string_collection (StringCollectionOutput): Base class for nodes that output a collection of strings
        string_generator (StringGeneratorOutput): Base class for nodes that output a collection of strings
        string_join (StringOutput): Base class for nodes that output a single string
        string_join_three (StringOutput): Base class for nodes that output a single string
        string_replace (StringOutput): Base class for nodes that output a single string
        string_split (String2Output): Base class for invocations that output two strings
        string_split_neg (StringPosNegOutput): Base class for invocations that output a positive and negative string
        sub (IntegerOutput): Base class for nodes that output a single integer
        t2i_adapter (T2IAdapterOutput):
        tensor_mask_to_image (ImageOutput): Base class for nodes that output a single image
        text_llm (StringOutput): Base class for nodes that output a single string
        tile_to_properties (TileToPropertiesOutput):
        tiled_multi_diffusion_denoise_latents (LatentsOutput): Base class for nodes that output a single latents tensor
        tomask (ImageOutput): Base class for nodes that output a single image
        unsharp_mask (ImageOutput): Base class for nodes that output a single image
        unsharp_mask_oklab (ImageOutput): Base class for nodes that output a single image
        vae_loader (VAEOutput): Base class for invocations that output a VAE field
        z_image_control (ZImageControlOutput): Z-Image Control output containing control configuration.
        z_image_denoise (LatentsOutput): Base class for nodes that output a single latents tensor
        z_image_denoise_meta (LatentsMetaOutput): Latents + metadata
        z_image_i2l (LatentsOutput): Base class for nodes that output a single latents tensor
        z_image_l2i (ImageOutput): Base class for nodes that output a single image
        z_image_lora_collection_loader (ZImageLoRALoaderOutput): Z-Image LoRA Loader Output
        z_image_lora_loader (ZImageLoRALoaderOutput): Z-Image LoRA Loader Output
        z_image_model_loader (ZImageModelLoaderOutput): Z-Image base model loader output.
        z_image_seed_variance_enhancer (ZImageConditioningOutput): Base class for nodes that output a Z-Image text
            conditioning tensor.
        z_image_text_encoder (ZImageConditioningOutput): Base class for nodes that output a Z-Image text conditioning
            tensor.
    """

    add: IntegerOutput
    alibabacloud_image_generation: ImageCollectionOutput
    alpha_mask_to_tensor: MaskOutput
    anima_denoise: LatentsOutput
    anima_i2l: LatentsOutput
    anima_l2i: ImageOutput
    anima_lora_collection_loader: AnimaLoRALoaderOutput
    anima_lora_loader: AnimaLoRALoaderOutput
    anima_model_loader: AnimaModelLoaderOutput
    anima_text_encoder: AnimaConditioningOutput
    apply_mask_to_image: ImageOutput
    apply_tensor_mask_to_image: ImageOutput
    blank_image: ImageOutput
    boolean: BooleanOutput
    boolean_collection: BooleanCollectionOutput
    bounding_box: BoundingBoxOutput
    calculate_image_tiles: CalculateImageTilesOutput
    calculate_image_tiles_even_split: CalculateImageTilesOutput
    calculate_image_tiles_min_overlap: CalculateImageTilesOutput
    canny_edge_detection: ImageOutput
    canvas_output: ImageOutput
    canvas_paste_back: ImageOutput
    canvas_v2_mask_and_crop: ImageOutput
    clip_skip: CLIPSkipInvocationOutput
    cogview4_denoise: LatentsOutput
    cogview4_i2l: LatentsOutput
    cogview4_l2i: ImageOutput
    cogview4_model_loader: CogView4ModelLoaderOutput
    cogview4_text_encoder: CogView4ConditioningOutput
    collect: CollectInvocationOutput
    color: ColorOutput
    color_correct: ImageOutput
    color_map: ImageOutput
    compel: ConditioningOutput
    conditioning: ConditioningOutput
    conditioning_collection: ConditioningCollectionOutput
    content_shuffle: ImageOutput
    controlnet: ControlOutput
    core_metadata: MetadataOutput
    create_denoise_mask: DenoiseMaskOutput
    create_gradient_mask: GradientMaskOutput
    crop_image_to_bounding_box: ImageOutput
    crop_latents: LatentsOutput
    cv_inpaint: ImageOutput
    decode_watermark: StringOutput
    denoise_latents: LatentsOutput
    denoise_latents_meta: LatentsMetaOutput
    depth_anything_depth_estimation: ImageOutput
    div: IntegerOutput
    dw_openpose_detection: ImageOutput
    dynamic_prompt: StringCollectionOutput
    esrgan: ImageOutput
    expand_mask_with_fade: ImageOutput
    face_identifier: ImageOutput
    face_mask_detection: FaceMaskOutput
    face_off: FaceOffOutput
    float_: FloatOutput
    float_batch: FloatOutput
    float_collection: FloatCollectionOutput
    float_generator: FloatGeneratorOutput
    float_math: FloatOutput
    float_range: FloatCollectionOutput
    float_to_int: IntegerOutput
    flux2_denoise: LatentsOutput
    flux2_klein_lora_collection_loader: Flux2KleinLoRALoaderOutput
    flux2_klein_lora_loader: Flux2KleinLoRALoaderOutput
    flux2_klein_model_loader: Flux2KleinModelLoaderOutput
    flux2_klein_text_encoder: FluxConditioningOutput
    flux2_vae_decode: ImageOutput
    flux2_vae_encode: LatentsOutput
    flux_control_lora_loader: FluxControlLoRALoaderOutput
    flux_controlnet: FluxControlNetOutput
    flux_denoise: LatentsOutput
    flux_denoise_meta: LatentsMetaOutput
    flux_fill: FluxFillOutput
    flux_ip_adapter: IPAdapterOutput
    flux_kontext: FluxKontextOutput
    flux_kontext_image_prep: ImageOutput
    flux_lora_collection_loader: FluxLoRALoaderOutput
    flux_lora_loader: FluxLoRALoaderOutput
    flux_model_loader: FluxModelLoaderOutput
    flux_redux: FluxReduxOutput
    flux_text_encoder: FluxConditioningOutput
    flux_vae_decode: ImageOutput
    flux_vae_encode: LatentsOutput
    freeu: UNetOutput
    gemini_image_generation: ImageCollectionOutput
    get_image_mask_bounding_box: BoundingBoxOutput
    grounding_dino: BoundingBoxCollectionOutput
    hed_edge_detection: ImageOutput
    heuristic_resize: ImageOutput
    i2l: LatentsOutput
    ideal_size: IdealSizeOutput
    if_: IfInvocationOutput
    image: ImageOutput
    image_batch: ImageOutput
    image_collection: ImageCollectionOutput
    image_generator: ImageGeneratorOutput
    image_mask_to_tensor: MaskOutput
    image_panel_layout: ImagePanelCoordinateOutput
    img_blur: ImageOutput
    img_chan: ImageOutput
    img_channel_multiply: ImageOutput
    img_channel_offset: ImageOutput
    img_conv: ImageOutput
    img_crop: ImageOutput
    img_hue_adjust: ImageOutput
    img_hue_adjust_oklch: ImageOutput
    img_ilerp: ImageOutput
    img_lerp: ImageOutput
    img_mul: ImageOutput
    img_noise: ImageOutput
    img_nsfw: ImageOutput
    img_pad_crop: ImageOutput
    img_paste: ImageOutput
    img_resize: ImageOutput
    img_scale: ImageOutput
    img_watermark: ImageOutput
    infill_cv2: ImageOutput
    infill_lama: ImageOutput
    infill_patchmatch: ImageOutput
    infill_rgba: ImageOutput
    infill_tile: ImageOutput
    integer: IntegerOutput
    integer_batch: IntegerOutput
    integer_collection: IntegerCollectionOutput
    integer_generator: IntegerGeneratorOutput
    integer_math: IntegerOutput
    invert_tensor_mask: MaskOutput
    invokeai_ealightness: ImageOutput
    invokeai_img_blend: ImageOutput
    invokeai_img_composite: ImageOutput
    invokeai_img_dilate_erode: ImageOutput
    invokeai_img_enhance: ImageOutput
    invokeai_img_hue_adjust_plus: ImageOutput
    invokeai_img_val_thresholds: ImageOutput
    ip_adapter: IPAdapterOutput
    iterate: IterateInvocationOutput
    l2i: ImageOutput
    latents: LatentsOutput
    latents_collection: LatentsCollectionOutput
    lblend: LatentsOutput
    lineart_anime_edge_detection: ImageOutput
    lineart_edge_detection: ImageOutput
    llava_onevision_vllm: StringOutput
    lora_collection_loader: LoRALoaderOutput
    lora_loader: LoRALoaderOutput
    lora_selector: LoRASelectorOutput
    lresize: LatentsOutput
    lscale: LatentsOutput
    main_model_loader: ModelLoaderOutput
    mask_combine: ImageOutput
    mask_edge: ImageOutput
    mask_from_id: ImageOutput
    mediapipe_face_detection: ImageOutput
    merge_metadata: MetadataOutput
    merge_tiles_to_image: ImageOutput
    metadata: MetadataOutput
    metadata_field_extractor: StringOutput
    metadata_from_image: MetadataOutput
    metadata_item: MetadataItemOutput
    metadata_item_linked: MetadataOutput
    metadata_to_bool: BooleanOutput
    metadata_to_bool_collection: BooleanCollectionOutput
    metadata_to_controlnets: MDControlListOutput
    metadata_to_float: FloatOutput
    metadata_to_float_collection: FloatCollectionOutput
    metadata_to_integer: IntegerOutput
    metadata_to_integer_collection: IntegerCollectionOutput
    metadata_to_ip_adapters: MDIPAdapterListOutput
    metadata_to_lora_collection: MetadataToLorasCollectionOutput
    metadata_to_loras: LoRALoaderOutput
    metadata_to_model: MetadataToModelOutput
    metadata_to_scheduler: SchedulerOutput
    metadata_to_sdlx_loras: SDXLLoRALoaderOutput
    metadata_to_sdxl_model: MetadataToSDXLModelOutput
    metadata_to_string: StringOutput
    metadata_to_string_collection: StringCollectionOutput
    metadata_to_t2i_adapters: MDT2IAdapterListOutput
    metadata_to_vae: VAEOutput
    mlsd_detection: ImageOutput
    model_identifier: ModelIdentifierOutput
    mul: IntegerOutput
    noise: NoiseOutput
    normal_map: ImageOutput
    openai_image_generation: ImageCollectionOutput
    pair_tile_image: PairTileImageOutput
    paste_image_into_bounding_box: ImageOutput
    pbr_maps: PBRMapsOutput
    pidi_edge_detection: ImageOutput
    prompt_from_file: StringCollectionOutput
    prompt_template: PromptTemplateOutput
    qwen_image_denoise: LatentsOutput
    qwen_image_i2l: LatentsOutput
    qwen_image_l2i: ImageOutput
    qwen_image_lora_collection_loader: QwenImageLoRALoaderOutput
    qwen_image_lora_loader: QwenImageLoRALoaderOutput
    qwen_image_model_loader: QwenImageModelLoaderOutput
    qwen_image_text_encoder: QwenImageConditioningOutput
    rand_float: FloatOutput
    rand_int: IntegerOutput
    random_range: IntegerCollectionOutput
    range_: IntegerCollectionOutput
    range_of_size: IntegerCollectionOutput
    rectangle_mask: MaskOutput
    round_float: FloatOutput
    save_image: ImageOutput
    save_image_to_file: ImageOutput
    scheduler: SchedulerOutput
    sd3_denoise: LatentsOutput
    sd3_i2l: LatentsOutput
    sd3_l2i: ImageOutput
    sd3_model_loader: Sd3ModelLoaderOutput
    sd3_text_encoder: SD3ConditioningOutput
    sdxl_compel_prompt: ConditioningOutput
    sdxl_lora_collection_loader: SDXLLoRALoaderOutput
    sdxl_lora_loader: SDXLLoRALoaderOutput
    sdxl_model_loader: SDXLModelLoaderOutput
    sdxl_refiner_compel_prompt: ConditioningOutput
    sdxl_refiner_model_loader: SDXLRefinerModelLoaderOutput
    seamless: SeamlessModeOutput
    seedream_image_generation: ImageCollectionOutput
    segment_anything: MaskOutput
    show_image: ImageOutput
    spandrel_image_to_image: ImageOutput
    spandrel_image_to_image_autoscale: ImageOutput
    string: StringOutput
    string_batch: StringOutput
    string_collection: StringCollectionOutput
    string_generator: StringGeneratorOutput
    string_join: StringOutput
    string_join_three: StringOutput
    string_replace: StringOutput
    string_split: String2Output
    string_split_neg: StringPosNegOutput
    sub: IntegerOutput
    t2i_adapter: T2IAdapterOutput
    tensor_mask_to_image: ImageOutput
    text_llm: StringOutput
    tile_to_properties: TileToPropertiesOutput
    tiled_multi_diffusion_denoise_latents: LatentsOutput
    tomask: ImageOutput
    unsharp_mask: ImageOutput
    unsharp_mask_oklab: ImageOutput
    vae_loader: VAEOutput
    z_image_control: ZImageControlOutput
    z_image_denoise: LatentsOutput
    z_image_denoise_meta: LatentsMetaOutput
    z_image_i2l: LatentsOutput
    z_image_l2i: ImageOutput
    z_image_lora_collection_loader: ZImageLoRALoaderOutput
    z_image_lora_loader: ZImageLoRALoaderOutput
    z_image_model_loader: ZImageModelLoaderOutput
    z_image_seed_variance_enhancer: ZImageConditioningOutput
    z_image_text_encoder: ZImageConditioningOutput
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add = self.add.to_dict()

        alibabacloud_image_generation = self.alibabacloud_image_generation.to_dict()

        alpha_mask_to_tensor = self.alpha_mask_to_tensor.to_dict()

        anima_denoise = self.anima_denoise.to_dict()

        anima_i2l = self.anima_i2l.to_dict()

        anima_l2i = self.anima_l2i.to_dict()

        anima_lora_collection_loader = self.anima_lora_collection_loader.to_dict()

        anima_lora_loader = self.anima_lora_loader.to_dict()

        anima_model_loader = self.anima_model_loader.to_dict()

        anima_text_encoder = self.anima_text_encoder.to_dict()

        apply_mask_to_image = self.apply_mask_to_image.to_dict()

        apply_tensor_mask_to_image = self.apply_tensor_mask_to_image.to_dict()

        blank_image = self.blank_image.to_dict()

        boolean = self.boolean.to_dict()

        boolean_collection = self.boolean_collection.to_dict()

        bounding_box = self.bounding_box.to_dict()

        calculate_image_tiles = self.calculate_image_tiles.to_dict()

        calculate_image_tiles_even_split = self.calculate_image_tiles_even_split.to_dict()

        calculate_image_tiles_min_overlap = self.calculate_image_tiles_min_overlap.to_dict()

        canny_edge_detection = self.canny_edge_detection.to_dict()

        canvas_output = self.canvas_output.to_dict()

        canvas_paste_back = self.canvas_paste_back.to_dict()

        canvas_v2_mask_and_crop = self.canvas_v2_mask_and_crop.to_dict()

        clip_skip = self.clip_skip.to_dict()

        cogview4_denoise = self.cogview4_denoise.to_dict()

        cogview4_i2l = self.cogview4_i2l.to_dict()

        cogview4_l2i = self.cogview4_l2i.to_dict()

        cogview4_model_loader = self.cogview4_model_loader.to_dict()

        cogview4_text_encoder = self.cogview4_text_encoder.to_dict()

        collect = self.collect.to_dict()

        color = self.color.to_dict()

        color_correct = self.color_correct.to_dict()

        color_map = self.color_map.to_dict()

        compel = self.compel.to_dict()

        conditioning = self.conditioning.to_dict()

        conditioning_collection = self.conditioning_collection.to_dict()

        content_shuffle = self.content_shuffle.to_dict()

        controlnet = self.controlnet.to_dict()

        core_metadata = self.core_metadata.to_dict()

        create_denoise_mask = self.create_denoise_mask.to_dict()

        create_gradient_mask = self.create_gradient_mask.to_dict()

        crop_image_to_bounding_box = self.crop_image_to_bounding_box.to_dict()

        crop_latents = self.crop_latents.to_dict()

        cv_inpaint = self.cv_inpaint.to_dict()

        decode_watermark = self.decode_watermark.to_dict()

        denoise_latents = self.denoise_latents.to_dict()

        denoise_latents_meta = self.denoise_latents_meta.to_dict()

        depth_anything_depth_estimation = self.depth_anything_depth_estimation.to_dict()

        div = self.div.to_dict()

        dw_openpose_detection = self.dw_openpose_detection.to_dict()

        dynamic_prompt = self.dynamic_prompt.to_dict()

        esrgan = self.esrgan.to_dict()

        expand_mask_with_fade = self.expand_mask_with_fade.to_dict()

        face_identifier = self.face_identifier.to_dict()

        face_mask_detection = self.face_mask_detection.to_dict()

        face_off = self.face_off.to_dict()

        float_ = self.float_.to_dict()

        float_batch = self.float_batch.to_dict()

        float_collection = self.float_collection.to_dict()

        float_generator = self.float_generator.to_dict()

        float_math = self.float_math.to_dict()

        float_range = self.float_range.to_dict()

        float_to_int = self.float_to_int.to_dict()

        flux2_denoise = self.flux2_denoise.to_dict()

        flux2_klein_lora_collection_loader = self.flux2_klein_lora_collection_loader.to_dict()

        flux2_klein_lora_loader = self.flux2_klein_lora_loader.to_dict()

        flux2_klein_model_loader = self.flux2_klein_model_loader.to_dict()

        flux2_klein_text_encoder = self.flux2_klein_text_encoder.to_dict()

        flux2_vae_decode = self.flux2_vae_decode.to_dict()

        flux2_vae_encode = self.flux2_vae_encode.to_dict()

        flux_control_lora_loader = self.flux_control_lora_loader.to_dict()

        flux_controlnet = self.flux_controlnet.to_dict()

        flux_denoise = self.flux_denoise.to_dict()

        flux_denoise_meta = self.flux_denoise_meta.to_dict()

        flux_fill = self.flux_fill.to_dict()

        flux_ip_adapter = self.flux_ip_adapter.to_dict()

        flux_kontext = self.flux_kontext.to_dict()

        flux_kontext_image_prep = self.flux_kontext_image_prep.to_dict()

        flux_lora_collection_loader = self.flux_lora_collection_loader.to_dict()

        flux_lora_loader = self.flux_lora_loader.to_dict()

        flux_model_loader = self.flux_model_loader.to_dict()

        flux_redux = self.flux_redux.to_dict()

        flux_text_encoder = self.flux_text_encoder.to_dict()

        flux_vae_decode = self.flux_vae_decode.to_dict()

        flux_vae_encode = self.flux_vae_encode.to_dict()

        freeu = self.freeu.to_dict()

        gemini_image_generation = self.gemini_image_generation.to_dict()

        get_image_mask_bounding_box = self.get_image_mask_bounding_box.to_dict()

        grounding_dino = self.grounding_dino.to_dict()

        hed_edge_detection = self.hed_edge_detection.to_dict()

        heuristic_resize = self.heuristic_resize.to_dict()

        i2l = self.i2l.to_dict()

        ideal_size = self.ideal_size.to_dict()

        if_ = self.if_.to_dict()

        image = self.image.to_dict()

        image_batch = self.image_batch.to_dict()

        image_collection = self.image_collection.to_dict()

        image_generator = self.image_generator.to_dict()

        image_mask_to_tensor = self.image_mask_to_tensor.to_dict()

        image_panel_layout = self.image_panel_layout.to_dict()

        img_blur = self.img_blur.to_dict()

        img_chan = self.img_chan.to_dict()

        img_channel_multiply = self.img_channel_multiply.to_dict()

        img_channel_offset = self.img_channel_offset.to_dict()

        img_conv = self.img_conv.to_dict()

        img_crop = self.img_crop.to_dict()

        img_hue_adjust = self.img_hue_adjust.to_dict()

        img_hue_adjust_oklch = self.img_hue_adjust_oklch.to_dict()

        img_ilerp = self.img_ilerp.to_dict()

        img_lerp = self.img_lerp.to_dict()

        img_mul = self.img_mul.to_dict()

        img_noise = self.img_noise.to_dict()

        img_nsfw = self.img_nsfw.to_dict()

        img_pad_crop = self.img_pad_crop.to_dict()

        img_paste = self.img_paste.to_dict()

        img_resize = self.img_resize.to_dict()

        img_scale = self.img_scale.to_dict()

        img_watermark = self.img_watermark.to_dict()

        infill_cv2 = self.infill_cv2.to_dict()

        infill_lama = self.infill_lama.to_dict()

        infill_patchmatch = self.infill_patchmatch.to_dict()

        infill_rgba = self.infill_rgba.to_dict()

        infill_tile = self.infill_tile.to_dict()

        integer = self.integer.to_dict()

        integer_batch = self.integer_batch.to_dict()

        integer_collection = self.integer_collection.to_dict()

        integer_generator = self.integer_generator.to_dict()

        integer_math = self.integer_math.to_dict()

        invert_tensor_mask = self.invert_tensor_mask.to_dict()

        invokeai_ealightness = self.invokeai_ealightness.to_dict()

        invokeai_img_blend = self.invokeai_img_blend.to_dict()

        invokeai_img_composite = self.invokeai_img_composite.to_dict()

        invokeai_img_dilate_erode = self.invokeai_img_dilate_erode.to_dict()

        invokeai_img_enhance = self.invokeai_img_enhance.to_dict()

        invokeai_img_hue_adjust_plus = self.invokeai_img_hue_adjust_plus.to_dict()

        invokeai_img_val_thresholds = self.invokeai_img_val_thresholds.to_dict()

        ip_adapter = self.ip_adapter.to_dict()

        iterate = self.iterate.to_dict()

        l2i = self.l2i.to_dict()

        latents = self.latents.to_dict()

        latents_collection = self.latents_collection.to_dict()

        lblend = self.lblend.to_dict()

        lineart_anime_edge_detection = self.lineart_anime_edge_detection.to_dict()

        lineart_edge_detection = self.lineart_edge_detection.to_dict()

        llava_onevision_vllm = self.llava_onevision_vllm.to_dict()

        lora_collection_loader = self.lora_collection_loader.to_dict()

        lora_loader = self.lora_loader.to_dict()

        lora_selector = self.lora_selector.to_dict()

        lresize = self.lresize.to_dict()

        lscale = self.lscale.to_dict()

        main_model_loader = self.main_model_loader.to_dict()

        mask_combine = self.mask_combine.to_dict()

        mask_edge = self.mask_edge.to_dict()

        mask_from_id = self.mask_from_id.to_dict()

        mediapipe_face_detection = self.mediapipe_face_detection.to_dict()

        merge_metadata = self.merge_metadata.to_dict()

        merge_tiles_to_image = self.merge_tiles_to_image.to_dict()

        metadata = self.metadata.to_dict()

        metadata_field_extractor = self.metadata_field_extractor.to_dict()

        metadata_from_image = self.metadata_from_image.to_dict()

        metadata_item = self.metadata_item.to_dict()

        metadata_item_linked = self.metadata_item_linked.to_dict()

        metadata_to_bool = self.metadata_to_bool.to_dict()

        metadata_to_bool_collection = self.metadata_to_bool_collection.to_dict()

        metadata_to_controlnets = self.metadata_to_controlnets.to_dict()

        metadata_to_float = self.metadata_to_float.to_dict()

        metadata_to_float_collection = self.metadata_to_float_collection.to_dict()

        metadata_to_integer = self.metadata_to_integer.to_dict()

        metadata_to_integer_collection = self.metadata_to_integer_collection.to_dict()

        metadata_to_ip_adapters = self.metadata_to_ip_adapters.to_dict()

        metadata_to_lora_collection = self.metadata_to_lora_collection.to_dict()

        metadata_to_loras = self.metadata_to_loras.to_dict()

        metadata_to_model = self.metadata_to_model.to_dict()

        metadata_to_scheduler = self.metadata_to_scheduler.to_dict()

        metadata_to_sdlx_loras = self.metadata_to_sdlx_loras.to_dict()

        metadata_to_sdxl_model = self.metadata_to_sdxl_model.to_dict()

        metadata_to_string = self.metadata_to_string.to_dict()

        metadata_to_string_collection = self.metadata_to_string_collection.to_dict()

        metadata_to_t2i_adapters = self.metadata_to_t2i_adapters.to_dict()

        metadata_to_vae = self.metadata_to_vae.to_dict()

        mlsd_detection = self.mlsd_detection.to_dict()

        model_identifier = self.model_identifier.to_dict()

        mul = self.mul.to_dict()

        noise = self.noise.to_dict()

        normal_map = self.normal_map.to_dict()

        openai_image_generation = self.openai_image_generation.to_dict()

        pair_tile_image = self.pair_tile_image.to_dict()

        paste_image_into_bounding_box = self.paste_image_into_bounding_box.to_dict()

        pbr_maps = self.pbr_maps.to_dict()

        pidi_edge_detection = self.pidi_edge_detection.to_dict()

        prompt_from_file = self.prompt_from_file.to_dict()

        prompt_template = self.prompt_template.to_dict()

        qwen_image_denoise = self.qwen_image_denoise.to_dict()

        qwen_image_i2l = self.qwen_image_i2l.to_dict()

        qwen_image_l2i = self.qwen_image_l2i.to_dict()

        qwen_image_lora_collection_loader = self.qwen_image_lora_collection_loader.to_dict()

        qwen_image_lora_loader = self.qwen_image_lora_loader.to_dict()

        qwen_image_model_loader = self.qwen_image_model_loader.to_dict()

        qwen_image_text_encoder = self.qwen_image_text_encoder.to_dict()

        rand_float = self.rand_float.to_dict()

        rand_int = self.rand_int.to_dict()

        random_range = self.random_range.to_dict()

        range_ = self.range_.to_dict()

        range_of_size = self.range_of_size.to_dict()

        rectangle_mask = self.rectangle_mask.to_dict()

        round_float = self.round_float.to_dict()

        save_image = self.save_image.to_dict()

        save_image_to_file = self.save_image_to_file.to_dict()

        scheduler = self.scheduler.to_dict()

        sd3_denoise = self.sd3_denoise.to_dict()

        sd3_i2l = self.sd3_i2l.to_dict()

        sd3_l2i = self.sd3_l2i.to_dict()

        sd3_model_loader = self.sd3_model_loader.to_dict()

        sd3_text_encoder = self.sd3_text_encoder.to_dict()

        sdxl_compel_prompt = self.sdxl_compel_prompt.to_dict()

        sdxl_lora_collection_loader = self.sdxl_lora_collection_loader.to_dict()

        sdxl_lora_loader = self.sdxl_lora_loader.to_dict()

        sdxl_model_loader = self.sdxl_model_loader.to_dict()

        sdxl_refiner_compel_prompt = self.sdxl_refiner_compel_prompt.to_dict()

        sdxl_refiner_model_loader = self.sdxl_refiner_model_loader.to_dict()

        seamless = self.seamless.to_dict()

        seedream_image_generation = self.seedream_image_generation.to_dict()

        segment_anything = self.segment_anything.to_dict()

        show_image = self.show_image.to_dict()

        spandrel_image_to_image = self.spandrel_image_to_image.to_dict()

        spandrel_image_to_image_autoscale = self.spandrel_image_to_image_autoscale.to_dict()

        string = self.string.to_dict()

        string_batch = self.string_batch.to_dict()

        string_collection = self.string_collection.to_dict()

        string_generator = self.string_generator.to_dict()

        string_join = self.string_join.to_dict()

        string_join_three = self.string_join_three.to_dict()

        string_replace = self.string_replace.to_dict()

        string_split = self.string_split.to_dict()

        string_split_neg = self.string_split_neg.to_dict()

        sub = self.sub.to_dict()

        t2i_adapter = self.t2i_adapter.to_dict()

        tensor_mask_to_image = self.tensor_mask_to_image.to_dict()

        text_llm = self.text_llm.to_dict()

        tile_to_properties = self.tile_to_properties.to_dict()

        tiled_multi_diffusion_denoise_latents = self.tiled_multi_diffusion_denoise_latents.to_dict()

        tomask = self.tomask.to_dict()

        unsharp_mask = self.unsharp_mask.to_dict()

        unsharp_mask_oklab = self.unsharp_mask_oklab.to_dict()

        vae_loader = self.vae_loader.to_dict()

        z_image_control = self.z_image_control.to_dict()

        z_image_denoise = self.z_image_denoise.to_dict()

        z_image_denoise_meta = self.z_image_denoise_meta.to_dict()

        z_image_i2l = self.z_image_i2l.to_dict()

        z_image_l2i = self.z_image_l2i.to_dict()

        z_image_lora_collection_loader = self.z_image_lora_collection_loader.to_dict()

        z_image_lora_loader = self.z_image_lora_loader.to_dict()

        z_image_model_loader = self.z_image_model_loader.to_dict()

        z_image_seed_variance_enhancer = self.z_image_seed_variance_enhancer.to_dict()

        z_image_text_encoder = self.z_image_text_encoder.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "add": add,
                "alibabacloud_image_generation": alibabacloud_image_generation,
                "alpha_mask_to_tensor": alpha_mask_to_tensor,
                "anima_denoise": anima_denoise,
                "anima_i2l": anima_i2l,
                "anima_l2i": anima_l2i,
                "anima_lora_collection_loader": anima_lora_collection_loader,
                "anima_lora_loader": anima_lora_loader,
                "anima_model_loader": anima_model_loader,
                "anima_text_encoder": anima_text_encoder,
                "apply_mask_to_image": apply_mask_to_image,
                "apply_tensor_mask_to_image": apply_tensor_mask_to_image,
                "blank_image": blank_image,
                "boolean": boolean,
                "boolean_collection": boolean_collection,
                "bounding_box": bounding_box,
                "calculate_image_tiles": calculate_image_tiles,
                "calculate_image_tiles_even_split": calculate_image_tiles_even_split,
                "calculate_image_tiles_min_overlap": calculate_image_tiles_min_overlap,
                "canny_edge_detection": canny_edge_detection,
                "canvas_output": canvas_output,
                "canvas_paste_back": canvas_paste_back,
                "canvas_v2_mask_and_crop": canvas_v2_mask_and_crop,
                "clip_skip": clip_skip,
                "cogview4_denoise": cogview4_denoise,
                "cogview4_i2l": cogview4_i2l,
                "cogview4_l2i": cogview4_l2i,
                "cogview4_model_loader": cogview4_model_loader,
                "cogview4_text_encoder": cogview4_text_encoder,
                "collect": collect,
                "color": color,
                "color_correct": color_correct,
                "color_map": color_map,
                "compel": compel,
                "conditioning": conditioning,
                "conditioning_collection": conditioning_collection,
                "content_shuffle": content_shuffle,
                "controlnet": controlnet,
                "core_metadata": core_metadata,
                "create_denoise_mask": create_denoise_mask,
                "create_gradient_mask": create_gradient_mask,
                "crop_image_to_bounding_box": crop_image_to_bounding_box,
                "crop_latents": crop_latents,
                "cv_inpaint": cv_inpaint,
                "decode_watermark": decode_watermark,
                "denoise_latents": denoise_latents,
                "denoise_latents_meta": denoise_latents_meta,
                "depth_anything_depth_estimation": depth_anything_depth_estimation,
                "div": div,
                "dw_openpose_detection": dw_openpose_detection,
                "dynamic_prompt": dynamic_prompt,
                "esrgan": esrgan,
                "expand_mask_with_fade": expand_mask_with_fade,
                "face_identifier": face_identifier,
                "face_mask_detection": face_mask_detection,
                "face_off": face_off,
                "float": float_,
                "float_batch": float_batch,
                "float_collection": float_collection,
                "float_generator": float_generator,
                "float_math": float_math,
                "float_range": float_range,
                "float_to_int": float_to_int,
                "flux2_denoise": flux2_denoise,
                "flux2_klein_lora_collection_loader": flux2_klein_lora_collection_loader,
                "flux2_klein_lora_loader": flux2_klein_lora_loader,
                "flux2_klein_model_loader": flux2_klein_model_loader,
                "flux2_klein_text_encoder": flux2_klein_text_encoder,
                "flux2_vae_decode": flux2_vae_decode,
                "flux2_vae_encode": flux2_vae_encode,
                "flux_control_lora_loader": flux_control_lora_loader,
                "flux_controlnet": flux_controlnet,
                "flux_denoise": flux_denoise,
                "flux_denoise_meta": flux_denoise_meta,
                "flux_fill": flux_fill,
                "flux_ip_adapter": flux_ip_adapter,
                "flux_kontext": flux_kontext,
                "flux_kontext_image_prep": flux_kontext_image_prep,
                "flux_lora_collection_loader": flux_lora_collection_loader,
                "flux_lora_loader": flux_lora_loader,
                "flux_model_loader": flux_model_loader,
                "flux_redux": flux_redux,
                "flux_text_encoder": flux_text_encoder,
                "flux_vae_decode": flux_vae_decode,
                "flux_vae_encode": flux_vae_encode,
                "freeu": freeu,
                "gemini_image_generation": gemini_image_generation,
                "get_image_mask_bounding_box": get_image_mask_bounding_box,
                "grounding_dino": grounding_dino,
                "hed_edge_detection": hed_edge_detection,
                "heuristic_resize": heuristic_resize,
                "i2l": i2l,
                "ideal_size": ideal_size,
                "if": if_,
                "image": image,
                "image_batch": image_batch,
                "image_collection": image_collection,
                "image_generator": image_generator,
                "image_mask_to_tensor": image_mask_to_tensor,
                "image_panel_layout": image_panel_layout,
                "img_blur": img_blur,
                "img_chan": img_chan,
                "img_channel_multiply": img_channel_multiply,
                "img_channel_offset": img_channel_offset,
                "img_conv": img_conv,
                "img_crop": img_crop,
                "img_hue_adjust": img_hue_adjust,
                "img_hue_adjust_oklch": img_hue_adjust_oklch,
                "img_ilerp": img_ilerp,
                "img_lerp": img_lerp,
                "img_mul": img_mul,
                "img_noise": img_noise,
                "img_nsfw": img_nsfw,
                "img_pad_crop": img_pad_crop,
                "img_paste": img_paste,
                "img_resize": img_resize,
                "img_scale": img_scale,
                "img_watermark": img_watermark,
                "infill_cv2": infill_cv2,
                "infill_lama": infill_lama,
                "infill_patchmatch": infill_patchmatch,
                "infill_rgba": infill_rgba,
                "infill_tile": infill_tile,
                "integer": integer,
                "integer_batch": integer_batch,
                "integer_collection": integer_collection,
                "integer_generator": integer_generator,
                "integer_math": integer_math,
                "invert_tensor_mask": invert_tensor_mask,
                "invokeai_ealightness": invokeai_ealightness,
                "invokeai_img_blend": invokeai_img_blend,
                "invokeai_img_composite": invokeai_img_composite,
                "invokeai_img_dilate_erode": invokeai_img_dilate_erode,
                "invokeai_img_enhance": invokeai_img_enhance,
                "invokeai_img_hue_adjust_plus": invokeai_img_hue_adjust_plus,
                "invokeai_img_val_thresholds": invokeai_img_val_thresholds,
                "ip_adapter": ip_adapter,
                "iterate": iterate,
                "l2i": l2i,
                "latents": latents,
                "latents_collection": latents_collection,
                "lblend": lblend,
                "lineart_anime_edge_detection": lineart_anime_edge_detection,
                "lineart_edge_detection": lineart_edge_detection,
                "llava_onevision_vllm": llava_onevision_vllm,
                "lora_collection_loader": lora_collection_loader,
                "lora_loader": lora_loader,
                "lora_selector": lora_selector,
                "lresize": lresize,
                "lscale": lscale,
                "main_model_loader": main_model_loader,
                "mask_combine": mask_combine,
                "mask_edge": mask_edge,
                "mask_from_id": mask_from_id,
                "mediapipe_face_detection": mediapipe_face_detection,
                "merge_metadata": merge_metadata,
                "merge_tiles_to_image": merge_tiles_to_image,
                "metadata": metadata,
                "metadata_field_extractor": metadata_field_extractor,
                "metadata_from_image": metadata_from_image,
                "metadata_item": metadata_item,
                "metadata_item_linked": metadata_item_linked,
                "metadata_to_bool": metadata_to_bool,
                "metadata_to_bool_collection": metadata_to_bool_collection,
                "metadata_to_controlnets": metadata_to_controlnets,
                "metadata_to_float": metadata_to_float,
                "metadata_to_float_collection": metadata_to_float_collection,
                "metadata_to_integer": metadata_to_integer,
                "metadata_to_integer_collection": metadata_to_integer_collection,
                "metadata_to_ip_adapters": metadata_to_ip_adapters,
                "metadata_to_lora_collection": metadata_to_lora_collection,
                "metadata_to_loras": metadata_to_loras,
                "metadata_to_model": metadata_to_model,
                "metadata_to_scheduler": metadata_to_scheduler,
                "metadata_to_sdlx_loras": metadata_to_sdlx_loras,
                "metadata_to_sdxl_model": metadata_to_sdxl_model,
                "metadata_to_string": metadata_to_string,
                "metadata_to_string_collection": metadata_to_string_collection,
                "metadata_to_t2i_adapters": metadata_to_t2i_adapters,
                "metadata_to_vae": metadata_to_vae,
                "mlsd_detection": mlsd_detection,
                "model_identifier": model_identifier,
                "mul": mul,
                "noise": noise,
                "normal_map": normal_map,
                "openai_image_generation": openai_image_generation,
                "pair_tile_image": pair_tile_image,
                "paste_image_into_bounding_box": paste_image_into_bounding_box,
                "pbr_maps": pbr_maps,
                "pidi_edge_detection": pidi_edge_detection,
                "prompt_from_file": prompt_from_file,
                "prompt_template": prompt_template,
                "qwen_image_denoise": qwen_image_denoise,
                "qwen_image_i2l": qwen_image_i2l,
                "qwen_image_l2i": qwen_image_l2i,
                "qwen_image_lora_collection_loader": qwen_image_lora_collection_loader,
                "qwen_image_lora_loader": qwen_image_lora_loader,
                "qwen_image_model_loader": qwen_image_model_loader,
                "qwen_image_text_encoder": qwen_image_text_encoder,
                "rand_float": rand_float,
                "rand_int": rand_int,
                "random_range": random_range,
                "range": range_,
                "range_of_size": range_of_size,
                "rectangle_mask": rectangle_mask,
                "round_float": round_float,
                "save_image": save_image,
                "save_image_to_file": save_image_to_file,
                "scheduler": scheduler,
                "sd3_denoise": sd3_denoise,
                "sd3_i2l": sd3_i2l,
                "sd3_l2i": sd3_l2i,
                "sd3_model_loader": sd3_model_loader,
                "sd3_text_encoder": sd3_text_encoder,
                "sdxl_compel_prompt": sdxl_compel_prompt,
                "sdxl_lora_collection_loader": sdxl_lora_collection_loader,
                "sdxl_lora_loader": sdxl_lora_loader,
                "sdxl_model_loader": sdxl_model_loader,
                "sdxl_refiner_compel_prompt": sdxl_refiner_compel_prompt,
                "sdxl_refiner_model_loader": sdxl_refiner_model_loader,
                "seamless": seamless,
                "seedream_image_generation": seedream_image_generation,
                "segment_anything": segment_anything,
                "show_image": show_image,
                "spandrel_image_to_image": spandrel_image_to_image,
                "spandrel_image_to_image_autoscale": spandrel_image_to_image_autoscale,
                "string": string,
                "string_batch": string_batch,
                "string_collection": string_collection,
                "string_generator": string_generator,
                "string_join": string_join,
                "string_join_three": string_join_three,
                "string_replace": string_replace,
                "string_split": string_split,
                "string_split_neg": string_split_neg,
                "sub": sub,
                "t2i_adapter": t2i_adapter,
                "tensor_mask_to_image": tensor_mask_to_image,
                "text_llm": text_llm,
                "tile_to_properties": tile_to_properties,
                "tiled_multi_diffusion_denoise_latents": tiled_multi_diffusion_denoise_latents,
                "tomask": tomask,
                "unsharp_mask": unsharp_mask,
                "unsharp_mask_oklab": unsharp_mask_oklab,
                "vae_loader": vae_loader,
                "z_image_control": z_image_control,
                "z_image_denoise": z_image_denoise,
                "z_image_denoise_meta": z_image_denoise_meta,
                "z_image_i2l": z_image_i2l,
                "z_image_l2i": z_image_l2i,
                "z_image_lora_collection_loader": z_image_lora_collection_loader,
                "z_image_lora_loader": z_image_lora_loader,
                "z_image_model_loader": z_image_model_loader,
                "z_image_seed_variance_enhancer": z_image_seed_variance_enhancer,
                "z_image_text_encoder": z_image_text_encoder,
            }
        )

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
        from ..models.clip_skip_invocation_output import CLIPSkipInvocationOutput
        from ..models.cog_view_4_conditioning_output import CogView4ConditioningOutput
        from ..models.cog_view_4_model_loader_output import CogView4ModelLoaderOutput
        from ..models.collect_invocation_output import CollectInvocationOutput
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
        add = IntegerOutput.from_dict(d.pop("add"))

        alibabacloud_image_generation = ImageCollectionOutput.from_dict(d.pop("alibabacloud_image_generation"))

        alpha_mask_to_tensor = MaskOutput.from_dict(d.pop("alpha_mask_to_tensor"))

        anima_denoise = LatentsOutput.from_dict(d.pop("anima_denoise"))

        anima_i2l = LatentsOutput.from_dict(d.pop("anima_i2l"))

        anima_l2i = ImageOutput.from_dict(d.pop("anima_l2i"))

        anima_lora_collection_loader = AnimaLoRALoaderOutput.from_dict(d.pop("anima_lora_collection_loader"))

        anima_lora_loader = AnimaLoRALoaderOutput.from_dict(d.pop("anima_lora_loader"))

        anima_model_loader = AnimaModelLoaderOutput.from_dict(d.pop("anima_model_loader"))

        anima_text_encoder = AnimaConditioningOutput.from_dict(d.pop("anima_text_encoder"))

        apply_mask_to_image = ImageOutput.from_dict(d.pop("apply_mask_to_image"))

        apply_tensor_mask_to_image = ImageOutput.from_dict(d.pop("apply_tensor_mask_to_image"))

        blank_image = ImageOutput.from_dict(d.pop("blank_image"))

        boolean = BooleanOutput.from_dict(d.pop("boolean"))

        boolean_collection = BooleanCollectionOutput.from_dict(d.pop("boolean_collection"))

        bounding_box = BoundingBoxOutput.from_dict(d.pop("bounding_box"))

        calculate_image_tiles = CalculateImageTilesOutput.from_dict(d.pop("calculate_image_tiles"))

        calculate_image_tiles_even_split = CalculateImageTilesOutput.from_dict(
            d.pop("calculate_image_tiles_even_split")
        )

        calculate_image_tiles_min_overlap = CalculateImageTilesOutput.from_dict(
            d.pop("calculate_image_tiles_min_overlap")
        )

        canny_edge_detection = ImageOutput.from_dict(d.pop("canny_edge_detection"))

        canvas_output = ImageOutput.from_dict(d.pop("canvas_output"))

        canvas_paste_back = ImageOutput.from_dict(d.pop("canvas_paste_back"))

        canvas_v2_mask_and_crop = ImageOutput.from_dict(d.pop("canvas_v2_mask_and_crop"))

        clip_skip = CLIPSkipInvocationOutput.from_dict(d.pop("clip_skip"))

        cogview4_denoise = LatentsOutput.from_dict(d.pop("cogview4_denoise"))

        cogview4_i2l = LatentsOutput.from_dict(d.pop("cogview4_i2l"))

        cogview4_l2i = ImageOutput.from_dict(d.pop("cogview4_l2i"))

        cogview4_model_loader = CogView4ModelLoaderOutput.from_dict(d.pop("cogview4_model_loader"))

        cogview4_text_encoder = CogView4ConditioningOutput.from_dict(d.pop("cogview4_text_encoder"))

        collect = CollectInvocationOutput.from_dict(d.pop("collect"))

        color = ColorOutput.from_dict(d.pop("color"))

        color_correct = ImageOutput.from_dict(d.pop("color_correct"))

        color_map = ImageOutput.from_dict(d.pop("color_map"))

        compel = ConditioningOutput.from_dict(d.pop("compel"))

        conditioning = ConditioningOutput.from_dict(d.pop("conditioning"))

        conditioning_collection = ConditioningCollectionOutput.from_dict(d.pop("conditioning_collection"))

        content_shuffle = ImageOutput.from_dict(d.pop("content_shuffle"))

        controlnet = ControlOutput.from_dict(d.pop("controlnet"))

        core_metadata = MetadataOutput.from_dict(d.pop("core_metadata"))

        create_denoise_mask = DenoiseMaskOutput.from_dict(d.pop("create_denoise_mask"))

        create_gradient_mask = GradientMaskOutput.from_dict(d.pop("create_gradient_mask"))

        crop_image_to_bounding_box = ImageOutput.from_dict(d.pop("crop_image_to_bounding_box"))

        crop_latents = LatentsOutput.from_dict(d.pop("crop_latents"))

        cv_inpaint = ImageOutput.from_dict(d.pop("cv_inpaint"))

        decode_watermark = StringOutput.from_dict(d.pop("decode_watermark"))

        denoise_latents = LatentsOutput.from_dict(d.pop("denoise_latents"))

        denoise_latents_meta = LatentsMetaOutput.from_dict(d.pop("denoise_latents_meta"))

        depth_anything_depth_estimation = ImageOutput.from_dict(d.pop("depth_anything_depth_estimation"))

        div = IntegerOutput.from_dict(d.pop("div"))

        dw_openpose_detection = ImageOutput.from_dict(d.pop("dw_openpose_detection"))

        dynamic_prompt = StringCollectionOutput.from_dict(d.pop("dynamic_prompt"))

        esrgan = ImageOutput.from_dict(d.pop("esrgan"))

        expand_mask_with_fade = ImageOutput.from_dict(d.pop("expand_mask_with_fade"))

        face_identifier = ImageOutput.from_dict(d.pop("face_identifier"))

        face_mask_detection = FaceMaskOutput.from_dict(d.pop("face_mask_detection"))

        face_off = FaceOffOutput.from_dict(d.pop("face_off"))

        float_ = FloatOutput.from_dict(d.pop("float"))

        float_batch = FloatOutput.from_dict(d.pop("float_batch"))

        float_collection = FloatCollectionOutput.from_dict(d.pop("float_collection"))

        float_generator = FloatGeneratorOutput.from_dict(d.pop("float_generator"))

        float_math = FloatOutput.from_dict(d.pop("float_math"))

        float_range = FloatCollectionOutput.from_dict(d.pop("float_range"))

        float_to_int = IntegerOutput.from_dict(d.pop("float_to_int"))

        flux2_denoise = LatentsOutput.from_dict(d.pop("flux2_denoise"))

        flux2_klein_lora_collection_loader = Flux2KleinLoRALoaderOutput.from_dict(
            d.pop("flux2_klein_lora_collection_loader")
        )

        flux2_klein_lora_loader = Flux2KleinLoRALoaderOutput.from_dict(d.pop("flux2_klein_lora_loader"))

        flux2_klein_model_loader = Flux2KleinModelLoaderOutput.from_dict(d.pop("flux2_klein_model_loader"))

        flux2_klein_text_encoder = FluxConditioningOutput.from_dict(d.pop("flux2_klein_text_encoder"))

        flux2_vae_decode = ImageOutput.from_dict(d.pop("flux2_vae_decode"))

        flux2_vae_encode = LatentsOutput.from_dict(d.pop("flux2_vae_encode"))

        flux_control_lora_loader = FluxControlLoRALoaderOutput.from_dict(d.pop("flux_control_lora_loader"))

        flux_controlnet = FluxControlNetOutput.from_dict(d.pop("flux_controlnet"))

        flux_denoise = LatentsOutput.from_dict(d.pop("flux_denoise"))

        flux_denoise_meta = LatentsMetaOutput.from_dict(d.pop("flux_denoise_meta"))

        flux_fill = FluxFillOutput.from_dict(d.pop("flux_fill"))

        flux_ip_adapter = IPAdapterOutput.from_dict(d.pop("flux_ip_adapter"))

        flux_kontext = FluxKontextOutput.from_dict(d.pop("flux_kontext"))

        flux_kontext_image_prep = ImageOutput.from_dict(d.pop("flux_kontext_image_prep"))

        flux_lora_collection_loader = FluxLoRALoaderOutput.from_dict(d.pop("flux_lora_collection_loader"))

        flux_lora_loader = FluxLoRALoaderOutput.from_dict(d.pop("flux_lora_loader"))

        flux_model_loader = FluxModelLoaderOutput.from_dict(d.pop("flux_model_loader"))

        flux_redux = FluxReduxOutput.from_dict(d.pop("flux_redux"))

        flux_text_encoder = FluxConditioningOutput.from_dict(d.pop("flux_text_encoder"))

        flux_vae_decode = ImageOutput.from_dict(d.pop("flux_vae_decode"))

        flux_vae_encode = LatentsOutput.from_dict(d.pop("flux_vae_encode"))

        freeu = UNetOutput.from_dict(d.pop("freeu"))

        gemini_image_generation = ImageCollectionOutput.from_dict(d.pop("gemini_image_generation"))

        get_image_mask_bounding_box = BoundingBoxOutput.from_dict(d.pop("get_image_mask_bounding_box"))

        grounding_dino = BoundingBoxCollectionOutput.from_dict(d.pop("grounding_dino"))

        hed_edge_detection = ImageOutput.from_dict(d.pop("hed_edge_detection"))

        heuristic_resize = ImageOutput.from_dict(d.pop("heuristic_resize"))

        i2l = LatentsOutput.from_dict(d.pop("i2l"))

        ideal_size = IdealSizeOutput.from_dict(d.pop("ideal_size"))

        if_ = IfInvocationOutput.from_dict(d.pop("if"))

        image = ImageOutput.from_dict(d.pop("image"))

        image_batch = ImageOutput.from_dict(d.pop("image_batch"))

        image_collection = ImageCollectionOutput.from_dict(d.pop("image_collection"))

        image_generator = ImageGeneratorOutput.from_dict(d.pop("image_generator"))

        image_mask_to_tensor = MaskOutput.from_dict(d.pop("image_mask_to_tensor"))

        image_panel_layout = ImagePanelCoordinateOutput.from_dict(d.pop("image_panel_layout"))

        img_blur = ImageOutput.from_dict(d.pop("img_blur"))

        img_chan = ImageOutput.from_dict(d.pop("img_chan"))

        img_channel_multiply = ImageOutput.from_dict(d.pop("img_channel_multiply"))

        img_channel_offset = ImageOutput.from_dict(d.pop("img_channel_offset"))

        img_conv = ImageOutput.from_dict(d.pop("img_conv"))

        img_crop = ImageOutput.from_dict(d.pop("img_crop"))

        img_hue_adjust = ImageOutput.from_dict(d.pop("img_hue_adjust"))

        img_hue_adjust_oklch = ImageOutput.from_dict(d.pop("img_hue_adjust_oklch"))

        img_ilerp = ImageOutput.from_dict(d.pop("img_ilerp"))

        img_lerp = ImageOutput.from_dict(d.pop("img_lerp"))

        img_mul = ImageOutput.from_dict(d.pop("img_mul"))

        img_noise = ImageOutput.from_dict(d.pop("img_noise"))

        img_nsfw = ImageOutput.from_dict(d.pop("img_nsfw"))

        img_pad_crop = ImageOutput.from_dict(d.pop("img_pad_crop"))

        img_paste = ImageOutput.from_dict(d.pop("img_paste"))

        img_resize = ImageOutput.from_dict(d.pop("img_resize"))

        img_scale = ImageOutput.from_dict(d.pop("img_scale"))

        img_watermark = ImageOutput.from_dict(d.pop("img_watermark"))

        infill_cv2 = ImageOutput.from_dict(d.pop("infill_cv2"))

        infill_lama = ImageOutput.from_dict(d.pop("infill_lama"))

        infill_patchmatch = ImageOutput.from_dict(d.pop("infill_patchmatch"))

        infill_rgba = ImageOutput.from_dict(d.pop("infill_rgba"))

        infill_tile = ImageOutput.from_dict(d.pop("infill_tile"))

        integer = IntegerOutput.from_dict(d.pop("integer"))

        integer_batch = IntegerOutput.from_dict(d.pop("integer_batch"))

        integer_collection = IntegerCollectionOutput.from_dict(d.pop("integer_collection"))

        integer_generator = IntegerGeneratorOutput.from_dict(d.pop("integer_generator"))

        integer_math = IntegerOutput.from_dict(d.pop("integer_math"))

        invert_tensor_mask = MaskOutput.from_dict(d.pop("invert_tensor_mask"))

        invokeai_ealightness = ImageOutput.from_dict(d.pop("invokeai_ealightness"))

        invokeai_img_blend = ImageOutput.from_dict(d.pop("invokeai_img_blend"))

        invokeai_img_composite = ImageOutput.from_dict(d.pop("invokeai_img_composite"))

        invokeai_img_dilate_erode = ImageOutput.from_dict(d.pop("invokeai_img_dilate_erode"))

        invokeai_img_enhance = ImageOutput.from_dict(d.pop("invokeai_img_enhance"))

        invokeai_img_hue_adjust_plus = ImageOutput.from_dict(d.pop("invokeai_img_hue_adjust_plus"))

        invokeai_img_val_thresholds = ImageOutput.from_dict(d.pop("invokeai_img_val_thresholds"))

        ip_adapter = IPAdapterOutput.from_dict(d.pop("ip_adapter"))

        iterate = IterateInvocationOutput.from_dict(d.pop("iterate"))

        l2i = ImageOutput.from_dict(d.pop("l2i"))

        latents = LatentsOutput.from_dict(d.pop("latents"))

        latents_collection = LatentsCollectionOutput.from_dict(d.pop("latents_collection"))

        lblend = LatentsOutput.from_dict(d.pop("lblend"))

        lineart_anime_edge_detection = ImageOutput.from_dict(d.pop("lineart_anime_edge_detection"))

        lineart_edge_detection = ImageOutput.from_dict(d.pop("lineart_edge_detection"))

        llava_onevision_vllm = StringOutput.from_dict(d.pop("llava_onevision_vllm"))

        lora_collection_loader = LoRALoaderOutput.from_dict(d.pop("lora_collection_loader"))

        lora_loader = LoRALoaderOutput.from_dict(d.pop("lora_loader"))

        lora_selector = LoRASelectorOutput.from_dict(d.pop("lora_selector"))

        lresize = LatentsOutput.from_dict(d.pop("lresize"))

        lscale = LatentsOutput.from_dict(d.pop("lscale"))

        main_model_loader = ModelLoaderOutput.from_dict(d.pop("main_model_loader"))

        mask_combine = ImageOutput.from_dict(d.pop("mask_combine"))

        mask_edge = ImageOutput.from_dict(d.pop("mask_edge"))

        mask_from_id = ImageOutput.from_dict(d.pop("mask_from_id"))

        mediapipe_face_detection = ImageOutput.from_dict(d.pop("mediapipe_face_detection"))

        merge_metadata = MetadataOutput.from_dict(d.pop("merge_metadata"))

        merge_tiles_to_image = ImageOutput.from_dict(d.pop("merge_tiles_to_image"))

        metadata = MetadataOutput.from_dict(d.pop("metadata"))

        metadata_field_extractor = StringOutput.from_dict(d.pop("metadata_field_extractor"))

        metadata_from_image = MetadataOutput.from_dict(d.pop("metadata_from_image"))

        metadata_item = MetadataItemOutput.from_dict(d.pop("metadata_item"))

        metadata_item_linked = MetadataOutput.from_dict(d.pop("metadata_item_linked"))

        metadata_to_bool = BooleanOutput.from_dict(d.pop("metadata_to_bool"))

        metadata_to_bool_collection = BooleanCollectionOutput.from_dict(d.pop("metadata_to_bool_collection"))

        metadata_to_controlnets = MDControlListOutput.from_dict(d.pop("metadata_to_controlnets"))

        metadata_to_float = FloatOutput.from_dict(d.pop("metadata_to_float"))

        metadata_to_float_collection = FloatCollectionOutput.from_dict(d.pop("metadata_to_float_collection"))

        metadata_to_integer = IntegerOutput.from_dict(d.pop("metadata_to_integer"))

        metadata_to_integer_collection = IntegerCollectionOutput.from_dict(d.pop("metadata_to_integer_collection"))

        metadata_to_ip_adapters = MDIPAdapterListOutput.from_dict(d.pop("metadata_to_ip_adapters"))

        metadata_to_lora_collection = MetadataToLorasCollectionOutput.from_dict(d.pop("metadata_to_lora_collection"))

        metadata_to_loras = LoRALoaderOutput.from_dict(d.pop("metadata_to_loras"))

        metadata_to_model = MetadataToModelOutput.from_dict(d.pop("metadata_to_model"))

        metadata_to_scheduler = SchedulerOutput.from_dict(d.pop("metadata_to_scheduler"))

        metadata_to_sdlx_loras = SDXLLoRALoaderOutput.from_dict(d.pop("metadata_to_sdlx_loras"))

        metadata_to_sdxl_model = MetadataToSDXLModelOutput.from_dict(d.pop("metadata_to_sdxl_model"))

        metadata_to_string = StringOutput.from_dict(d.pop("metadata_to_string"))

        metadata_to_string_collection = StringCollectionOutput.from_dict(d.pop("metadata_to_string_collection"))

        metadata_to_t2i_adapters = MDT2IAdapterListOutput.from_dict(d.pop("metadata_to_t2i_adapters"))

        metadata_to_vae = VAEOutput.from_dict(d.pop("metadata_to_vae"))

        mlsd_detection = ImageOutput.from_dict(d.pop("mlsd_detection"))

        model_identifier = ModelIdentifierOutput.from_dict(d.pop("model_identifier"))

        mul = IntegerOutput.from_dict(d.pop("mul"))

        noise = NoiseOutput.from_dict(d.pop("noise"))

        normal_map = ImageOutput.from_dict(d.pop("normal_map"))

        openai_image_generation = ImageCollectionOutput.from_dict(d.pop("openai_image_generation"))

        pair_tile_image = PairTileImageOutput.from_dict(d.pop("pair_tile_image"))

        paste_image_into_bounding_box = ImageOutput.from_dict(d.pop("paste_image_into_bounding_box"))

        pbr_maps = PBRMapsOutput.from_dict(d.pop("pbr_maps"))

        pidi_edge_detection = ImageOutput.from_dict(d.pop("pidi_edge_detection"))

        prompt_from_file = StringCollectionOutput.from_dict(d.pop("prompt_from_file"))

        prompt_template = PromptTemplateOutput.from_dict(d.pop("prompt_template"))

        qwen_image_denoise = LatentsOutput.from_dict(d.pop("qwen_image_denoise"))

        qwen_image_i2l = LatentsOutput.from_dict(d.pop("qwen_image_i2l"))

        qwen_image_l2i = ImageOutput.from_dict(d.pop("qwen_image_l2i"))

        qwen_image_lora_collection_loader = QwenImageLoRALoaderOutput.from_dict(
            d.pop("qwen_image_lora_collection_loader")
        )

        qwen_image_lora_loader = QwenImageLoRALoaderOutput.from_dict(d.pop("qwen_image_lora_loader"))

        qwen_image_model_loader = QwenImageModelLoaderOutput.from_dict(d.pop("qwen_image_model_loader"))

        qwen_image_text_encoder = QwenImageConditioningOutput.from_dict(d.pop("qwen_image_text_encoder"))

        rand_float = FloatOutput.from_dict(d.pop("rand_float"))

        rand_int = IntegerOutput.from_dict(d.pop("rand_int"))

        random_range = IntegerCollectionOutput.from_dict(d.pop("random_range"))

        range_ = IntegerCollectionOutput.from_dict(d.pop("range"))

        range_of_size = IntegerCollectionOutput.from_dict(d.pop("range_of_size"))

        rectangle_mask = MaskOutput.from_dict(d.pop("rectangle_mask"))

        round_float = FloatOutput.from_dict(d.pop("round_float"))

        save_image = ImageOutput.from_dict(d.pop("save_image"))

        save_image_to_file = ImageOutput.from_dict(d.pop("save_image_to_file"))

        scheduler = SchedulerOutput.from_dict(d.pop("scheduler"))

        sd3_denoise = LatentsOutput.from_dict(d.pop("sd3_denoise"))

        sd3_i2l = LatentsOutput.from_dict(d.pop("sd3_i2l"))

        sd3_l2i = ImageOutput.from_dict(d.pop("sd3_l2i"))

        sd3_model_loader = Sd3ModelLoaderOutput.from_dict(d.pop("sd3_model_loader"))

        sd3_text_encoder = SD3ConditioningOutput.from_dict(d.pop("sd3_text_encoder"))

        sdxl_compel_prompt = ConditioningOutput.from_dict(d.pop("sdxl_compel_prompt"))

        sdxl_lora_collection_loader = SDXLLoRALoaderOutput.from_dict(d.pop("sdxl_lora_collection_loader"))

        sdxl_lora_loader = SDXLLoRALoaderOutput.from_dict(d.pop("sdxl_lora_loader"))

        sdxl_model_loader = SDXLModelLoaderOutput.from_dict(d.pop("sdxl_model_loader"))

        sdxl_refiner_compel_prompt = ConditioningOutput.from_dict(d.pop("sdxl_refiner_compel_prompt"))

        sdxl_refiner_model_loader = SDXLRefinerModelLoaderOutput.from_dict(d.pop("sdxl_refiner_model_loader"))

        seamless = SeamlessModeOutput.from_dict(d.pop("seamless"))

        seedream_image_generation = ImageCollectionOutput.from_dict(d.pop("seedream_image_generation"))

        segment_anything = MaskOutput.from_dict(d.pop("segment_anything"))

        show_image = ImageOutput.from_dict(d.pop("show_image"))

        spandrel_image_to_image = ImageOutput.from_dict(d.pop("spandrel_image_to_image"))

        spandrel_image_to_image_autoscale = ImageOutput.from_dict(d.pop("spandrel_image_to_image_autoscale"))

        string = StringOutput.from_dict(d.pop("string"))

        string_batch = StringOutput.from_dict(d.pop("string_batch"))

        string_collection = StringCollectionOutput.from_dict(d.pop("string_collection"))

        string_generator = StringGeneratorOutput.from_dict(d.pop("string_generator"))

        string_join = StringOutput.from_dict(d.pop("string_join"))

        string_join_three = StringOutput.from_dict(d.pop("string_join_three"))

        string_replace = StringOutput.from_dict(d.pop("string_replace"))

        string_split = String2Output.from_dict(d.pop("string_split"))

        string_split_neg = StringPosNegOutput.from_dict(d.pop("string_split_neg"))

        sub = IntegerOutput.from_dict(d.pop("sub"))

        t2i_adapter = T2IAdapterOutput.from_dict(d.pop("t2i_adapter"))

        tensor_mask_to_image = ImageOutput.from_dict(d.pop("tensor_mask_to_image"))

        text_llm = StringOutput.from_dict(d.pop("text_llm"))

        tile_to_properties = TileToPropertiesOutput.from_dict(d.pop("tile_to_properties"))

        tiled_multi_diffusion_denoise_latents = LatentsOutput.from_dict(d.pop("tiled_multi_diffusion_denoise_latents"))

        tomask = ImageOutput.from_dict(d.pop("tomask"))

        unsharp_mask = ImageOutput.from_dict(d.pop("unsharp_mask"))

        unsharp_mask_oklab = ImageOutput.from_dict(d.pop("unsharp_mask_oklab"))

        vae_loader = VAEOutput.from_dict(d.pop("vae_loader"))

        z_image_control = ZImageControlOutput.from_dict(d.pop("z_image_control"))

        z_image_denoise = LatentsOutput.from_dict(d.pop("z_image_denoise"))

        z_image_denoise_meta = LatentsMetaOutput.from_dict(d.pop("z_image_denoise_meta"))

        z_image_i2l = LatentsOutput.from_dict(d.pop("z_image_i2l"))

        z_image_l2i = ImageOutput.from_dict(d.pop("z_image_l2i"))

        z_image_lora_collection_loader = ZImageLoRALoaderOutput.from_dict(d.pop("z_image_lora_collection_loader"))

        z_image_lora_loader = ZImageLoRALoaderOutput.from_dict(d.pop("z_image_lora_loader"))

        z_image_model_loader = ZImageModelLoaderOutput.from_dict(d.pop("z_image_model_loader"))

        z_image_seed_variance_enhancer = ZImageConditioningOutput.from_dict(d.pop("z_image_seed_variance_enhancer"))

        z_image_text_encoder = ZImageConditioningOutput.from_dict(d.pop("z_image_text_encoder"))

        invocation_output_map = cls(
            add=add,
            alibabacloud_image_generation=alibabacloud_image_generation,
            alpha_mask_to_tensor=alpha_mask_to_tensor,
            anima_denoise=anima_denoise,
            anima_i2l=anima_i2l,
            anima_l2i=anima_l2i,
            anima_lora_collection_loader=anima_lora_collection_loader,
            anima_lora_loader=anima_lora_loader,
            anima_model_loader=anima_model_loader,
            anima_text_encoder=anima_text_encoder,
            apply_mask_to_image=apply_mask_to_image,
            apply_tensor_mask_to_image=apply_tensor_mask_to_image,
            blank_image=blank_image,
            boolean=boolean,
            boolean_collection=boolean_collection,
            bounding_box=bounding_box,
            calculate_image_tiles=calculate_image_tiles,
            calculate_image_tiles_even_split=calculate_image_tiles_even_split,
            calculate_image_tiles_min_overlap=calculate_image_tiles_min_overlap,
            canny_edge_detection=canny_edge_detection,
            canvas_output=canvas_output,
            canvas_paste_back=canvas_paste_back,
            canvas_v2_mask_and_crop=canvas_v2_mask_and_crop,
            clip_skip=clip_skip,
            cogview4_denoise=cogview4_denoise,
            cogview4_i2l=cogview4_i2l,
            cogview4_l2i=cogview4_l2i,
            cogview4_model_loader=cogview4_model_loader,
            cogview4_text_encoder=cogview4_text_encoder,
            collect=collect,
            color=color,
            color_correct=color_correct,
            color_map=color_map,
            compel=compel,
            conditioning=conditioning,
            conditioning_collection=conditioning_collection,
            content_shuffle=content_shuffle,
            controlnet=controlnet,
            core_metadata=core_metadata,
            create_denoise_mask=create_denoise_mask,
            create_gradient_mask=create_gradient_mask,
            crop_image_to_bounding_box=crop_image_to_bounding_box,
            crop_latents=crop_latents,
            cv_inpaint=cv_inpaint,
            decode_watermark=decode_watermark,
            denoise_latents=denoise_latents,
            denoise_latents_meta=denoise_latents_meta,
            depth_anything_depth_estimation=depth_anything_depth_estimation,
            div=div,
            dw_openpose_detection=dw_openpose_detection,
            dynamic_prompt=dynamic_prompt,
            esrgan=esrgan,
            expand_mask_with_fade=expand_mask_with_fade,
            face_identifier=face_identifier,
            face_mask_detection=face_mask_detection,
            face_off=face_off,
            float_=float_,
            float_batch=float_batch,
            float_collection=float_collection,
            float_generator=float_generator,
            float_math=float_math,
            float_range=float_range,
            float_to_int=float_to_int,
            flux2_denoise=flux2_denoise,
            flux2_klein_lora_collection_loader=flux2_klein_lora_collection_loader,
            flux2_klein_lora_loader=flux2_klein_lora_loader,
            flux2_klein_model_loader=flux2_klein_model_loader,
            flux2_klein_text_encoder=flux2_klein_text_encoder,
            flux2_vae_decode=flux2_vae_decode,
            flux2_vae_encode=flux2_vae_encode,
            flux_control_lora_loader=flux_control_lora_loader,
            flux_controlnet=flux_controlnet,
            flux_denoise=flux_denoise,
            flux_denoise_meta=flux_denoise_meta,
            flux_fill=flux_fill,
            flux_ip_adapter=flux_ip_adapter,
            flux_kontext=flux_kontext,
            flux_kontext_image_prep=flux_kontext_image_prep,
            flux_lora_collection_loader=flux_lora_collection_loader,
            flux_lora_loader=flux_lora_loader,
            flux_model_loader=flux_model_loader,
            flux_redux=flux_redux,
            flux_text_encoder=flux_text_encoder,
            flux_vae_decode=flux_vae_decode,
            flux_vae_encode=flux_vae_encode,
            freeu=freeu,
            gemini_image_generation=gemini_image_generation,
            get_image_mask_bounding_box=get_image_mask_bounding_box,
            grounding_dino=grounding_dino,
            hed_edge_detection=hed_edge_detection,
            heuristic_resize=heuristic_resize,
            i2l=i2l,
            ideal_size=ideal_size,
            if_=if_,
            image=image,
            image_batch=image_batch,
            image_collection=image_collection,
            image_generator=image_generator,
            image_mask_to_tensor=image_mask_to_tensor,
            image_panel_layout=image_panel_layout,
            img_blur=img_blur,
            img_chan=img_chan,
            img_channel_multiply=img_channel_multiply,
            img_channel_offset=img_channel_offset,
            img_conv=img_conv,
            img_crop=img_crop,
            img_hue_adjust=img_hue_adjust,
            img_hue_adjust_oklch=img_hue_adjust_oklch,
            img_ilerp=img_ilerp,
            img_lerp=img_lerp,
            img_mul=img_mul,
            img_noise=img_noise,
            img_nsfw=img_nsfw,
            img_pad_crop=img_pad_crop,
            img_paste=img_paste,
            img_resize=img_resize,
            img_scale=img_scale,
            img_watermark=img_watermark,
            infill_cv2=infill_cv2,
            infill_lama=infill_lama,
            infill_patchmatch=infill_patchmatch,
            infill_rgba=infill_rgba,
            infill_tile=infill_tile,
            integer=integer,
            integer_batch=integer_batch,
            integer_collection=integer_collection,
            integer_generator=integer_generator,
            integer_math=integer_math,
            invert_tensor_mask=invert_tensor_mask,
            invokeai_ealightness=invokeai_ealightness,
            invokeai_img_blend=invokeai_img_blend,
            invokeai_img_composite=invokeai_img_composite,
            invokeai_img_dilate_erode=invokeai_img_dilate_erode,
            invokeai_img_enhance=invokeai_img_enhance,
            invokeai_img_hue_adjust_plus=invokeai_img_hue_adjust_plus,
            invokeai_img_val_thresholds=invokeai_img_val_thresholds,
            ip_adapter=ip_adapter,
            iterate=iterate,
            l2i=l2i,
            latents=latents,
            latents_collection=latents_collection,
            lblend=lblend,
            lineart_anime_edge_detection=lineart_anime_edge_detection,
            lineart_edge_detection=lineart_edge_detection,
            llava_onevision_vllm=llava_onevision_vllm,
            lora_collection_loader=lora_collection_loader,
            lora_loader=lora_loader,
            lora_selector=lora_selector,
            lresize=lresize,
            lscale=lscale,
            main_model_loader=main_model_loader,
            mask_combine=mask_combine,
            mask_edge=mask_edge,
            mask_from_id=mask_from_id,
            mediapipe_face_detection=mediapipe_face_detection,
            merge_metadata=merge_metadata,
            merge_tiles_to_image=merge_tiles_to_image,
            metadata=metadata,
            metadata_field_extractor=metadata_field_extractor,
            metadata_from_image=metadata_from_image,
            metadata_item=metadata_item,
            metadata_item_linked=metadata_item_linked,
            metadata_to_bool=metadata_to_bool,
            metadata_to_bool_collection=metadata_to_bool_collection,
            metadata_to_controlnets=metadata_to_controlnets,
            metadata_to_float=metadata_to_float,
            metadata_to_float_collection=metadata_to_float_collection,
            metadata_to_integer=metadata_to_integer,
            metadata_to_integer_collection=metadata_to_integer_collection,
            metadata_to_ip_adapters=metadata_to_ip_adapters,
            metadata_to_lora_collection=metadata_to_lora_collection,
            metadata_to_loras=metadata_to_loras,
            metadata_to_model=metadata_to_model,
            metadata_to_scheduler=metadata_to_scheduler,
            metadata_to_sdlx_loras=metadata_to_sdlx_loras,
            metadata_to_sdxl_model=metadata_to_sdxl_model,
            metadata_to_string=metadata_to_string,
            metadata_to_string_collection=metadata_to_string_collection,
            metadata_to_t2i_adapters=metadata_to_t2i_adapters,
            metadata_to_vae=metadata_to_vae,
            mlsd_detection=mlsd_detection,
            model_identifier=model_identifier,
            mul=mul,
            noise=noise,
            normal_map=normal_map,
            openai_image_generation=openai_image_generation,
            pair_tile_image=pair_tile_image,
            paste_image_into_bounding_box=paste_image_into_bounding_box,
            pbr_maps=pbr_maps,
            pidi_edge_detection=pidi_edge_detection,
            prompt_from_file=prompt_from_file,
            prompt_template=prompt_template,
            qwen_image_denoise=qwen_image_denoise,
            qwen_image_i2l=qwen_image_i2l,
            qwen_image_l2i=qwen_image_l2i,
            qwen_image_lora_collection_loader=qwen_image_lora_collection_loader,
            qwen_image_lora_loader=qwen_image_lora_loader,
            qwen_image_model_loader=qwen_image_model_loader,
            qwen_image_text_encoder=qwen_image_text_encoder,
            rand_float=rand_float,
            rand_int=rand_int,
            random_range=random_range,
            range_=range_,
            range_of_size=range_of_size,
            rectangle_mask=rectangle_mask,
            round_float=round_float,
            save_image=save_image,
            save_image_to_file=save_image_to_file,
            scheduler=scheduler,
            sd3_denoise=sd3_denoise,
            sd3_i2l=sd3_i2l,
            sd3_l2i=sd3_l2i,
            sd3_model_loader=sd3_model_loader,
            sd3_text_encoder=sd3_text_encoder,
            sdxl_compel_prompt=sdxl_compel_prompt,
            sdxl_lora_collection_loader=sdxl_lora_collection_loader,
            sdxl_lora_loader=sdxl_lora_loader,
            sdxl_model_loader=sdxl_model_loader,
            sdxl_refiner_compel_prompt=sdxl_refiner_compel_prompt,
            sdxl_refiner_model_loader=sdxl_refiner_model_loader,
            seamless=seamless,
            seedream_image_generation=seedream_image_generation,
            segment_anything=segment_anything,
            show_image=show_image,
            spandrel_image_to_image=spandrel_image_to_image,
            spandrel_image_to_image_autoscale=spandrel_image_to_image_autoscale,
            string=string,
            string_batch=string_batch,
            string_collection=string_collection,
            string_generator=string_generator,
            string_join=string_join,
            string_join_three=string_join_three,
            string_replace=string_replace,
            string_split=string_split,
            string_split_neg=string_split_neg,
            sub=sub,
            t2i_adapter=t2i_adapter,
            tensor_mask_to_image=tensor_mask_to_image,
            text_llm=text_llm,
            tile_to_properties=tile_to_properties,
            tiled_multi_diffusion_denoise_latents=tiled_multi_diffusion_denoise_latents,
            tomask=tomask,
            unsharp_mask=unsharp_mask,
            unsharp_mask_oklab=unsharp_mask_oklab,
            vae_loader=vae_loader,
            z_image_control=z_image_control,
            z_image_denoise=z_image_denoise,
            z_image_denoise_meta=z_image_denoise_meta,
            z_image_i2l=z_image_i2l,
            z_image_l2i=z_image_l2i,
            z_image_lora_collection_loader=z_image_lora_collection_loader,
            z_image_lora_loader=z_image_lora_loader,
            z_image_model_loader=z_image_model_loader,
            z_image_seed_variance_enhancer=z_image_seed_variance_enhancer,
            z_image_text_encoder=z_image_text_encoder,
        )

        invocation_output_map.additional_properties = d
        return invocation_output_map

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
