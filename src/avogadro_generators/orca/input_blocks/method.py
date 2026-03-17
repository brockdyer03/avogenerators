"""Classes and methods for the %method block in ORCA.

WORK IN PROGRESS!!
"""

from collections.abc import Sequence
from .block_base import BlockEnum, ORCAString


class Method(BlockEnum):
    """Enumeration of keywords available in the %method block"""

    RUNTYPE = "RunType", ORCAString, ("Energy", "Gradient", "Opt", "Scan", "CIM"), 0
    METHOD = (
        "Method",
        ORCAString,
        (
            "HF", "DFT",
            "AM1", "PM3",
            "MNDO",
            "CNDO_1",  "CNDO_2",  "CNDO_S",
            "INDO_1",  "INDO_2",  "INDO_S",
            "ZINDO_1", "ZINDO_2", "ZINDO_S",
            "ZNDDO_1", "ZNDDO_2",
        ),
        0 # Default HF
    )

    # Integration Grids
    ANGULARGRID  = "AngularGrid",  int,   None, None, 0, 7
    INTACC       = "IntAcc",       float, None, 5.0
    ANGULARGRIDX = "AngularGridX", Sequence
    NTHETAMAX    = "NThetaMax",    float, None, 0.4
    GRIDPRUNING  = "GridPruning",  ORCAString, ("Unpruned", "OldPruning", "Adaptive"), 2
    HGRIDREDUCED = "HGridReduced", bool,  None, True
    BFCUT        = "BFCut",        float, None, 1e-10
    WEIGHTCUT    = "WeightCut",    float, None, 1e-14
