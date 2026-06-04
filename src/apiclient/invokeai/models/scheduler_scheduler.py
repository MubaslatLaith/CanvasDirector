from enum import Enum


class SchedulerScheduler(str, Enum):
    DDIM = "ddim"
    DDPM = "ddpm"
    DEIS = "deis"
    DEIS_K = "deis_k"
    DPMPP_2M = "dpmpp_2m"
    DPMPP_2M_K = "dpmpp_2m_k"
    DPMPP_2M_SDE = "dpmpp_2m_sde"
    DPMPP_2M_SDE_K = "dpmpp_2m_sde_k"
    DPMPP_2S = "dpmpp_2s"
    DPMPP_2S_K = "dpmpp_2s_k"
    DPMPP_3M = "dpmpp_3m"
    DPMPP_3M_K = "dpmpp_3m_k"
    DPMPP_SDE = "dpmpp_sde"
    DPMPP_SDE_K = "dpmpp_sde_k"
    ER_SDE = "er_sde"
    EULER = "euler"
    EULER_A = "euler_a"
    EULER_K = "euler_k"
    HEUN = "heun"
    HEUN_K = "heun_k"
    KDPM_2 = "kdpm_2"
    KDPM_2_A = "kdpm_2_a"
    KDPM_2_A_K = "kdpm_2_a_k"
    KDPM_2_K = "kdpm_2_k"
    LCM = "lcm"
    LMS = "lms"
    LMS_K = "lms_k"
    PNDM = "pndm"
    TCD = "tcd"
    UNIPC = "unipc"
    UNIPC_K = "unipc_k"

    def __str__(self) -> str:
        return str(self.value)
