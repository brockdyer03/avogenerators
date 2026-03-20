from abc import ABC
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
from avogadro_generators.orca.wft import MP2, CoupledCluster
from avogadro_generators.orca.simple_keywords import (
    RunType,
    SemiEmpirical,
    SCFConv,
    DeterminantType,
    Opt,
    Output,
    Grid,
    RIApproximation,
    PartialCharges,
    Relativistic,
    PNO,
)
from avogadro_generators.orca.implicit_solvation import Solvent, XTBSolvent
from avogadro_generators.orca.input_blocks.block_base import BlockKeyword, ORCAString
from avogadro_generators.orca.input_blocks.elprop import ElProp
from avogadro_generators.orca.input_blocks.basis import Basis
from avogadro_generators.orca.input_blocks.scf import SCF


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
            default=0, # r2SCAN-3c
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
                "HF",
                MP2.RI_MP2,
                MP2.DLPNO_MP2,
                MP2.SCS_DLPNO_MP2,
                CoupledCluster.RI_CCSD_T_,
                CoupledCluster.DLPNO_CCSD_T_,
                CoupledCluster.DLPNO_CCSD_T1_,
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
        "basic_constrain": BasicOption(
            dtype="boolean",
            default=False,
            label="Use Constraints",
        ),
        "basic_simple_keywords": BasicOption(
            dtype="string",
            default="",
            label="Additional Simple Keywords",
            toolTip="Comma- or whitespace-separated list of simple input keywords.",
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
        add_dummy: bool = False,
    ):
        self.option_name = keyword.key_name
        self.dtype       = keyword.dtype
        self.options     = keyword.options
        self.default     = keyword.default
        self.minimum     = keyword.minimum
        self.maximum     = keyword.maximum
        self.label       = label
        self.toolTip     = toolTip
        self.add_dummy   = add_dummy


class BlockTab(ABC):
    """Abstract class for block tabs"""

    @classmethod
    def write_tab(cls) -> str:
        """Write the ``options.toml`` entry for this tab."""
        tab = ""
        if hasattr(cls, "extra_inputs"):
            for key, val in cls.extra_inputs.items():
                tab += f'["{key}"]\n'
                tab += f'label = "{val.label}"\n'
                tab += f'type = "{val.dtype}"\n'
                if val.dtype == "string" and val.default is not None:
                    tab += f'default = "{val.default}"\n'
                elif val.dtype == "boolean" and val.default is not None:
                    tab += f"default = {str(val.default).lower()}\n"
                elif val.default is not None:
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

        for key, val in cls.inputs.items():
            tab += f'["{key}"]\n'
            tab += f'label = "{val.label}"\n'
            tab += f'type = "{val.dtype}"\n'
            if val.dtype == "string" and val.default is not None:
                if val.options is None:
                    tab += f'default = "{val.default}"\n'
                else:
                    tab += f'default = {val.default}\n'
            elif val.dtype == "boolean" and val.default is not None:
                tab += f"default = {str(val.default).lower()}\n"
            elif val.default is not None:
                tab += f"default = {val.default}\n"

            if val.options is not None:
                tab += "values = [\n"
                if val.add_dummy: # Add a blank option at the beginning.
                    tab += '    "",\n'
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


class ElPropTab(BlockTab):
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


class BasisTab(BlockTab):
    """Class for writing the %basis tab"""

    name = "Basis"

    inputs = {
        # "basis_basis": BlockOption(
        #     keyword=Basis.BASIS,
        #     toolTip="Specify a basis set.",
        #     label="Basis",
        # ),
        "basis_auxj": BlockOption(
            keyword=Basis.AUXJ,
            toolTip="Specify a Coulomb-fitting auxiliary basis set.",
            label="AuxJ",
            add_dummy=True,
        ),
        "basis_auxjk": BlockOption(
            keyword=Basis.AUXJK,
            toolTip="Specify a Coulomb- and Exchange-fitting auxiliary basis set.",
            label="AuxJK",
            add_dummy=True,
        ),
        "basis_auxc": BlockOption(
            keyword=Basis.AUXC,
            toolTip="Specify a Post-HF auxiliary basis set.",
            label="AuxC",
            add_dummy=True,
        ),
        "basis_cabs": BlockOption(
            keyword=Basis.CABS,
            toolTip="Specify a Complementary Auxiliary Basis Set (CABS) for F12 calculations.",
            label="CABS (F12 only)",
        ),
        "basis_ecp": BlockOption(
            keyword=Basis.ECP,
            toolTip="Specify an Effective Core Potential (ECP).",
            label="ECP",
        ),
        "basis_ghost_ecp": BlockOption(
            keyword=Basis.GHOSTECP,
            toolTip="Specify whether or not to use ECPs for Ghost atoms.",
            label="Allow Ghost ECPs",
        ),
        # "basis_decontract": BlockOption(
        #     keyword=Basis.DECONTRACT,
        #     toolTip="Decontract all orbital and auxiliary basis sets.",
        #     label="Decontract All",
        # ),
        # "basis_decontract_bas": BlockOption(
        #     keyword=Basis.DECONTRACTBAS,
        #     toolTip="Decontract only orbital basis sets.",
        #     label="Decontract Orbital Basis",
        # ),
        # "basis_decontract_auxj": BlockOption(
        #     keyword=Basis.DECONTRACTAUXJ,
        #     toolTip="Decontract only AuxJ basis sets.",
        #     label="Decontract AuxJ Basis",
        # ),
        # "basis_decontract_auxjk": BlockOption(
        #     keyword=Basis.DECONTRACTAUXJK,
        #     toolTip="Decontract only AuxJK basis sets.",
        #     label="Decontract AuxJK Basis",
        # ),
        # "basis_decontract_auxc": BlockOption(
        #     keyword=Basis.DECONTRACTAUXC,
        #     toolTip="Decontract only AuxC basis sets.",
        #     label="Decontract AuxC Basis",
        # ),
        # "basis_decontract_cabs": BlockOption(
        #     keyword=Basis.DECONTRACTCABS,
        #     toolTip="Decontract only CABS basis sets.",
        #     label="Decontract CABS Basis",
        # ),
        # "basis_pcd_trim_bas": BlockOption(
        #     keyword=Basis.PCDTRIMBAS,
        #     toolTip="Trim the orbital basis in the overlap metric.",
        #     label="Trim Orbital Basis",
        # ),
        # "basis_pcd_trim_auxj": BlockOption(
        #     keyword=Basis.PCDTRIMAUXJ,
        #     toolTip="Trim the AuxJ basis in the Coulomb metric.",
        #     label="Trim AuxJ Basis",
        # ),
        # "basis_pcd_trim_auxjk": BlockOption(
        #     keyword=Basis.PCDTRIMAUXJK,
        #     toolTip="Trim the AuxJK basis in the Coulomb metric.",
        #     label="Trim AuxJK Basis",
        # ),
        # "basis_pcd_trim_auxc": BlockOption(
        #     keyword=Basis.PCDTRIMAUXC,
        #     toolTip="Trim the AuxC basis in the Coulomb metric.",
        #     label="Trim AuxC Basis",
        # ),
        # "basis_pcd_thresh": BlockOption(
        #     keyword=Basis.PCDTHRESH,
        #     toolTip="Threshold for PCD (suggested 1e-16 to 1e-10, automatically chosen if < 0).",
        #     label="PCD Threshold",
        # ),
        "basis_autoaux_size": BlockOption(
            keyword=Basis.AUTOAUXSIZE,
            toolTip="Control size of AutoAux basis sets. Larger value means larger basis.",
            label="AutoAux Size",
        ),
        "basis_autoaux_l_max": BlockOption(
            keyword=Basis.AUTOAUXLMAX,
            toolTip="Enable use of highest-possible angular momentum permitted by ORCA",
            label="AutoAux L Max",
        ),
        "basis_autoaux_l_limit": BlockOption(
            keyword=Basis.AUTOAUXLLIMIT,
            toolTip="Set the highest allowed angular momentum (-1 means do not set limit)",
            label="AutoAux L Limit",
        ),
        # "basis_autoaux_f_0": BlockOption(
        #     keyword=Basis.AUTOAUXF_0,
        #     toolTip="Factor by which to increase the maximal s-exponent.",
        #     label="AutoAux F[0]",
        # ),
        # "basis_autoaux_f_1": BlockOption(
        #     keyword=Basis.AUTOAUXF_1,
        #     toolTip="Factor by which to increase the maximal p-exponent.",
        #     label="AutoAux F[1]",
        # ),
        # "basis_autoaux_f_2": BlockOption(
        #     keyword=Basis.AUTOAUXF_2,
        #     toolTip="Factor by which to increase the maximal d-exponent.",
        #     label="AutoAux F[2]",
        # ),
        # "basis_autoaux_f_3": BlockOption(
        #     keyword=Basis.AUTOAUXF_3,
        #     toolTip="Factor by which to increase the maximal f-exponent.",
        #     label="AutoAux F[3]",
        # ),
        # "basis_autoaux_f_4": BlockOption(
        #     keyword=Basis.AUTOAUXF_4,
        #     toolTip="Factor by which to increase the maximal g-exponent.",
        #     label="AutoAux F[4]",
        # ),
        # "basis_autoaux_f_5": BlockOption(
        #     keyword=Basis.AUTOAUXF_5,
        #     toolTip="Factor by which to increase the maximal h-exponent.",
        #     label="AutoAux F[5]",
        # ),
        # "basis_autoaux_f_6": BlockOption(
        #     keyword=Basis.AUTOAUXF_6,
        #     toolTip="Factor by which to increase the maximal i-exponent.",
        #     label="AutoAux F[6]",
        # ),
        # "basis_autoaux_f_7": BlockOption(
        #     keyword=Basis.AUTOAUXF_7,
        #     toolTip="Factor by which to increase the maximal j-exponent.",
        #     label="AutoAux F[7]",
        # ),
        # "basis_autoaux_B_0": BlockOption(
        #     keyword=Basis.AUTOAUXB_0,
        #     toolTip="Even-tempered expansion factor for the s-shell.",
        #     label="AutoAux B[0]",
        # ),
        # "basis_autoaux_B_1": BlockOption(
        #     keyword=Basis.AUTOAUXB_1,
        #     toolTip="Even-tempered expansion factor for the p-shell.",
        #     label="AutoAux B[1]",
        # ),
        # "basis_autoaux_B_2": BlockOption(
        #     keyword=Basis.AUTOAUXB_2,
        #     toolTip="Even-tempered expansion factor for the d-shell.",
        #     label="AutoAux B[2]",
        # ),
        # "basis_autoaux_B_3": BlockOption(
        #     keyword=Basis.AUTOAUXB_3,
        #     toolTip="Even-tempered expansion factor for the f-shell.",
        #     label="AutoAux B[3]",
        # ),
        # "basis_autoaux_B_4": BlockOption(
        #     keyword=Basis.AUTOAUXB_4,
        #     toolTip="Even-tempered expansion factor for the g-shell.",
        #     label="AutoAux B[4]",
        # ),
        # "basis_autoaux_B_5": BlockOption(
        #     keyword=Basis.AUTOAUXB_5,
        #     toolTip="Even-tempered expansion factor for the h-shell.",
        #     label="AutoAux B[5]",
        # ),
        # "basis_autoaux_B_6": BlockOption(
        #     keyword=Basis.AUTOAUXB_6,
        #     toolTip="Even-tempered expansion factor for the i-shell.",
        #     label="AutoAux B[6]",
        # ),
        # "basis_autoaux_B_7": BlockOption(
        #     keyword=Basis.AUTOAUXB_7,
        #     toolTip="Even-tempered expansion factor for the j-shell.",
        #     label="AutoAux B[7]",
        # ),
        # "basis_autoaux_tight_b": BlockOption(
        #     keyword=Basis.AUTOAUXTIGHTB,
        #     toolTip="Only use AutoAuxB[1] for shells with high L and AutoAuxB[0] for the rest.",
        #     label="AutoAux Tight B",
        # ),
    }

    extra_inputs = {
        "basis_pople_basis": BasicOption(
            dtype="stringList",
            default=0,
            label="Pople Basis Set",
            options=[""]+[str(i) for i in PopleBasisSet],
            toolTip="Pople-style split-valence basis sets.",
        ),
        "basis_def2_basis": BasicOption(
            dtype="stringList",
            default=0,
            label="def2 Basis Set",
            options=[""]+[str(i) for i in def2BasisSet],
            toolTip="Karlsruhe def2-n(Z)VP basis sets.",
        ),
        "basis_cc_basis": BasicOption(
            dtype="stringList",
            default=0,
            label="cc-pVnZ Basis Set",
            options=[""]+[str(i) for i in ccBasisSet],
            toolTip="Correlation Consistent basis sets.",
        ),
        "basis_jensen_basis": BasicOption(
            dtype="stringList",
            default=0,
            label="pc-n Basis Set",
            options=[""]+[str(i) for i in JensenBasisSet],
            toolTip="Jensen's Polarization-Consistent basis sets.",
        ),
        "basis_relativistic_basis": BasicOption(
            dtype="stringList",
            default=0,
            label="Relativistic Basis Set",
            options=[""]+[str(i) for i in RelativisticBasisSet],
            toolTip="Relativistic SARC/ZORA/DKH/x2c basis sets.",
        ),
    }


class SCFTab(BlockTab):
    """Class for writing the %scf tab"""

    name = "SCF"

    inputs = {
        "scf_guess": BlockOption(
            keyword=SCF.GUESS,
            toolTip="Pick initial guess for SCF orbitals",
            label="Initial Guess",
        ),
        "scf_guess_mode": BlockOption(
            keyword=SCF.GUESSMODE,
            toolTip="Mode for projecting initial guess orbitals onto the basis set (not for Guess=HCore)",
            label="Guess Mode",
        ),
        "scf_autostart": BlockOption(
            keyword=SCF.AUTOSTART,
            toolTip="Try to use orbitals from existing GBW file of the same name (if it exists).",
            label="AutoStart",
        ),
        "scf_moinp": BlockOption(
            keyword=SCF.MOINP,
            toolTip="GBW file used for MORead",
            label="MOInp GBW File",
        ),
        "scf_convergence": BlockOption(
            keyword=SCF.CONVERGENCE,
            toolTip="Set the SCF convergence tolerances.",
            label="Convergence Tolerance",
        ),
        "scf_tol_e": BlockOption(
            keyword=SCF.TOL_E,
            toolTip="Set the SCF energy convergence criteria.",
            label="Energy Tolerance",
        ),
        "scf_tol_rmsp": BlockOption(
            keyword=SCF.TOL_RMSP,
            toolTip="Set the SCF RMS density change convergence criteria.",
            label="RMS Density Tolerance",
        ),
        "scf_tol_maxp": BlockOption(
            keyword=SCF.TOL_MAXP,
            toolTip="Set the SCF maximum density change convergence criteria.",
            label="Max Density Tolerance",
        ),
        "scf_tol_err": BlockOption(
            keyword=SCF.TOL_ERR,
            toolTip="Set the SCF DIIS Error convergence criteria.",
            label="DIIS Error Tolerance",
        ),
        "scf_tol_g": BlockOption(
            keyword=SCF.TOL_G,
            toolTip="Set the SCF orbital gradient convergence criteria.",
            label="Orbital Gradient Tolerance",
        ),
        "scf_tol_x": BlockOption(
            keyword=SCF.TOL_X,
            toolTip="Set the SCF orbital rotation angle convergence criteria.",
            label="Orbital Rotation Angle Tolerance",
        ),
        "scf_int_thresh": BlockOption(
            keyword=SCF.THRESH,
            toolTip="Set the SCF integral prescreening threshold.",
            label="Integral Prescreening Threshold",
        ),
        "scf_conv_check_mode": BlockOption(
            keyword=SCF.CONVCHECKMODE,
            toolTip="Set the SCF convergence check mode.",
            label="Convergence Check Mode",
        ),
        "scf_conv_forced": BlockOption(
            keyword=SCF.CONVFORCED,
            toolTip="Toggle whether or not convergence is mandatory for the next calculation step.",
            label="Require Convergence",
        ),
        # "scf_hf_type": BlockOption(
        #     keyword=SCF.HFTYP,
        #     toolTip="Set the wavefunction type for HF calculations.",
        #     label="HF Wavefunction Type",
        # ),
        # "scf_rohf_case": BlockOption(
        #     keyword=SCF.ROHF_CASE,
        #     toolTip="Type of ROHF wavefunction (only if HFTyp=ROHF).",
        #     label="ROHF Case",
        # ),
        # "scf_rohf_nel": BlockOption(
        #     keyword=SCF.ROHF_NEL,
        #     toolTip="Number of open-shell electrons (only if HFTyp=ROHF).",
        #     label="ROHF Num. Electrons",
        # ),
        # "scf_rohf_numop": BlockOption(
        #     keyword=SCF.ROHF_NUMOP,
        #     toolTip="Number of Operators (only if HFTyp=ROHF).",
        #     label="ROHF Num. Operators",
        # ),
        # "scf_rohf_norb": BlockOption(
        #     keyword=SCF.ROHF_NORB,
        #     toolTip="Number of open-shell orbitals (only if HFTyp=ROHF).",
        #     label="ROHF Num. Orbitals",
        # ),
        # # "scf_rohf_ref": BlockOption(
        # #     keyword=SCF.ROHF_REF,
        # #     toolTip="Specify orbital rotations (only if HFTyp=ROHF).",
        # #     label="ROHF Orbital Rotations",
        # # ),
        # # "scf_rohf_aforbs": BlockOption(
        # #     keyword=SCF.ROHF_AFORBS,
        # #     toolTip="User-defined anti-ferromagnetic orbitals (only if HFTyp=ROHF).",
        # #     label="ROHF AF Orbitals",
        # # ),
        # "scf_xtbfod": BlockOption(
        #     keyword=SCF.XTBFOD,
        #     toolTip="Enable FOD Printout for native-xTB calculations.",
        #     label="xTB FOD Printout",
        # ),
        # "scf_use_xtb_mixer": BlockOption(
        #     keyword=SCF.USEXTBMIXER,
        #     toolTip="Use special SCF settings similar to the ones in xTB.",
        #     label="Use xTB Mixer",
        # ),
        # "scf_soscf_max_step": BlockOption(
        #     keyword=SCF.SOSCFMAXSTEP,
        #     toolTip="Maximum SOSCF Step Size.",
        #     label="SOSCF Max Step",
        # ),
        # "scf_soscf_block_diag": BlockOption(
        #     keyword=SCF.SOSCFBLOCKDIAG,
        #     toolTip="Perform a diagonalization of the occupied and virtual orbital blocks of the Fock matrix at the start.",
        #     label="Use SOSCF Block Diagonalization",
        # ),
        # "scf_delta_scf_from_gs": BlockOption(
        #     keyword=SCF.DELTASCFFROMGS,
        #     toolTip="Start ΔSCF from an input converged ground state solution or assume it is an excited state solution.",
        #     label="Start ΔSCF From Ground State",
        # ),
        # "scf_do_mom": BlockOption(
        #     keyword=SCF.DOMOM,
        #     toolTip="Use maximum overlap method.",
        #     label="Use Maximum Overlap Method",
        # ),
        # "scf_keep_initial_ref": BlockOption(
        #     keyword=SCF.KEEPINITIALREF,
        #     toolTip="Always keep initial reference: IMOM.",
        #     label="Keep Initial Reference",
        # ),
        # "scf_pmom": BlockOption(
        #     keyword=SCF.PMOM,
        #     toolTip="Use the PMOM metric instead of regular MOM.",
        #     label="Use PMOM Metric",
        # ),
        # # "scf_alpha_conf": BlockOption(
        # #     keyword=SCF.ALPHACONF,
        # #     toolTip="Define occupation of frontier orbitals in the alpha spin channel.",
        # #     label="Alpha Configuration",
        # # ),
        # # "scf_beta_conf": BlockOption(
        # #     keyword=SCF.BETACONF,
        # #     toolTip="Define occupation of frontier orbitals in the beta spin channel.",
        # #     label="Beta Configuration",
        # # ),
        # "scf_ionize_alpha": BlockOption(
        #     keyword=SCF.IONIZEALPHA,
        #     toolTip="Remove electrons from specified MOs in alpha spin channel.",
        #     label="Ionize Alpha",
        # ),
        # "scf_ionize_beta": BlockOption(
        #     keyword=SCF.IONIZEBETA,
        #     toolTip="Remove electrons from specified MOs in beta spin channel.",
        #     label="Ionize Beta",
        # ),
        # "scf_soscf_hess_up": BlockOption(
        #     keyword=SCF.SOSCFHESSUP,
        #     toolTip="Select quasi-Newton method for SOSCF Hessian Update.",
        #     label="SOSCF Hessian Update Method",
        # ),
        # "scf_soscf_constraints": BlockOption(
        #     keyword=SCF.SOSCFCONSTRAINTS,
        #     toolTip="Activate freeze-and-release SOSCF.",
        #     label="SOSCF Contraints",
        # ),
        # "scf_soscf_constrained_maxstep": BlockOption(
        #     keyword=SCF.SOSCFCONSTRAINEDMAXSTEP,
        #     toolTip="Maximum step size for the constrained SOSCF minimization.",
        #     label="SOSCF Const. Max Step",
        # ),
        # "scf_soscf_conv_factor": BlockOption(
        #     keyword=SCF.SOSCFCONVFACTOR,
        #     toolTip="Factor to multiply convergence criteria with in the constrained minimization. e.g. 100 loosens the criteria by two orders of magnitude.",
        #     label="SOSCF Conv. Factor",
        # ),
        # "scf_soscf_constrained_hess_up": BlockOption(
        #     keyword=SCF.SOSCFCONSTRAINEDHESSUP,
        #     toolTip="SOSCF Hessian update for constrained minimization.",
        #     label="SOSCF Const. Hess. Update",
        # ),
        # "scf_soscf_write_constrained_gbw": BlockOption(
        #     keyword=SCF.SOSCFWRITECONSTRAINEDGBW,
        #     toolTip="Write a GBW file for the constrained solution.",
        #     label="Write SOSCF Const. GBW",
        # ),
        # "scf_soscf_davidson_maxit": BlockOption(
        #     keyword=SCF.SOSCFDAVIDSONMAXIT,
        #     toolTip="Maximum number of iterations for Davidson diagonalization in SOSCF procedure.",
        #     label="SOSCF Davidson MaxIter",
        # ),
        # "scf_soscf_davidson_tol_r": BlockOption(
        #     keyword=SCF.SOSCFDAVIDSONTOLR,
        #     toolTip="SOSCF Davidson convergence tolerance for the maximum component of each residual vector.",
        #     label="SOSCF Davidson Residual Tol.",
        # ),
        # "scf_soscf_max_red": BlockOption(
        #     keyword=SCF.SOSCFDAVIDSONMAXRED,
        #     toolTip="Davidson maximum size of the Krylov subspace per target eigenvector, meaning this will be multiplied by the target saddle point order.",
        #     label="SOSCF Davidson Max Reduction",
        # ),
        # "scf_soscf_davidson_fd_mode": BlockOption(
        #     keyword=SCF.SOSCFDAVIDSONFDMODE,
        #     toolTip="SOSCF Davidson finite difference stencil.",
        #     label="SOSCF Davidson FD Stencil",
        # ),
        # "scf_soscf_davidson_fd_step": BlockOption(
        #     keyword=SCF.SOSCFDAVIDSONFDSTEP,
        #     toolTip="Davidson finite difference step size.",
        #     label="SOSCF Davidson FD Step",
        # ),
        # "scf_soscf_precond_type": BlockOption(
        #     keyword=SCF.SOSCFPRECONDTYPE,
        #     toolTip="SOSCF Preconditioner to use",
        #     label="SOSCF Preconditioner",
        # ),
        # "scf_soscf_precond_gamma": BlockOption(
        #     keyword=SCF.SOSCFPRECONDGAMMA,
        #     toolTip="Mixing Factor for GradientExpansion preconditioner",
        #     label="SOSCF Preconditioner Gamma (GradientExpansion only)",
        # ),
        # "scf_soscf_gmf": BlockOption(
        #     keyword=SCF.SOSCFGMF,
        #     toolTip="Use generalized mode following (GMF).",
        #     label="Use GMF",
        # ),
        # "scf_soscf_spo": BlockOption(
        #     keyword=SCF.SOSCFSPO,
        #     toolTip="GMF only: Optional user-defined target saddle point order (SPO).",
        #     label="GMF Saddle Point Order (SPO)",
        # ),
        # "scf_soscf_spo_est": BlockOption(
        #     keyword=SCF.SOSCFSPOEST,
        #     toolTip="GMF only: Target saddle point order estimate.",
        #     label="GMF SPO Estimate",
        # ),
        # "scf_soscf_update_spo_est": BlockOption(
        #     keyword=SCF.SOSCFUPDATESPOEST,
        #     toolTip="GMF only: Update the SPO with the number of negative eigenvalues of the first Davidson run.",
        #     label="GMF Update SPO Estimate",
        # ),
        # "scf_soscf_spo_est_ntrial": BlockOption(
        #     keyword=SCF.SOSCFSPOESTNTRIAL,
        #     toolTip="GMF Only: How many eigenvectors of the Hessian to target more for the SPO estimate.",
        #     label="GMF SPO Num Eigenvectors",
        # ),
        # "scf_soscf_update_spo_thresh": BlockOption(
        #     keyword=SCF.SOSCFUPDATESPOTHRESH,
        #     toolTip="GMF Only: Only eigenvalues below this threshold are considered negative enough for the SPO estimate.",
        #     label="GMF SPO Eigenvalue Threshold",
        # ),
    }


if __name__ == "__main__":
    orca_toml = Path(__file__).parent.parent / "src/avogadro_generators/orca/options.toml"

    toml = "# This file was automatically generated, do NOT modify manually!\n\n"

    toml += f'tabs = ["{BasicTab.name}", "{BasisTab.name}", "{SCFTab.name}", "{ElPropTab.name}"]\n\n'
    toml += BasicTab.write_tab()
    toml += ElPropTab.write_tab()
    toml += BasisTab.write_tab()
    toml += SCFTab.write_tab()

    with open(orca_toml, "w") as orca:
        orca.write(toml)
