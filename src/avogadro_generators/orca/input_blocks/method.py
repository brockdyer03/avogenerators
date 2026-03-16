"""Classes and methods for the %method block in ORCA.

WORK IN PROGRESS!!
"""

from .block_base import BlockEnum, ORCAString

class Method(BlockEnum):
    """Enumeration of keywords available in the %method block"""

    RUNTYPE = "RunType", ORCAString, ("Energy", "Gradient", "Opt", "Scan", "CIM")
    METHOD  = "Method", ORCAString, ("HF", "DFT", "AM1", "")
