# SPDX-FileCopyrightText: 2026 Avogadro Project
# SPDX-License-Identifier: BSD 3-Clause
# ******************************************************************************
# This source file is part of the Avogadro project.
#
# This source code is released under the New BSD License, (the "License").
# ******************************************************************************
"""Classes and functions for the %elprop block."""

from .block_base import BlockEnum, ORCAString


class ElProp(BlockEnum):
    """Keywords for the electrical properties."""
                      # name,         dtype,    default, options, minimum, maximum
    DIPOLE          = "Dipole",        bool,       True
    QUADRUPOLE      = "Quadrupole",    bool,       False
    POLAR           = "Polar",         bool,       False
    HYPERPOL        = "HyperPol",      bool,       False
    POLARVELOCITY   = "PolarVelocity", bool,       False
    POLARDIPQUAD    = "PolarDipQuad",  bool,       False
    POLARQUADQUAD   = "PolarQuadQuad", bool,       False
    FREQ_R          = "Freq_r",        float,      0.0, None, 0.0
    FREQ_I          = "Freq_i",        float,      0.0, None, 0.0
    SOLVER          = "Solver",        ORCAString, 2, ("CG", "DIIS", "Pople")
    MAXDIIS         = "MaxDIIS",       int,        5
    SHIFT           = "Shift",         float,      0.2
    TOL             = "Tol",           float,      1e-3
    MAXITER         = "MaxIter",       int,        64
    PRINTLEVEL      = "PrintLevel",    int,        2
    # Todo - Add support for specifying origin as atom position or XYZ coordinate
    ORIGIN = (
        "Origin",
        ORCAString,
        3, # CenterOfMass
        ("CenterOfElCharge", "CenterOfNucCharge", "CenterOfSpinDens", "CenterOfMass"),
    )

