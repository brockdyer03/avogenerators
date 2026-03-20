# SPDX-FileCopyrightText: 2026 Avogadro Project
# SPDX-License-Identifier: BSD 3-Clause
# ******************************************************************************
# This source file is part of the Avogadro project.
#
# This source code is released under the New BSD License, (the "License").
# ******************************************************************************
"""Input generation for ORCA (https://www.faccts.de/orca/)."""
from .input_blocks import SCF, Basis, ElProp, format_block_keyword
from .simple_keywords import (
    RunType,
    Output,
    match_simple_keyword,
)
from .dft import Composite, Functionals, Disp
from .wft import MP2, CoupledCluster
from .basis_sets import (
    PopleBasisSet,
    def2BasisSet,
    JensenBasisSet,
    ccBasisSet,
    RelativisticBasisSet,
    get_basis_set,
    get_aux_basis,
    get_basis_family,
)
from .implicit_solvation import Solvent, SolvationModel
from ..utilities import Element

def write_block(block_name: str, keys_vals: dict):
    """Write an input block."""
    block = f"%{block_name}\n"

    for key, value in keys_vals.items():
        if key._dtype is str:
            block += f'    {key.name} = "{value}"\n'
        else:
            block += f"    {key.name} = {value}\n"

    block += "end\n"
    return block


def get_method(value: str) -> str | Functionals | Composite | MP2 | CoupledCluster:
    """Get a method from a string."""

    if value == "HF":
        return value
    elif "MP2" in value:
        return MP2(value)
    elif "CCSD" in value:
        return CoupledCluster(value)
    elif "-3c" in value:
        return Composite(value)
    else:
        return Functionals(value)


SCF_BLOCK_KEYWORDS = {
    "scf_guess":           SCF.GUESS,
    "scf_guess_mode":      SCF.GUESSMODE,
    "scf_autostart":       SCF.AUTOSTART,
    "scf_moinp":           SCF.MOINP,
    "scf_convergence":     SCF.CONVERGENCE,
    "scf_tol_e":           SCF.TOL_E,
    "scf_tol_rmsp":        SCF.TOL_RMSP,
    "scf_tol_maxp":        SCF.TOL_MAXP,
    "scf_tol_err":         SCF.TOL_ERR,
    "scf_tol_g":           SCF.TOL_G,
    "scf_tol_x":           SCF.TOL_X,
    "scf_int_thresh":      SCF.THRESH,
    "scf_conv_check_mode": SCF.CONVCHECKMODE,
    "scf_conv_forced":     SCF.CONVFORCED,
}

BASIS_BLOCK_KEYWORDS = {
    # "basis_basis":            Basis.BASIS,
    # "basis_auxj":             Basis.AUXJ,
    # "basis_auxjk":            Basis.AUXJK,
    # "basis_auxc":             Basis.AUXC,
    "basis_cabs":             Basis.CABS,
    "basis_ecp":              Basis.ECP,
    "basis_ghost_ecp":        Basis.GHOSTECP,
    # "basis_decontract":       Basis.DECONTRACT,
    # "basis_decontract_bas":   Basis.DECONTRACTBAS,
    # "basis_decontract_auxj":  Basis.DECONTRACTAUXJ,
    # "basis_decontract_auxjk": Basis.DECONTRACTAUXJK,
    # "basis_decontract_auxc":  Basis.DECONTRACTAUXC,
    # "basis_decontract_cabs":  Basis.DECONTRACTCABS,
    # "basis_pcd_trim_bas":     Basis.PCDTRIMBAS,
    # "basis_pcd_trim_auxj":    Basis.PCDTRIMAUXJ,
    # "basis_pcd_trim_auxjk":   Basis.PCDTRIMAUXJK,
    # "basis_pcd_trim_auxc":    Basis.PCDTRIMAUXC,
    # "basis_pcd_thresh":       Basis.PCDTHRESH,
    "basis_autoaux_size":     Basis.AUTOAUXSIZE,
    # "basis_autoaux_l_max":    Basis.AUTOAUXLMAX,
    # "basis_autoaux_l_limit":  Basis.AUTOAUXLLIMIT,
}

ELPROP_BLOCK_KEYWORDS = {
    "elprop_dipole":          ElProp.DIPOLE,
    "elprop_quadrupole":      ElProp.QUADRUPOLE,
    "elprop_polar":           ElProp.POLAR,
    "elprop_polar_velocity":  ElProp.POLARVELOCITY,
    "elprop_polar_dip_quad":  ElProp.POLARDIPQUAD,
    "elprop_polar_quad_quad": ElProp.POLARQUADQUAD,
    "elprop_hyper_pol":       ElProp.HYPERPOL,
    "elprop_freq_r":          ElProp.FREQ_R,
    "elprop_freq_i":          ElProp.FREQ_I,
    "elprop_solver":          ElProp.SOLVER,
    "elprop_max_diis":        ElProp.MAXDIIS,
    "elprop_shift":           ElProp.SHIFT,
    "elprop_tol":             ElProp.TOL,
    "elprop_max_iter":        ElProp.MAXITER,
    "elprop_print_level":     ElProp.PRINTLEVEL,
    "elprop_origin":          ElProp.ORIGIN,
}

def generateInputFile(input_json: dict) -> tuple[str, list[str], list[str]]:
    # Collect warning strings as we go
    warnings = []
    syntax_groups = ["default"]

    opts = input_json["options"]
    cjson = input_json["cjson"]

    # Extract undefined options:
    title: str          = opts["Title"]
    charge: int         = opts["Charge"]
    multiplicity: int   = opts["Multiplicity"]
    nprocs: int         = opts["Processor Cores"]
    max_mem: int        = opts["Memory"]
    extra_keywords: str = opts["basic_simple_keywords"]

    # Extract defined options
    run_type        = RunType(opts["Calculation Type"])
    method          = get_method(opts["Theory"])
    basis_set       = get_basis_set(opts["Basis"])
    solvent         = opts["Solvent"]
    disp            = opts["basic_disp_corr"]
    print_mos: bool = opts["basic_print_mos"]
    print_level     = Output(opts["basic_print_level"])
    constrain: bool = opts["basic_constrain"]

    # Extract some items from other tabs
    auxj_basis  = get_aux_basis(opts["basis_auxj"])
    auxjk_basis = get_aux_basis(opts["basis_auxjk"])
    auxc_basis  = get_aux_basis(opts["basis_auxc"])

    override_bases = {
        "basis_def2_basis": def2BasisSet,
        "basis_cc_basis": ccBasisSet,
        "basis_pople_basis": PopleBasisSet,
        "basis_jensen_basis": JensenBasisSet,
        "basis_relativistic_basis": RelativisticBasisSet,
    }

    for basis, basis_type in override_bases.items():
        basis = opts[basis]
        if basis == "":
            pass
        else:
            basis_set = basis_type(basis)

    simple_keywords = []

    if "atoms" in cjson:
        for element in set(cjson["atoms"]["elements"]["number"]):
            element = Element(element)
            if element not in basis_set.elements:
                warnings.append(
                    f"Element {element.symbol} is not defined for the {basis_set.value} basis set!"
                )

    if isinstance(method, Functionals):
        if disp == "":
            simple_keywords.extend([method.value, basis_set])
        elif Disp[disp] not in method.disp:
            warnings.append(
                f"The dispersion correction {Disp[disp]} is not available for {method.value}!"
            )
            simple_keywords.extend([method.value, basis_set])
        else:
            simple_keywords.extend([method.value, disp, basis_set])
    elif isinstance(method, Composite):
        basis_set = ""
        simple_keywords.append(method.value)
    elif isinstance(method, (MP2, CoupledCluster)):
        if auxc_basis is None:
            warnings.append("No AuxC basis selected, please select one from the Basis tab.")
            simple_keywords.extend([method.value, basis_set])
        elif auxc_basis.parent_basis != basis_set.__class__.__name__:
            aux_fam  = get_basis_family(auxc_basis.parent_basis)
            main_fam = get_basis_family(basis_set.__class__.__name__)
            warnings.append(
                f"The auxiliary basis {auxc_basis.basis_name} belongs to the {aux_fam} family, but your primary basis is of the {main_fam} family."
            )
            simple_keywords.extend([method.value, basis_set, auxc_basis])
        else:
            simple_keywords.extend([method.value, basis_set, auxc_basis])
    elif method == "HF":
        simple_keywords.extend([method, basis_set])

    if auxj_basis is not None:
        simple_keywords.append(auxj_basis)

    if auxjk_basis is not None:
        simple_keywords.append(auxjk_basis)

    if solvent != "":
        solvent = Solvent(solvent)
        solvent_model = SolvationModel[opts["Solvation Model"].upper()]
        if solvent_model not in solvent.models:
            warnings.append(
                f"Solvation model {solvent_model} not available for solvent {solvent.aliases[0]}!"
            )
        else:
            simple_keywords.append(f"{solvent_model}({solvent})")
        syntax_groups.append("solvent")

    if print_mos:
        simple_keywords.extend([Output.PRINTMOS, Output.PRINTBASIS])

    if print_level != "NormalPrint":
        simple_keywords.append(print_level)

    for keyword in extra_keywords.replace(",", " ").split():
        kwd = match_simple_keyword(keyword)
        if kwd is not None:
            simple_keywords.append(kwd)
        else:
            warnings.append(
                f"Keyword {keyword} is not recognized!"
            )

    generated_input = (
        "# File Generated with Avogadro\n"
       f"# {title}\n"
       f"#\n"
    )
    generated_input += f"!{run_type.value}"
    for kwd in simple_keywords:
        generated_input += f" {kwd}"
    generated_input += " \n" # Trailing whitespace to avoid syntax highlighting bugs

    if max_mem != 4:
        generated_input += f"%MaxCore {int(max_mem*1024/nprocs)}\n"

    if nprocs != 1:
        generated_input += (
            "%pal\n"
           f"    nprocs = {nprocs}\n"
            "end\n"
        )

    if constrain is True and "atoms" in cjson and ("constraints" in cjson or "frozen" in cjson):
        # check for constraints and frozen atoms in cjson
        generated_input += "%geom Constraints\n"

        # look for bond, angle, torsion constraints
        if "constraints" in cjson:
            # loop through the output
            # e.g. "{ B N1 N2 value C }"
            for constraint in cjson["constraints"]:
                if len(constraint) == 3:
                    # distance
                    value, atom1, atom2 = constraint
                    generated_input += f"{{ B {atom1} {atom2} {value:.6f} C }}\n"
                if len(constraint) == 4:
                    # angle
                    value, atom1, atom2, atom3 = constraint
                    generated_input += f"{{ A {atom1} {atom2} {atom3} {value:.6f} C }}\n"
                if len(constraint) == 5:
                    # torsion / dihedral
                    value, atom1, atom2, atom3, atom4 = constraint
                    generated_input += f"{{ D {atom1} {atom2} {atom3} {atom4} {value:.6f} C }}\n"

        # look for frozen atoms
        if "frozen" in cjson["atoms"]:
            # two possibilities - same number of atoms
            # or .. 3*number of atoms
            frozen = cjson["atoms"]["frozen"]
            atomCount = len(cjson["atoms"]["elements"]["number"])
            if len(frozen) == atomCount:
                # look for 1 or 0
                for i in range(len(frozen)):
                    if frozen[i] == 1:
                        generated_input += f"{{ C {i} C }}\n"
            elif len(frozen) == 3 * atomCount:
                # look for 1 or 0 - x, y, z for each atom
                for i in range(0, len(frozen), 3):
                    if frozen[i] == 0:
                        generated_input += f"{{ X {i} C }}\n"
                    if frozen[i + 1] == 0:
                        generated_input += f"{{ Y {i} C }}\n"
                    if frozen[i + 2] == 0:
                        generated_input += f"{{ Z {i} C }}\n"

        generated_input += "end\n"
        generated_input += "end\n\n"

    scf_block = "%scf\n"
    for kwd, kwd_type in SCF_BLOCK_KEYWORDS.items():
        val = opts[kwd]
        try:
            val = kwd_type._dtype(val)
        except ValueError:
            pass
        if not kwd_type.is_default(val):
            scf_block += format_block_keyword(kwd_type, val)
    scf_block += "end\n"

    basis_block = "%basis\n"
    for kwd, kwd_type in BASIS_BLOCK_KEYWORDS.items():
        val = opts[kwd]
        try:
            val = kwd_type._dtype(val)
        except ValueError:
            pass
        if not kwd_type.is_default(val):
            basis_block += format_block_keyword(kwd_type, val)
    basis_block += "end\n"

    elprop_block = "%elprop\n"
    for kwd, kwd_type in ELPROP_BLOCK_KEYWORDS.items():
        val = opts[kwd]
        try:
            val = kwd_type._dtype(val)
        except ValueError:
            pass
        if not kwd_type.is_default(val):
            elprop_block += format_block_keyword(kwd_type, val)
    elprop_block += "end\n"

    if scf_block != "%scf\nend\n":
        generated_input += scf_block
        syntax_groups.append("scf")
    if basis_block != "%basis\nend\n":
        generated_input += basis_block
        syntax_groups.append("basis")
    if elprop_block != "%elprop\nend\n":
        generated_input += elprop_block
        syntax_groups.append("elprop")

    generated_input += f"* xyz {charge} {multiplicity}\n"
    generated_input += "$$coords:___Sxyz$$\n"
    generated_input += "*\n\n\n"

    return generated_input, warnings, syntax_groups


def generateInput(input_json: dict, debug: bool) -> dict:

    generated_input, warnings, syntax_groups = generateInputFile(input_json)

    filename = input_json['options']['Filename Base'] + '.inp'

    result = {
        'files': [
            {
                'filename': filename,
                'contents': generated_input,
                'highlightStyles': syntax_groups,
            },
        ],
        'mainFile': filename,
    }

    if warnings:
        result['warnings'] = warnings

    return result


