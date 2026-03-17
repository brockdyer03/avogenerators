"""Classes and methods for the %scf block in ORCA.

Currently unused.
"""

from collections.abc import Sequence
from .block_base import BlockEnum, ORCAString, NestedBlockEnum


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

    # Wavefunction Types
    HFTYP = "HFTyp", ORCAString, ("RHF", "UHF", "ROHF", "CASSCF")
    ROHF_CASE = "ROHF_Case", ORCAString, ("HighSpin", "CAHF", "SAHF", "USER_CSF", "AF_CSF")
    ROHF_NEL = "ROHF_NEl", Sequence
    ROHF_NUMOP = "ROHF_NumOp", int, None, None, 1, 3
    ROHF_NORB = "ROHF_NOrb", Sequence
    ROHF_REF = "ROHF_Ref", dict
    ROHF_AFORBS = "ROHF_AFOrbs", Sequence


class TRAH(NestedBlockEnum):

    MAXRED = "MaxRed", int, None, 24
    NSTART = "NStart", int, None, 2, 2
    TOLFACMICRO = "TolFacMicro", float, None, 0.1
    MINTOLMICRO = "MinTolMicro", float, None, 1e-2
    QUADREGIONSTART = "QuadRegionStart", float, None, 1e-4
    TRADIUS = "TRadius", float, None, 0.4
    ALPHAMIN = "AlphaMin", float, None, 0.1
    ALPHAMAX = "AlphaMax", float, None, 1000
    RANDOMIZE = "Randomize", bool, None, True
    PSEUDORAND = "PseudoRand", bool, None, False
    MAXNOISE = "MaxNoise", float, None, 1e-2
    ORBUPDATE = "OrbUpdate", ORCAString, ("Taylor", "Cayley"), 0
    INACTIVEMOS = "InactiveMOs", ORCAString, ("Canonical", "NotSet"), 0
    PRECOND = "Precond", ORCAString, ("Diag", "Full", "None"), 0
    PRECONMAXRED = "PreconMaxRed", int, None, 250