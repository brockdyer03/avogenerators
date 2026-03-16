"""Classes and functions for the %elprop block"""

from .block_base import BlockEnum, ORCAString


class ElProp(BlockEnum):
    """Keywords for the electrical properties."""
                      # name,         dtype,    options, default, minimum, maximum
    DIPOLE          = "Dipole",        bool,       None, True
    QUADRUPOLE      = "Quadrupole",    bool,       None, False
    POLAR           = "Polar",         bool,       None, False
    HYPERPOL        = "HyperPol",      bool,       None, False
    POLARVELOCITY   = "PolarVelocity", bool,       None, False
    POLARDIPQUAD    = "PolarDipQuad",  bool,       None, False
    POLARQUADQUAD   = "PolarQuadQuad", bool,       None, False
    FREQ_R          = "Freq_r",        float,      None, 0.0, 0.0
    FREQ_I          = "Freq_i",        float,      None, 0.0, 0.0
    SOLVER          = "Solver",        ORCAString, ("CG", "DIIS", "Pople"), 2
    MAXDIIS         = "MaxDIIS",       int,        None, 5
    SHIFT           = "Shift",         float,      None, 0.2
    TOL             = "Tol",           float,      None, 1e-3
    MAXITER         = "MaxIter",       int,        None, 64
    PRINTLEVEL      = "PrintLevel",    int,        None, 2
    # Todo - Add support for specifying origin as atom position or XYZ coordinate
    ORIGIN = (
        "Origin",
        ORCAString,
        ("CenterOfElCharge", "CenterOfNucCharge", "CenterOfSpinDens", "CenterOfMass"),
        3, # CenterOfMass
    )

