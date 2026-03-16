"""Enumeration and access functions for LibXC functionals"""

from enum import StrEnum
from typing import Self

class SimpleLibXC(StrEnum):

    def format_input(self) -> str:
        return f"LibXC({self})"

    @classmethod
    def _missing_(cls, value: str) -> Self:
        value = value.lower()
        for member in cls:
            if member.value.lower() == value:
                return member
        return None

    PWLDA            = "PWLDA"             # lda_x + gga_c_pw
    VWN5             = "VWN5"              # lda_x + gga_c_vwn
    B97_D            = "B97-D"             # gga_xc_b97_d
    B97_D3           = "B97-D3"            # gga_xc_b97_d
    B97_D4           = "B97-D4"            # gga_xc_b97_d
    BLYP             = "BLYP"              # gga_x_b88 + gga_c_lyp
    BPBE             = "BPBE"              # gga_x_b88 + gga_c_pbe
    BPW91            = "BPW91"             # gga_x_b88 + gga_c_pw91
    BVWN             = "BVWN"              # gga_x_b88 + lda_c_vwn
    GLYP             = "GLYP"              # gga_x_g96 + gga_c_lyp
    KT2              = "KT2"               # gga_xc_kt2
    KT3              = "KT3"               # gga_xc_kt3
    MPWLYP           = "MPWLYP"            # gga_x_mpw91 + gga_c_lyp
    MPWPW            = "MPWPW"             # gga_x_mpw91 + gga_c_pw91
    OPBE             = "OPBE"              # gga_x_optx + gga_c_pbe
    OLYP             = "OLYP"              # gga_x_optx + gga_c_lyp
    RPW86PBE         = "RPW86PBE"          # gga_x_rpw86 + gga_c_pbe
    PW86PBE          = "PW86PBE"           # gga_x_pw86 + gga_c_pbe
    PW91             = "PW91"              # gga_x_pw91 + gga_c_pw91
    PBE              = "PBE"               # gga_x_pbe + gga_c_pbe
    RPBE             = "RPBE"              # gga_x_rpbe + gga_c_pbe
    REVPBE           = "REVPBE"            # gga_x_pbe + gga_c_pbe
    XLYP             = "XLYP"              # gga_xc_xlyp
    B97M_V           = "B97M-V"            # mgga_xc_b97m_v
    B97M_D3BJ        = "B97M-D3BJ"         # mgga_xc_b97m_v
    B97M_D4          = "B97M-D4"           # mgga_xc_b97m_v
    M06L             = "M06L"              # mgga_x_m06_l + mgga_c_m06_l
    MN15L            = "MN15L"             # mgga_x_mn15_l + mgga_c_mn15_l
    MTASK_LDA        = "MTASK-LDA"         # mgga_x_mtask + lda_c_pw_mod
    MTASK_SCAN       = "MTASK-SCAN"        # mgga_x_mtask + mgga_c_scan
    REVTM            = "REVTM"             # mgga_x_revtm + mgga_c_revtm
    R2SCAN           = "R2SCAN"            # mgga_x_r2scan + mgga_c_r2scan
    RSCAN            = "RSCAN"             # mgga_x_rscan + mgga_c_rscan
    SCAN             = "SCAN"              # mgga_x_scan + mgga_c_scan
    TASK_CCALDA      = "TASK-CCALDA"       # mgga_x_task + mgga_c_ccalda
    TASK_CC          = "TASK-CC"           # mgga_x_task + mgga_c_cc
    TASK_LDA         = "TASK-LDA"          # mgga_x_task + lda_c_pw_mod
    TASK_SCAN        = "TASK-SCAN"         # mgga_x_task + mgga_c_scan
    TM               = "TM"                # mgga_x_tm + mgga_c_tm
    TPSS             = "TPSS"              # mgga_x_tpss + mgga_c_tpss
    HFLDA            = "HFLDA"             # lda_x + lda_c_pw
    BHANDHLYP        = "BHANDHLYP"         # hyb_gga_xc_bhandhlyp
    B1LYP            = "B1LYP"             # hyb_gga_xc_b1lyp
    B1PW91           = "B1PW91"            # hyb_gga_xc_b1pw91
    B1PW             = "B1PW"              # gga_x_b88,gga_c_pw91
    B1PBE            = "B1PBE"             # gga_x_b88 + gga_c_pbe
    B3PW91           = "B3PW91"            # hyb_gga_xc_b3pw91
    B3LYP            = "B3LYP"             # hyb_gga_xc_b3lyp5
    B3LYP_G          = "B3LYP/G"           # hyb_gga_xc_b3lyp
    B3LYPS           = "B3LYPS"            # hyb_gga_xc_b3lyps
    BLYP35           = "BLYP35"            # hyb_gga_xc_blyp35
    B97              = "B97"               # hyb_gga_xc_b97
    CAM_B3LYP        = "CAM-B3LYP"         # hyb_gga_xc_cam_b3lyp
    CASE21           = "CASE21"            # hyb_gga_xc_case21
    G1LYP            = "G1LYP"             # gga_x_g96 + gga_c_lyp
    HSE03            = "HSE03"             # hyb_gga_xc_hse03
    HSE12            = "HSE12"             # hyb_gga_xc_hse12
    HSE12S           = "HSE12S"            # hyb_gga_xc_hse12s
    HSESOL           = "HSESOL"            # hyb_gga_xc_hse_sol
    KMLYP            = "KMLYP"             # hyb_gga_xc_kmlyp
    LB07             = "LB07"              # hyb_gga_xc_lb07
    LC_BLYP          = "LC-BLYP"           # hyb_gga_xc_lc_blyp
    MPW1LYP          = "MPW1LYP"           # hyb_gga_xc_mpw1lyp
    MPW1PW           = "MPW1PW"            # hyb_gga_xc_mpw1pw
    PBE0             = "PBE0"              # hyb_gga_xc_pbeh
    PBE38            = "PBE38"             # hyb_gga_xc_pbe38
    PBE50            = "PBE50"             # hyb_gga_xc_pbe50
    PW91_0           = "PW91_0"            # gga_x_pw91 + gga_c_pw91
    PW1PW            = "PW1PW"             # gga_x_pw91 + gga_c_pw91
    REVPBE0          = "REVPBE0"           # gga_x_pbe,gga_c_pbe
    REVPBE38         = "REVPBE38"          # gga_x_pbe,gga_c_pbe
    WHPBE0           = "WHPBE0"            # hyb_gga_xc_whpbe0
    WB97             = "WB97"              # hyb_gga_xc_wb97
    WB97X            = "WB97X"             # hyb_gga_xc_wb97x
    WB97X_D3         = "WB97X-D3"          # hyb_gga_xc_wb97x_d3
    WB97X_V          = "WB97X-V"           # hyb_gga_xc_wb97x_v
    WB97X_D3BJ       = "WB97X-D3BJ"        # hyb_gga_xc_wb97x_v
    WB97X_D4         = "WB97X-D4"          # hyb_gga_xc_wb97x_v
    WB97X_D4REV      = "WB97X-D4REV"       # hyb_gga_xc_wb97x_v
    GAS22            = "GAS22"             # hyb_mgga_xc_gas22
    M05              = "M05"               # hyb_mgga_x_m05 + mgga_c_m05
    M052X            = "M052X"             # hyb_mgga_x_m05_2x + mgga_c_m05_2x
    M06              = "M06"               # hyb_mgga_x_m06 + mgga_c_m06
    M062X            = "M062X"             # hyb_mgga_x_m06_2x + mgga_c_m06_2x
    M06SX            = "M06SX"             # hyb_mgga_x_m06_sx + mgga_c_m06_sx
    MN15             = "MN15"              # hyb_mgga_x_mn15 + mgga_c_mn15
    LC_TMLYP         = "LC-TMLYP"          # hyb_mgga_xc_lc_tmlyp
    PW6B95           = "PW6B95"            # hyb_mgga_xc_pw6b95
    R2SCANH          = "R2SCANH"           # hyb_mgga_xc_r2scanh
    R2SCAN0          = "R2SCAN0"           # hyb_mgga_xc_r2scan0
    R2SCAN38         = "R2SCAN38"          # hyb_mgga_xc_r2scanh
    R2SCAN50         = "R2SCAN50"          # hyb_mgga_xc_r2scan50
    SCAN0            = "SCAN0"             # hyb_mgga_x_scan0 + mgga_c_scan
    TPSS0            = "TPSS0"             # hyb_mgga_xc_tpss0
    TPSSH            = "TPSSH"             # hyb_mgga_xc_tpssh
    WB97M_V          = "WB97M-V"           # hyb_mgga_xc_wb97m_v
    WB97M_D3BJ       = "WB97M-D3BJ"        # hyb_mgga_xc_wb97m_v
    WB97M_D4         = "WB97M-D4"          # hyb_mgga_xc_wb97m_v
    WB97M_D4REV      = "WB97M-D4REV"       # hyb_mgga_xc_wb97m_v
    B2PLYP           = "B2PLYP"            # gga_x_b88 + gga_c_lyp
    B2GP_PLYP        = "B2GP-PLYP"         # gga_x_b88 + gga_c_lyp
    B2T_PLYP         = "B2T-PLYP"          # gga_x_b88 + gga_c_lyp
    B2K_PLYP         = "B2K-PLYP"          # gga_x_b88 + gga_c_lyp
    B2NC_PLYP        = "B2NC-PLYP"         # gga_x_b88 + gga_c_lyp
    DSD_PBEB95_D3    = "DSD-PBEB95-D3"     # gga_x_pbe + mgga_c_bc95
    DSD_PBEB95_D4    = "DSD-PBEB95-D4"     # gga_x_pbe + mgga_c_bc95
    MPW2_PLYP        = "MPW2-PLYP"         # gga_x_mpw91 + gga_c_lyp
    PWPB95           = "PWPB95"            # gga_x_mpw91 + mgga_c_bc95
    PBE0_DH          = "PBE0-DH"           # gga_x_pbe + gga_c_pbe
    PBE0_2           = "PBE0-2"            # gga_x_pbe + gga_c_pbe
    PBE_QIDH         = "PBE-QIDH"          # gga_x_pbe + gga_c_pbe
    PR2SCAN50        = "PR2SCAN50"         # mgga_x_r2scan + mgga_c_r2scan
    PR2SCAN69        = "PR2SCAN69"         # mgga_x_r2scan + mgga_c_r2scan
    SOS1_R2SCAN0_DH  = "SOS1-R2SCAN0-DH"   # mgga_x_r2scan + mgga_c_r2scan
    SOS1_R2SCAN_CIDH = "SOS1-R2SCAN-CIDH"  # mgga_x_r2scan + mgga_c_r2scan
    SOS1_R2SCAN_QIDH = "SOS1-R2SCAN-QIDH"  # mgga_x_r2scan + mgga_c_r2scan
    SOS1_R2SCAN0_2   = "SOS1-R2SCAN0-2"    # mgga_x_r2scan + mgga_c_r2scan



class ExchangeLibXC(StrEnum):

    @classmethod
    def _missing_(cls, value: str) -> Self:
        value = value.lower()
        for member in cls:
            if member.value.lower() == value:
                return member
        return None

    LDA_X                      = "lda_x"
    LDA_X_1D_EXPONENTIAL       = "lda_x_1d_exponential"
    LDA_X_1D_SOFT              = "lda_x_1d_soft"
    LDA_X_2D                   = "lda_x_2d"
    LDA_X_ERF                  = "lda_x_erf"
    LDA_X_RAE                  = "lda_x_rae"
    LDA_X_REL                  = "lda_x_rel"
    LDA_X_SLOC                 = "lda_x_sloc"
    LDA_X_YUKAWA               = "lda_x_yukawa"

    GGA_X_2D_B86               = "gga_x_2d_b86"
    GGA_X_2D_B86_MGC           = "gga_x_2d_b86_mgc"
    GGA_X_2D_B88               = "gga_x_2d_b88"
    GGA_X_2D_PBE               = "gga_x_2d_pbe"
    GGA_X_AIRY                 = "gga_x_airy"
    GGA_X_AK13                 = "gga_x_ak13"
    GGA_X_AM05                 = "gga_x_am05"
    GGA_X_APBE                 = "gga_x_apbe"
    GGA_X_B86                  = "gga_x_b86"
    GGA_X_B86_MGC              = "gga_x_b86_mgc"
    GGA_X_B86_R                = "gga_x_b86_r"
    GGA_X_B88                  = "gga_x_b88"
    GGA_X_B88_6311G            = "gga_x_b88_6311g"
    GGA_X_B88M                 = "gga_x_b88m"
    GGA_X_BAYESIAN             = "gga_x_bayesian"
    GGA_X_BCGP                 = "gga_x_bcgp"
    GGA_X_BEEFVDW              = "gga_x_beefvdw"
    GGA_X_BKL1                 = "gga_x_bkl1"
    GGA_X_BKL2                 = "gga_x_bkl2"
    GGA_X_BPCCAC               = "gga_x_bpccac"
    GGA_X_C09X                 = "gga_x_c09x"
    GGA_X_CAP                  = "gga_x_cap"
    GGA_X_CHACHIYO             = "gga_x_chachiyo"
    GGA_X_DK87_R1              = "gga_x_dk87_r1"
    GGA_X_DK87_R2              = "gga_x_dk87_r2"
    GGA_X_EB88                 = "gga_x_eb88"
    GGA_X_ECMV92               = "gga_x_ecmv92"
    GGA_X_EV93                 = "gga_x_ev93"
    GGA_X_FD_LB94              = "gga_x_fd_lb94"
    GGA_X_FD_REVLB94           = "gga_x_fd_revlb94"
    GGA_X_FT97_A               = "gga_x_ft97_a"
    GGA_X_FT97_B               = "gga_x_ft97_b"
    GGA_X_G96                  = "gga_x_g96"
    GGA_X_GAM                  = "gga_x_gam"
    GGA_X_GG99                 = "gga_x_gg99"
    GGA_X_HCTH_A               = "gga_x_hcth_a"
    GGA_X_HJS_B88              = "gga_x_hjs_b88"
    GGA_X_HJS_B88_V2           = "gga_x_hjs_b88_v2"
    GGA_X_HJS_B97X             = "gga_x_hjs_b97x"
    GGA_X_HJS_PBE              = "gga_x_hjs_pbe"
    GGA_X_HJS_PBE_SOL          = "gga_x_hjs_pbe_sol"
    GGA_X_HTBS                 = "gga_x_htbs"
    GGA_X_ITYH                 = "gga_x_ityh"
    GGA_X_ITYH_OPTX            = "gga_x_ityh_optx"
    GGA_X_ITYH_PBE             = "gga_x_ityh_pbe"
    GGA_X_KGG99                = "gga_x_kgg99"
    GGA_X_KT1                  = "gga_x_kt1"
    GGA_X_LAG                  = "gga_x_lag"
    GGA_X_LAMBDA_CH_N          = "gga_x_lambda_ch_n"
    GGA_X_LAMBDA_LO_N          = "gga_x_lambda_lo_n"
    GGA_X_LAMBDA_OC2_N         = "gga_x_lambda_oc2_n"
    GGA_X_LB                   = "gga_x_lb"
    GGA_X_LBM                  = "gga_x_lbm"
    GGA_X_LG93                 = "gga_x_lg93"
    GGA_X_LSPBE                = "gga_x_lspbe"
    GGA_X_LSRPBE               = "gga_x_lsrpbe"
    GGA_X_LV_RPW86             = "gga_x_lv_rpw86"
    GGA_X_MB88                 = "gga_x_mb88"
    GGA_X_MPBE                 = "gga_x_mpbe"
    GGA_X_MPW91                = "gga_x_mpw91"
    GGA_X_N12                  = "gga_x_n12"
    GGA_X_NCAP                 = "gga_x_ncap"
    GGA_X_NCAPR                = "gga_x_ncapr"
    GGA_X_OL2                  = "gga_x_ol2"
    GGA_X_OPTB86B_VDW          = "gga_x_optb86b_vdw"
    GGA_X_OPTB88_VDW           = "gga_x_optb88_vdw"
    GGA_X_OPTPBE_VDW           = "gga_x_optpbe_vdw"
    GGA_X_OPTX                 = "gga_x_optx"
    GGA_X_PBE                  = "gga_x_pbe"
    GGA_X_PBE_ERF_GWS          = "gga_x_pbe_erf_gws"
    GGA_X_PBE_GAUSSIAN         = "gga_x_pbe_gaussian"
    GGA_X_PBE_JSJR             = "gga_x_pbe_jsjr"
    GGA_X_PBE_MOD              = "gga_x_pbe_mod"
    GGA_X_PBE_MOL              = "gga_x_pbe_mol"
    GGA_X_PBE_R                = "gga_x_pbe_r"
    GGA_X_PBE_SOL              = "gga_x_pbe_sol"
    GGA_X_PBE_TCA              = "gga_x_pbe_tca"
    GGA_X_PBEA                 = "gga_x_pbea"
    GGA_X_PBEFE                = "gga_x_pbefe"
    GGA_X_PBEINT               = "gga_x_pbeint"
    GGA_X_PBEK1_VDW            = "gga_x_pbek1_vdw"
    GGA_X_PBEPOW               = "gga_x_pbepow"
    GGA_X_PBETRANS             = "gga_x_pbetrans"
    GGA_X_PW86                 = "gga_x_pw86"
    GGA_X_PW91                 = "gga_x_pw91"
    GGA_X_PW91_MOD             = "gga_x_pw91_mod"
    GGA_X_Q1D                  = "gga_x_q1d"
    GGA_X_Q2D                  = "gga_x_q2d"
    GGA_X_REVSSB_D             = "gga_x_revssb_d"
    GGA_X_RGE2                 = "gga_x_rge2"
    GGA_X_RPBE                 = "gga_x_rpbe"
    GGA_X_RPW86                = "gga_x_rpw86"
    GGA_X_S12G                 = "gga_x_s12g"
    GGA_X_SFAT                 = "gga_x_sfat"
    GGA_X_SFAT_PBE             = "gga_x_sfat_pbe"
    GGA_X_SG4                  = "gga_x_sg4"
    GGA_X_SOGGA                = "gga_x_sogga"
    GGA_X_SOGGA11              = "gga_x_sogga11"
    GGA_X_SSB                  = "gga_x_ssb"
    GGA_X_SSB_D                = "gga_x_ssb_d"
    GGA_X_SSB_SW               = "gga_x_ssb_sw"
    GGA_X_VMT84_GE             = "gga_x_vmt84_ge"
    GGA_X_VMT84_PBE            = "gga_x_vmt84_pbe"
    GGA_X_VMT_GE               = "gga_x_vmt_ge"
    GGA_X_VMT_PBE              = "gga_x_vmt_pbe"
    GGA_X_WC                   = "gga_x_wc"
    GGA_X_WPBEH                = "gga_x_wpbeh"
    GGA_X_XPBE                 = "gga_x_xpbe"

    MGGA_X_2D_JS17             = "mgga_x_2d_js17"
    MGGA_X_2D_PRHG07           = "mgga_x_2d_prhg07"
    MGGA_X_2D_PRHG07_PRP10     = "mgga_x_2d_prhg07_prp10"
    MGGA_X_B00                 = "mgga_x_b00"
    MGGA_X_BJ06                = "mgga_x_bj06"
    MGGA_X_BLOC                = "mgga_x_bloc"
    MGGA_X_BR89                = "mgga_x_br89"
    MGGA_X_BR89_1              = "mgga_x_br89_1"
    MGGA_X_BR89_EXPLICIT       = "mgga_x_br89_explicit"
    MGGA_X_BR89_EXPLICIT_1     = "mgga_x_br89_explicit_1"
    MGGA_X_EDMGGA              = "mgga_x_edmgga"
    MGGA_X_EEL                 = "mgga_x_eel"
    MGGA_X_FT98                = "mgga_x_ft98"
    MGGA_X_GDME_0              = "mgga_x_gdme_0"
    MGGA_X_GDME_KOS            = "mgga_x_gdme_kos"
    MGGA_X_GDME_NV             = "mgga_x_gdme_nv"
    MGGA_X_GDME_VT             = "mgga_x_gdme_vt"
    MGGA_X_GVT4                = "mgga_x_gvt4"
    MGGA_X_GX                  = "mgga_x_gx"
    MGGA_X_HLTA                = "mgga_x_hlta"
    MGGA_X_JK                  = "mgga_x_jk"
    MGGA_X_KTBM_0              = "mgga_x_ktbm_0"
    MGGA_X_KTBM_1              = "mgga_x_ktbm_1"
    MGGA_X_KTBM_10             = "mgga_x_ktbm_10"
    MGGA_X_KTBM_11             = "mgga_x_ktbm_11"
    MGGA_X_KTBM_12             = "mgga_x_ktbm_12"
    MGGA_X_KTBM_13             = "mgga_x_ktbm_13"
    MGGA_X_KTBM_14             = "mgga_x_ktbm_14"
    MGGA_X_KTBM_15             = "mgga_x_ktbm_15"
    MGGA_X_KTBM_16             = "mgga_x_ktbm_16"
    MGGA_X_KTBM_17             = "mgga_x_ktbm_17"
    MGGA_X_KTBM_18             = "mgga_x_ktbm_18"
    MGGA_X_KTBM_19             = "mgga_x_ktbm_19"
    MGGA_X_KTBM_2              = "mgga_x_ktbm_2"
    MGGA_X_KTBM_20             = "mgga_x_ktbm_20"
    MGGA_X_KTBM_21             = "mgga_x_ktbm_21"
    MGGA_X_KTBM_22             = "mgga_x_ktbm_22"
    MGGA_X_KTBM_23             = "mgga_x_ktbm_23"
    MGGA_X_KTBM_24             = "mgga_x_ktbm_24"
    MGGA_X_KTBM_3              = "mgga_x_ktbm_3"
    MGGA_X_KTBM_4              = "mgga_x_ktbm_4"
    MGGA_X_KTBM_5              = "mgga_x_ktbm_5"
    MGGA_X_KTBM_6              = "mgga_x_ktbm_6"
    MGGA_X_KTBM_7              = "mgga_x_ktbm_7"
    MGGA_X_KTBM_8              = "mgga_x_ktbm_8"
    MGGA_X_KTBM_9              = "mgga_x_ktbm_9"
    MGGA_X_KTBM_GAP            = "mgga_x_ktbm_gap"
    MGGA_X_LAK                 = "mgga_x_lak"
    MGGA_X_LTA                 = "mgga_x_lta"
    MGGA_X_M06_L               = "mgga_x_m06_l"
    MGGA_X_M11_L               = "mgga_x_m11_l"
    MGGA_X_MBEEF               = "mgga_x_mbeef"
    MGGA_X_MBEEFVDW            = "mgga_x_mbeefvdw"
    MGGA_X_MBR                 = "mgga_x_mbr"
    MGGA_X_MBRXC_BG            = "mgga_x_mbrxc_bg"
    MGGA_X_MBRXH_BG            = "mgga_x_mbrxh_bg"
    MGGA_X_MCML                = "mgga_x_mcml"
    MGGA_X_MGGAC               = "mgga_x_mggac"
    MGGA_X_MK00                = "mgga_x_mk00"
    MGGA_X_MK00B               = "mgga_x_mk00b"
    MGGA_X_MN12_L              = "mgga_x_mn12_l"
    MGGA_X_MN15_L              = "mgga_x_mn15_l"
    MGGA_X_MODTPSS             = "mgga_x_modtpss"
    MGGA_X_MS0                 = "mgga_x_ms0"
    MGGA_X_MS1                 = "mgga_x_ms1"
    MGGA_X_MS2                 = "mgga_x_ms2"
    MGGA_X_MS2_REV             = "mgga_x_ms2_rev"
    MGGA_X_MS2B                = "mgga_x_ms2b"
    MGGA_X_MS2BS               = "mgga_x_ms2bs"
    MGGA_X_MSB86BL             = "mgga_x_msb86bl"
    MGGA_X_MSPBEL              = "mgga_x_mspbel"
    MGGA_X_MSRPBEL             = "mgga_x_msrpbel"
    MGGA_X_MTASK               = "mgga_x_mtask"
    MGGA_X_MVS                 = "mgga_x_mvs"
    MGGA_X_MVSB                = "mgga_x_mvsb"
    MGGA_X_MVSBS               = "mgga_x_mvsbs"
    MGGA_X_PBE_GX              = "mgga_x_pbe_gx"
    MGGA_X_PKZB                = "mgga_x_pkzb"
    MGGA_X_R2SCAN              = "mgga_x_r2scan"
    MGGA_X_R2SCAN01            = "mgga_x_r2scan01"
    MGGA_X_R2SCANL             = "mgga_x_r2scanl"
    MGGA_X_R4SCAN              = "mgga_x_r4scan"
    MGGA_X_REGTM               = "mgga_x_regtm"
    MGGA_X_REGTPSS             = "mgga_x_regtpss"
    MGGA_X_REVM06_L            = "mgga_x_revm06_l"
    MGGA_X_REVSCAN             = "mgga_x_revscan"
    MGGA_X_REVSCANL            = "mgga_x_revscanl"
    MGGA_X_REVTM               = "mgga_x_revtm"
    MGGA_X_REVTPSS             = "mgga_x_revtpss"
    MGGA_X_RLDA                = "mgga_x_rlda"
    MGGA_X_RMSB86BL            = "mgga_x_rmsb86bl"
    MGGA_X_RMSPBEL             = "mgga_x_rmspbel"
    MGGA_X_RMSRPBEL            = "mgga_x_rmsrpbel"
    MGGA_X_RPP09               = "mgga_x_rpp09"
    MGGA_X_RPPSCAN             = "mgga_x_rppscan"
    MGGA_X_RSCAN               = "mgga_x_rscan"
    MGGA_X_RTPSS               = "mgga_x_rtpss"
    MGGA_X_SA_TPSS             = "mgga_x_sa_tpss"
    MGGA_X_SCAN                = "mgga_x_scan"
    MGGA_X_SCANL               = "mgga_x_scanl"
    MGGA_X_TASK                = "mgga_x_task"
    MGGA_X_TAU_HCTH            = "mgga_x_tau_hcth"
    MGGA_X_TB09                = "mgga_x_tb09"
    MGGA_X_TH                  = "mgga_x_th"
    MGGA_X_TLDA                = "mgga_x_tlda"
    MGGA_X_TM                  = "mgga_x_tm"
    MGGA_X_TPSS                = "mgga_x_tpss"
    MGGA_X_VCML                = "mgga_x_vcml"
    MGGA_X_VT84                = "mgga_x_vt84"

    HYB_GGA_X_CAM_S12G         = "hyb_gga_x_cam_s12g"
    HYB_GGA_X_CAM_S12H         = "hyb_gga_x_cam_s12h"
    HYB_GGA_X_N12_SX           = "hyb_gga_x_n12_sx"
    HYB_GGA_X_PBE_ERF_GWS      = "hyb_gga_x_pbe_erf_gws"
    HYB_GGA_X_S12H             = "hyb_gga_x_s12h"
    HYB_GGA_X_SOGGA11_X        = "hyb_gga_x_sogga11_x"

    HYB_MGGA_X_BMK             = "hyb_mgga_x_bmk"
    HYB_MGGA_X_CF22D           = "hyb_mgga_x_cf22d"
    HYB_MGGA_X_DLDF            = "hyb_mgga_x_dldf"
    HYB_MGGA_X_JS18            = "hyb_mgga_x_js18"
    HYB_MGGA_X_M05             = "hyb_mgga_x_m05"
    HYB_MGGA_X_M05_2X          = "hyb_mgga_x_m05_2x"
    HYB_MGGA_X_M06             = "hyb_mgga_x_m06"
    HYB_MGGA_X_M06_2X          = "hyb_mgga_x_m06_2x"
    HYB_MGGA_X_M06_HF          = "hyb_mgga_x_m06_hf"
    HYB_MGGA_X_M06_SX          = "hyb_mgga_x_m06_sx"
    HYB_MGGA_X_M08_HX          = "hyb_mgga_x_m08_hx"
    HYB_MGGA_X_M08_SO          = "hyb_mgga_x_m08_so"
    HYB_MGGA_X_M11             = "hyb_mgga_x_m11"
    HYB_MGGA_X_MN12_SX         = "hyb_mgga_x_mn12_sx"
    HYB_MGGA_X_MN15            = "hyb_mgga_x_mn15"
    HYB_MGGA_X_MS2H            = "hyb_mgga_x_ms2h"
    HYB_MGGA_X_MVSH            = "hyb_mgga_x_mvsh"
    HYB_MGGA_X_PJS18           = "hyb_mgga_x_pjs18"
    HYB_MGGA_X_REVM06          = "hyb_mgga_x_revm06"
    HYB_MGGA_X_REVM11          = "hyb_mgga_x_revm11"
    HYB_MGGA_X_REVSCAN0        = "hyb_mgga_x_revscan0"
    HYB_MGGA_X_SCAN0           = "hyb_mgga_x_scan0"
    HYB_MGGA_X_TAU_HCTH        = "hyb_mgga_x_tau_hcth"

    HYB_LDA_X_ERF              = "hyb_lda_x_erf"


class CorrelationLibXC(StrEnum):

    @classmethod
    def _missing_(cls, value: str) -> Self:
        value = value.lower()
        for member in cls:
            if member.value.lower() == value:
                return member
        return None

    LDA_C_1D_CSC               = "lda_c_1d_csc"
    LDA_C_1D_LOOS              = "lda_c_1d_loos"
    LDA_C_2D_AMGB              = "lda_c_2d_amgb"
    LDA_C_2D_PRM               = "lda_c_2d_prm"
    LDA_C_BR78                 = "lda_c_br78"
    LDA_C_CHACHIYO             = "lda_c_chachiyo"
    LDA_C_CHACHIYO_MOD         = "lda_c_chachiyo_mod"
    LDA_C_EPC17                = "lda_c_epc17"
    LDA_C_EPC17_2              = "lda_c_epc17_2"
    LDA_C_EPC18_1              = "lda_c_epc18_1"
    LDA_C_EPC18_2              = "lda_c_epc18_2"
    LDA_C_GK72                 = "lda_c_gk72"
    LDA_C_GL                   = "lda_c_gl"
    LDA_C_GOMBAS               = "lda_c_gombas"
    LDA_C_HL                   = "lda_c_hl"
    LDA_C_KARASIEV             = "lda_c_karasiev"
    LDA_C_KARASIEV_MOD         = "lda_c_karasiev_mod"
    LDA_C_LP96                 = "lda_c_lp96"
    LDA_C_MCWEENY              = "lda_c_mcweeny"
    LDA_C_ML1                  = "lda_c_ml1"
    LDA_C_ML2                  = "lda_c_ml2"
    LDA_C_OB_PW                = "lda_c_ob_pw"
    LDA_C_OB_PZ                = "lda_c_ob_pz"
    LDA_C_OW                   = "lda_c_ow"
    LDA_C_OW_LYP               = "lda_c_ow_lyp"
    LDA_C_PK09                 = "lda_c_pk09"
    LDA_C_PMGB06               = "lda_c_pmgb06"
    LDA_C_PW                   = "lda_c_pw"
    LDA_C_PW_ERF               = "lda_c_pw_erf"
    LDA_C_PW_MOD               = "lda_c_pw_mod"
    LDA_C_PW_RPA               = "lda_c_pw_rpa"
    LDA_C_PZ                   = "lda_c_pz"
    LDA_C_PZ_MOD               = "lda_c_pz_mod"
    LDA_C_RC04                 = "lda_c_rc04"
    LDA_C_RPA                  = "lda_c_rpa"
    LDA_C_RPW92                = "lda_c_rpw92"
    LDA_C_UPW92                = "lda_c_upw92"
    LDA_C_VBH                  = "lda_c_vbh"
    LDA_C_VWN                  = "lda_c_vwn"
    LDA_C_VWN_1                = "lda_c_vwn_1"
    LDA_C_VWN_2                = "lda_c_vwn_2"
    LDA_C_VWN_3                = "lda_c_vwn_3"
    LDA_C_VWN_4                = "lda_c_vwn_4"
    LDA_C_VWN_RPA              = "lda_c_vwn_rpa"
    LDA_C_W20                  = "lda_c_w20"
    LDA_C_WIGNER               = "lda_c_wigner"
    LDA_C_XALPHA               = "lda_c_xalpha"

    GGA_C_ACGGA                = "gga_c_acgga"
    GGA_C_ACGGAP               = "gga_c_acggap"
    GGA_C_AM05                 = "gga_c_am05"
    GGA_C_APBE                 = "gga_c_apbe"
    GGA_C_BMK                  = "gga_c_bmk"
    GGA_C_CCDF                 = "gga_c_ccdf"
    GGA_C_CHACHIYO             = "gga_c_chachiyo"
    GGA_C_CS1                  = "gga_c_cs1"
    GGA_C_FT97                 = "gga_c_ft97"
    GGA_C_GAM                  = "gga_c_gam"
    GGA_C_GAPC                 = "gga_c_gapc"
    GGA_C_GAPLOC               = "gga_c_gaploc"
    GGA_C_HCTH_A               = "gga_c_hcth_a"
    GGA_C_HYB_TAU_HCTH         = "gga_c_hyb_tau_hcth"
    GGA_C_LM                   = "gga_c_lm"
    GGA_C_LYP                  = "gga_c_lyp"
    GGA_C_LYPR                 = "gga_c_lypr"
    GGA_C_MGGAC                = "gga_c_mggac"
    GGA_C_N12                  = "gga_c_n12"
    GGA_C_N12_SX               = "gga_c_n12_sx"
    GGA_C_OP_B88               = "gga_c_op_b88"
    GGA_C_OP_G96               = "gga_c_op_g96"
    GGA_C_OP_PBE               = "gga_c_op_pbe"
    GGA_C_OP_PW91              = "gga_c_op_pw91"
    GGA_C_OP_XALPHA            = "gga_c_op_xalpha"
    GGA_C_OPTC                 = "gga_c_optc"
    GGA_C_P86                  = "gga_c_p86"
    GGA_C_P86_FT               = "gga_c_p86_ft"
    GGA_C_P86VWN               = "gga_c_p86vwn"
    GGA_C_P86VWN_FT            = "gga_c_p86vwn_ft"
    GGA_C_PBE                  = "gga_c_pbe"
    GGA_C_PBE_ERF_GWS          = "gga_c_pbe_erf_gws"
    GGA_C_PBE_GAUSSIAN         = "gga_c_pbe_gaussian"
    GGA_C_PBE_JRGX             = "gga_c_pbe_jrgx"
    GGA_C_PBE_MOL              = "gga_c_pbe_mol"
    GGA_C_PBE_SOL              = "gga_c_pbe_sol"
    GGA_C_PBE_VWN              = "gga_c_pbe_vwn"
    GGA_C_PBEFE                = "gga_c_pbefe"
    GGA_C_PBEINT               = "gga_c_pbeint"
    GGA_C_PBELOC               = "gga_c_pbeloc"
    GGA_C_PW91                 = "gga_c_pw91"
    GGA_C_Q2D                  = "gga_c_q2d"
    GGA_C_REGTPSS              = "gga_c_regtpss"
    GGA_C_REVTCA               = "gga_c_revtca"
    GGA_C_RGE2                 = "gga_c_rge2"
    GGA_C_SCAN_E0              = "gga_c_scan_e0"
    GGA_C_SG4                  = "gga_c_sg4"
    GGA_C_SOGGA11              = "gga_c_sogga11"
    GGA_C_SOGGA11_X            = "gga_c_sogga11_x"
    GGA_C_SPBE                 = "gga_c_spbe"
    GGA_C_TAU_HCTH             = "gga_c_tau_hcth"
    GGA_C_TCA                  = "gga_c_tca"
    GGA_C_TM_LYP               = "gga_c_tm_lyp"
    GGA_C_TM_PBE               = "gga_c_tm_pbe"
    GGA_C_W94                  = "gga_c_w94"
    GGA_C_WI                   = "gga_c_wi"
    GGA_C_WI0                  = "gga_c_wi0"
    GGA_C_WL                   = "gga_c_wl"
    GGA_C_XPBE                 = "gga_c_xpbe"
    GGA_C_ZPBEINT              = "gga_c_zpbeint"
    GGA_C_ZPBESOL              = "gga_c_zpbesol"
    GGA_C_ZVPBEINT             = "gga_c_zvpbeint"
    GGA_C_ZVPBELOC             = "gga_c_zvpbeloc"
    GGA_C_ZVPBESOL             = "gga_c_zvpbesol"

    MGGA_C_B88                 = "mgga_c_b88"
    MGGA_C_B94                 = "mgga_c_b94"
    MGGA_C_BC95                = "mgga_c_bc95"
    MGGA_C_CC                  = "mgga_c_cc"
    MGGA_C_CCALDA              = "mgga_c_ccalda"
    MGGA_C_CF22D               = "mgga_c_cf22d"
    MGGA_C_CS                  = "mgga_c_cs"
    MGGA_C_DLDF                = "mgga_c_dldf"
    MGGA_C_HLTAPW              = "mgga_c_hltapw"
    MGGA_C_KCIS                = "mgga_c_kcis"
    MGGA_C_KCISK               = "mgga_c_kcisk"
    MGGA_C_M05                 = "mgga_c_m05"
    MGGA_C_M05_2X              = "mgga_c_m05_2x"
    MGGA_C_M06                 = "mgga_c_m06"
    MGGA_C_M06_2X              = "mgga_c_m06_2x"
    MGGA_C_M06_HF              = "mgga_c_m06_hf"
    MGGA_C_M06_L               = "mgga_c_m06_l"
    MGGA_C_M06_SX              = "mgga_c_m06_sx"
    MGGA_C_M08_HX              = "mgga_c_m08_hx"
    MGGA_C_M08_SO              = "mgga_c_m08_so"
    MGGA_C_M11                 = "mgga_c_m11"
    MGGA_C_M11_L               = "mgga_c_m11_l"
    MGGA_C_MN12_L              = "mgga_c_mn12_l"
    MGGA_C_MN12_SX             = "mgga_c_mn12_sx"
    MGGA_C_MN15                = "mgga_c_mn15"
    MGGA_C_MN15_L              = "mgga_c_mn15_l"
    MGGA_C_PKZB                = "mgga_c_pkzb"
    MGGA_C_R2SCAN              = "mgga_c_r2scan"
    MGGA_C_R2SCAN01            = "mgga_c_r2scan01"
    MGGA_C_R2SCANL             = "mgga_c_r2scanl"
    MGGA_C_REVM06              = "mgga_c_revm06"
    MGGA_C_REVM06_L            = "mgga_c_revm06_l"
    MGGA_C_REVM11              = "mgga_c_revm11"
    MGGA_C_REVSCAN             = "mgga_c_revscan"
    MGGA_C_REVSCAN_VV10        = "mgga_c_revscan_vv10"
    MGGA_C_REVTM               = "mgga_c_revtm"
    MGGA_C_REVTPSS             = "mgga_c_revtpss"
    MGGA_C_RMGGAC              = "mgga_c_rmggac"
    MGGA_C_RPPSCAN             = "mgga_c_rppscan"
    MGGA_C_RREGTM              = "mgga_c_rregtm"
    MGGA_C_RSCAN               = "mgga_c_rscan"
    MGGA_C_SCAN                = "mgga_c_scan"
    MGGA_C_SCAN_RVV10          = "mgga_c_scan_rvv10"
    MGGA_C_SCAN_VV10           = "mgga_c_scan_vv10"
    MGGA_C_SCANL               = "mgga_c_scanl"
    MGGA_C_SCANL_RVV10         = "mgga_c_scanl_rvv10"
    MGGA_C_SCANL_VV10          = "mgga_c_scanl_vv10"
    MGGA_C_TM                  = "mgga_c_tm"
    MGGA_C_TPSS                = "mgga_c_tpss"
    MGGA_C_TPSS_GAUSSIAN       = "mgga_c_tpss_gaussian"
    MGGA_C_TPSSLOC             = "mgga_c_tpssloc"
    MGGA_C_VSXC                = "mgga_c_vsxc"


class ExCorrLibXC(StrEnum):

    @classmethod
    def _missing_(cls, value: str) -> Self:
        value = value.lower()
        for member in cls:
            if member.value.lower() == value:
                return member
        return None

    LDA_XC_1D_EHWLRG_1         = "lda_xc_1d_ehwlrg_1"
    LDA_XC_1D_EHWLRG_2         = "lda_xc_1d_ehwlrg_2"
    LDA_XC_1D_EHWLRG_3         = "lda_xc_1d_ehwlrg_3"
    LDA_XC_CORRKSDT            = "lda_xc_corrksdt"
    LDA_XC_GDSMFB              = "lda_xc_gdsmfb"
    LDA_XC_KSDT                = "lda_xc_ksdt"
    LDA_XC_LP_A                = "lda_xc_lp_a"
    LDA_XC_LP_B                = "lda_xc_lp_b"
    LDA_XC_TETER93             = "lda_xc_teter93"
    LDA_XC_TIH                 = "lda_xc_tih"
    LDA_XC_ZLP                 = "lda_xc_zlp"

    GGA_XC_B97_3C              = "gga_xc_b97_3c"
    GGA_XC_B97_D               = "gga_xc_b97_d"
    GGA_XC_B97_GGA1            = "gga_xc_b97_gga1"
    GGA_XC_BEEFVDW             = "gga_xc_beefvdw"
    GGA_XC_EDF1                = "gga_xc_edf1"
    GGA_XC_HCTH_120            = "gga_xc_hcth_120"
    GGA_XC_HCTH_147            = "gga_xc_hcth_147"
    GGA_XC_HCTH_407            = "gga_xc_hcth_407"
    GGA_XC_HCTH_407P           = "gga_xc_hcth_407p"
    GGA_XC_HCTH_93             = "gga_xc_hcth_93"
    GGA_XC_HCTH_P14            = "gga_xc_hcth_p14"
    GGA_XC_HCTH_P76            = "gga_xc_hcth_p76"
    GGA_XC_HLE16               = "gga_xc_hle16"
    GGA_XC_KT1                 = "gga_xc_kt1"
    GGA_XC_KT2                 = "gga_xc_kt2"
    GGA_XC_KT3                 = "gga_xc_kt3"
    GGA_XC_MOHLYP              = "gga_xc_mohlyp"
    GGA_XC_MOHLYP2             = "gga_xc_mohlyp2"
    GGA_XC_MPWLYP1W            = "gga_xc_mpwlyp1w"
    GGA_XC_NCAP                = "gga_xc_ncap"
    GGA_XC_OBLYP_D             = "gga_xc_oblyp_d"
    GGA_XC_OPBE_D              = "gga_xc_opbe_d"
    GGA_XC_OPWLYP_D            = "gga_xc_opwlyp_d"
    GGA_XC_PBE1W               = "gga_xc_pbe1w"
    GGA_XC_PBELYP1W            = "gga_xc_pbelyp1w"
    GGA_XC_TH1                 = "gga_xc_th1"
    GGA_XC_TH2                 = "gga_xc_th2"
    GGA_XC_TH3                 = "gga_xc_th3"
    GGA_XC_TH4                 = "gga_xc_th4"
    GGA_XC_TH_FC               = "gga_xc_th_fc"
    GGA_XC_TH_FCFO             = "gga_xc_th_fcfo"
    GGA_XC_TH_FCO              = "gga_xc_th_fco"
    GGA_XC_TH_FL               = "gga_xc_th_fl"
    GGA_XC_VV10                = "gga_xc_vv10"
    GGA_XC_XLYP                = "gga_xc_xlyp"

    MGGA_XC_B97M_V             = "mgga_xc_b97m_v"
    MGGA_XC_CC06               = "mgga_xc_cc06"
    MGGA_XC_HLE17              = "mgga_xc_hle17"
    MGGA_XC_LP90               = "mgga_xc_lp90"
    MGGA_XC_OTPSS_D            = "mgga_xc_otpss_d"
    MGGA_XC_TPSSLYP1W          = "mgga_xc_tpsslyp1w"
    MGGA_XC_VCML_RVV10         = "mgga_xc_vcml_rvv10"
    MGGA_XC_ZLP                = "mgga_xc_zlp"

    HYB_GGA_XC_APBE0           = "hyb_gga_xc_apbe0"
    HYB_GGA_XC_APF             = "hyb_gga_xc_apf"
    HYB_GGA_XC_B1LYP           = "hyb_gga_xc_b1lyp"
    HYB_GGA_XC_B1PW91          = "hyb_gga_xc_b1pw91"
    HYB_GGA_XC_B1WC            = "hyb_gga_xc_b1wc"
    HYB_GGA_XC_B3LYP           = "hyb_gga_xc_b3lyp"
    HYB_GGA_XC_B3LYP3          = "hyb_gga_xc_b3lyp3"
    HYB_GGA_XC_B3LYP5          = "hyb_gga_xc_b3lyp5"
    HYB_GGA_XC_B3LYP_MCM1      = "hyb_gga_xc_b3lyp_mcm1"
    HYB_GGA_XC_B3LYP_MCM2      = "hyb_gga_xc_b3lyp_mcm2"
    HYB_GGA_XC_B3LYPS          = "hyb_gga_xc_b3lyps"
    HYB_GGA_XC_B3P86           = "hyb_gga_xc_b3p86"
    HYB_GGA_XC_B3P86_NWCHEM    = "hyb_gga_xc_b3p86_nwchem"
    HYB_GGA_XC_B3PW91          = "hyb_gga_xc_b3pw91"
    HYB_GGA_XC_B5050LYP        = "hyb_gga_xc_b5050lyp"
    HYB_GGA_XC_B97             = "hyb_gga_xc_b97"
    HYB_GGA_XC_B97_1           = "hyb_gga_xc_b97_1"
    HYB_GGA_XC_B97_1P          = "hyb_gga_xc_b97_1p"
    HYB_GGA_XC_B97_2           = "hyb_gga_xc_b97_2"
    HYB_GGA_XC_B97_3           = "hyb_gga_xc_b97_3"
    HYB_GGA_XC_B97_K           = "hyb_gga_xc_b97_k"
    HYB_GGA_XC_BHANDH          = "hyb_gga_xc_bhandh"
    HYB_GGA_XC_BHANDHLYP       = "hyb_gga_xc_bhandhlyp"
    HYB_GGA_XC_BLYP35          = "hyb_gga_xc_blyp35"
    HYB_GGA_XC_CAM_B3LYP       = "hyb_gga_xc_cam_b3lyp"
    HYB_GGA_XC_CAM_O3LYP       = "hyb_gga_xc_cam_o3lyp"
    HYB_GGA_XC_CAM_PBEH        = "hyb_gga_xc_cam_pbeh"
    HYB_GGA_XC_CAM_QTP_00      = "hyb_gga_xc_cam_qtp_00"
    HYB_GGA_XC_CAM_QTP_01      = "hyb_gga_xc_cam_qtp_01"
    HYB_GGA_XC_CAM_QTP_02      = "hyb_gga_xc_cam_qtp_02"
    HYB_GGA_XC_CAMH_B3LYP      = "hyb_gga_xc_camh_b3lyp"
    HYB_GGA_XC_CAMY_B3LYP      = "hyb_gga_xc_camy_b3lyp"
    HYB_GGA_XC_CAMY_BLYP       = "hyb_gga_xc_camy_blyp"
    HYB_GGA_XC_CAMY_PBEH       = "hyb_gga_xc_camy_pbeh"
    HYB_GGA_XC_CAP0            = "hyb_gga_xc_cap0"
    HYB_GGA_XC_CASE21          = "hyb_gga_xc_case21"
    HYB_GGA_XC_EDF2            = "hyb_gga_xc_edf2"
    HYB_GGA_XC_HAPBE           = "hyb_gga_xc_hapbe"
    HYB_GGA_XC_HFLYP           = "hyb_gga_xc_hflyp"
    HYB_GGA_XC_HJS_B88         = "hyb_gga_xc_hjs_b88"
    HYB_GGA_XC_HJS_B97X        = "hyb_gga_xc_hjs_b97x"
    HYB_GGA_XC_HJS_PBE         = "hyb_gga_xc_hjs_pbe"
    HYB_GGA_XC_HJS_PBE_SOL     = "hyb_gga_xc_hjs_pbe_sol"
    HYB_GGA_XC_HPBEINT         = "hyb_gga_xc_hpbeint"
    HYB_GGA_XC_HSE03           = "hyb_gga_xc_hse03"
    HYB_GGA_XC_HSE06           = "hyb_gga_xc_hse06"
    HYB_GGA_XC_HSE12           = "hyb_gga_xc_hse12"
    HYB_GGA_XC_HSE12S          = "hyb_gga_xc_hse12s"
    HYB_GGA_XC_HSE_SOL         = "hyb_gga_xc_hse_sol"
    HYB_GGA_XC_KMLYP           = "hyb_gga_xc_kmlyp"
    HYB_GGA_XC_LB07            = "hyb_gga_xc_lb07"
    HYB_GGA_XC_LC_BLYP         = "hyb_gga_xc_lc_blyp"
    HYB_GGA_XC_LC_BLYP_EA      = "hyb_gga_xc_lc_blyp_ea"
    HYB_GGA_XC_LC_BLYPR        = "hyb_gga_xc_lc_blypr"
    HYB_GGA_XC_LC_BOP          = "hyb_gga_xc_lc_bop"
    HYB_GGA_XC_LC_PBEOP        = "hyb_gga_xc_lc_pbeop"
    HYB_GGA_XC_LC_QTP          = "hyb_gga_xc_lc_qtp"
    HYB_GGA_XC_LC_VV10         = "hyb_gga_xc_lc_vv10"
    HYB_GGA_XC_LC_WPBE         = "hyb_gga_xc_lc_wpbe"
    HYB_GGA_XC_LC_WPBE08_WHS   = "hyb_gga_xc_lc_wpbe08_whs"
    HYB_GGA_XC_LC_WPBE_WHS     = "hyb_gga_xc_lc_wpbe_whs"
    HYB_GGA_XC_LC_WPBEH_WHS    = "hyb_gga_xc_lc_wpbeh_whs"
    HYB_GGA_XC_LC_WPBESOL_WHS  = "hyb_gga_xc_lc_wpbesol_whs"
    HYB_GGA_XC_LCY_BLYP        = "hyb_gga_xc_lcy_blyp"
    HYB_GGA_XC_LCY_PBE         = "hyb_gga_xc_lcy_pbe"
    HYB_GGA_XC_LRC_WPBE        = "hyb_gga_xc_lrc_wpbe"
    HYB_GGA_XC_LRC_WPBEH       = "hyb_gga_xc_lrc_wpbeh"
    HYB_GGA_XC_MB3LYP_RC04     = "hyb_gga_xc_mb3lyp_rc04"
    HYB_GGA_XC_MCAM_B3LYP      = "hyb_gga_xc_mcam_b3lyp"
    HYB_GGA_XC_MPW1K           = "hyb_gga_xc_mpw1k"
    HYB_GGA_XC_MPW1LYP         = "hyb_gga_xc_mpw1lyp"
    HYB_GGA_XC_MPW1PBE         = "hyb_gga_xc_mpw1pbe"
    HYB_GGA_XC_MPW1PW          = "hyb_gga_xc_mpw1pw"
    HYB_GGA_XC_MPW3LYP         = "hyb_gga_xc_mpw3lyp"
    HYB_GGA_XC_MPW3PW          = "hyb_gga_xc_mpw3pw"
    HYB_GGA_XC_MPWLYP1M        = "hyb_gga_xc_mpwlyp1m"
    HYB_GGA_XC_O3LYP           = "hyb_gga_xc_o3lyp"
    HYB_GGA_XC_OPB3LYP         = "hyb_gga_xc_opb3lyp"
    HYB_GGA_XC_PBE0_13         = "hyb_gga_xc_pbe0_13"
    HYB_GGA_XC_PBE38           = "hyb_gga_xc_pbe38"
    HYB_GGA_XC_PBE50           = "hyb_gga_xc_pbe50"
    HYB_GGA_XC_PBE_2X          = "hyb_gga_xc_pbe_2x"
    HYB_GGA_XC_PBE_MOL0        = "hyb_gga_xc_pbe_mol0"
    HYB_GGA_XC_PBE_MOLB0       = "hyb_gga_xc_pbe_molb0"
    HYB_GGA_XC_PBE_SOL0        = "hyb_gga_xc_pbe_sol0"
    HYB_GGA_XC_PBEB0           = "hyb_gga_xc_pbeb0"
    HYB_GGA_XC_PBEH            = "hyb_gga_xc_pbeh"
    HYB_GGA_XC_QTP17           = "hyb_gga_xc_qtp17"
    HYB_GGA_XC_RCAM_B3LYP      = "hyb_gga_xc_rcam_b3lyp"
    HYB_GGA_XC_RELPBE0         = "hyb_gga_xc_relpbe0"
    HYB_GGA_XC_REVB3LYP        = "hyb_gga_xc_revb3lyp"
    HYB_GGA_XC_SB98_1A         = "hyb_gga_xc_sb98_1a"
    HYB_GGA_XC_SB98_1B         = "hyb_gga_xc_sb98_1b"
    HYB_GGA_XC_SB98_1C         = "hyb_gga_xc_sb98_1c"
    HYB_GGA_XC_SB98_2A         = "hyb_gga_xc_sb98_2a"
    HYB_GGA_XC_SB98_2B         = "hyb_gga_xc_sb98_2b"
    HYB_GGA_XC_SB98_2C         = "hyb_gga_xc_sb98_2c"
    HYB_GGA_XC_TUNED_CAM_B3LYP = "hyb_gga_xc_tuned_cam_b3lyp"
    HYB_GGA_XC_WB97            = "hyb_gga_xc_wb97"
    HYB_GGA_XC_WB97X           = "hyb_gga_xc_wb97x"
    HYB_GGA_XC_WB97X_D         = "hyb_gga_xc_wb97x_d"
    HYB_GGA_XC_WB97X_D3        = "hyb_gga_xc_wb97x_d3"
    HYB_GGA_XC_WB97X_V         = "hyb_gga_xc_wb97x_v"
    HYB_GGA_XC_WC04            = "hyb_gga_xc_wc04"
    HYB_GGA_XC_WHPBE0          = "hyb_gga_xc_whpbe0"
    HYB_GGA_XC_WP04            = "hyb_gga_xc_wp04"
    HYB_GGA_XC_X3LYP           = "hyb_gga_xc_x3lyp"

    HYB_MGGA_XC_B0KCIS         = "hyb_mgga_xc_b0kcis"
    HYB_MGGA_XC_B86B95         = "hyb_mgga_xc_b86b95"
    HYB_MGGA_XC_B88B95         = "hyb_mgga_xc_b88b95"
    HYB_MGGA_XC_B94_HYB        = "hyb_mgga_xc_b94_hyb"
    HYB_MGGA_XC_B98            = "hyb_mgga_xc_b98"
    HYB_MGGA_XC_BB1K           = "hyb_mgga_xc_bb1k"
    HYB_MGGA_XC_BR3P86         = "hyb_mgga_xc_br3p86"
    HYB_MGGA_XC_EDMGGAH        = "hyb_mgga_xc_edmggah"
    HYB_MGGA_XC_GAS22          = "hyb_mgga_xc_gas22"
    HYB_MGGA_XC_LC_TMLYP       = "hyb_mgga_xc_lc_tmlyp"
    HYB_MGGA_XC_MPW1B95        = "hyb_mgga_xc_mpw1b95"
    HYB_MGGA_XC_MPW1KCIS       = "hyb_mgga_xc_mpw1kcis"
    HYB_MGGA_XC_MPWB1K         = "hyb_mgga_xc_mpwb1k"
    HYB_MGGA_XC_MPWKCIS1K      = "hyb_mgga_xc_mpwkcis1k"
    HYB_MGGA_XC_PBE1KCIS       = "hyb_mgga_xc_pbe1kcis"
    HYB_MGGA_XC_PW6B95         = "hyb_mgga_xc_pw6b95"
    HYB_MGGA_XC_PW86B95        = "hyb_mgga_xc_pw86b95"
    HYB_MGGA_XC_PWB6K          = "hyb_mgga_xc_pwb6k"
    HYB_MGGA_XC_R2SCAN0        = "hyb_mgga_xc_r2scan0"
    HYB_MGGA_XC_R2SCAN50       = "hyb_mgga_xc_r2scan50"
    HYB_MGGA_XC_R2SCANH        = "hyb_mgga_xc_r2scanh"
    HYB_MGGA_XC_REVTPSSH       = "hyb_mgga_xc_revtpssh"
    HYB_MGGA_XC_TPSS0          = "hyb_mgga_xc_tpss0"
    HYB_MGGA_XC_TPSS1KCIS      = "hyb_mgga_xc_tpss1kcis"
    HYB_MGGA_XC_TPSSH          = "hyb_mgga_xc_tpssh"
    HYB_MGGA_XC_WB97M_V        = "hyb_mgga_xc_wb97m_v"
    HYB_MGGA_XC_X1B95          = "hyb_mgga_xc_x1b95"
    HYB_MGGA_XC_XB1K           = "hyb_mgga_xc_xb1k"

    HYB_LDA_XC_BN05            = "hyb_lda_xc_bn05"
    HYB_LDA_XC_CAM_LDA0        = "hyb_lda_xc_cam_lda0"
    HYB_LDA_XC_LDA0            = "hyb_lda_xc_lda0"


def check_libxc(
    func1: ExCorrLibXC | ExchangeLibXC | CorrelationLibXC,
    func2: ExchangeLibXC | CorrelationLibXC | None = None,
) -> bool:
    """Check if you have specified the necessary components for an
    exchange-correlation functional.
    """
    match (func1, func2):
        case ExCorrLibXC(), None:
            return True
        case ExchangeLibXC(), CorrelationLibXC():
            return True
        case CorrelationLibXC(), ExchangeLibXC():
            return True
        case _:
            return False


def format_libxc(
    func1: ExCorrLibXC | ExchangeLibXC | CorrelationLibXC,
    func2: ExchangeLibXC | CorrelationLibXC | None = None,
) -> str:
    """Format a non-simple input LibXC functional in the %method block.
    
    This function presupposes that you have already checked that the
    chosen functional(s) are valid.
    """
    if isinstance(func1, ExCorrLibXC):
        libxc_str = (
            "%method\n"
            "    Method     DFT\n"
           f"    Functional {func1}\n"
            "end\n"
        )
    elif isinstance(func1, ExchangeLibXC):
        libxc_str = (
            "%method\n"
            "    Method      DFT\n"
           f"    Exchange    {func1}\n"
           f"    Correlation {func2}\n"
            "end"
        )
    elif isinstance(func1, CorrelationLibXC):
        libxc_str = (
            "%method\n"
            "    Method      DFT\n"
           f"    Exchange    {func2}\n"
           f"    Correlation {func1}\n"
            "end"
        )
    return libxc_str