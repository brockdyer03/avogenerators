# SPDX-FileCopyrightText: 2026 Avogadro Project
# SPDX-License-Identifier: BSD 3-Clause
# ******************************************************************************
# This source file is part of the Avogadro project.
#
# This source code is released under the New BSD License, (the "License").
# ******************************************************************************
"""Input generation for ORCA (https://www.faccts.de/orca/)."""
from .input_blocks.scf import SCF
from .input_blocks.basis import Basis
from .input_blocks.elprop import ElProp
from .simple_keywords import (
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
from .dft import Composite, Functionals, Disp
from .basis_sets import (
    PopleBasisSet,
    def2BasisSet,
    JensenBasisSet,
    ccBasisSet,
    RelativisticBasisSet,
    AuxJBasisSet,
    AuxJKBasisSet,
    AuxCBasisSet,
)
from .implicit_solvation import Solvent, SolvationModel

BASIC_TAB_KEYWORDS = {
    "Title": str,
    "Filename Base": str,
    "Processor Cores": int,
    "Memory": int,
    "Calculation Type": RunType,
    "Theory": (Composite, Functionals),
    "Basis": (def2BasisSet, ccBasisSet, JensenBasisSet),
    "Charge": int,
    "Multiplicity": int,
    "Solvent": Solvent,
    "Solvation Model": str,
    "basic_disp_corr": Disp,
    "basic_print_mos": bool,
    "basic_print_level": Output,
}

SCF_BLOCK_KEYWORDS = {
    "scf_guess":                       SCF.GUESS,
    "scf_guess_mode":                  SCF.GUESSMODE,
    "scf_autostart":                   SCF.AUTOSTART,
    "scf_moinp":                       SCF.MOINP,
    "scf_convergence":                 SCF.CONVERGENCE,
    "scf_tol_e":                       SCF.TOL_E,
    "scf_tol_rmsp":                    SCF.TOL_RMSP,
    "scf_tol_maxp":                    SCF.TOL_MAXP,
    "scf_tol_err":                     SCF.TOL_ERR,
    "scf_tol_g":                       SCF.TOL_G,
    "scf_tol_x":                       SCF.TOL_X,
    "scf_int_thresh":                  SCF.THRESH,
    "scf_conv_check_mode":             SCF.CONVCHECKMODE,
    "scf_conv_forced":                 SCF.CONVFORCED,
    "scf_hf_type":                     SCF.HFTYP,
    "scf_rohf_case":                   SCF.ROHF_CASE,
    "scf_rohf_nel":                    SCF.ROHF_NEL,
    "scf_rohf_numop":                  SCF.ROHF_NUMOP,
    "scf_rohf_norb":                   SCF.ROHF_NORB,
    # "scf_rohf_ref":                    SCF.ROHF_REF,
    # "scf_rohf_aforbs":                 SCF.ROHF_AFORBS,
    "scf_xtbfod":                      SCF.XTBFOD,
    "scf_use_xtb_mixer":               SCF.USEXTBMIXER,
    "scf_soscf_max_step":              SCF.SOSCFMAXSTEP,
    "scf_soscf_block_diag":            SCF.SOSCFBLOCKDIAG,
    "scf_delta_scf_from_gs":           SCF.DELTASCFFROMGS,
    "scf_do_mom":                      SCF.DOMOM,
    "scf_keep_initial_ref":            SCF.KEEPINITIALREF,
    "scf_pmom":                        SCF.PMOM,
    # "scf_alpha_conf":                  SCF.ALPHACONF,
    # "scf_beta_conf":                   SCF.BETACONF,
    "scf_ionize_alpha":                SCF.IONIZEALPHA,
    "scf_ionize_beta":                 SCF.IONIZEBETA,
    "scf_soscf_hess_up":               SCF.SOSCFHESSUP,
    "scf_soscf_constraints":           SCF.SOSCFCONSTRAINTS,
    "scf_soscf_constrained_maxstep":   SCF.SOSCFCONSTRAINEDMAXSTEP,
    "scf_soscf_conv_factor":           SCF.SOSCFCONVFACTOR,
    "scf_soscf_constrained_hess_up":   SCF.SOSCFCONSTRAINEDHESSUP,
    "scf_soscf_write_constrained_gbw": SCF.SOSCFWRITECONSTRAINEDGBW,
    "scf_soscf_davidson_maxit":        SCF.SOSCFDAVIDSONMAXIT,
    "scf_soscf_davidson_tol_r":        SCF.SOSCFDAVIDSONTOLR,
    "scf_soscf_max_red":               SCF.SOSCFDAVIDSONMAXRED,
    "scf_soscf_davidson_fd_mode":      SCF.SOSCFDAVIDSONFDMODE,
    "scf_soscf_davidson_fd_step":      SCF.SOSCFDAVIDSONFDSTEP,
    "scf_soscf_precond_type":          SCF.SOSCFPRECONDTYPE,
    "scf_soscf_precond_gamma":         SCF.SOSCFPRECONDGAMMA,
    "scf_soscf_gmf":                   SCF.SOSCFGMF,
    "scf_soscf_spo":                   SCF.SOSCFSPO,
    "scf_soscf_spo_est":               SCF.SOSCFSPOEST,
    "scf_soscf_update_spo_est":        SCF.SOSCFUPDATESPOEST,
    "scf_soscf_spo_est_ntrial":        SCF.SOSCFSPOESTNTRIAL,
    "scf_soscf_update_spo_thresh":     SCF.SOSCFUPDATESPOTHRESH,
}

BASIS_BLOCK_KEYWORDS = {
    "basis_basis":            Basis.BASIS,
    "basis_auxj":             Basis.AUXJ,
    "basis_auxjk":            Basis.AUXJK,
    "basis_auxc":             Basis.AUXC,
    "basis_cabs":             Basis.CABS,
    "basis_ecp":              Basis.ECP,
    "basis_ghost_ecp":        Basis.GHOSTECP,
    "basis_decontract":       Basis.DECONTRACT,
    "basis_decontract_bas":   Basis.DECONTRACTBAS,
    "basis_decontract_auxj":  Basis.DECONTRACTAUXJ,
    "basis_decontract_auxjk": Basis.DECONTRACTAUXJK,
    "basis_decontract_auxc":  Basis.DECONTRACTAUXC,
    "basis_decontract_cabs":  Basis.DECONTRACTCABS,
    "basis_pcd_trim_bas":     Basis.PCDTRIMBAS,
    "basis_pcd_trim_auxj":    Basis.PCDTRIMAUXJ,
    "basis_pcd_trim_auxjk":   Basis.PCDTRIMAUXJK,
    "basis_pcd_trim_auxc":    Basis.PCDTRIMAUXC,
    "basis_pcd_thresh":       Basis.PCDTHRESH,
    "basis_autoaux_size":     Basis.AUTOAUXSIZE,
    "basis_autoaux_l_max":    Basis.AUTOAUXLMAX,
    "basis_autoaux_l_limit":  Basis.AUTOAUXLLIMIT,
    "basis_autoaux_f_0":      Basis.AUTOAUXF_0,
    "basis_autoaux_f_1":      Basis.AUTOAUXF_1,
    "basis_autoaux_f_2":      Basis.AUTOAUXF_2,
    "basis_autoaux_f_3":      Basis.AUTOAUXF_3,
    "basis_autoaux_f_4":      Basis.AUTOAUXF_4,
    "basis_autoaux_f_5":      Basis.AUTOAUXF_5,
    "basis_autoaux_f_6":      Basis.AUTOAUXF_6,
    "basis_autoaux_f_7":      Basis.AUTOAUXF_7,
    "basis_autoaux_B_0":      Basis.AUTOAUXB_0,
    "basis_autoaux_B_1":      Basis.AUTOAUXB_1,
    "basis_autoaux_B_2":      Basis.AUTOAUXB_2,
    "basis_autoaux_B_3":      Basis.AUTOAUXB_3,
    "basis_autoaux_B_4":      Basis.AUTOAUXB_4,
    "basis_autoaux_B_5":      Basis.AUTOAUXB_5,
    "basis_autoaux_B_6":      Basis.AUTOAUXB_6,
    "basis_autoaux_B_7":      Basis.AUTOAUXB_7,
    "basis_autoaux_tight_b":  Basis.AUTOAUXTIGHTB,
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

def generateInputFile(input_json: dict) -> tuple[str, list[str]]:
    # Collect warning strings as we go
    warnings = []

    opts = input_json["options"]
    cjson = input_json["cjson"]

    # Extract options:
    title = opts["Title"]
    calculate = opts["Calculation Type"]
    theory = opts["Theory"]
    basis = opts["Basis"]
    charge = opts["Charge"]
    multiplicity = opts["Multiplicity"]
    nCores = int(opts["Processor Cores"])
    memory = int((opts["Memory"] * 1024) / nCores)
    solvtype = opts["Solvation Model"]
    solvent = opts["Solvent"]
    mos = opts["Print Molecular Orbitals"]
    sym = opts["Use Symmetry"]
    constrain = opts["Constrain Geometry"]
    # autoaux = opts["AutoAux"]
    disp = opts["Dispersion Correction"]
    ri = opts["RI Approximation"]
    auxbasis = "None"
    excit = opts["Excited State Method"]
    nroots = opts["Number of States"]
    iroot = opts["Target State"]

    rijbasis = {
        "6-31G(d)": "AutoAux",
        "cc-pVDZ": "Def2/J",
        "cc-pVTZ": "Def2/J",
        "cc-pVQZ": "Def2/J",
        "aug-cc-pVDZ": "AutoAux",
        "aug-cc-pVTZ": "AutoAux",
        "aug-cc-pVQZ": "AutoAux",
        "def2-SVP": "Def2/J",
        "def2-TZVP": "Def2/J",
        "def2-QZVP": "Def2/J",
        "def2-TZVPP": "Def2/J",
        "def2-QZVPP": "Def2/J",
        "def2-TZVPPD": "AutoAux",
        "def2-QZVPPD": "AutoAux",
        "ma-def2-SVP": "AutoAux",
        "ma-def2-TZVP": "AutoAux",
        "ma-def2-QZVP": "AutoAux",
    }

    rijkbasis = {
        "6-31G(d)": "AutoAux",
        "cc-pVDZ": "cc-pVDZ/JK",
        "cc-pVTZ": "cc-pVTZ/JK",
        "cc-pVQZ": "cc-pVQZ/JK",
        "aug-cc-pVDZ": "aug-cc-pVDZ/JK",
        "aug-cc-pVTZ": "aug-cc-pVTZ/JK",
        "aug-cc-pVQZ": "aug-cc-pVQZ/JK",
        "def2-SVP": "Def2/JK",
        "def2-TZVP": "Def2/JK",
        "def2-QZVP": "Def2/JK",
        "def2-TZVPP": "Def2/JK",
        "def2-QZVPP": "Def2/JK",
        "def2-TZVPPD": "aug-cc-pVTZ/JK",
        "def2-QZVPPD": "aug-cc-pVQZ/JK",
        "ma-def2-SVP": "aug-cc-pVDZ/JK",
        "ma-def2-TZVP": "aug-cc-pVTZ/JK",
        "ma-def2-QZVP": "aug-cc-pVQZ/JK",
    }

    # Convert to code-specific strings
    calcStr = ""
    if calculate == "Single Point":
        calcStr = "SP"
    elif calculate == "Geometry Optimization":
        calcStr = "Opt"
    elif calculate == "Frequencies":
        calcStr = "Opt Freq"
    elif calculate == "Dynamics":
        calcStr = "MD"
    elif calculate == "Transition State":
        calcStr = "OptTS"
    else:
        warnings.append("Unhandled calculation type: %s" % calculate)

    solvation = ""
    if "None" not in opts["Solvent"] and solvtype == "CPCM":
        solvation = "CPCM(" + solvent + ")"
    elif "None" not in opts["Solvent"] and solvtype == "SMD":
        solvation = "CPCM"

    if disp == "None":
        disp = ""
    else:
        disp = " " + disp

    if ri in ["None"]:
        #autoaux = False
        ri = ""
    # see https://discuss.avogadro.cc/t/orca-input-generator-does-not-print-nori-when-selected/5489
    elif ri in ["NORI"]:
        #autoaux = False
        ri = " " + ri
    else:
        if ri in ["RIJONX", "RIJCOSX"]:
            auxbasis = rijbasis[basis]
        else:
            auxbasis = rijkbasis[basis]
        ri = " " + ri

    #if autoaux == True:
    #    auxbasis = "AutoAux"

    if auxbasis != "None":
        basis = basis + " " + auxbasis

    if auxbasis == "None" and excit == "CIS(D)":
        basis = basis + " " + "AutoAux"

    if sym is True:
        usesymmetry = 'UseSym'
    else:
        usesymmetry = ''

    if excit == 'EOM-CCSD':
        theory="EOM-CCSD"
    elif excit in ["CIS", "CIS(D)"]:
        theory="HF"

    if "-3c" in theory or "-3C" in theory:
        # -3c composite methods have everything together
        code = f"{calcStr} {theory} {ri} {solvation} {usesymmetry}"
    else:
        theory = theory + disp + ri
        # put the pieces together
        code = f"{calcStr} {theory} {basis} {solvation} {usesymmetry}"

    generated_input = ""

    generated_input += "# avogadro generated ORCA file\n"
    generated_input += "# " + title + "\n"
    generated_input += "# \n"
    generated_input += f"! {code}\n\n"
    generated_input += "%maxcore " + str(memory) + "\n\n"
    if nCores > 1:
        generated_input += "%pal\n"
        generated_input += "   nprocs " + str(nCores) + "\n"
        generated_input += "end\n\n"
    if "None" not in opts["Solvent"] and solvtype == "SMD":
        generated_input += "%cpcm\n"
        generated_input += "   smd true\n"
        generated_input += '   SMDSolvent "' + solvent + '"\n'
        generated_input += "end\n\n"

    if calcStr == "MD":
        generated_input += "%md\n"
        generated_input += "   timestep " + opts["AIMD TimeStep"] + "\n"
        generated_input += "   initvel " + opts["AIMD Initvel"] + "_k\n"
        generated_input += (
            "   thermostat berendsen "
            + str(opts["AIMD Thermostat Temp"])
            + "_k timecon "
            + opts["AIMD Thermostat Time"]
            + "\n"
        )
        generated_input += '   dump position stride 1 filename "trajectory.xyz"\n'
        generated_input += "   run " + str(opts["AIMD RunTime"]) + "\n"
        generated_input += "end\n\n"

    # Excited states
    if excit == "CIS" or excit == "CIS(D)":
        generated_input += "%cis\n"
    elif excit == "TDDFT":
        generated_input += "%tddft\n"
    elif excit == "EOM-CCSD":
        generated_input += "%mdci\n"
    if excit != "None":
        generated_input += f"   nroots {nroots}\n"
        generated_input += f"   iroot  {iroot}\n"
        if excit == "CIS(D)":
            generated_input += "   dcorr 1\n"
        generated_input += "end\n\n"

    if mos is True:
        generated_input += "%output\n"
        generated_input += "   print[p_mos] 1\n"
        generated_input += "   print[p_basis] 2\n"
        generated_input += "end\n\n"

    if constrain is True:
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

    generated_input += f"* xyz {charge} {multiplicity}\n"
    generated_input += "$$coords:___Sxyz$$\n"
    generated_input += "*\n\n\n"

    return generated_input, warnings


def generateInput(input_json: dict, debug: bool) -> dict:

    generated_input, warnings = generateInputFile(input_json)

    filename = input_json['options']['Filename Base'] + '.inp'

    result = {
        'files': [
            {'filename': filename, 'contents': generated_input},
        ],
        'mainFile': filename,
    }

    if warnings:
        result['warnings'] = warnings

    return result


