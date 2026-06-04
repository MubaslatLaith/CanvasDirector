from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
    from ..models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
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


T = TypeVar("T", bound="ModelsList")


@_attrs_define
class ModelsList:
    """Return list of configs.

    Attributes:
        models (list[CLIPEmbedDiffusersGConfig | CLIPEmbedDiffusersLConfig | CLIPVisionDiffusersConfig |
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
            VAEDiffusersSD1Config | VAEDiffusersSDXLConfig]):
    """

    models: list[
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
    ]
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

        models = []
        for models_item_data in self.models:
            models_item: dict[str, Any]
            if isinstance(models_item_data, MainDiffusersSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersSDXLRefinerConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersSD3Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersFlux2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersCogView4Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersQwenImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainDiffusersZImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointSDXLRefinerConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointFlux2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointZImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainCheckpointAnimaConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainBnBNF4FLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainGGUFFlux2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainGGUFFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainGGUFQwenImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, MainGGUFZImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAECheckpointSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAECheckpointSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAECheckpointSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAECheckpointFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAECheckpointFlux2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAECheckpointQwenImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAECheckpointAnimaConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAEDiffusersSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAEDiffusersSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, VAEDiffusersFlux2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetCheckpointSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetCheckpointSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetCheckpointSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetCheckpointFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetCheckpointZImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetDiffusersSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetDiffusersSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetDiffusersSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlNetDiffusersFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISFlux2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISZImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISQwenImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRALyCORISAnimaConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRAOMISDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRAOMIFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRADiffusersSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRADiffusersSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRADiffusersSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRADiffusersFlux2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRADiffusersFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LoRADiffusersZImageConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ControlLoRALyCORISFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, T5EncoderT5EncoderConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, T5EncoderBnBLLMint8Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, Qwen3EncoderQwen3EncoderConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, Qwen3EncoderCheckpointConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, Qwen3EncoderGGUFConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, QwenVLEncoderDiffusersConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, QwenVLEncoderCheckpointConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, TIFileSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, TIFileSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, TIFileSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, TIFolderSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, TIFolderSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, TIFolderSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, IPAdapterInvokeAISD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, IPAdapterInvokeAISD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, IPAdapterInvokeAISDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, IPAdapterCheckpointSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, IPAdapterCheckpointSD2Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, IPAdapterCheckpointSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, IPAdapterCheckpointFLUXConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, T2IAdapterDiffusersSD1Config):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, T2IAdapterDiffusersSDXLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, SpandrelCheckpointConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, CLIPEmbedDiffusersGConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, CLIPEmbedDiffusersLConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, CLIPVisionDiffusersConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, SigLIPDiffusersConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, FLUXReduxCheckpointConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, LlavaOnevisionDiffusersConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, TextLLMDiffusersConfig):
                models_item = models_item_data.to_dict()
            elif isinstance(models_item_data, ExternalApiModelConfig):
                models_item = models_item_data.to_dict()
            else:
                models_item = models_item_data.to_dict()

            models.append(models_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "models": models,
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
        from ..models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
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
        models = []
        _models = d.pop("models")
        for models_item_data in _models:

            def _parse_models_item(
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
                    models_item_type_0 = MainDiffusersSD1Config.from_dict(data)

                    return models_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_1 = MainDiffusersSD2Config.from_dict(data)

                    return models_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_2 = MainDiffusersSDXLConfig.from_dict(data)

                    return models_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_3 = MainDiffusersSDXLRefinerConfig.from_dict(data)

                    return models_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_4 = MainDiffusersSD3Config.from_dict(data)

                    return models_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_5 = MainDiffusersFLUXConfig.from_dict(data)

                    return models_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_6 = MainDiffusersFlux2Config.from_dict(data)

                    return models_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_7 = MainDiffusersCogView4Config.from_dict(data)

                    return models_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_8 = MainDiffusersQwenImageConfig.from_dict(data)

                    return models_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_9 = MainDiffusersZImageConfig.from_dict(data)

                    return models_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_10 = MainCheckpointSD1Config.from_dict(data)

                    return models_item_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_11 = MainCheckpointSD2Config.from_dict(data)

                    return models_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_12 = MainCheckpointSDXLConfig.from_dict(data)

                    return models_item_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_13 = MainCheckpointSDXLRefinerConfig.from_dict(data)

                    return models_item_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_14 = MainCheckpointFlux2Config.from_dict(data)

                    return models_item_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_15 = MainCheckpointFLUXConfig.from_dict(data)

                    return models_item_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_16 = MainCheckpointZImageConfig.from_dict(data)

                    return models_item_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_17 = MainCheckpointAnimaConfig.from_dict(data)

                    return models_item_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_18 = MainBnBNF4FLUXConfig.from_dict(data)

                    return models_item_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_19 = MainGGUFFlux2Config.from_dict(data)

                    return models_item_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_20 = MainGGUFFLUXConfig.from_dict(data)

                    return models_item_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_21 = MainGGUFQwenImageConfig.from_dict(data)

                    return models_item_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_22 = MainGGUFZImageConfig.from_dict(data)

                    return models_item_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_23 = VAECheckpointSD1Config.from_dict(data)

                    return models_item_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_24 = VAECheckpointSD2Config.from_dict(data)

                    return models_item_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_25 = VAECheckpointSDXLConfig.from_dict(data)

                    return models_item_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_26 = VAECheckpointFLUXConfig.from_dict(data)

                    return models_item_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_27 = VAECheckpointFlux2Config.from_dict(data)

                    return models_item_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_28 = VAECheckpointQwenImageConfig.from_dict(data)

                    return models_item_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_29 = VAECheckpointAnimaConfig.from_dict(data)

                    return models_item_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_30 = VAEDiffusersSD1Config.from_dict(data)

                    return models_item_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_31 = VAEDiffusersSDXLConfig.from_dict(data)

                    return models_item_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_32 = VAEDiffusersFlux2Config.from_dict(data)

                    return models_item_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_33 = ControlNetCheckpointSD1Config.from_dict(data)

                    return models_item_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_34 = ControlNetCheckpointSD2Config.from_dict(data)

                    return models_item_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_35 = ControlNetCheckpointSDXLConfig.from_dict(data)

                    return models_item_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_36 = ControlNetCheckpointFLUXConfig.from_dict(data)

                    return models_item_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_37 = ControlNetCheckpointZImageConfig.from_dict(data)

                    return models_item_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_38 = ControlNetDiffusersSD1Config.from_dict(data)

                    return models_item_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_39 = ControlNetDiffusersSD2Config.from_dict(data)

                    return models_item_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_40 = ControlNetDiffusersSDXLConfig.from_dict(data)

                    return models_item_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_41 = ControlNetDiffusersFLUXConfig.from_dict(data)

                    return models_item_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_42 = LoRALyCORISSD1Config.from_dict(data)

                    return models_item_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_43 = LoRALyCORISSD2Config.from_dict(data)

                    return models_item_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_44 = LoRALyCORISSDXLConfig.from_dict(data)

                    return models_item_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_45 = LoRALyCORISFlux2Config.from_dict(data)

                    return models_item_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_46 = LoRALyCORISFLUXConfig.from_dict(data)

                    return models_item_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_47 = LoRALyCORISZImageConfig.from_dict(data)

                    return models_item_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_48 = LoRALyCORISQwenImageConfig.from_dict(data)

                    return models_item_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_49 = LoRALyCORISAnimaConfig.from_dict(data)

                    return models_item_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_50 = LoRAOMISDXLConfig.from_dict(data)

                    return models_item_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_51 = LoRAOMIFLUXConfig.from_dict(data)

                    return models_item_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_52 = LoRADiffusersSD1Config.from_dict(data)

                    return models_item_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_53 = LoRADiffusersSD2Config.from_dict(data)

                    return models_item_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_54 = LoRADiffusersSDXLConfig.from_dict(data)

                    return models_item_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_55 = LoRADiffusersFlux2Config.from_dict(data)

                    return models_item_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_56 = LoRADiffusersFLUXConfig.from_dict(data)

                    return models_item_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_57 = LoRADiffusersZImageConfig.from_dict(data)

                    return models_item_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_58 = ControlLoRALyCORISFLUXConfig.from_dict(data)

                    return models_item_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_59 = T5EncoderT5EncoderConfig.from_dict(data)

                    return models_item_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_60 = T5EncoderBnBLLMint8Config.from_dict(data)

                    return models_item_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_61 = Qwen3EncoderQwen3EncoderConfig.from_dict(data)

                    return models_item_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_62 = Qwen3EncoderCheckpointConfig.from_dict(data)

                    return models_item_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_63 = Qwen3EncoderGGUFConfig.from_dict(data)

                    return models_item_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_64 = QwenVLEncoderDiffusersConfig.from_dict(data)

                    return models_item_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_65 = QwenVLEncoderCheckpointConfig.from_dict(data)

                    return models_item_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_66 = TIFileSD1Config.from_dict(data)

                    return models_item_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_67 = TIFileSD2Config.from_dict(data)

                    return models_item_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_68 = TIFileSDXLConfig.from_dict(data)

                    return models_item_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_69 = TIFolderSD1Config.from_dict(data)

                    return models_item_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_70 = TIFolderSD2Config.from_dict(data)

                    return models_item_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_71 = TIFolderSDXLConfig.from_dict(data)

                    return models_item_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_72 = IPAdapterInvokeAISD1Config.from_dict(data)

                    return models_item_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_73 = IPAdapterInvokeAISD2Config.from_dict(data)

                    return models_item_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_74 = IPAdapterInvokeAISDXLConfig.from_dict(data)

                    return models_item_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_75 = IPAdapterCheckpointSD1Config.from_dict(data)

                    return models_item_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_76 = IPAdapterCheckpointSD2Config.from_dict(data)

                    return models_item_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_77 = IPAdapterCheckpointSDXLConfig.from_dict(data)

                    return models_item_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_78 = IPAdapterCheckpointFLUXConfig.from_dict(data)

                    return models_item_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_79 = T2IAdapterDiffusersSD1Config.from_dict(data)

                    return models_item_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_80 = T2IAdapterDiffusersSDXLConfig.from_dict(data)

                    return models_item_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_81 = SpandrelCheckpointConfig.from_dict(data)

                    return models_item_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_82 = CLIPEmbedDiffusersGConfig.from_dict(data)

                    return models_item_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_83 = CLIPEmbedDiffusersLConfig.from_dict(data)

                    return models_item_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_84 = CLIPVisionDiffusersConfig.from_dict(data)

                    return models_item_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_85 = SigLIPDiffusersConfig.from_dict(data)

                    return models_item_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_86 = FLUXReduxCheckpointConfig.from_dict(data)

                    return models_item_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_87 = LlavaOnevisionDiffusersConfig.from_dict(data)

                    return models_item_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_88 = TextLLMDiffusersConfig.from_dict(data)

                    return models_item_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    models_item_type_89 = ExternalApiModelConfig.from_dict(data)

                    return models_item_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                models_item_type_90 = UnknownConfig.from_dict(data)

                return models_item_type_90

            models_item = _parse_models_item(models_item_data)

            models.append(models_item)

        models_list = cls(
            models=models,
        )

        models_list.additional_properties = d
        return models_list

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
