from ..basis_sets import (
    PopleBasisSet,
    def2BasisSet,
    JensenBasisSet,
    CorrelationConsistentBasisSet,
    RelativisticBasisSet,
    AuxJBasisSet,
    AuxJKBasisSet,
    AuxCBasisSet,
)
from ..dft import Composite, Functionals
from ..simple_keywords import (
    RunType,
    SemiEmpirical,
    SCF,
    DeterminantType,
    Opt,
    Output,
    Grid,
    RIApproximation,
    PartialCharges,
    Relativistic,
    PNO,
)
from ..wft import MP2, CoupledCluster
from ..implicit_solvation import Solvent, XTBSolvent


class BasicTab:
    """Class for writing the Basic tab"""

    name = "Basic"
