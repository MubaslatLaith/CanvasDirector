from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.install_status import InstallStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_metadata import BaseMetadata
    from ..models.clip_embed_diffusers_g_config import CLIPEmbedDiffusersGConfig
    from ..models.clip_embed_diffusers_l_config import CLIPEmbedDiffusersLConfig
    from ..models.clip_vision_diffusers_config import CLIPVisionDiffusersConfig
    from ..models.control_lo_ra_ly_corisflux_config import ControlLoRALyCORISFLUXConfig
    from ..models.control_net_checkpoint_flux_config import ControlNetCheckpointFLUXConfig
    from ..models.control_net_checkpoint_sd1_config import ControlNetCheckpointSD1Config
    from ..models.control_net_checkpoint_sd2_config import ControlNetCheckpointSD2Config
    from ..models.control_net_checkpoint_sdxl_config import ControlNetCheckpointSDXLConfig
    from ..models.control_net_checkpoint_z_image_config import ControlNetCheckpointZImageConfig
    from ..models.control_net_diffusers_flux_config import ControlNetDiffusersFLUXConfig
    from ..models.control_net_diffusers_sd1_config import ControlNetDiffusersSD1Config
    from ..models.control_net_diffusers_sd2_config import ControlNetDiffusersSD2Config
    from ..models.control_net_diffusers_sdxl_config import ControlNetDiffusersSDXLConfig
    from ..models.download_job import DownloadJob
    from ..models.external_api_model_config import ExternalApiModelConfig
    from ..models.external_model_source import ExternalModelSource
    from ..models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
    from ..models.hf_model_source import HFModelSource
    from ..models.hugging_face_metadata import HuggingFaceMetadata
    from ..models.ip_adapter_checkpoint_flux_config import IPAdapterCheckpointFLUXConfig
    from ..models.ip_adapter_checkpoint_sd1_config import IPAdapterCheckpointSD1Config
    from ..models.ip_adapter_checkpoint_sd2_config import IPAdapterCheckpointSD2Config
    from ..models.ip_adapter_checkpoint_sdxl_config import IPAdapterCheckpointSDXLConfig
    from ..models.ip_adapter_invoke_aisd1_config import IPAdapterInvokeAISD1Config
    from ..models.ip_adapter_invoke_aisd2_config import IPAdapterInvokeAISD2Config
    from ..models.ip_adapter_invoke_aisdxl_config import IPAdapterInvokeAISDXLConfig
    from ..models.llava_onevision_diffusers_config import LlavaOnevisionDiffusersConfig
    from ..models.lo_ra_diffusers_flux_2_config import LoRADiffusersFlux2Config
    from ..models.lo_ra_diffusers_flux_config import LoRADiffusersFLUXConfig
    from ..models.lo_ra_diffusers_sd1_config import LoRADiffusersSD1Config
    from ..models.lo_ra_diffusers_sd2_config import LoRADiffusersSD2Config
    from ..models.lo_ra_diffusers_sdxl_config import LoRADiffusersSDXLConfig
    from ..models.lo_ra_diffusers_z_image_config import LoRADiffusersZImageConfig
    from ..models.lo_ra_ly_coris_anima_config import LoRALyCORISAnimaConfig
    from ..models.lo_ra_ly_coris_flux_2_config import LoRALyCORISFlux2Config
    from ..models.lo_ra_ly_coris_qwen_image_config import LoRALyCORISQwenImageConfig
    from ..models.lo_ra_ly_corisflux_config import LoRALyCORISFLUXConfig
    from ..models.lo_ra_ly_corissd1_config import LoRALyCORISSD1Config
    from ..models.lo_ra_ly_corissd2_config import LoRALyCORISSD2Config
    from ..models.lo_ra_ly_corissdxl_config import LoRALyCORISSDXLConfig
    from ..models.lo_ra_ly_corisz_image_config import LoRALyCORISZImageConfig
    from ..models.lo_raomiflux_config import LoRAOMIFLUXConfig
    from ..models.lo_raomisdxl_config import LoRAOMISDXLConfig
    from ..models.local_model_source import LocalModelSource
    from ..models.main_bn_bnf4flux_config import MainBnBNF4FLUXConfig
    from ..models.main_checkpoint_anima_config import MainCheckpointAnimaConfig
    from ..models.main_checkpoint_flux_2_config import MainCheckpointFlux2Config
    from ..models.main_checkpoint_flux_config import MainCheckpointFLUXConfig
    from ..models.main_checkpoint_sd1_config import MainCheckpointSD1Config
    from ..models.main_checkpoint_sd2_config import MainCheckpointSD2Config
    from ..models.main_checkpoint_sdxl_config import MainCheckpointSDXLConfig
    from ..models.main_checkpoint_sdxl_refiner_config import MainCheckpointSDXLRefinerConfig
    from ..models.main_checkpoint_z_image_config import MainCheckpointZImageConfig
    from ..models.main_diffusers_cog_view_4_config import MainDiffusersCogView4Config
    from ..models.main_diffusers_flux_2_config import MainDiffusersFlux2Config
    from ..models.main_diffusers_flux_config import MainDiffusersFLUXConfig
    from ..models.main_diffusers_qwen_image_config import MainDiffusersQwenImageConfig
    from ..models.main_diffusers_sd1_config import MainDiffusersSD1Config
    from ..models.main_diffusers_sd2_config import MainDiffusersSD2Config
    from ..models.main_diffusers_sd3_config import MainDiffusersSD3Config
    from ..models.main_diffusers_sdxl_config import MainDiffusersSDXLConfig
    from ..models.main_diffusers_sdxl_refiner_config import MainDiffusersSDXLRefinerConfig
    from ..models.main_diffusers_z_image_config import MainDiffusersZImageConfig
    from ..models.main_gguf_flux_2_config import MainGGUFFlux2Config
    from ..models.main_gguf_qwen_image_config import MainGGUFQwenImageConfig
    from ..models.main_ggufflux_config import MainGGUFFLUXConfig
    from ..models.main_ggufz_image_config import MainGGUFZImageConfig
    from ..models.model_record_changes import ModelRecordChanges
    from ..models.qwen_3_encoder_checkpoint_config import Qwen3EncoderCheckpointConfig
    from ..models.qwen_3_encoder_gguf_config import Qwen3EncoderGGUFConfig
    from ..models.qwen_3_encoder_qwen_3_encoder_config import Qwen3EncoderQwen3EncoderConfig
    from ..models.qwen_vl_encoder_checkpoint_config import QwenVLEncoderCheckpointConfig
    from ..models.qwen_vl_encoder_diffusers_config import QwenVLEncoderDiffusersConfig
    from ..models.sig_lip_diffusers_config import SigLIPDiffusersConfig
    from ..models.spandrel_checkpoint_config import SpandrelCheckpointConfig
    from ..models.t2i_adapter_diffusers_sd1_config import T2IAdapterDiffusersSD1Config
    from ..models.t2i_adapter_diffusers_sdxl_config import T2IAdapterDiffusersSDXLConfig
    from ..models.t5_encoder_bn_bll_mint_8_config import T5EncoderBnBLLMint8Config
    from ..models.t5_encoder_t5_encoder_config import T5EncoderT5EncoderConfig
    from ..models.text_llm_diffusers_config import TextLLMDiffusersConfig
    from ..models.ti_file_sd1_config import TIFileSD1Config
    from ..models.ti_file_sd2_config import TIFileSD2Config
    from ..models.ti_file_sdxl_config import TIFileSDXLConfig
    from ..models.ti_folder_sd1_config import TIFolderSD1Config
    from ..models.ti_folder_sd2_config import TIFolderSD2Config
    from ..models.ti_folder_sdxl_config import TIFolderSDXLConfig
    from ..models.unknown_config import UnknownConfig
    from ..models.url_model_source import URLModelSource
    from ..models.vae_checkpoint_anima_config import VAECheckpointAnimaConfig
    from ..models.vae_checkpoint_flux_2_config import VAECheckpointFlux2Config
    from ..models.vae_checkpoint_flux_config import VAECheckpointFLUXConfig
    from ..models.vae_checkpoint_qwen_image_config import VAECheckpointQwenImageConfig
    from ..models.vae_checkpoint_sd1_config import VAECheckpointSD1Config
    from ..models.vae_checkpoint_sd2_config import VAECheckpointSD2Config
    from ..models.vae_checkpoint_sdxl_config import VAECheckpointSDXLConfig
    from ..models.vae_diffusers_flux_2_config import VAEDiffusersFlux2Config
    from ..models.vae_diffusers_sd1_config import VAEDiffusersSD1Config
    from ..models.vae_diffusers_sdxl_config import VAEDiffusersSDXLConfig


T = TypeVar("T", bound="ModelInstallJob")


@_attrs_define
class ModelInstallJob:
    """Object that tracks the current status of an install request.

    Attributes:
        id (int): Unique ID for this job
        source (ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource): Source (URL, repo_id, or local
            path) of model
        local_path (str): Path to locally-downloaded model; may be the same as the source
        status (InstallStatus | Unset): State of an install job running in the background.
        error_reason (None | str | Unset): Information about why the job failed
        config_in (ModelRecordChanges | Unset): A set of changes to apply to a model.
        config_out (CLIPEmbedDiffusersGConfig | CLIPEmbedDiffusersLConfig | CLIPVisionDiffusersConfig |
            ControlLoRALyCORISFLUXConfig | ControlNetCheckpointFLUXConfig | ControlNetCheckpointSD1Config |
            ControlNetCheckpointSD2Config | ControlNetCheckpointSDXLConfig | ControlNetCheckpointZImageConfig |
            ControlNetDiffusersFLUXConfig | ControlNetDiffusersSD1Config | ControlNetDiffusersSD2Config |
            ControlNetDiffusersSDXLConfig | ExternalApiModelConfig | FLUXReduxCheckpointConfig |
            IPAdapterCheckpointFLUXConfig | IPAdapterCheckpointSD1Config | IPAdapterCheckpointSD2Config |
            IPAdapterCheckpointSDXLConfig | IPAdapterInvokeAISD1Config | IPAdapterInvokeAISD2Config |
            IPAdapterInvokeAISDXLConfig | LlavaOnevisionDiffusersConfig | LoRADiffusersFlux2Config | LoRADiffusersFLUXConfig
            | LoRADiffusersSD1Config | LoRADiffusersSD2Config | LoRADiffusersSDXLConfig | LoRADiffusersZImageConfig |
            LoRALyCORISAnimaConfig | LoRALyCORISFlux2Config | LoRALyCORISFLUXConfig | LoRALyCORISQwenImageConfig |
            LoRALyCORISSD1Config | LoRALyCORISSD2Config | LoRALyCORISSDXLConfig | LoRALyCORISZImageConfig |
            LoRAOMIFLUXConfig | LoRAOMISDXLConfig | MainBnBNF4FLUXConfig | MainCheckpointAnimaConfig |
            MainCheckpointFlux2Config | MainCheckpointFLUXConfig | MainCheckpointSD1Config | MainCheckpointSD2Config |
            MainCheckpointSDXLConfig | MainCheckpointSDXLRefinerConfig | MainCheckpointZImageConfig |
            MainDiffusersCogView4Config | MainDiffusersFlux2Config | MainDiffusersFLUXConfig | MainDiffusersQwenImageConfig
            | MainDiffusersSD1Config | MainDiffusersSD2Config | MainDiffusersSD3Config | MainDiffusersSDXLConfig |
            MainDiffusersSDXLRefinerConfig | MainDiffusersZImageConfig | MainGGUFFlux2Config | MainGGUFFLUXConfig |
            MainGGUFQwenImageConfig | MainGGUFZImageConfig | None | Qwen3EncoderCheckpointConfig | Qwen3EncoderGGUFConfig |
            Qwen3EncoderQwen3EncoderConfig | QwenVLEncoderCheckpointConfig | QwenVLEncoderDiffusersConfig |
            SigLIPDiffusersConfig | SpandrelCheckpointConfig | T2IAdapterDiffusersSD1Config | T2IAdapterDiffusersSDXLConfig
            | T5EncoderBnBLLMint8Config | T5EncoderT5EncoderConfig | TextLLMDiffusersConfig | TIFileSD1Config |
            TIFileSD2Config | TIFileSDXLConfig | TIFolderSD1Config | TIFolderSD2Config | TIFolderSDXLConfig | UnknownConfig
            | Unset | VAECheckpointAnimaConfig | VAECheckpointFlux2Config | VAECheckpointFLUXConfig |
            VAECheckpointQwenImageConfig | VAECheckpointSD1Config | VAECheckpointSD2Config | VAECheckpointSDXLConfig |
            VAEDiffusersFlux2Config | VAEDiffusersSD1Config | VAEDiffusersSDXLConfig): After successful installation, this
            will hold the configuration object.
        inplace (bool | Unset): Leave model in its current location; otherwise install under models directory Default:
            False.
        bytes_ (int | Unset): For a remote model, the number of bytes downloaded so far (may not be available) Default:
            0.
        total_bytes (int | Unset): Total size of the model to be installed Default: 0.
        source_metadata (BaseMetadata | HuggingFaceMetadata | None | Unset): Metadata provided by the model source
        download_parts (list[DownloadJob] | Unset): Download jobs contributing to this install
        error (None | str | Unset): On an error condition, this field will contain the text of the exception
        error_traceback (None | str | Unset): On an error condition, this field will contain the exception traceback
    """

    id: int
    source: ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource
    local_path: str
    status: InstallStatus | Unset = UNSET
    error_reason: None | str | Unset = UNSET
    config_in: ModelRecordChanges | Unset = UNSET
    config_out: (
        CLIPEmbedDiffusersGConfig
        | CLIPEmbedDiffusersLConfig
        | CLIPVisionDiffusersConfig
        | ControlLoRALyCORISFLUXConfig
        | ControlNetCheckpointFLUXConfig
        | ControlNetCheckpointSD1Config
        | ControlNetCheckpointSD2Config
        | ControlNetCheckpointSDXLConfig
        | ControlNetCheckpointZImageConfig
        | ControlNetDiffusersFLUXConfig
        | ControlNetDiffusersSD1Config
        | ControlNetDiffusersSD2Config
        | ControlNetDiffusersSDXLConfig
        | ExternalApiModelConfig
        | FLUXReduxCheckpointConfig
        | IPAdapterCheckpointFLUXConfig
        | IPAdapterCheckpointSD1Config
        | IPAdapterCheckpointSD2Config
        | IPAdapterCheckpointSDXLConfig
        | IPAdapterInvokeAISD1Config
        | IPAdapterInvokeAISD2Config
        | IPAdapterInvokeAISDXLConfig
        | LlavaOnevisionDiffusersConfig
        | LoRADiffusersFlux2Config
        | LoRADiffusersFLUXConfig
        | LoRADiffusersSD1Config
        | LoRADiffusersSD2Config
        | LoRADiffusersSDXLConfig
        | LoRADiffusersZImageConfig
        | LoRALyCORISAnimaConfig
        | LoRALyCORISFlux2Config
        | LoRALyCORISFLUXConfig
        | LoRALyCORISQwenImageConfig
        | LoRALyCORISSD1Config
        | LoRALyCORISSD2Config
        | LoRALyCORISSDXLConfig
        | LoRALyCORISZImageConfig
        | LoRAOMIFLUXConfig
        | LoRAOMISDXLConfig
        | MainBnBNF4FLUXConfig
        | MainCheckpointAnimaConfig
        | MainCheckpointFlux2Config
        | MainCheckpointFLUXConfig
        | MainCheckpointSD1Config
        | MainCheckpointSD2Config
        | MainCheckpointSDXLConfig
        | MainCheckpointSDXLRefinerConfig
        | MainCheckpointZImageConfig
        | MainDiffusersCogView4Config
        | MainDiffusersFlux2Config
        | MainDiffusersFLUXConfig
        | MainDiffusersQwenImageConfig
        | MainDiffusersSD1Config
        | MainDiffusersSD2Config
        | MainDiffusersSD3Config
        | MainDiffusersSDXLConfig
        | MainDiffusersSDXLRefinerConfig
        | MainDiffusersZImageConfig
        | MainGGUFFlux2Config
        | MainGGUFFLUXConfig
        | MainGGUFQwenImageConfig
        | MainGGUFZImageConfig
        | None
        | Qwen3EncoderCheckpointConfig
        | Qwen3EncoderGGUFConfig
        | Qwen3EncoderQwen3EncoderConfig
        | QwenVLEncoderCheckpointConfig
        | QwenVLEncoderDiffusersConfig
        | SigLIPDiffusersConfig
        | SpandrelCheckpointConfig
        | T2IAdapterDiffusersSD1Config
        | T2IAdapterDiffusersSDXLConfig
        | T5EncoderBnBLLMint8Config
        | T5EncoderT5EncoderConfig
        | TextLLMDiffusersConfig
        | TIFileSD1Config
        | TIFileSD2Config
        | TIFileSDXLConfig
        | TIFolderSD1Config
        | TIFolderSD2Config
        | TIFolderSDXLConfig
        | UnknownConfig
        | Unset
        | VAECheckpointAnimaConfig
        | VAECheckpointFlux2Config
        | VAECheckpointFLUXConfig
        | VAECheckpointQwenImageConfig
        | VAECheckpointSD1Config
        | VAECheckpointSD2Config
        | VAECheckpointSDXLConfig
        | VAEDiffusersFlux2Config
        | VAEDiffusersSD1Config
        | VAEDiffusersSDXLConfig
    ) = UNSET
    inplace: bool | Unset = False
    bytes_: int | Unset = 0
    total_bytes: int | Unset = 0
    source_metadata: BaseMetadata | HuggingFaceMetadata | None | Unset = UNSET
    download_parts: list[DownloadJob] | Unset = UNSET
    error: None | str | Unset = UNSET
    error_traceback: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_metadata import BaseMetadata
        from ..models.clip_embed_diffusers_g_config import CLIPEmbedDiffusersGConfig
        from ..models.clip_embed_diffusers_l_config import CLIPEmbedDiffusersLConfig
        from ..models.clip_vision_diffusers_config import CLIPVisionDiffusersConfig
        from ..models.control_lo_ra_ly_corisflux_config import ControlLoRALyCORISFLUXConfig
        from ..models.control_net_checkpoint_flux_config import ControlNetCheckpointFLUXConfig
        from ..models.control_net_checkpoint_sd1_config import ControlNetCheckpointSD1Config
        from ..models.control_net_checkpoint_sd2_config import ControlNetCheckpointSD2Config
        from ..models.control_net_checkpoint_sdxl_config import ControlNetCheckpointSDXLConfig
        from ..models.control_net_checkpoint_z_image_config import ControlNetCheckpointZImageConfig
        from ..models.control_net_diffusers_flux_config import ControlNetDiffusersFLUXConfig
        from ..models.control_net_diffusers_sd1_config import ControlNetDiffusersSD1Config
        from ..models.control_net_diffusers_sd2_config import ControlNetDiffusersSD2Config
        from ..models.control_net_diffusers_sdxl_config import ControlNetDiffusersSDXLConfig
        from ..models.external_api_model_config import ExternalApiModelConfig
        from ..models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
        from ..models.hf_model_source import HFModelSource
        from ..models.hugging_face_metadata import HuggingFaceMetadata
        from ..models.ip_adapter_checkpoint_flux_config import IPAdapterCheckpointFLUXConfig
        from ..models.ip_adapter_checkpoint_sd1_config import IPAdapterCheckpointSD1Config
        from ..models.ip_adapter_checkpoint_sd2_config import IPAdapterCheckpointSD2Config
        from ..models.ip_adapter_checkpoint_sdxl_config import IPAdapterCheckpointSDXLConfig
        from ..models.ip_adapter_invoke_aisd1_config import IPAdapterInvokeAISD1Config
        from ..models.ip_adapter_invoke_aisd2_config import IPAdapterInvokeAISD2Config
        from ..models.ip_adapter_invoke_aisdxl_config import IPAdapterInvokeAISDXLConfig
        from ..models.llava_onevision_diffusers_config import LlavaOnevisionDiffusersConfig
        from ..models.lo_ra_diffusers_flux_2_config import LoRADiffusersFlux2Config
        from ..models.lo_ra_diffusers_flux_config import LoRADiffusersFLUXConfig
        from ..models.lo_ra_diffusers_sd1_config import LoRADiffusersSD1Config
        from ..models.lo_ra_diffusers_sd2_config import LoRADiffusersSD2Config
        from ..models.lo_ra_diffusers_sdxl_config import LoRADiffusersSDXLConfig
        from ..models.lo_ra_diffusers_z_image_config import LoRADiffusersZImageConfig
        from ..models.lo_ra_ly_coris_anima_config import LoRALyCORISAnimaConfig
        from ..models.lo_ra_ly_coris_flux_2_config import LoRALyCORISFlux2Config
        from ..models.lo_ra_ly_coris_qwen_image_config import LoRALyCORISQwenImageConfig
        from ..models.lo_ra_ly_corisflux_config import LoRALyCORISFLUXConfig
        from ..models.lo_ra_ly_corissd1_config import LoRALyCORISSD1Config
        from ..models.lo_ra_ly_corissd2_config import LoRALyCORISSD2Config
        from ..models.lo_ra_ly_corissdxl_config import LoRALyCORISSDXLConfig
        from ..models.lo_ra_ly_corisz_image_config import LoRALyCORISZImageConfig
        from ..models.lo_raomiflux_config import LoRAOMIFLUXConfig
        from ..models.lo_raomisdxl_config import LoRAOMISDXLConfig
        from ..models.local_model_source import LocalModelSource
        from ..models.main_bn_bnf4flux_config import MainBnBNF4FLUXConfig
        from ..models.main_checkpoint_anima_config import MainCheckpointAnimaConfig
        from ..models.main_checkpoint_flux_2_config import MainCheckpointFlux2Config
        from ..models.main_checkpoint_flux_config import MainCheckpointFLUXConfig
        from ..models.main_checkpoint_sd1_config import MainCheckpointSD1Config
        from ..models.main_checkpoint_sd2_config import MainCheckpointSD2Config
        from ..models.main_checkpoint_sdxl_config import MainCheckpointSDXLConfig
        from ..models.main_checkpoint_sdxl_refiner_config import MainCheckpointSDXLRefinerConfig
        from ..models.main_checkpoint_z_image_config import MainCheckpointZImageConfig
        from ..models.main_diffusers_cog_view_4_config import MainDiffusersCogView4Config
        from ..models.main_diffusers_flux_2_config import MainDiffusersFlux2Config
        from ..models.main_diffusers_flux_config import MainDiffusersFLUXConfig
        from ..models.main_diffusers_qwen_image_config import MainDiffusersQwenImageConfig
        from ..models.main_diffusers_sd1_config import MainDiffusersSD1Config
        from ..models.main_diffusers_sd2_config import MainDiffusersSD2Config
        from ..models.main_diffusers_sd3_config import MainDiffusersSD3Config
        from ..models.main_diffusers_sdxl_config import MainDiffusersSDXLConfig
        from ..models.main_diffusers_sdxl_refiner_config import MainDiffusersSDXLRefinerConfig
        from ..models.main_diffusers_z_image_config import MainDiffusersZImageConfig
        from ..models.main_gguf_flux_2_config import MainGGUFFlux2Config
        from ..models.main_gguf_qwen_image_config import MainGGUFQwenImageConfig
        from ..models.main_ggufflux_config import MainGGUFFLUXConfig
        from ..models.main_ggufz_image_config import MainGGUFZImageConfig
        from ..models.qwen_3_encoder_checkpoint_config import Qwen3EncoderCheckpointConfig
        from ..models.qwen_3_encoder_gguf_config import Qwen3EncoderGGUFConfig
        from ..models.qwen_3_encoder_qwen_3_encoder_config import Qwen3EncoderQwen3EncoderConfig
        from ..models.qwen_vl_encoder_checkpoint_config import QwenVLEncoderCheckpointConfig
        from ..models.qwen_vl_encoder_diffusers_config import QwenVLEncoderDiffusersConfig
        from ..models.sig_lip_diffusers_config import SigLIPDiffusersConfig
        from ..models.spandrel_checkpoint_config import SpandrelCheckpointConfig
        from ..models.t2i_adapter_diffusers_sd1_config import T2IAdapterDiffusersSD1Config
        from ..models.t2i_adapter_diffusers_sdxl_config import T2IAdapterDiffusersSDXLConfig
        from ..models.t5_encoder_bn_bll_mint_8_config import T5EncoderBnBLLMint8Config
        from ..models.t5_encoder_t5_encoder_config import T5EncoderT5EncoderConfig
        from ..models.text_llm_diffusers_config import TextLLMDiffusersConfig
        from ..models.ti_file_sd1_config import TIFileSD1Config
        from ..models.ti_file_sd2_config import TIFileSD2Config
        from ..models.ti_file_sdxl_config import TIFileSDXLConfig
        from ..models.ti_folder_sd1_config import TIFolderSD1Config
        from ..models.ti_folder_sd2_config import TIFolderSD2Config
        from ..models.ti_folder_sdxl_config import TIFolderSDXLConfig
        from ..models.unknown_config import UnknownConfig
        from ..models.url_model_source import URLModelSource
        from ..models.vae_checkpoint_anima_config import VAECheckpointAnimaConfig
        from ..models.vae_checkpoint_flux_2_config import VAECheckpointFlux2Config
        from ..models.vae_checkpoint_flux_config import VAECheckpointFLUXConfig
        from ..models.vae_checkpoint_qwen_image_config import VAECheckpointQwenImageConfig
        from ..models.vae_checkpoint_sd1_config import VAECheckpointSD1Config
        from ..models.vae_checkpoint_sd2_config import VAECheckpointSD2Config
        from ..models.vae_checkpoint_sdxl_config import VAECheckpointSDXLConfig
        from ..models.vae_diffusers_flux_2_config import VAEDiffusersFlux2Config
        from ..models.vae_diffusers_sd1_config import VAEDiffusersSD1Config
        from ..models.vae_diffusers_sdxl_config import VAEDiffusersSDXLConfig

        id = self.id

        source: dict[str, Any]
        if isinstance(self.source, LocalModelSource):
            source = self.source.to_dict()
        elif isinstance(self.source, HFModelSource):
            source = self.source.to_dict()
        elif isinstance(self.source, URLModelSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        local_path = self.local_path

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error_reason: None | str | Unset
        if isinstance(self.error_reason, Unset):
            error_reason = UNSET
        else:
            error_reason = self.error_reason

        config_in: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_in, Unset):
            config_in = self.config_in.to_dict()

        config_out: dict[str, Any] | None | Unset
        if isinstance(self.config_out, Unset):
            config_out = UNSET
        elif isinstance(self.config_out, MainDiffusersSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersSDXLRefinerConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersSD3Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersFlux2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersCogView4Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersQwenImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainDiffusersZImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointSDXLRefinerConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointFlux2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointZImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainCheckpointAnimaConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainBnBNF4FLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainGGUFFlux2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainGGUFFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainGGUFQwenImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, MainGGUFZImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAECheckpointSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAECheckpointSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAECheckpointSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAECheckpointFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAECheckpointFlux2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAECheckpointQwenImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAECheckpointAnimaConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAEDiffusersSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAEDiffusersSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, VAEDiffusersFlux2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetCheckpointSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetCheckpointSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetCheckpointSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetCheckpointFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetCheckpointZImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetDiffusersSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetDiffusersSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetDiffusersSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlNetDiffusersFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISFlux2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISZImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISQwenImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRALyCORISAnimaConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRAOMISDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRAOMIFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRADiffusersSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRADiffusersSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRADiffusersSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRADiffusersFlux2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRADiffusersFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LoRADiffusersZImageConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ControlLoRALyCORISFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, T5EncoderT5EncoderConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, T5EncoderBnBLLMint8Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, Qwen3EncoderQwen3EncoderConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, Qwen3EncoderCheckpointConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, Qwen3EncoderGGUFConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, QwenVLEncoderDiffusersConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, QwenVLEncoderCheckpointConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, TIFileSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, TIFileSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, TIFileSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, TIFolderSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, TIFolderSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, TIFolderSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, IPAdapterInvokeAISD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, IPAdapterInvokeAISD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, IPAdapterInvokeAISDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, IPAdapterCheckpointSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, IPAdapterCheckpointSD2Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, IPAdapterCheckpointSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, IPAdapterCheckpointFLUXConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, T2IAdapterDiffusersSD1Config):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, T2IAdapterDiffusersSDXLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, SpandrelCheckpointConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, CLIPEmbedDiffusersGConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, CLIPEmbedDiffusersLConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, CLIPVisionDiffusersConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, SigLIPDiffusersConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, FLUXReduxCheckpointConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, LlavaOnevisionDiffusersConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, TextLLMDiffusersConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, ExternalApiModelConfig):
            config_out = self.config_out.to_dict()
        elif isinstance(self.config_out, UnknownConfig):
            config_out = self.config_out.to_dict()
        else:
            config_out = self.config_out

        inplace = self.inplace

        bytes_ = self.bytes_

        total_bytes = self.total_bytes

        source_metadata: dict[str, Any] | None | Unset
        if isinstance(self.source_metadata, Unset):
            source_metadata = UNSET
        elif isinstance(self.source_metadata, BaseMetadata):
            source_metadata = self.source_metadata.to_dict()
        elif isinstance(self.source_metadata, HuggingFaceMetadata):
            source_metadata = self.source_metadata.to_dict()
        else:
            source_metadata = self.source_metadata

        download_parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.download_parts, Unset):
            download_parts = []
            for download_parts_item_data in self.download_parts:
                download_parts_item = download_parts_item_data.to_dict()
                download_parts.append(download_parts_item)

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_traceback: None | str | Unset
        if isinstance(self.error_traceback, Unset):
            error_traceback = UNSET
        else:
            error_traceback = self.error_traceback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "local_path": local_path,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if error_reason is not UNSET:
            field_dict["error_reason"] = error_reason
        if config_in is not UNSET:
            field_dict["config_in"] = config_in
        if config_out is not UNSET:
            field_dict["config_out"] = config_out
        if inplace is not UNSET:
            field_dict["inplace"] = inplace
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if total_bytes is not UNSET:
            field_dict["total_bytes"] = total_bytes
        if source_metadata is not UNSET:
            field_dict["source_metadata"] = source_metadata
        if download_parts is not UNSET:
            field_dict["download_parts"] = download_parts
        if error is not UNSET:
            field_dict["error"] = error
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_metadata import BaseMetadata
        from ..models.clip_embed_diffusers_g_config import CLIPEmbedDiffusersGConfig
        from ..models.clip_embed_diffusers_l_config import CLIPEmbedDiffusersLConfig
        from ..models.clip_vision_diffusers_config import CLIPVisionDiffusersConfig
        from ..models.control_lo_ra_ly_corisflux_config import ControlLoRALyCORISFLUXConfig
        from ..models.control_net_checkpoint_flux_config import ControlNetCheckpointFLUXConfig
        from ..models.control_net_checkpoint_sd1_config import ControlNetCheckpointSD1Config
        from ..models.control_net_checkpoint_sd2_config import ControlNetCheckpointSD2Config
        from ..models.control_net_checkpoint_sdxl_config import ControlNetCheckpointSDXLConfig
        from ..models.control_net_checkpoint_z_image_config import ControlNetCheckpointZImageConfig
        from ..models.control_net_diffusers_flux_config import ControlNetDiffusersFLUXConfig
        from ..models.control_net_diffusers_sd1_config import ControlNetDiffusersSD1Config
        from ..models.control_net_diffusers_sd2_config import ControlNetDiffusersSD2Config
        from ..models.control_net_diffusers_sdxl_config import ControlNetDiffusersSDXLConfig
        from ..models.download_job import DownloadJob
        from ..models.external_api_model_config import ExternalApiModelConfig
        from ..models.external_model_source import ExternalModelSource
        from ..models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
        from ..models.hf_model_source import HFModelSource
        from ..models.hugging_face_metadata import HuggingFaceMetadata
        from ..models.ip_adapter_checkpoint_flux_config import IPAdapterCheckpointFLUXConfig
        from ..models.ip_adapter_checkpoint_sd1_config import IPAdapterCheckpointSD1Config
        from ..models.ip_adapter_checkpoint_sd2_config import IPAdapterCheckpointSD2Config
        from ..models.ip_adapter_checkpoint_sdxl_config import IPAdapterCheckpointSDXLConfig
        from ..models.ip_adapter_invoke_aisd1_config import IPAdapterInvokeAISD1Config
        from ..models.ip_adapter_invoke_aisd2_config import IPAdapterInvokeAISD2Config
        from ..models.ip_adapter_invoke_aisdxl_config import IPAdapterInvokeAISDXLConfig
        from ..models.llava_onevision_diffusers_config import LlavaOnevisionDiffusersConfig
        from ..models.lo_ra_diffusers_flux_2_config import LoRADiffusersFlux2Config
        from ..models.lo_ra_diffusers_flux_config import LoRADiffusersFLUXConfig
        from ..models.lo_ra_diffusers_sd1_config import LoRADiffusersSD1Config
        from ..models.lo_ra_diffusers_sd2_config import LoRADiffusersSD2Config
        from ..models.lo_ra_diffusers_sdxl_config import LoRADiffusersSDXLConfig
        from ..models.lo_ra_diffusers_z_image_config import LoRADiffusersZImageConfig
        from ..models.lo_ra_ly_coris_anima_config import LoRALyCORISAnimaConfig
        from ..models.lo_ra_ly_coris_flux_2_config import LoRALyCORISFlux2Config
        from ..models.lo_ra_ly_coris_qwen_image_config import LoRALyCORISQwenImageConfig
        from ..models.lo_ra_ly_corisflux_config import LoRALyCORISFLUXConfig
        from ..models.lo_ra_ly_corissd1_config import LoRALyCORISSD1Config
        from ..models.lo_ra_ly_corissd2_config import LoRALyCORISSD2Config
        from ..models.lo_ra_ly_corissdxl_config import LoRALyCORISSDXLConfig
        from ..models.lo_ra_ly_corisz_image_config import LoRALyCORISZImageConfig
        from ..models.lo_raomiflux_config import LoRAOMIFLUXConfig
        from ..models.lo_raomisdxl_config import LoRAOMISDXLConfig
        from ..models.local_model_source import LocalModelSource
        from ..models.main_bn_bnf4flux_config import MainBnBNF4FLUXConfig
        from ..models.main_checkpoint_anima_config import MainCheckpointAnimaConfig
        from ..models.main_checkpoint_flux_2_config import MainCheckpointFlux2Config
        from ..models.main_checkpoint_flux_config import MainCheckpointFLUXConfig
        from ..models.main_checkpoint_sd1_config import MainCheckpointSD1Config
        from ..models.main_checkpoint_sd2_config import MainCheckpointSD2Config
        from ..models.main_checkpoint_sdxl_config import MainCheckpointSDXLConfig
        from ..models.main_checkpoint_sdxl_refiner_config import MainCheckpointSDXLRefinerConfig
        from ..models.main_checkpoint_z_image_config import MainCheckpointZImageConfig
        from ..models.main_diffusers_cog_view_4_config import MainDiffusersCogView4Config
        from ..models.main_diffusers_flux_2_config import MainDiffusersFlux2Config
        from ..models.main_diffusers_flux_config import MainDiffusersFLUXConfig
        from ..models.main_diffusers_qwen_image_config import MainDiffusersQwenImageConfig
        from ..models.main_diffusers_sd1_config import MainDiffusersSD1Config
        from ..models.main_diffusers_sd2_config import MainDiffusersSD2Config
        from ..models.main_diffusers_sd3_config import MainDiffusersSD3Config
        from ..models.main_diffusers_sdxl_config import MainDiffusersSDXLConfig
        from ..models.main_diffusers_sdxl_refiner_config import MainDiffusersSDXLRefinerConfig
        from ..models.main_diffusers_z_image_config import MainDiffusersZImageConfig
        from ..models.main_gguf_flux_2_config import MainGGUFFlux2Config
        from ..models.main_gguf_qwen_image_config import MainGGUFQwenImageConfig
        from ..models.main_ggufflux_config import MainGGUFFLUXConfig
        from ..models.main_ggufz_image_config import MainGGUFZImageConfig
        from ..models.model_record_changes import ModelRecordChanges
        from ..models.qwen_3_encoder_checkpoint_config import Qwen3EncoderCheckpointConfig
        from ..models.qwen_3_encoder_gguf_config import Qwen3EncoderGGUFConfig
        from ..models.qwen_3_encoder_qwen_3_encoder_config import Qwen3EncoderQwen3EncoderConfig
        from ..models.qwen_vl_encoder_checkpoint_config import QwenVLEncoderCheckpointConfig
        from ..models.qwen_vl_encoder_diffusers_config import QwenVLEncoderDiffusersConfig
        from ..models.sig_lip_diffusers_config import SigLIPDiffusersConfig
        from ..models.spandrel_checkpoint_config import SpandrelCheckpointConfig
        from ..models.t2i_adapter_diffusers_sd1_config import T2IAdapterDiffusersSD1Config
        from ..models.t2i_adapter_diffusers_sdxl_config import T2IAdapterDiffusersSDXLConfig
        from ..models.t5_encoder_bn_bll_mint_8_config import T5EncoderBnBLLMint8Config
        from ..models.t5_encoder_t5_encoder_config import T5EncoderT5EncoderConfig
        from ..models.text_llm_diffusers_config import TextLLMDiffusersConfig
        from ..models.ti_file_sd1_config import TIFileSD1Config
        from ..models.ti_file_sd2_config import TIFileSD2Config
        from ..models.ti_file_sdxl_config import TIFileSDXLConfig
        from ..models.ti_folder_sd1_config import TIFolderSD1Config
        from ..models.ti_folder_sd2_config import TIFolderSD2Config
        from ..models.ti_folder_sdxl_config import TIFolderSDXLConfig
        from ..models.unknown_config import UnknownConfig
        from ..models.url_model_source import URLModelSource
        from ..models.vae_checkpoint_anima_config import VAECheckpointAnimaConfig
        from ..models.vae_checkpoint_flux_2_config import VAECheckpointFlux2Config
        from ..models.vae_checkpoint_flux_config import VAECheckpointFLUXConfig
        from ..models.vae_checkpoint_qwen_image_config import VAECheckpointQwenImageConfig
        from ..models.vae_checkpoint_sd1_config import VAECheckpointSD1Config
        from ..models.vae_checkpoint_sd2_config import VAECheckpointSD2Config
        from ..models.vae_checkpoint_sdxl_config import VAECheckpointSDXLConfig
        from ..models.vae_diffusers_flux_2_config import VAEDiffusersFlux2Config
        from ..models.vae_diffusers_sd1_config import VAEDiffusersSD1Config
        from ..models.vae_diffusers_sdxl_config import VAEDiffusersSDXLConfig

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_source(data: object) -> ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = LocalModelSource.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_1 = HFModelSource.from_dict(data)

                return source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_2 = URLModelSource.from_dict(data)

                return source_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            source_type_3 = ExternalModelSource.from_dict(data)

            return source_type_3

        source = _parse_source(d.pop("source"))

        local_path = d.pop("local_path")

        _status = d.pop("status", UNSET)
        status: InstallStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InstallStatus(_status)

        def _parse_error_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_reason = _parse_error_reason(d.pop("error_reason", UNSET))

        _config_in = d.pop("config_in", UNSET)
        config_in: ModelRecordChanges | Unset
        if isinstance(_config_in, Unset):
            config_in = UNSET
        else:
            config_in = ModelRecordChanges.from_dict(_config_in)

        def _parse_config_out(
            data: object,
        ) -> (
            CLIPEmbedDiffusersGConfig
            | CLIPEmbedDiffusersLConfig
            | CLIPVisionDiffusersConfig
            | ControlLoRALyCORISFLUXConfig
            | ControlNetCheckpointFLUXConfig
            | ControlNetCheckpointSD1Config
            | ControlNetCheckpointSD2Config
            | ControlNetCheckpointSDXLConfig
            | ControlNetCheckpointZImageConfig
            | ControlNetDiffusersFLUXConfig
            | ControlNetDiffusersSD1Config
            | ControlNetDiffusersSD2Config
            | ControlNetDiffusersSDXLConfig
            | ExternalApiModelConfig
            | FLUXReduxCheckpointConfig
            | IPAdapterCheckpointFLUXConfig
            | IPAdapterCheckpointSD1Config
            | IPAdapterCheckpointSD2Config
            | IPAdapterCheckpointSDXLConfig
            | IPAdapterInvokeAISD1Config
            | IPAdapterInvokeAISD2Config
            | IPAdapterInvokeAISDXLConfig
            | LlavaOnevisionDiffusersConfig
            | LoRADiffusersFlux2Config
            | LoRADiffusersFLUXConfig
            | LoRADiffusersSD1Config
            | LoRADiffusersSD2Config
            | LoRADiffusersSDXLConfig
            | LoRADiffusersZImageConfig
            | LoRALyCORISAnimaConfig
            | LoRALyCORISFlux2Config
            | LoRALyCORISFLUXConfig
            | LoRALyCORISQwenImageConfig
            | LoRALyCORISSD1Config
            | LoRALyCORISSD2Config
            | LoRALyCORISSDXLConfig
            | LoRALyCORISZImageConfig
            | LoRAOMIFLUXConfig
            | LoRAOMISDXLConfig
            | MainBnBNF4FLUXConfig
            | MainCheckpointAnimaConfig
            | MainCheckpointFlux2Config
            | MainCheckpointFLUXConfig
            | MainCheckpointSD1Config
            | MainCheckpointSD2Config
            | MainCheckpointSDXLConfig
            | MainCheckpointSDXLRefinerConfig
            | MainCheckpointZImageConfig
            | MainDiffusersCogView4Config
            | MainDiffusersFlux2Config
            | MainDiffusersFLUXConfig
            | MainDiffusersQwenImageConfig
            | MainDiffusersSD1Config
            | MainDiffusersSD2Config
            | MainDiffusersSD3Config
            | MainDiffusersSDXLConfig
            | MainDiffusersSDXLRefinerConfig
            | MainDiffusersZImageConfig
            | MainGGUFFlux2Config
            | MainGGUFFLUXConfig
            | MainGGUFQwenImageConfig
            | MainGGUFZImageConfig
            | None
            | Qwen3EncoderCheckpointConfig
            | Qwen3EncoderGGUFConfig
            | Qwen3EncoderQwen3EncoderConfig
            | QwenVLEncoderCheckpointConfig
            | QwenVLEncoderDiffusersConfig
            | SigLIPDiffusersConfig
            | SpandrelCheckpointConfig
            | T2IAdapterDiffusersSD1Config
            | T2IAdapterDiffusersSDXLConfig
            | T5EncoderBnBLLMint8Config
            | T5EncoderT5EncoderConfig
            | TextLLMDiffusersConfig
            | TIFileSD1Config
            | TIFileSD2Config
            | TIFileSDXLConfig
            | TIFolderSD1Config
            | TIFolderSD2Config
            | TIFolderSDXLConfig
            | UnknownConfig
            | Unset
            | VAECheckpointAnimaConfig
            | VAECheckpointFlux2Config
            | VAECheckpointFLUXConfig
            | VAECheckpointQwenImageConfig
            | VAECheckpointSD1Config
            | VAECheckpointSD2Config
            | VAECheckpointSDXLConfig
            | VAEDiffusersFlux2Config
            | VAEDiffusersSD1Config
            | VAEDiffusersSDXLConfig
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_0 = MainDiffusersSD1Config.from_dict(data)

                return config_out_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_1 = MainDiffusersSD2Config.from_dict(data)

                return config_out_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_2 = MainDiffusersSDXLConfig.from_dict(data)

                return config_out_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_3 = MainDiffusersSDXLRefinerConfig.from_dict(data)

                return config_out_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_4 = MainDiffusersSD3Config.from_dict(data)

                return config_out_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_5 = MainDiffusersFLUXConfig.from_dict(data)

                return config_out_type_0_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_6 = MainDiffusersFlux2Config.from_dict(data)

                return config_out_type_0_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_7 = MainDiffusersCogView4Config.from_dict(data)

                return config_out_type_0_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_8 = MainDiffusersQwenImageConfig.from_dict(data)

                return config_out_type_0_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_9 = MainDiffusersZImageConfig.from_dict(data)

                return config_out_type_0_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_10 = MainCheckpointSD1Config.from_dict(data)

                return config_out_type_0_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_11 = MainCheckpointSD2Config.from_dict(data)

                return config_out_type_0_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_12 = MainCheckpointSDXLConfig.from_dict(data)

                return config_out_type_0_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_13 = MainCheckpointSDXLRefinerConfig.from_dict(data)

                return config_out_type_0_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_14 = MainCheckpointFlux2Config.from_dict(data)

                return config_out_type_0_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_15 = MainCheckpointFLUXConfig.from_dict(data)

                return config_out_type_0_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_16 = MainCheckpointZImageConfig.from_dict(data)

                return config_out_type_0_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_17 = MainCheckpointAnimaConfig.from_dict(data)

                return config_out_type_0_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_18 = MainBnBNF4FLUXConfig.from_dict(data)

                return config_out_type_0_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_19 = MainGGUFFlux2Config.from_dict(data)

                return config_out_type_0_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_20 = MainGGUFFLUXConfig.from_dict(data)

                return config_out_type_0_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_21 = MainGGUFQwenImageConfig.from_dict(data)

                return config_out_type_0_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_22 = MainGGUFZImageConfig.from_dict(data)

                return config_out_type_0_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_23 = VAECheckpointSD1Config.from_dict(data)

                return config_out_type_0_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_24 = VAECheckpointSD2Config.from_dict(data)

                return config_out_type_0_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_25 = VAECheckpointSDXLConfig.from_dict(data)

                return config_out_type_0_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_26 = VAECheckpointFLUXConfig.from_dict(data)

                return config_out_type_0_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_27 = VAECheckpointFlux2Config.from_dict(data)

                return config_out_type_0_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_28 = VAECheckpointQwenImageConfig.from_dict(data)

                return config_out_type_0_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_29 = VAECheckpointAnimaConfig.from_dict(data)

                return config_out_type_0_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_30 = VAEDiffusersSD1Config.from_dict(data)

                return config_out_type_0_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_31 = VAEDiffusersSDXLConfig.from_dict(data)

                return config_out_type_0_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_32 = VAEDiffusersFlux2Config.from_dict(data)

                return config_out_type_0_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_33 = ControlNetCheckpointSD1Config.from_dict(data)

                return config_out_type_0_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_34 = ControlNetCheckpointSD2Config.from_dict(data)

                return config_out_type_0_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_35 = ControlNetCheckpointSDXLConfig.from_dict(data)

                return config_out_type_0_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_36 = ControlNetCheckpointFLUXConfig.from_dict(data)

                return config_out_type_0_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_37 = ControlNetCheckpointZImageConfig.from_dict(data)

                return config_out_type_0_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_38 = ControlNetDiffusersSD1Config.from_dict(data)

                return config_out_type_0_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_39 = ControlNetDiffusersSD2Config.from_dict(data)

                return config_out_type_0_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_40 = ControlNetDiffusersSDXLConfig.from_dict(data)

                return config_out_type_0_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_41 = ControlNetDiffusersFLUXConfig.from_dict(data)

                return config_out_type_0_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_42 = LoRALyCORISSD1Config.from_dict(data)

                return config_out_type_0_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_43 = LoRALyCORISSD2Config.from_dict(data)

                return config_out_type_0_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_44 = LoRALyCORISSDXLConfig.from_dict(data)

                return config_out_type_0_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_45 = LoRALyCORISFlux2Config.from_dict(data)

                return config_out_type_0_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_46 = LoRALyCORISFLUXConfig.from_dict(data)

                return config_out_type_0_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_47 = LoRALyCORISZImageConfig.from_dict(data)

                return config_out_type_0_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_48 = LoRALyCORISQwenImageConfig.from_dict(data)

                return config_out_type_0_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_49 = LoRALyCORISAnimaConfig.from_dict(data)

                return config_out_type_0_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_50 = LoRAOMISDXLConfig.from_dict(data)

                return config_out_type_0_type_50
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_51 = LoRAOMIFLUXConfig.from_dict(data)

                return config_out_type_0_type_51
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_52 = LoRADiffusersSD1Config.from_dict(data)

                return config_out_type_0_type_52
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_53 = LoRADiffusersSD2Config.from_dict(data)

                return config_out_type_0_type_53
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_54 = LoRADiffusersSDXLConfig.from_dict(data)

                return config_out_type_0_type_54
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_55 = LoRADiffusersFlux2Config.from_dict(data)

                return config_out_type_0_type_55
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_56 = LoRADiffusersFLUXConfig.from_dict(data)

                return config_out_type_0_type_56
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_57 = LoRADiffusersZImageConfig.from_dict(data)

                return config_out_type_0_type_57
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_58 = ControlLoRALyCORISFLUXConfig.from_dict(data)

                return config_out_type_0_type_58
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_59 = T5EncoderT5EncoderConfig.from_dict(data)

                return config_out_type_0_type_59
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_60 = T5EncoderBnBLLMint8Config.from_dict(data)

                return config_out_type_0_type_60
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_61 = Qwen3EncoderQwen3EncoderConfig.from_dict(data)

                return config_out_type_0_type_61
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_62 = Qwen3EncoderCheckpointConfig.from_dict(data)

                return config_out_type_0_type_62
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_63 = Qwen3EncoderGGUFConfig.from_dict(data)

                return config_out_type_0_type_63
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_64 = QwenVLEncoderDiffusersConfig.from_dict(data)

                return config_out_type_0_type_64
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_65 = QwenVLEncoderCheckpointConfig.from_dict(data)

                return config_out_type_0_type_65
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_66 = TIFileSD1Config.from_dict(data)

                return config_out_type_0_type_66
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_67 = TIFileSD2Config.from_dict(data)

                return config_out_type_0_type_67
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_68 = TIFileSDXLConfig.from_dict(data)

                return config_out_type_0_type_68
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_69 = TIFolderSD1Config.from_dict(data)

                return config_out_type_0_type_69
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_70 = TIFolderSD2Config.from_dict(data)

                return config_out_type_0_type_70
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_71 = TIFolderSDXLConfig.from_dict(data)

                return config_out_type_0_type_71
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_72 = IPAdapterInvokeAISD1Config.from_dict(data)

                return config_out_type_0_type_72
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_73 = IPAdapterInvokeAISD2Config.from_dict(data)

                return config_out_type_0_type_73
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_74 = IPAdapterInvokeAISDXLConfig.from_dict(data)

                return config_out_type_0_type_74
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_75 = IPAdapterCheckpointSD1Config.from_dict(data)

                return config_out_type_0_type_75
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_76 = IPAdapterCheckpointSD2Config.from_dict(data)

                return config_out_type_0_type_76
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_77 = IPAdapterCheckpointSDXLConfig.from_dict(data)

                return config_out_type_0_type_77
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_78 = IPAdapterCheckpointFLUXConfig.from_dict(data)

                return config_out_type_0_type_78
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_79 = T2IAdapterDiffusersSD1Config.from_dict(data)

                return config_out_type_0_type_79
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_80 = T2IAdapterDiffusersSDXLConfig.from_dict(data)

                return config_out_type_0_type_80
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_81 = SpandrelCheckpointConfig.from_dict(data)

                return config_out_type_0_type_81
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_82 = CLIPEmbedDiffusersGConfig.from_dict(data)

                return config_out_type_0_type_82
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_83 = CLIPEmbedDiffusersLConfig.from_dict(data)

                return config_out_type_0_type_83
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_84 = CLIPVisionDiffusersConfig.from_dict(data)

                return config_out_type_0_type_84
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_85 = SigLIPDiffusersConfig.from_dict(data)

                return config_out_type_0_type_85
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_86 = FLUXReduxCheckpointConfig.from_dict(data)

                return config_out_type_0_type_86
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_87 = LlavaOnevisionDiffusersConfig.from_dict(data)

                return config_out_type_0_type_87
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_88 = TextLLMDiffusersConfig.from_dict(data)

                return config_out_type_0_type_88
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_89 = ExternalApiModelConfig.from_dict(data)

                return config_out_type_0_type_89
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_out_type_0_type_90 = UnknownConfig.from_dict(data)

                return config_out_type_0_type_90
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CLIPEmbedDiffusersGConfig
                | CLIPEmbedDiffusersLConfig
                | CLIPVisionDiffusersConfig
                | ControlLoRALyCORISFLUXConfig
                | ControlNetCheckpointFLUXConfig
                | ControlNetCheckpointSD1Config
                | ControlNetCheckpointSD2Config
                | ControlNetCheckpointSDXLConfig
                | ControlNetCheckpointZImageConfig
                | ControlNetDiffusersFLUXConfig
                | ControlNetDiffusersSD1Config
                | ControlNetDiffusersSD2Config
                | ControlNetDiffusersSDXLConfig
                | ExternalApiModelConfig
                | FLUXReduxCheckpointConfig
                | IPAdapterCheckpointFLUXConfig
                | IPAdapterCheckpointSD1Config
                | IPAdapterCheckpointSD2Config
                | IPAdapterCheckpointSDXLConfig
                | IPAdapterInvokeAISD1Config
                | IPAdapterInvokeAISD2Config
                | IPAdapterInvokeAISDXLConfig
                | LlavaOnevisionDiffusersConfig
                | LoRADiffusersFlux2Config
                | LoRADiffusersFLUXConfig
                | LoRADiffusersSD1Config
                | LoRADiffusersSD2Config
                | LoRADiffusersSDXLConfig
                | LoRADiffusersZImageConfig
                | LoRALyCORISAnimaConfig
                | LoRALyCORISFlux2Config
                | LoRALyCORISFLUXConfig
                | LoRALyCORISQwenImageConfig
                | LoRALyCORISSD1Config
                | LoRALyCORISSD2Config
                | LoRALyCORISSDXLConfig
                | LoRALyCORISZImageConfig
                | LoRAOMIFLUXConfig
                | LoRAOMISDXLConfig
                | MainBnBNF4FLUXConfig
                | MainCheckpointAnimaConfig
                | MainCheckpointFlux2Config
                | MainCheckpointFLUXConfig
                | MainCheckpointSD1Config
                | MainCheckpointSD2Config
                | MainCheckpointSDXLConfig
                | MainCheckpointSDXLRefinerConfig
                | MainCheckpointZImageConfig
                | MainDiffusersCogView4Config
                | MainDiffusersFlux2Config
                | MainDiffusersFLUXConfig
                | MainDiffusersQwenImageConfig
                | MainDiffusersSD1Config
                | MainDiffusersSD2Config
                | MainDiffusersSD3Config
                | MainDiffusersSDXLConfig
                | MainDiffusersSDXLRefinerConfig
                | MainDiffusersZImageConfig
                | MainGGUFFlux2Config
                | MainGGUFFLUXConfig
                | MainGGUFQwenImageConfig
                | MainGGUFZImageConfig
                | None
                | Qwen3EncoderCheckpointConfig
                | Qwen3EncoderGGUFConfig
                | Qwen3EncoderQwen3EncoderConfig
                | QwenVLEncoderCheckpointConfig
                | QwenVLEncoderDiffusersConfig
                | SigLIPDiffusersConfig
                | SpandrelCheckpointConfig
                | T2IAdapterDiffusersSD1Config
                | T2IAdapterDiffusersSDXLConfig
                | T5EncoderBnBLLMint8Config
                | T5EncoderT5EncoderConfig
                | TextLLMDiffusersConfig
                | TIFileSD1Config
                | TIFileSD2Config
                | TIFileSDXLConfig
                | TIFolderSD1Config
                | TIFolderSD2Config
                | TIFolderSDXLConfig
                | UnknownConfig
                | Unset
                | VAECheckpointAnimaConfig
                | VAECheckpointFlux2Config
                | VAECheckpointFLUXConfig
                | VAECheckpointQwenImageConfig
                | VAECheckpointSD1Config
                | VAECheckpointSD2Config
                | VAECheckpointSDXLConfig
                | VAEDiffusersFlux2Config
                | VAEDiffusersSD1Config
                | VAEDiffusersSDXLConfig,
                data,
            )

        config_out = _parse_config_out(d.pop("config_out", UNSET))

        inplace = d.pop("inplace", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        total_bytes = d.pop("total_bytes", UNSET)

        def _parse_source_metadata(data: object) -> BaseMetadata | HuggingFaceMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_metadata_type_0_type_0 = BaseMetadata.from_dict(data)

                return source_metadata_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_metadata_type_0_type_1 = HuggingFaceMetadata.from_dict(data)

                return source_metadata_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseMetadata | HuggingFaceMetadata | None | Unset, data)

        source_metadata = _parse_source_metadata(d.pop("source_metadata", UNSET))

        _download_parts = d.pop("download_parts", UNSET)
        download_parts: list[DownloadJob] | Unset = UNSET
        if _download_parts is not UNSET:
            download_parts = []
            for download_parts_item_data in _download_parts:
                download_parts_item = DownloadJob.from_dict(download_parts_item_data)

                download_parts.append(download_parts_item)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_error_traceback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_traceback = _parse_error_traceback(d.pop("error_traceback", UNSET))

        model_install_job = cls(
            id=id,
            source=source,
            local_path=local_path,
            status=status,
            error_reason=error_reason,
            config_in=config_in,
            config_out=config_out,
            inplace=inplace,
            bytes_=bytes_,
            total_bytes=total_bytes,
            source_metadata=source_metadata,
            download_parts=download_parts,
            error=error,
            error_traceback=error_traceback,
        )

        model_install_job.additional_properties = d
        return model_install_job

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
