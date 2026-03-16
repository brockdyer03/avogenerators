from dataclasses import dataclass
from collections.abc import Sequence

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


@dataclass
class UserOption:
    """Possible values for a user option."""

    dtype:   str # string, stringList, filePath, boolean, integer, float, text, table
    default: str | int
    values:  tuple | None       = None
    toolTip: str | None         = None
    hide:    bool | None        = None
    minimum: int | float | None = None
    maximum: int | float | None = None


class BasicTab:
    """Class for writing the Basic tab"""

    name = "Basic"

    title = UserOption(
        dtype="string",
        default="",
        toolTip="Title of the input file (not recognized by ORCA)",
    )

    file_name_base = UserOption(
        dtype="string",
        default="job",
    )

    processor_cores = UserOption(
        dtype="integer",
        default=1,
        minimum=1,
    )

    memory = UserOption(
        dtype="integer",
        default=4,
        minimum=1,
        toolTip="Total available memory (divided by nprocs to get memory per core)"
    )

    calculation_type = UserOption(
        dtype="stringList",
        default=2, # Opt
        values=(
            RunType.SP,
            RunType.ENGRAD,
            RunType.OPT,
            RunType.OPTTS,
            RunType.FREQ,
            RunType.NUMFREQ,
        ),
        toolTip="Type of calculation to run"
    )

    theory = UserOption(
        dtype="stringList",
        default=0,
        values=(
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
    )

    basis = UserOption(
        dtype="stringList",
        default=6, # def2-TZVP
        values=(
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
    )

    charge = UserOption(
        dtype="integer",
        default=0,
    )

    multiplicity = UserOption(
        dtype="integer",
        default=1,
        minimum=1,
        toolTip="Calculated as 2S+1 where S is the number of unpaired electrons"
    )

    solvent = UserOption(
        dtype="stringList",
        default=0,
        values=(
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
    )

    solvation_model = UserOption(
        dtype="stringList",
        default=0,
        values=(
            "CPCM",     # CPCM
            "SMD",      # SMD
            "COSMO_RS", # COSMO_RS
            "ALPB",     # ALPB
            "ddCOSMO",  # DDCOSMO
            "CPCMX",    # CPCMX
        )
    )

    dispersion_correction = UserOption(
        dtype="stringList",
        default=0,
        values=(
            Disp.NODISP,
            Disp.D3BJ,
            Disp.D3ZERO,
            Disp.D4,
            Disp.NL,
            Disp.SCNL,
        ),
    )

    print_mos = UserOption(
        dtype="boolean",
        default=True,
    )

    print_level = UserOption(
        dtype="stringList",
        default=2, # NormalPrint
        values=(
            Output.MINIPRINT,
            Output.SMALLPRINT,
            Output.NORMALPRINT,
            Output.LARGEPRINT,
        )
    )

    electric_properties = UserOption(
        dtype="string",
        default="",
        toolTip="Comma-separated list of strings",
    )

    inputs = {
        "Title": title,
        "Filename Base": file_name_base,
        "Processor Cores": processor_cores,
        "Memory": memory,
        "Calculation Type": calculation_type,
        "Theory": theory,
        "Basis": basis,
        "Charge": charge,
        "Multiplicity": multiplicity,
        "Solvent": solvent,
        "Solvation Model": solvation_model,
        "Dispersion Correction": dispersion_correction,
        "Print Molecular Orbitals": print_mos,
        "Print Level": print_level,
        "Electric Properties": electric_properties,
    }

    @classmethod
    def write_tab(cls) -> str:
        """Write the ``options.toml`` for this tab."""

        tab = ""
        for key, val in cls.inputs.items():
            tab += f'["{key}"]\n'
            tab += f'type = "{val.dtype}"\n'
            if val.dtype == "string":
                tab += f'default = "{val.default}"\n'
            elif val.dtype == "boolean":
                tab += f"default = {str(val.default).lower()}\n"
            else:
                tab += f"default = {val.default}\n"
            
            if val.values is not None:
                tab += "values = [\n"
                for option in val.values:
                    tab += f'    "{option}",\n'
                tab += "]\n"

            if val.minimum is not None:
                tab += f"minimum = {val.minimum}\n"
            
            if val.maximum is not None:
                tab += f"maximum = {val.maximum}\n"

            if val.toolTip is not None:
                tab += f'toolTip = "{val.toolTip}"\n'

            tab += 'tab = "Basic"\n\n'

        return tab



if __name__ == "__main__":

    toml = "#+ This file was automatically generated, do NOT modify manually!\n\n"

    toml += 'tabs = ["Basic"]\n\n'
    toml += BasicTab.write_tab()

    with open("test.toml", "w") as test:
        test.write(toml)
