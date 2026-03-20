# SPDX-FileCopyrightText: 2026 Avogadro Project
# SPDX-License-Identifier: BSD 3-Clause
# ******************************************************************************
# This source file is part of the Avogadro project.
#
# This source code is released under the New BSD License, (the "License").
# ******************************************************************************
"""Classes and methods for using WFT methods such as DLPNO-CCSD(T) and MP2."""

from enum import StrEnum


class MP2(StrEnum):
    """All MP2 methods in ORCA."""

    MP2             = "MP2"
    RI_MP2          = "RI-MP2"
    DLPNO_MP2       = "DLPNO-MP2"
    SCS_MP2         = "SCS-MP2"
    SOS_MP2         = "SOS-MP2"
    SCS_RI_MP2      = "SCS-RI-MP2"
    SOS_RI_MP2      = "SOS-RI-MP2"
    SCS_DLPNO_MP2   = "SCS-DLPNO-MP2"
    SOS_DLPNO_MP2   = "SOS-DLPNO-MP2"
    OO_RI_MP2       = "OO-RI-MP2"
    OO_RI_SCS_MP2   = "OO-SCS-RI-MP2"
    OO_RI_SOS_MP2   = "OO-SOS-RI-MP2"
    F12_MP2         = "F12-MP2"
    F12_RI_MP2      = "F12-RI-MP2"
    F12_D_RI_MP2    = "F12/D-RI-MP2"
    F12_DLPNO_MP2   = "F12-DLPNO-MP2"
    F12_D_DLPNO_MP2 = "F12/D-DLPNO-MP2"


class CoupledCluster(StrEnum):
    """All Coupled-Cluster methods in ORCA."""

    CCSD                = "CCSD"
    RI_CCSD             = "RI-CCSD"
    CCSD_T_             = "CCSD(T)"
    RI_CCSD_T_          = "RI-CCSD(T)"
    CCSD_F12            = "CCSD-F12"
    CCSD_T_F12          = "CCSD(T)-F12"
    CCSD_F12_RI         = "CCSD-F12/RI"
    CCSD_F12D_RI        = "CCSD-F12D/RI"
    CCSD_T_F12_RI       = "CCSD(T)-F12/RI"
    CCSD_T_F12_D_RI     = "CCSD(T)-F12D/RI"
    DLPNO_CCSD          = "DLPNO-CCSD"
    DLPNO_CCSD_T_       = "DLPNO-CCSD(T)"
    DLPNO_CCSD_T1_      = "DLPNO-CCSD(T1)"
    DLPNO_CCSD_F12      = "DLPNO-CCSD-F12"
    DLPNO_CCSD_F12_D    = "DLPNO-CCSD-F12/D"
    DLPNO_CCSD_T_F12    = "DLPNO-CCSD(T)-F12"
    DLPNO_CCSD_T_F12_D  = "DLPNO-CCSD(T)-F12/D"
    DLPNO_CCSD_T1_F12   = "DLPNO-CCSD(T1)-F12"
    DLPNO_CCSD_T1_F12_D = "DLPNO-CCSD(T1)-F12/D"


