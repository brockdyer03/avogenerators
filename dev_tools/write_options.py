from dataclasses import dataclass
from collections.abc import Sequence
from pathlib import Path

from avogadro_generators.orca.basis_sets import (
    PopleBasisSet,
    def2BasisSet,
    JensenBasisSet,
    ccBasisSet,
    RelativisticBasisSet,
    AuxJBasisSet,
    AuxJKBasisSet,
    AuxCBasisSet,
)
from avogadro_generators.orca.dft import Composite, Functionals, Disp
from avogadro_generators.orca.simple_keywords import (
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
from avogadro_generators.orca.wft import MP2, CoupledCluster
from avogadro_generators.orca.implicit_solvation import Solvent, XTBSolvent
from avogadro_generators.orca.input_blocks.block_base import BlockKeyword, ORCAString
from avogadro_generators.orca.input_blocks.elprop import ElProp


@dataclass
class BasicOption:
    """Possible values for a user option."""

    dtype:   str # string, stringList, filePath, boolean, integer, float, text, table
    default: str | int
    label:   str
    options: tuple | None       = None
    toolTip: str | None         = None
    hide:    bool | None        = None
    minimum: int | float | None = None
    maximum: int | float | None = None


class BasicTab:
    """Class for writing the Basic tab"""

    name = "Basic"

    inputs = {
        "Title": BasicOption(
            dtype="string",
            default="",
            label="Title",
            toolTip="Title of the input file (not recognized by ORCA)",
        ),
        "Filename Base": BasicOption(
            dtype="string",
            default="job",
            label="Filename Base",
        ),
        "Processor Cores": BasicOption(
            dtype="integer",
            default=1,
            label="Number of Processes",
            minimum=1,
        ),
        "Memory": BasicOption(
            dtype="integer",
            default=4,
            label="Memory",
            minimum=1,
            toolTip="Total available memory (divided by nprocs to get memory per core)"
        ),
        "Calculation Type": BasicOption(
            dtype="stringList",
            default=2, # Opt
            label="Calculation Type",
            options=(
                RunType.SP,
                RunType.ENGRAD,
                RunType.OPT,
                RunType.OPTTS,
                RunType.FREQ,
                RunType.NUMFREQ,
            ),
            toolTip="Type of calculation to run"
        ),
        "Theory": BasicOption(
            dtype="stringList",
            default=0,
            label="Theory",
            options=(
                Composite.R2SCAN_3C,
                Composite.PBEH_3C,
                Composite.B97_3C,
                Composite.WB97X_3C,
                Functionals.LDA,
                Functionals.PBE,
                Functionals.B97M_V,
                Functionals.B97M_D4,
                Functionals.R2SCAN,
                Functionals.PBE0,
                Functionals.R2SCAN0,
                Functionals.WB97X_D4,
                Functionals.WB97X_V,
                Functionals.WB97M_D4,
                Functionals.WB97M_V,
                Functionals.PR2SCAN69,
                Functionals.B2GP_PLYP,
            ),
        ),
        "Basis": BasicOption(
            dtype="stringList",
            default=6, # def2-TZVP
            label="Basis",
            options=(
                def2BasisSet.DEF2_SVP,
                def2BasisSet.DEF2_SVPD,
                ccBasisSet.CC_PVDZ,
                ccBasisSet.AUG_CC_PVDZ,
                JensenBasisSet.PC_1,
                JensenBasisSet.AUG_PC_1,

                def2BasisSet.DEF2_TZVP,
                def2BasisSet.DEF2_TZVPP,
                def2BasisSet.DEF2_TZVPPD,
                ccBasisSet.CC_PVTZ,
                ccBasisSet.AUG_CC_PVTZ,
                JensenBasisSet.PC_2,
                JensenBasisSet.AUG_PC_2,

                def2BasisSet.DEF2_QZVP,
                def2BasisSet.DEF2_QZVPP,
                def2BasisSet.DEF2_QZVPPD,
                ccBasisSet.CC_PVQZ,
                ccBasisSet.AUG_CC_PVQZ,
                JensenBasisSet.PC_3,
                JensenBasisSet.AUG_PC_3,
            )
        ),
        "Charge": BasicOption(
            dtype="integer",
            default=0,
            label="Charge",
        ),
        "Multiplicity": BasicOption(
            dtype="integer",
            default=1,
            label="Multiplicity",
            minimum=1,
            toolTip="Calculated as 2S+1 where S is the number of unpaired electrons"
        ),
        "Solvent": BasicOption(
            dtype="stringList",
            default=0,
            label="Solvent",
            options=(
                Solvent.s_NONE,
                Solvent.s_WATER,
                Solvent.s_ACETONITRILE,
                Solvent.s_ACETONE,
                Solvent.s_ETHANOL,
                Solvent.s_METHANOL,
                Solvent.s_CARBON_TETRACHLORIDE,
                Solvent.s_DICHLOROMETHANE,
                Solvent.s_CHLOROFORM,
                Solvent.s_DIMETHYLSULFOXIDE,
                Solvent.s_NN_DIMETHYLFORMAMIDE,
                Solvent.s_N_HEXANE,
                Solvent.s_TOLUENE,
                Solvent.s_PYRIDINE,
                Solvent.s_TETRAHYDROFURAN,
            )
        ),
        "Solvation Model": BasicOption(
            dtype="stringList",
            default=0, # CPCM, but really is nothing without Solvent
            label="Solvation Model",
            options=(
                "CPCM",     # CPCM
                "SMD",      # SMD
                "COSMO_RS", # COSMO_RS
                "ALPB",     # ALPB
                "ddCOSMO",  # DDCOSMO
                "CPCMX",    # CPCMX
            )
        ),
        "basic_disp_corr": BasicOption(
            dtype="stringList",
            default=0,
            label="Dispersion Correction",
            options=(
                Disp.NODISP,
                Disp.D3BJ,
                Disp.D3ZERO,
                Disp.D4,
                Disp.NL,
                Disp.SCNL,
            ),
        ),
        "basic_print_mos": BasicOption(
            dtype="boolean",
            default=True,
            label="Print Molecular Orbitals",
        ),
        "basic_print_level": BasicOption(
            dtype="stringList",
            default=2, # NormalPrint
            label="Print Level",
            options=(
                Output.MINIPRINT,
                Output.SMALLPRINT,
                Output.NORMALPRINT,
                Output.LARGEPRINT,
            )
        ),
    }

    @classmethod
    def write_tab(cls) -> str:
        """Write the ``options.toml`` entry for this tab."""

        tab = ""
        for key, val in cls.inputs.items():
            tab += f'["{key}"]\n'
            tab += f'label = "{val.label}"\n'
            tab += f'type = "{val.dtype}"\n'
            if val.dtype == "string":
                tab += f'default = "{val.default}"\n'
            elif val.dtype == "boolean":
                tab += f"default = {str(val.default).lower()}\n"
            else:
                tab += f"default = {val.default}\n"

            if val.options is not None:
                tab += "values = [\n"
                for option in val.options:
                    tab += f'    "{option}",\n'
                tab += "]\n"

            if val.minimum is not None:
                tab += f"minimum = {val.minimum}\n"

            if val.maximum is not None:
                tab += f"maximum = {val.maximum}\n"

            if val.toolTip is not None:
                tab += f'toolTip = "{val.toolTip}"\n'

            tab += f'tab = "{cls.name}"\n\n'

        return tab


class BlockOption:
    """Options for a block tab."""

    def __init__(
        self,
        keyword: BlockKeyword,
        label: str,
        toolTip: str | None = None,
    ):
        self.option_name = keyword.key_name
        self.dtype   = keyword.dtype
        self.options = keyword.options
        self.default = keyword.default
        self.minimum = keyword.minimum
        self.maximum = keyword.maximum
        self.label   = label
        self.toolTip = toolTip


class ElPropTab:
    """Class for writing the %elprop tab"""

    name = "Electric Properties"

    inputs = {
        "elprop_dipole": BlockOption(
            keyword=ElProp.DIPOLE,
            toolTip="Calculate dipole moment.",
            label="Dipole",
        ),
        "elprop_quadrupole": BlockOption(
            keyword=ElProp.QUADRUPOLE,
            toolTip="Calculate quadrupole moment.",
            label="Quadrupole",
        ),
        "elprop_polar": BlockOption(
            keyword=ElProp.POLAR,
            toolTip="Calculate dipole-dipole polarizability.",
            label="Polar",
        ),
        "elprop_polar_velocity": BlockOption(
            keyword=ElProp.POLARVELOCITY,
            toolTip="Calculate polarizability with respect to velocity perturbations.",
            label="Velocity Polarizability",
        ),
        "elprop_polar_dip_quad": BlockOption(
            keyword=ElProp.POLARDIPQUAD,
            toolTip="Calculate dipole-quadrupole polarizability.",
            label="Dipole-Quadrupole Polarizability",
        ),
        "elprop_polar_quad_quad": BlockOption(
            keyword=ElProp.POLARQUADQUAD,
            toolTip="Calculate quadrupole-quadrupole polarizability.",
            label="Quadrupole-Quadrupole Polarizability",
        ),
        "elprop_hyper_pol": BlockOption(
            keyword=ElProp.HYPERPOL,
            toolTip="Calculate Dipole-Dipole Polarizability.",
            label="Dip-Dip-Dip Hyperpolarizability",
        ),
        "elprop_freq_r": BlockOption(
            keyword=ElProp.FREQ_R,
            toolTip="Purely real frequency, leave blank for static calculation.",
            label="Real Frequency",
        ),
        "elprop_freq_i": BlockOption(
            keyword=ElProp.FREQ_I,
            toolTip="Purely imaginary frequency, leave blank for static calculation.",
            label="Imaginary Frequency",
        ),
        "elprop_solver": BlockOption(
            keyword=ElProp.SOLVER,
            toolTip="CG: Conjugate Gradient, DIIS: Direct Inversion in the Iterative Subspace.",
            label="CP-SCF Solver",
        ),
        "elprop_max_diis": BlockOption(
            keyword=ElProp.MAXDIIS,
            toolTip="Maximum dimension of DIIS method.",
            label="Max DIIS Dimension",
        ),
        "elprop_shift": BlockOption(
            keyword=ElProp.SHIFT,
            toolTip="Level shift used in DIIS solver",
            label="DIIS Level Shift",
        ),
        "elprop_tol": BlockOption(
            keyword=ElProp.TOL,
            toolTip="Convergence of Coupled-Perturbed SCF Equations (norm of the residual).",
            label="CP-SCF Convergence Tolerance",
        ),
        "elprop_max_iter": BlockOption(
            keyword=ElProp.MAXITER,
            toolTip="Maximum number of iterations in the CP-SCF solver.",
            label="Maximum Iterations",
        ),
        "elprop_print_level": BlockOption(
            keyword=ElProp.PRINTLEVEL,
            toolTip="Control print level for electric property calculation.",
            label="Print Level",
        ),
        "elprop_origin": BlockOption(
            keyword=ElProp.ORIGIN,
            toolTip="Origin to use for electric properties.",
            label="Origin",
        ),
    }

    @classmethod
    def write_tab(cls) -> str:
        """Write the ``options.toml`` entry for this tab."""
        tab = ""
        for key, val in cls.inputs.items():
            tab += f'["{key}"]\n'
            tab += f'label = "{val.label}"\n'
            tab += f'type = "{val.dtype}"\n'
            if val.dtype == "string":
                tab += f'default = "{val.default}"\n'
            elif val.dtype == "boolean":
                tab += f"default = {str(val.default).lower()}\n"
            else:
                tab += f"default = {val.default}\n"

            if val.options is not None:
                tab += "values = [\n"
                for option in val.options:
                    tab += f'    "{option}",\n'
                tab += "]\n"

            if val.minimum is not None:
                tab += f"minimum = {val.minimum}\n"

            if val.maximum is not None:
                tab += f"maximum = {val.maximum}\n"

            if val.toolTip is not None:
                tab += f'toolTip = "{val.toolTip}"\n'

            tab += f'tab = "{cls.name}"\n\n'

        return tab


class BasisTab:
    """Class for writing the %basis tab"""

    inputs = {
        "basis_"
    }




if __name__ == "__main__":
    orca_toml = Path(__file__).parent.parent / "src/avogadro_generators/orca/options.toml"

    toml = "# This file was automatically generated, do NOT modify manually!\n\n"

    toml += 'tabs = ["Basic", "Electric Properties"]\n\n'
    toml += BasicTab.write_tab()
    toml += ElPropTab.write_tab()

    with open(orca_toml, "w") as orca:
        orca.write(toml)
