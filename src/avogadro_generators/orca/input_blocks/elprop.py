"""Classes and functions for the %elprop block"""

from .block_base import BlockEnum, ORCAString


class ElProp(BlockEnum):
    """Keywords for the electrical properties."""

    DIPOLE          = "Dipole",         bool
    QUADRUPOLE      = "Quadrupole",     bool
    POLAR           = "Polar",          bool
    HYPERPOL        = "HyperPol",       bool
    POLARVELOCITY   = "PolarVelocity",  bool
    POLARDIPQUAD    = "PolarDipQuad",   bool
    POLARQUADQUAD   = "PolarQuadQuad",  bool
    FREQ_R          = "Freq_r",         float, None, 0.0
    FREQ_I          = "Freq_i",         float, None, 0.0
    SOLVER          = "Solver",         ORCAString, ("CG", "DIIS", "Pople")
    MAXDIIS         = "MaxDIIS",        int
    SHIFT           = "Shift",          float
    TOL             = "Tol",            float
    MAXITER         = "MaxIter",        int
    PRINTLEVEL      = "PrintLevel",     int
    # Todo - Add support for specifying origin as atom position or XYZ coordinate
    ORIGIN          = "Origin",         ORCAString, ("CenterOfElCharge", "CenterOfNucCharge", "CenterOfSpinDens", "CenterOfMass")


