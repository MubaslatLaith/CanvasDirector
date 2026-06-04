from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
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
    from ..models.external_model_source import ExternalModelSource
    from ..models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
    from ..models.hf_model_source import HFModelSource
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


T = TypeVar("T", bound="ModelInstallCompleteEvent")


@_attrs_define
class ModelInstallCompleteEvent:
    """Event model for model_install_complete

    Attributes:
        timestamp (int): The timestamp of the event
        id (int): The ID of the install job
        source (ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource): Source of the model; local
            path, repo_id or url
        key (str): Model config record key
        total_bytes (int | None): Size of the model (may be None for installation of a local path)
        config (CLIPEmbedDiffusersGConfig | CLIPEmbedDiffusersLConfig | CLIPVisionDiffusersConfig |
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
            MainGGUFQwenImageConfig | MainGGUFZImageConfig | Qwen3EncoderCheckpointConfig | Qwen3EncoderGGUFConfig |
            Qwen3EncoderQwen3EncoderConfig | QwenVLEncoderCheckpointConfig | QwenVLEncoderDiffusersConfig |
            SigLIPDiffusersConfig | SpandrelCheckpointConfig | T2IAdapterDiffusersSD1Config | T2IAdapterDiffusersSDXLConfig
            | T5EncoderBnBLLMint8Config | T5EncoderT5EncoderConfig | TextLLMDiffusersConfig | TIFileSD1Config |
            TIFileSD2Config | TIFileSDXLConfig | TIFolderSD1Config | TIFolderSD2Config | TIFolderSDXLConfig | UnknownConfig
            | VAECheckpointAnimaConfig | VAECheckpointFlux2Config | VAECheckpointFLUXConfig | VAECheckpointQwenImageConfig |
            VAECheckpointSD1Config | VAECheckpointSD2Config | VAECheckpointSDXLConfig | VAEDiffusersFlux2Config |
            VAEDiffusersSD1Config | VAEDiffusersSDXLConfig): The installed model's config
    """

    timestamp: int
    id: int
    source: ExternalModelSource | HFModelSource | LocalModelSource | URLModelSource
    key: str
    total_bytes: int | None
    config: (
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
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        timestamp = self.timestamp

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

        key = self.key

        total_bytes: int | None
        total_bytes = self.total_bytes

        config: dict[str, Any]
        if isinstance(self.config, MainDiffusersSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersSDXLRefinerConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersSD3Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersFlux2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersCogView4Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersQwenImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainDiffusersZImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointSDXLRefinerConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointFlux2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointZImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainCheckpointAnimaConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainBnBNF4FLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainGGUFFlux2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, MainGGUFFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainGGUFQwenImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, MainGGUFZImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, VAECheckpointSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, VAECheckpointSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, VAECheckpointSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, VAECheckpointFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, VAECheckpointFlux2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, VAECheckpointQwenImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, VAECheckpointAnimaConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, VAEDiffusersSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, VAEDiffusersSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, VAEDiffusersFlux2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetCheckpointSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetCheckpointSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetCheckpointSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetCheckpointFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetCheckpointZImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetDiffusersSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetDiffusersSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetDiffusersSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlNetDiffusersFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISFlux2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISZImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISQwenImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRALyCORISAnimaConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRAOMISDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRAOMIFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRADiffusersSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRADiffusersSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRADiffusersSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRADiffusersFlux2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRADiffusersFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LoRADiffusersZImageConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, ControlLoRALyCORISFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, T5EncoderT5EncoderConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, T5EncoderBnBLLMint8Config):
            config = self.config.to_dict()
        elif isinstance(self.config, Qwen3EncoderQwen3EncoderConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, Qwen3EncoderCheckpointConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, Qwen3EncoderGGUFConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, QwenVLEncoderDiffusersConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, QwenVLEncoderCheckpointConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, TIFileSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, TIFileSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, TIFileSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, TIFolderSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, TIFolderSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, TIFolderSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, IPAdapterInvokeAISD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, IPAdapterInvokeAISD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, IPAdapterInvokeAISDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, IPAdapterCheckpointSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, IPAdapterCheckpointSD2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, IPAdapterCheckpointSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, IPAdapterCheckpointFLUXConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, T2IAdapterDiffusersSD1Config):
            config = self.config.to_dict()
        elif isinstance(self.config, T2IAdapterDiffusersSDXLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, SpandrelCheckpointConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, CLIPEmbedDiffusersGConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, CLIPEmbedDiffusersLConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, CLIPVisionDiffusersConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, SigLIPDiffusersConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, FLUXReduxCheckpointConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, LlavaOnevisionDiffusersConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, TextLLMDiffusersConfig):
            config = self.config.to_dict()
        elif isinstance(self.config, ExternalApiModelConfig):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "id": id,
                "source": source,
                "key": key,
                "total_bytes": total_bytes,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
        from ..models.external_model_source import ExternalModelSource
        from ..models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
        from ..models.hf_model_source import HFModelSource
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

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

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

        key = d.pop("key")

        def _parse_total_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_bytes = _parse_total_bytes(d.pop("total_bytes"))

        def _parse_config(
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = MainDiffusersSD1Config.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = MainDiffusersSD2Config.from_dict(data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_2 = MainDiffusersSDXLConfig.from_dict(data)

                return config_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_3 = MainDiffusersSDXLRefinerConfig.from_dict(data)

                return config_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_4 = MainDiffusersSD3Config.from_dict(data)

                return config_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_5 = MainDiffusersFLUXConfig.from_dict(data)

                return config_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_6 = MainDiffusersFlux2Config.from_dict(data)

                return config_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_7 = MainDiffusersCogView4Config.from_dict(data)

                return config_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_8 = MainDiffusersQwenImageConfig.from_dict(data)

                return config_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_9 = MainDiffusersZImageConfig.from_dict(data)

                return config_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_10 = MainCheckpointSD1Config.from_dict(data)

                return config_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_11 = MainCheckpointSD2Config.from_dict(data)

                return config_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_12 = MainCheckpointSDXLConfig.from_dict(data)

                return config_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_13 = MainCheckpointSDXLRefinerConfig.from_dict(data)

                return config_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_14 = MainCheckpointFlux2Config.from_dict(data)

                return config_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_15 = MainCheckpointFLUXConfig.from_dict(data)

                return config_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_16 = MainCheckpointZImageConfig.from_dict(data)

                return config_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_17 = MainCheckpointAnimaConfig.from_dict(data)

                return config_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_18 = MainBnBNF4FLUXConfig.from_dict(data)

                return config_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_19 = MainGGUFFlux2Config.from_dict(data)

                return config_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_20 = MainGGUFFLUXConfig.from_dict(data)

                return config_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_21 = MainGGUFQwenImageConfig.from_dict(data)

                return config_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_22 = MainGGUFZImageConfig.from_dict(data)

                return config_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_23 = VAECheckpointSD1Config.from_dict(data)

                return config_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_24 = VAECheckpointSD2Config.from_dict(data)

                return config_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_25 = VAECheckpointSDXLConfig.from_dict(data)

                return config_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_26 = VAECheckpointFLUXConfig.from_dict(data)

                return config_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_27 = VAECheckpointFlux2Config.from_dict(data)

                return config_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_28 = VAECheckpointQwenImageConfig.from_dict(data)

                return config_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_29 = VAECheckpointAnimaConfig.from_dict(data)

                return config_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_30 = VAEDiffusersSD1Config.from_dict(data)

                return config_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_31 = VAEDiffusersSDXLConfig.from_dict(data)

                return config_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_32 = VAEDiffusersFlux2Config.from_dict(data)

                return config_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_33 = ControlNetCheckpointSD1Config.from_dict(data)

                return config_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_34 = ControlNetCheckpointSD2Config.from_dict(data)

                return config_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_35 = ControlNetCheckpointSDXLConfig.from_dict(data)

                return config_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_36 = ControlNetCheckpointFLUXConfig.from_dict(data)

                return config_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_37 = ControlNetCheckpointZImageConfig.from_dict(data)

                return config_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_38 = ControlNetDiffusersSD1Config.from_dict(data)

                return config_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_39 = ControlNetDiffusersSD2Config.from_dict(data)

                return config_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_40 = ControlNetDiffusersSDXLConfig.from_dict(data)

                return config_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_41 = ControlNetDiffusersFLUXConfig.from_dict(data)

                return config_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_42 = LoRALyCORISSD1Config.from_dict(data)

                return config_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_43 = LoRALyCORISSD2Config.from_dict(data)

                return config_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_44 = LoRALyCORISSDXLConfig.from_dict(data)

                return config_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_45 = LoRALyCORISFlux2Config.from_dict(data)

                return config_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_46 = LoRALyCORISFLUXConfig.from_dict(data)

                return config_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_47 = LoRALyCORISZImageConfig.from_dict(data)

                return config_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_48 = LoRALyCORISQwenImageConfig.from_dict(data)

                return config_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_49 = LoRALyCORISAnimaConfig.from_dict(data)

                return config_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_50 = LoRAOMISDXLConfig.from_dict(data)

                return config_type_50
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_51 = LoRAOMIFLUXConfig.from_dict(data)

                return config_type_51
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_52 = LoRADiffusersSD1Config.from_dict(data)

                return config_type_52
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_53 = LoRADiffusersSD2Config.from_dict(data)

                return config_type_53
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_54 = LoRADiffusersSDXLConfig.from_dict(data)

                return config_type_54
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_55 = LoRADiffusersFlux2Config.from_dict(data)

                return config_type_55
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_56 = LoRADiffusersFLUXConfig.from_dict(data)

                return config_type_56
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_57 = LoRADiffusersZImageConfig.from_dict(data)

                return config_type_57
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_58 = ControlLoRALyCORISFLUXConfig.from_dict(data)

                return config_type_58
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_59 = T5EncoderT5EncoderConfig.from_dict(data)

                return config_type_59
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_60 = T5EncoderBnBLLMint8Config.from_dict(data)

                return config_type_60
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_61 = Qwen3EncoderQwen3EncoderConfig.from_dict(data)

                return config_type_61
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_62 = Qwen3EncoderCheckpointConfig.from_dict(data)

                return config_type_62
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_63 = Qwen3EncoderGGUFConfig.from_dict(data)

                return config_type_63
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_64 = QwenVLEncoderDiffusersConfig.from_dict(data)

                return config_type_64
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_65 = QwenVLEncoderCheckpointConfig.from_dict(data)

                return config_type_65
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_66 = TIFileSD1Config.from_dict(data)

                return config_type_66
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_67 = TIFileSD2Config.from_dict(data)

                return config_type_67
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_68 = TIFileSDXLConfig.from_dict(data)

                return config_type_68
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_69 = TIFolderSD1Config.from_dict(data)

                return config_type_69
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_70 = TIFolderSD2Config.from_dict(data)

                return config_type_70
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_71 = TIFolderSDXLConfig.from_dict(data)

                return config_type_71
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_72 = IPAdapterInvokeAISD1Config.from_dict(data)

                return config_type_72
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_73 = IPAdapterInvokeAISD2Config.from_dict(data)

                return config_type_73
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_74 = IPAdapterInvokeAISDXLConfig.from_dict(data)

                return config_type_74
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_75 = IPAdapterCheckpointSD1Config.from_dict(data)

                return config_type_75
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_76 = IPAdapterCheckpointSD2Config.from_dict(data)

                return config_type_76
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_77 = IPAdapterCheckpointSDXLConfig.from_dict(data)

                return config_type_77
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_78 = IPAdapterCheckpointFLUXConfig.from_dict(data)

                return config_type_78
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_79 = T2IAdapterDiffusersSD1Config.from_dict(data)

                return config_type_79
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_80 = T2IAdapterDiffusersSDXLConfig.from_dict(data)

                return config_type_80
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_81 = SpandrelCheckpointConfig.from_dict(data)

                return config_type_81
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_82 = CLIPEmbedDiffusersGConfig.from_dict(data)

                return config_type_82
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_83 = CLIPEmbedDiffusersLConfig.from_dict(data)

                return config_type_83
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_84 = CLIPVisionDiffusersConfig.from_dict(data)

                return config_type_84
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_85 = SigLIPDiffusersConfig.from_dict(data)

                return config_type_85
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_86 = FLUXReduxCheckpointConfig.from_dict(data)

                return config_type_86
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_87 = LlavaOnevisionDiffusersConfig.from_dict(data)

                return config_type_87
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_88 = TextLLMDiffusersConfig.from_dict(data)

                return config_type_88
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_89 = ExternalApiModelConfig.from_dict(data)

                return config_type_89
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type_90 = UnknownConfig.from_dict(data)

            return config_type_90

        config = _parse_config(d.pop("config"))

        model_install_complete_event = cls(
            timestamp=timestamp,
            id=id,
            source=source,
            key=key,
            total_bytes=total_bytes,
            config=config,
        )

        model_install_complete_event.additional_properties = d
        return model_install_complete_event

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
