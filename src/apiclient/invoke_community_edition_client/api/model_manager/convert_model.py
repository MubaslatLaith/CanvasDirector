from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clip_embed_diffusers_g_config import CLIPEmbedDiffusersGConfig
from ...models.clip_embed_diffusers_l_config import CLIPEmbedDiffusersLConfig
from ...models.clip_vision_diffusers_config import CLIPVisionDiffusersConfig
from ...models.control_lo_ra_ly_corisflux_config import ControlLoRALyCORISFLUXConfig
from ...models.control_net_checkpoint_flux_config import ControlNetCheckpointFLUXConfig
from ...models.control_net_checkpoint_sd1_config import ControlNetCheckpointSD1Config
from ...models.control_net_checkpoint_sd2_config import ControlNetCheckpointSD2Config
from ...models.control_net_checkpoint_sdxl_config import ControlNetCheckpointSDXLConfig
from ...models.control_net_checkpoint_z_image_config import ControlNetCheckpointZImageConfig
from ...models.control_net_diffusers_flux_config import ControlNetDiffusersFLUXConfig
from ...models.control_net_diffusers_sd1_config import ControlNetDiffusersSD1Config
from ...models.control_net_diffusers_sd2_config import ControlNetDiffusersSD2Config
from ...models.control_net_diffusers_sdxl_config import ControlNetDiffusersSDXLConfig
from ...models.external_api_model_config import ExternalApiModelConfig
from ...models.flux_redux_checkpoint_config import FLUXReduxCheckpointConfig
from ...models.http_validation_error import HTTPValidationError
from ...models.ip_adapter_checkpoint_flux_config import IPAdapterCheckpointFLUXConfig
from ...models.ip_adapter_checkpoint_sd1_config import IPAdapterCheckpointSD1Config
from ...models.ip_adapter_checkpoint_sd2_config import IPAdapterCheckpointSD2Config
from ...models.ip_adapter_checkpoint_sdxl_config import IPAdapterCheckpointSDXLConfig
from ...models.ip_adapter_invoke_aisd1_config import IPAdapterInvokeAISD1Config
from ...models.ip_adapter_invoke_aisd2_config import IPAdapterInvokeAISD2Config
from ...models.ip_adapter_invoke_aisdxl_config import IPAdapterInvokeAISDXLConfig
from ...models.llava_onevision_diffusers_config import LlavaOnevisionDiffusersConfig
from ...models.lo_ra_diffusers_flux_2_config import LoRADiffusersFlux2Config
from ...models.lo_ra_diffusers_flux_config import LoRADiffusersFLUXConfig
from ...models.lo_ra_diffusers_sd1_config import LoRADiffusersSD1Config
from ...models.lo_ra_diffusers_sd2_config import LoRADiffusersSD2Config
from ...models.lo_ra_diffusers_sdxl_config import LoRADiffusersSDXLConfig
from ...models.lo_ra_diffusers_z_image_config import LoRADiffusersZImageConfig
from ...models.lo_ra_ly_coris_anima_config import LoRALyCORISAnimaConfig
from ...models.lo_ra_ly_coris_flux_2_config import LoRALyCORISFlux2Config
from ...models.lo_ra_ly_coris_qwen_image_config import LoRALyCORISQwenImageConfig
from ...models.lo_ra_ly_corisflux_config import LoRALyCORISFLUXConfig
from ...models.lo_ra_ly_corissd1_config import LoRALyCORISSD1Config
from ...models.lo_ra_ly_corissd2_config import LoRALyCORISSD2Config
from ...models.lo_ra_ly_corissdxl_config import LoRALyCORISSDXLConfig
from ...models.lo_ra_ly_corisz_image_config import LoRALyCORISZImageConfig
from ...models.lo_raomiflux_config import LoRAOMIFLUXConfig
from ...models.lo_raomisdxl_config import LoRAOMISDXLConfig
from ...models.main_bn_bnf4flux_config import MainBnBNF4FLUXConfig
from ...models.main_checkpoint_anima_config import MainCheckpointAnimaConfig
from ...models.main_checkpoint_flux_2_config import MainCheckpointFlux2Config
from ...models.main_checkpoint_flux_config import MainCheckpointFLUXConfig
from ...models.main_checkpoint_sd1_config import MainCheckpointSD1Config
from ...models.main_checkpoint_sd2_config import MainCheckpointSD2Config
from ...models.main_checkpoint_sdxl_config import MainCheckpointSDXLConfig
from ...models.main_checkpoint_sdxl_refiner_config import MainCheckpointSDXLRefinerConfig
from ...models.main_checkpoint_z_image_config import MainCheckpointZImageConfig
from ...models.main_diffusers_cog_view_4_config import MainDiffusersCogView4Config
from ...models.main_diffusers_flux_2_config import MainDiffusersFlux2Config
from ...models.main_diffusers_flux_config import MainDiffusersFLUXConfig
from ...models.main_diffusers_qwen_image_config import MainDiffusersQwenImageConfig
from ...models.main_diffusers_sd1_config import MainDiffusersSD1Config
from ...models.main_diffusers_sd2_config import MainDiffusersSD2Config
from ...models.main_diffusers_sd3_config import MainDiffusersSD3Config
from ...models.main_diffusers_sdxl_config import MainDiffusersSDXLConfig
from ...models.main_diffusers_sdxl_refiner_config import MainDiffusersSDXLRefinerConfig
from ...models.main_diffusers_z_image_config import MainDiffusersZImageConfig
from ...models.main_gguf_flux_2_config import MainGGUFFlux2Config
from ...models.main_gguf_qwen_image_config import MainGGUFQwenImageConfig
from ...models.main_ggufflux_config import MainGGUFFLUXConfig
from ...models.main_ggufz_image_config import MainGGUFZImageConfig
from ...models.qwen_3_encoder_checkpoint_config import Qwen3EncoderCheckpointConfig
from ...models.qwen_3_encoder_gguf_config import Qwen3EncoderGGUFConfig
from ...models.qwen_3_encoder_qwen_3_encoder_config import Qwen3EncoderQwen3EncoderConfig
from ...models.qwen_vl_encoder_checkpoint_config import QwenVLEncoderCheckpointConfig
from ...models.qwen_vl_encoder_diffusers_config import QwenVLEncoderDiffusersConfig
from ...models.sig_lip_diffusers_config import SigLIPDiffusersConfig
from ...models.spandrel_checkpoint_config import SpandrelCheckpointConfig
from ...models.t2i_adapter_diffusers_sd1_config import T2IAdapterDiffusersSD1Config
from ...models.t2i_adapter_diffusers_sdxl_config import T2IAdapterDiffusersSDXLConfig
from ...models.t5_encoder_bn_bll_mint_8_config import T5EncoderBnBLLMint8Config
from ...models.t5_encoder_t5_encoder_config import T5EncoderT5EncoderConfig
from ...models.text_llm_diffusers_config import TextLLMDiffusersConfig
from ...models.ti_file_sd1_config import TIFileSD1Config
from ...models.ti_file_sd2_config import TIFileSD2Config
from ...models.ti_file_sdxl_config import TIFileSDXLConfig
from ...models.ti_folder_sd1_config import TIFolderSD1Config
from ...models.ti_folder_sd2_config import TIFolderSD2Config
from ...models.ti_folder_sdxl_config import TIFolderSDXLConfig
from ...models.unknown_config import UnknownConfig
from ...models.vae_checkpoint_anima_config import VAECheckpointAnimaConfig
from ...models.vae_checkpoint_flux_2_config import VAECheckpointFlux2Config
from ...models.vae_checkpoint_flux_config import VAECheckpointFLUXConfig
from ...models.vae_checkpoint_qwen_image_config import VAECheckpointQwenImageConfig
from ...models.vae_checkpoint_sd1_config import VAECheckpointSD1Config
from ...models.vae_checkpoint_sd2_config import VAECheckpointSD2Config
from ...models.vae_checkpoint_sdxl_config import VAECheckpointSDXLConfig
from ...models.vae_diffusers_flux_2_config import VAEDiffusersFlux2Config
from ...models.vae_diffusers_sd1_config import VAEDiffusersSD1Config
from ...models.vae_diffusers_sdxl_config import VAEDiffusersSDXLConfig
from ...types import Response


def _get_kwargs(
    key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/models/convert/{key}".format(
            key=quote(str(key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CLIPEmbedDiffusersGConfig
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
    | HTTPValidationError
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
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
                response_200_type_0 = MainDiffusersSD1Config.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = MainDiffusersSD2Config.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = MainDiffusersSDXLConfig.from_dict(data)

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = MainDiffusersSDXLRefinerConfig.from_dict(data)

                return response_200_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = MainDiffusersSD3Config.from_dict(data)

                return response_200_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_5 = MainDiffusersFLUXConfig.from_dict(data)

                return response_200_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_6 = MainDiffusersFlux2Config.from_dict(data)

                return response_200_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_7 = MainDiffusersCogView4Config.from_dict(data)

                return response_200_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_8 = MainDiffusersQwenImageConfig.from_dict(data)

                return response_200_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_9 = MainDiffusersZImageConfig.from_dict(data)

                return response_200_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_10 = MainCheckpointSD1Config.from_dict(data)

                return response_200_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_11 = MainCheckpointSD2Config.from_dict(data)

                return response_200_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_12 = MainCheckpointSDXLConfig.from_dict(data)

                return response_200_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_13 = MainCheckpointSDXLRefinerConfig.from_dict(data)

                return response_200_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_14 = MainCheckpointFlux2Config.from_dict(data)

                return response_200_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_15 = MainCheckpointFLUXConfig.from_dict(data)

                return response_200_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_16 = MainCheckpointZImageConfig.from_dict(data)

                return response_200_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_17 = MainCheckpointAnimaConfig.from_dict(data)

                return response_200_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_18 = MainBnBNF4FLUXConfig.from_dict(data)

                return response_200_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_19 = MainGGUFFlux2Config.from_dict(data)

                return response_200_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_20 = MainGGUFFLUXConfig.from_dict(data)

                return response_200_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_21 = MainGGUFQwenImageConfig.from_dict(data)

                return response_200_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_22 = MainGGUFZImageConfig.from_dict(data)

                return response_200_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_23 = VAECheckpointSD1Config.from_dict(data)

                return response_200_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_24 = VAECheckpointSD2Config.from_dict(data)

                return response_200_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_25 = VAECheckpointSDXLConfig.from_dict(data)

                return response_200_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_26 = VAECheckpointFLUXConfig.from_dict(data)

                return response_200_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_27 = VAECheckpointFlux2Config.from_dict(data)

                return response_200_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_28 = VAECheckpointQwenImageConfig.from_dict(data)

                return response_200_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_29 = VAECheckpointAnimaConfig.from_dict(data)

                return response_200_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_30 = VAEDiffusersSD1Config.from_dict(data)

                return response_200_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_31 = VAEDiffusersSDXLConfig.from_dict(data)

                return response_200_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_32 = VAEDiffusersFlux2Config.from_dict(data)

                return response_200_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_33 = ControlNetCheckpointSD1Config.from_dict(data)

                return response_200_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_34 = ControlNetCheckpointSD2Config.from_dict(data)

                return response_200_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_35 = ControlNetCheckpointSDXLConfig.from_dict(data)

                return response_200_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_36 = ControlNetCheckpointFLUXConfig.from_dict(data)

                return response_200_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_37 = ControlNetCheckpointZImageConfig.from_dict(data)

                return response_200_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_38 = ControlNetDiffusersSD1Config.from_dict(data)

                return response_200_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_39 = ControlNetDiffusersSD2Config.from_dict(data)

                return response_200_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_40 = ControlNetDiffusersSDXLConfig.from_dict(data)

                return response_200_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_41 = ControlNetDiffusersFLUXConfig.from_dict(data)

                return response_200_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_42 = LoRALyCORISSD1Config.from_dict(data)

                return response_200_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_43 = LoRALyCORISSD2Config.from_dict(data)

                return response_200_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_44 = LoRALyCORISSDXLConfig.from_dict(data)

                return response_200_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_45 = LoRALyCORISFlux2Config.from_dict(data)

                return response_200_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_46 = LoRALyCORISFLUXConfig.from_dict(data)

                return response_200_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_47 = LoRALyCORISZImageConfig.from_dict(data)

                return response_200_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_48 = LoRALyCORISQwenImageConfig.from_dict(data)

                return response_200_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_49 = LoRALyCORISAnimaConfig.from_dict(data)

                return response_200_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_50 = LoRAOMISDXLConfig.from_dict(data)

                return response_200_type_50
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_51 = LoRAOMIFLUXConfig.from_dict(data)

                return response_200_type_51
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_52 = LoRADiffusersSD1Config.from_dict(data)

                return response_200_type_52
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_53 = LoRADiffusersSD2Config.from_dict(data)

                return response_200_type_53
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_54 = LoRADiffusersSDXLConfig.from_dict(data)

                return response_200_type_54
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_55 = LoRADiffusersFlux2Config.from_dict(data)

                return response_200_type_55
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_56 = LoRADiffusersFLUXConfig.from_dict(data)

                return response_200_type_56
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_57 = LoRADiffusersZImageConfig.from_dict(data)

                return response_200_type_57
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_58 = ControlLoRALyCORISFLUXConfig.from_dict(data)

                return response_200_type_58
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_59 = T5EncoderT5EncoderConfig.from_dict(data)

                return response_200_type_59
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_60 = T5EncoderBnBLLMint8Config.from_dict(data)

                return response_200_type_60
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_61 = Qwen3EncoderQwen3EncoderConfig.from_dict(data)

                return response_200_type_61
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_62 = Qwen3EncoderCheckpointConfig.from_dict(data)

                return response_200_type_62
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_63 = Qwen3EncoderGGUFConfig.from_dict(data)

                return response_200_type_63
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_64 = QwenVLEncoderDiffusersConfig.from_dict(data)

                return response_200_type_64
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_65 = QwenVLEncoderCheckpointConfig.from_dict(data)

                return response_200_type_65
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_66 = TIFileSD1Config.from_dict(data)

                return response_200_type_66
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_67 = TIFileSD2Config.from_dict(data)

                return response_200_type_67
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_68 = TIFileSDXLConfig.from_dict(data)

                return response_200_type_68
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_69 = TIFolderSD1Config.from_dict(data)

                return response_200_type_69
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_70 = TIFolderSD2Config.from_dict(data)

                return response_200_type_70
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_71 = TIFolderSDXLConfig.from_dict(data)

                return response_200_type_71
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_72 = IPAdapterInvokeAISD1Config.from_dict(data)

                return response_200_type_72
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_73 = IPAdapterInvokeAISD2Config.from_dict(data)

                return response_200_type_73
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_74 = IPAdapterInvokeAISDXLConfig.from_dict(data)

                return response_200_type_74
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_75 = IPAdapterCheckpointSD1Config.from_dict(data)

                return response_200_type_75
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_76 = IPAdapterCheckpointSD2Config.from_dict(data)

                return response_200_type_76
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_77 = IPAdapterCheckpointSDXLConfig.from_dict(data)

                return response_200_type_77
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_78 = IPAdapterCheckpointFLUXConfig.from_dict(data)

                return response_200_type_78
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_79 = T2IAdapterDiffusersSD1Config.from_dict(data)

                return response_200_type_79
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_80 = T2IAdapterDiffusersSDXLConfig.from_dict(data)

                return response_200_type_80
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_81 = SpandrelCheckpointConfig.from_dict(data)

                return response_200_type_81
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_82 = CLIPEmbedDiffusersGConfig.from_dict(data)

                return response_200_type_82
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_83 = CLIPEmbedDiffusersLConfig.from_dict(data)

                return response_200_type_83
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_84 = CLIPVisionDiffusersConfig.from_dict(data)

                return response_200_type_84
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_85 = SigLIPDiffusersConfig.from_dict(data)

                return response_200_type_85
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_86 = FLUXReduxCheckpointConfig.from_dict(data)

                return response_200_type_86
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_87 = LlavaOnevisionDiffusersConfig.from_dict(data)

                return response_200_type_87
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_88 = TextLLMDiffusersConfig.from_dict(data)

                return response_200_type_88
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_89 = ExternalApiModelConfig.from_dict(data)

                return response_200_type_89
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_90 = UnknownConfig.from_dict(data)

            return response_200_type_90

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CLIPEmbedDiffusersGConfig
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
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | CLIPEmbedDiffusersGConfig
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
    | HTTPValidationError
]:
    """Convert Model

     Permanently convert a model into diffusers format, replacing the safetensors version.
    Note that during the conversion process the key and model hash will change.
    The return value is the model configuration for the converted model.

    Args:
        key (str): Unique key of the safetensors main model to convert to diffusers format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIPEmbedDiffusersGConfig | CLIPEmbedDiffusersLConfig | CLIPVisionDiffusersConfig | ControlLoRALyCORISFLUXConfig | ControlNetCheckpointFLUXConfig | ControlNetCheckpointSD1Config | ControlNetCheckpointSD2Config | ControlNetCheckpointSDXLConfig | ControlNetCheckpointZImageConfig | ControlNetDiffusersFLUXConfig | ControlNetDiffusersSD1Config | ControlNetDiffusersSD2Config | ControlNetDiffusersSDXLConfig | ExternalApiModelConfig | FLUXReduxCheckpointConfig | IPAdapterCheckpointFLUXConfig | IPAdapterCheckpointSD1Config | IPAdapterCheckpointSD2Config | IPAdapterCheckpointSDXLConfig | IPAdapterInvokeAISD1Config | IPAdapterInvokeAISD2Config | IPAdapterInvokeAISDXLConfig | LlavaOnevisionDiffusersConfig | LoRADiffusersFlux2Config | LoRADiffusersFLUXConfig | LoRADiffusersSD1Config | LoRADiffusersSD2Config | LoRADiffusersSDXLConfig | LoRADiffusersZImageConfig | LoRALyCORISAnimaConfig | LoRALyCORISFlux2Config | LoRALyCORISFLUXConfig | LoRALyCORISQwenImageConfig | LoRALyCORISSD1Config | LoRALyCORISSD2Config | LoRALyCORISSDXLConfig | LoRALyCORISZImageConfig | LoRAOMIFLUXConfig | LoRAOMISDXLConfig | MainBnBNF4FLUXConfig | MainCheckpointAnimaConfig | MainCheckpointFlux2Config | MainCheckpointFLUXConfig | MainCheckpointSD1Config | MainCheckpointSD2Config | MainCheckpointSDXLConfig | MainCheckpointSDXLRefinerConfig | MainCheckpointZImageConfig | MainDiffusersCogView4Config | MainDiffusersFlux2Config | MainDiffusersFLUXConfig | MainDiffusersQwenImageConfig | MainDiffusersSD1Config | MainDiffusersSD2Config | MainDiffusersSD3Config | MainDiffusersSDXLConfig | MainDiffusersSDXLRefinerConfig | MainDiffusersZImageConfig | MainGGUFFlux2Config | MainGGUFFLUXConfig | MainGGUFQwenImageConfig | MainGGUFZImageConfig | Qwen3EncoderCheckpointConfig | Qwen3EncoderGGUFConfig | Qwen3EncoderQwen3EncoderConfig | QwenVLEncoderCheckpointConfig | QwenVLEncoderDiffusersConfig | SigLIPDiffusersConfig | SpandrelCheckpointConfig | T2IAdapterDiffusersSD1Config | T2IAdapterDiffusersSDXLConfig | T5EncoderBnBLLMint8Config | T5EncoderT5EncoderConfig | TextLLMDiffusersConfig | TIFileSD1Config | TIFileSD2Config | TIFileSDXLConfig | TIFolderSD1Config | TIFolderSD2Config | TIFolderSDXLConfig | UnknownConfig | VAECheckpointAnimaConfig | VAECheckpointFlux2Config | VAECheckpointFLUXConfig | VAECheckpointQwenImageConfig | VAECheckpointSD1Config | VAECheckpointSD2Config | VAECheckpointSDXLConfig | VAEDiffusersFlux2Config | VAEDiffusersSD1Config | VAEDiffusersSDXLConfig | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | CLIPEmbedDiffusersGConfig
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
    | HTTPValidationError
    | None
):
    """Convert Model

     Permanently convert a model into diffusers format, replacing the safetensors version.
    Note that during the conversion process the key and model hash will change.
    The return value is the model configuration for the converted model.

    Args:
        key (str): Unique key of the safetensors main model to convert to diffusers format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIPEmbedDiffusersGConfig | CLIPEmbedDiffusersLConfig | CLIPVisionDiffusersConfig | ControlLoRALyCORISFLUXConfig | ControlNetCheckpointFLUXConfig | ControlNetCheckpointSD1Config | ControlNetCheckpointSD2Config | ControlNetCheckpointSDXLConfig | ControlNetCheckpointZImageConfig | ControlNetDiffusersFLUXConfig | ControlNetDiffusersSD1Config | ControlNetDiffusersSD2Config | ControlNetDiffusersSDXLConfig | ExternalApiModelConfig | FLUXReduxCheckpointConfig | IPAdapterCheckpointFLUXConfig | IPAdapterCheckpointSD1Config | IPAdapterCheckpointSD2Config | IPAdapterCheckpointSDXLConfig | IPAdapterInvokeAISD1Config | IPAdapterInvokeAISD2Config | IPAdapterInvokeAISDXLConfig | LlavaOnevisionDiffusersConfig | LoRADiffusersFlux2Config | LoRADiffusersFLUXConfig | LoRADiffusersSD1Config | LoRADiffusersSD2Config | LoRADiffusersSDXLConfig | LoRADiffusersZImageConfig | LoRALyCORISAnimaConfig | LoRALyCORISFlux2Config | LoRALyCORISFLUXConfig | LoRALyCORISQwenImageConfig | LoRALyCORISSD1Config | LoRALyCORISSD2Config | LoRALyCORISSDXLConfig | LoRALyCORISZImageConfig | LoRAOMIFLUXConfig | LoRAOMISDXLConfig | MainBnBNF4FLUXConfig | MainCheckpointAnimaConfig | MainCheckpointFlux2Config | MainCheckpointFLUXConfig | MainCheckpointSD1Config | MainCheckpointSD2Config | MainCheckpointSDXLConfig | MainCheckpointSDXLRefinerConfig | MainCheckpointZImageConfig | MainDiffusersCogView4Config | MainDiffusersFlux2Config | MainDiffusersFLUXConfig | MainDiffusersQwenImageConfig | MainDiffusersSD1Config | MainDiffusersSD2Config | MainDiffusersSD3Config | MainDiffusersSDXLConfig | MainDiffusersSDXLRefinerConfig | MainDiffusersZImageConfig | MainGGUFFlux2Config | MainGGUFFLUXConfig | MainGGUFQwenImageConfig | MainGGUFZImageConfig | Qwen3EncoderCheckpointConfig | Qwen3EncoderGGUFConfig | Qwen3EncoderQwen3EncoderConfig | QwenVLEncoderCheckpointConfig | QwenVLEncoderDiffusersConfig | SigLIPDiffusersConfig | SpandrelCheckpointConfig | T2IAdapterDiffusersSD1Config | T2IAdapterDiffusersSDXLConfig | T5EncoderBnBLLMint8Config | T5EncoderT5EncoderConfig | TextLLMDiffusersConfig | TIFileSD1Config | TIFileSD2Config | TIFileSDXLConfig | TIFolderSD1Config | TIFolderSD2Config | TIFolderSDXLConfig | UnknownConfig | VAECheckpointAnimaConfig | VAECheckpointFlux2Config | VAECheckpointFLUXConfig | VAECheckpointQwenImageConfig | VAECheckpointSD1Config | VAECheckpointSD2Config | VAECheckpointSDXLConfig | VAEDiffusersFlux2Config | VAEDiffusersSD1Config | VAEDiffusersSDXLConfig | HTTPValidationError
    """

    return sync_detailed(
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | CLIPEmbedDiffusersGConfig
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
    | HTTPValidationError
]:
    """Convert Model

     Permanently convert a model into diffusers format, replacing the safetensors version.
    Note that during the conversion process the key and model hash will change.
    The return value is the model configuration for the converted model.

    Args:
        key (str): Unique key of the safetensors main model to convert to diffusers format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIPEmbedDiffusersGConfig | CLIPEmbedDiffusersLConfig | CLIPVisionDiffusersConfig | ControlLoRALyCORISFLUXConfig | ControlNetCheckpointFLUXConfig | ControlNetCheckpointSD1Config | ControlNetCheckpointSD2Config | ControlNetCheckpointSDXLConfig | ControlNetCheckpointZImageConfig | ControlNetDiffusersFLUXConfig | ControlNetDiffusersSD1Config | ControlNetDiffusersSD2Config | ControlNetDiffusersSDXLConfig | ExternalApiModelConfig | FLUXReduxCheckpointConfig | IPAdapterCheckpointFLUXConfig | IPAdapterCheckpointSD1Config | IPAdapterCheckpointSD2Config | IPAdapterCheckpointSDXLConfig | IPAdapterInvokeAISD1Config | IPAdapterInvokeAISD2Config | IPAdapterInvokeAISDXLConfig | LlavaOnevisionDiffusersConfig | LoRADiffusersFlux2Config | LoRADiffusersFLUXConfig | LoRADiffusersSD1Config | LoRADiffusersSD2Config | LoRADiffusersSDXLConfig | LoRADiffusersZImageConfig | LoRALyCORISAnimaConfig | LoRALyCORISFlux2Config | LoRALyCORISFLUXConfig | LoRALyCORISQwenImageConfig | LoRALyCORISSD1Config | LoRALyCORISSD2Config | LoRALyCORISSDXLConfig | LoRALyCORISZImageConfig | LoRAOMIFLUXConfig | LoRAOMISDXLConfig | MainBnBNF4FLUXConfig | MainCheckpointAnimaConfig | MainCheckpointFlux2Config | MainCheckpointFLUXConfig | MainCheckpointSD1Config | MainCheckpointSD2Config | MainCheckpointSDXLConfig | MainCheckpointSDXLRefinerConfig | MainCheckpointZImageConfig | MainDiffusersCogView4Config | MainDiffusersFlux2Config | MainDiffusersFLUXConfig | MainDiffusersQwenImageConfig | MainDiffusersSD1Config | MainDiffusersSD2Config | MainDiffusersSD3Config | MainDiffusersSDXLConfig | MainDiffusersSDXLRefinerConfig | MainDiffusersZImageConfig | MainGGUFFlux2Config | MainGGUFFLUXConfig | MainGGUFQwenImageConfig | MainGGUFZImageConfig | Qwen3EncoderCheckpointConfig | Qwen3EncoderGGUFConfig | Qwen3EncoderQwen3EncoderConfig | QwenVLEncoderCheckpointConfig | QwenVLEncoderDiffusersConfig | SigLIPDiffusersConfig | SpandrelCheckpointConfig | T2IAdapterDiffusersSD1Config | T2IAdapterDiffusersSDXLConfig | T5EncoderBnBLLMint8Config | T5EncoderT5EncoderConfig | TextLLMDiffusersConfig | TIFileSD1Config | TIFileSD2Config | TIFileSDXLConfig | TIFolderSD1Config | TIFolderSD2Config | TIFolderSDXLConfig | UnknownConfig | VAECheckpointAnimaConfig | VAECheckpointFlux2Config | VAECheckpointFLUXConfig | VAECheckpointQwenImageConfig | VAECheckpointSD1Config | VAECheckpointSD2Config | VAECheckpointSDXLConfig | VAEDiffusersFlux2Config | VAEDiffusersSD1Config | VAEDiffusersSDXLConfig | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | CLIPEmbedDiffusersGConfig
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
    | HTTPValidationError
    | None
):
    """Convert Model

     Permanently convert a model into diffusers format, replacing the safetensors version.
    Note that during the conversion process the key and model hash will change.
    The return value is the model configuration for the converted model.

    Args:
        key (str): Unique key of the safetensors main model to convert to diffusers format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIPEmbedDiffusersGConfig | CLIPEmbedDiffusersLConfig | CLIPVisionDiffusersConfig | ControlLoRALyCORISFLUXConfig | ControlNetCheckpointFLUXConfig | ControlNetCheckpointSD1Config | ControlNetCheckpointSD2Config | ControlNetCheckpointSDXLConfig | ControlNetCheckpointZImageConfig | ControlNetDiffusersFLUXConfig | ControlNetDiffusersSD1Config | ControlNetDiffusersSD2Config | ControlNetDiffusersSDXLConfig | ExternalApiModelConfig | FLUXReduxCheckpointConfig | IPAdapterCheckpointFLUXConfig | IPAdapterCheckpointSD1Config | IPAdapterCheckpointSD2Config | IPAdapterCheckpointSDXLConfig | IPAdapterInvokeAISD1Config | IPAdapterInvokeAISD2Config | IPAdapterInvokeAISDXLConfig | LlavaOnevisionDiffusersConfig | LoRADiffusersFlux2Config | LoRADiffusersFLUXConfig | LoRADiffusersSD1Config | LoRADiffusersSD2Config | LoRADiffusersSDXLConfig | LoRADiffusersZImageConfig | LoRALyCORISAnimaConfig | LoRALyCORISFlux2Config | LoRALyCORISFLUXConfig | LoRALyCORISQwenImageConfig | LoRALyCORISSD1Config | LoRALyCORISSD2Config | LoRALyCORISSDXLConfig | LoRALyCORISZImageConfig | LoRAOMIFLUXConfig | LoRAOMISDXLConfig | MainBnBNF4FLUXConfig | MainCheckpointAnimaConfig | MainCheckpointFlux2Config | MainCheckpointFLUXConfig | MainCheckpointSD1Config | MainCheckpointSD2Config | MainCheckpointSDXLConfig | MainCheckpointSDXLRefinerConfig | MainCheckpointZImageConfig | MainDiffusersCogView4Config | MainDiffusersFlux2Config | MainDiffusersFLUXConfig | MainDiffusersQwenImageConfig | MainDiffusersSD1Config | MainDiffusersSD2Config | MainDiffusersSD3Config | MainDiffusersSDXLConfig | MainDiffusersSDXLRefinerConfig | MainDiffusersZImageConfig | MainGGUFFlux2Config | MainGGUFFLUXConfig | MainGGUFQwenImageConfig | MainGGUFZImageConfig | Qwen3EncoderCheckpointConfig | Qwen3EncoderGGUFConfig | Qwen3EncoderQwen3EncoderConfig | QwenVLEncoderCheckpointConfig | QwenVLEncoderDiffusersConfig | SigLIPDiffusersConfig | SpandrelCheckpointConfig | T2IAdapterDiffusersSD1Config | T2IAdapterDiffusersSDXLConfig | T5EncoderBnBLLMint8Config | T5EncoderT5EncoderConfig | TextLLMDiffusersConfig | TIFileSD1Config | TIFileSD2Config | TIFileSDXLConfig | TIFolderSD1Config | TIFolderSD2Config | TIFolderSDXLConfig | UnknownConfig | VAECheckpointAnimaConfig | VAECheckpointFlux2Config | VAECheckpointFLUXConfig | VAECheckpointQwenImageConfig | VAECheckpointSD1Config | VAECheckpointSD2Config | VAECheckpointSDXLConfig | VAEDiffusersFlux2Config | VAEDiffusersSD1Config | VAEDiffusersSDXLConfig | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
        )
    ).parsed
