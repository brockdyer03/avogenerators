"""Classes and methods for the %scf block in ORCA."""

from .block_base import BlockEnum, ORCAString


class SCF(BlockEnum):

    CONVERGENCE   = "Convergence",   ORCAString, ("Sloppy", "Loose", "Medium", "Strong", "Tight", "VeryTight", "Extreme"), 2
    TOL_E         = "TolE",          float, None, 1e-8
    TOL_RMSP      = "TolRMSP",       float, None, 5e-9
    TOL_MAXP      = "TolMaxP",       float, None, 1e-7
    TOL_ERR       = "TolErr",        float, None, 5e-7
    TOL_G         = "TolG",          float, None, 1e-5
    TOL_X         = "TolX",          float, None, 1e-5
    THRESH        = "Thresh",        float, None, 2.5e-11
    TCUT          = "TCut",          float, None, 2.5e-12
    CONVCHECKMODE = "ConvCheckMode", int,   None, 2, 0, 2
    CONVFORCED    = "ConvForced",    int,   None, 1, 0, 1

