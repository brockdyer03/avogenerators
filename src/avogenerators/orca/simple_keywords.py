"""Enums of simple input keywords for ORCA calculations"""

from dataclasses import dataclass
from enum import Enum, StrEnum, Flag, auto
from ..utilities import Element

class Disp(Flag):
    """Dispersion corrections available in ORCA

    Attributes
    ----------
    NODISP : ""
        Either no dispersion correction available, or the correction is
        part of the functional's name. (e.g. wB97M-V)
    D3BJ : "D3BJ"
        D3 dispersion w/ Becke-Johnson Damping
    D3 : "D3BJ"
        Alias for `D3BJ`
    D3ZERO : "D3ZERO"
        D3 dispersion w/out Becke-Johnson Damping
    D4 : "D4"
        D4 dispersion
    NL : "NL"
        Non-local dispersion via the VV10 vdW correlation functional
    SCNL : "SCNL"
        Self-consistent variant of the non-local dispersion

    Notes
    -----
    The DFT-D and DFT-D2 dispersion corrections are deprecated, and so
    are not included here.

    The ``D3`` keyword automatically activates D3(BJ) dispersion in
    ORCA, so it is merely an alias for ``D3BJ`` here.
    """

    def __str__(self) -> str:
        match self:
            case Disp.NODISP:
                return ""
            case Disp.D3BJ:
                return "D3BJ"
            case Disp.D3ZERO:
                return "D3ZERO"
            case Disp.D4:
                return "D4"
            case Disp.NL:
                return "NL"
            case Disp.SCNL:
                return "SCNL"
            case _:
                raise ValueError("How did you even get here?")

    NODISP = 0
    D3BJ   = auto()
    D3     = D3BJ
    D3ZERO = auto()
    D4     = auto()
    NL     = auto() # VV10 Non-local dispersion correction
    SCNL   = auto() # Self-consistent variant


@dataclass
class Functional:
    """Class storing a functional's name and the available dispersion
    corrections.
    """

    name: str
    disp: Disp


class Composite(StrEnum):

    HF_3C     = "HF-3C"
    B97_3C    = "B97-3C"
    R2SCAN_3C = "r2SCAN-3C"
    PBEH_3C   = "PBEh-3C"
    B3LYP_3C  = "B3LYP-3C"
    WB97X_3C  = "wB97X-3C"


class Functionals(Enum, Functional):
    """Enumeration of all density functionals available via simple
    input keyword.

    Notes
    -----
    Functionals that already have a dispersion correction in their name
    are marked as having no dispersion corrections available. This is
    because trying to add a dispersion correction keyword to these
    functionals is either redundant or incorrect.

    Three functionals have a dispersion correction in their name,
    B97M-V, ωB97M-V, and ωB97X-V, but are marked with ``Disp.SCNL``.
    This is because these functionals, by default, use the
    non-self-consistent version of the NL correction, but it is still
    possible to switch on the self-consistent version with the SCNL
    keyword.
    """

    def __new__(
        cls,
        name: str,
        dispersion: Disp,
    ):
        functional = Functional.__new__(cls)
        functional._value_ = name
        return functional

    def __str__(self) -> str:
        return self.value

    def check_disp(self, disp: Disp) -> bool:
        if disp in self.disp:
            return True
        else:
            return False

    # Local Density Approximation (LDA)
    HFS    = "HFS",   Disp.NODISP
    LDA    = "LDA",   Disp.NODISP
    LSD    = LDA
    VWN_5  = "VWN5",  Disp.NODISP
    VWN_3  = "VWN3",  Disp.NODISP
    PW_LDA = "PWLDA", Disp.NODISP

    # Generalized Gradient Approximation (GGA)
    BP86     = "BP86",       Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    BLYP     = "BLYP",       Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    OLYP     = "OLYP",       Disp.D4 | Disp.D3BJ
    GLYP     = "GLYP",       Disp.D4
    XLYP     = "XLYP",       Disp.D4
    PW91     = "PW91",       Disp.D4
    MPWPW    = "mPWPW",      Disp.D4
    MPWLYP   = "mPWLYP",     Disp.D4 | Disp.D3BJ | Disp.D3ZERO
    PBE      = "PBE",        Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    RPBE     = "RPBE",       Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    REVPBE   = "revPBE",     Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    RPW86PBE = "RPW86PBE",   Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    PWP      = "PWP",        Disp.D4

    # Meta GGA (mGGA)
    B97M_V    = "B97M-V",    Disp.SCNL
    B97M_D3BJ = "B97M-D3BJ", Disp.NODISP
    B97M_D4   = "B97M-D4",   Disp.NODISP
    SCANFUNC  = "SCANFUNC",  Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    RSCAN     = "rSCAN",     Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    R2SCAN    = "r2SCAN",    Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    M06_L     = "M06L",      Disp.D4 | Disp.D3ZERO
    TPSS      = "TPSS",      Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    REVTPSS   = "revTPSS",   Disp.D4

    # Hybrid GGA (hGGA)
    B1LYP     = "B1LYP",     Disp.D4
    B3LYP     = "B3LYP",     Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    B3LYP_G   = "B3LYP/G",   Disp.NL | Disp.SCNL
    O3LYP     = "O3LYP",     Disp.D4
    X3LYP     = "X3LYP",     Disp.D4
    B1P86     = "B1P86",     Disp.NODISP
    B3P86     = "B3P86",     Disp.D4 | Disp.NL | Disp.SCNL
    B3PW91    = "B3PW91",    Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    PW1PW     = "PW1PW",     Disp.D4 | Disp.NL | Disp.SCNL
    MPW1PW    = "mPW1PW",    Disp.D4 | Disp.NL | Disp.SCNL
    MPW1LYP   = "mPW1LYP",   Disp.D4
    PBE0      = "PBE0",      Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    REVPBE0   = "revPBE0",   Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    REVPBE38  = "revPBE38",  Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    BHANDHLYP = "BHandHLYP", Disp.D4 | Disp.D3BJ | Disp.D3ZERO

    # Hybrid mGGA (hmGGA)
    M06      = "M06",      Disp.D4 | Disp.D3ZERO
    M06_2X   = "M062X",    Disp.D3ZERO
    PW6B95   = "PW6B95",   Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    TPSSH    = "TPSSh",    Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    TPSS0    = "TPSS0",    Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    R2SCANH  = "r2SCANh",  Disp.D4 | Disp.D3BJ | Disp.NL | Disp.SCNL
    R2SCAN0  = "r2SCAN0",  Disp.D4 | Disp.D3BJ | Disp.NL | Disp.SCNL
    R2SCAN50 = "r2SCAN50", Disp.D4 | Disp.D3BJ | Disp.NL | Disp.SCNL

    # Range-Separated hGGA (rshGGA)
    WB97        = "wB97",        Disp.NODISP
    WB97X       = "wB97X",       Disp.NODISP
    WB97X_V     = "wB97X-V",     Disp.SCNL
    WB97X_D3    = "wB97X-D3",    Disp.NODISP
    WB97X_D3BJ  = "wB97X-D3BJ",  Disp.NODISP
    WB97X_D4    = "wB97X-D4",    Disp.NODISP
    WB97X_D4REV = "wB97X-D4rev", Disp.NODISP
    CAM_B3LYP   = "CAM-B3LYP",   Disp.D4 | Disp.D3BJ | Disp.D3ZERO
    LC_BLYP     = "LC-BLYP",     Disp.D4
    LC_PBE      = "LC-PBE",      Disp.NODISP

    # Range-Separated hmGGA (rshmGGA)
    WB97M_V     = "wB97M-V",     Disp.SCNL
    WB97M_D3BJ  = "wB97M-D3BJ",  Disp.NODISP
    WB97M_D4    = "wB97M-D4",    Disp.NODISP
    WB97M_D4REV = "wB97M-D4rev", Disp.NODISP
    WR2SCAN     = "wr2SCAN",     Disp.D4 | Disp.D3BJ | Disp.NL | Disp.SCNL

    # Double Hybrids (DH)
    DSD_BLYP              = "DSD-BLYP D3BJ",         Disp.NODISP
    DSD_BLYP_NODISP_2013  = "DSD-BLYP/2013",         Disp.D3BJ | Disp.NL | Disp.SCNL
    DSD_BLYP_2013_D3BJ    = "DSD-BLYP/2013 D3BJ",    Disp.NODISP
    DSD_PBEP86_D3BJ       = "DSD-PBEP86 D3BJ",       Disp.NODISP
    DSD_PBEP86_2013       = "DSD-PBEP86/2013",       Disp.NL | Disp.SCNL
    DSD_PBEP86_2013_D3BJ  = "DSD-PBEP86/2013 D3BJ",  Disp.NODISP
    DSD_PBEB95            = "DSD-PBEB95",            Disp.NODISP
    DSD_PBEB95_D3BJ       = "DSD-PBEB95 D3BJ",       Disp.NODISP
    B2PLYP                = "B2PLYP",                Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    MPW2PLYP              = "mPW2PLYP",              Disp.D4
    B2GP_PLYP             = "B2GP-PLYP",             Disp.D4 | Disp.D3BJ | Disp.D3ZERO
    B2K_PLYP              = "B2K-PLYP",              Disp.NODISP
    B2T_PLYP              = "B2T-PLYP",              Disp.NODISP
    B2NC_PLYP             = "B2NC-PLYP",             Disp.NODISP
    PWPB95                = "PWPB95",                Disp.D4 | Disp.D3BJ | Disp.D3ZERO | Disp.NL | Disp.SCNL
    PBE_QIDH              = "PBE-QIDH",              Disp.D3BJ | Disp.D3ZERO
    PBE0_DH               = "PBE0-DH",               Disp.D3BJ | Disp.D3ZERO
    REVDSD_PBEP86_2021    = "revDSD-PBEP86/2021",    Disp.NODISP
    REVDSD_PBEP86_D4_2021 = "revDSD-PBEP86-D4/2021", Disp.NODISP
    REVDOD_PBEP86_2021    = "revDOD-PBEP86/2021",    Disp.NODISP
    REVDOD_PBEP86_D4_2021 = "revDOD-PBEP86-D4/2021", Disp.NODISP
    R2SCAN_CIDH           = "r2SCAN-CIDH",           Disp.D4 | Disp.D3BJ
    R2SCAN_QIDH           = "r2SCAN-QIDH",           Disp.D4 | Disp.D3BJ
    R2SCAN0_2             = "r2SCAN0-2",             Disp.D4 | Disp.D3BJ
    R2SCAN0_DH            = "r2SCAN0-DH",            Disp.D4 | Disp.D3BJ
    PR2SCAN50             = "Pr2SCAN50",             Disp.D4 | Disp.D3BJ | Disp.NL | Disp.SCNL
    PR2SCAN69             = "Pr2SCAN69",             Disp.D4 | Disp.D3BJ | Disp.NL | Disp.SCNL
    KPR2SCAN50            = "kPr2SCAN",              Disp.D4 | Disp.D3BJ | Disp.NL | Disp.SCNL
    SCS_SOS_B2PLYP21      = "SCS/SOS-B2PLYP21",      Disp.NODISP
    SCS_PBE_QIDH          = "SCS-PBE-QIDH",          Disp.NODISP
    SOS_PBE_QIDH          = "SOS-PBE-QIDH",          Disp.NODISP
    SCS_B2GP_PLYP21       = "SCS-B2GP-PLYP21",       Disp.NODISP
    SOS_B2GP_PLYP21       = "SOS-B2GP-PLYP21",       Disp.NODISP


@dataclass(init=False, frozen=True)
class BasisSet:
    """Dataclass to store a basis set's name, the supported elements,
    and the ECPs that may required for heavy elements.
    """

    name: str
    elements: tuple[Element]
    ecp: str | None
    ecp_elements: tuple[Element] | None

    def __init__(
        self,
        name: str,
        element_ranges: tuple[str],
        ecp: str | None = None,
        ecp_elements: tuple[str] | None = None,
    ):
        self.name = name
        self.elements = BasisSet.split_elements(element_ranges)
        self.ecp = ecp
        self.ecp_elements = (
            BasisSet.split_elements(ecp_elements)
            if ecp_elements is not None
            else None
        )

    @staticmethod
    def split_elements(element_ranges: list[str]) -> tuple[Element]:
        """Take a list of strings of the general form ``["H-Br"]`` and
        convert it into a tuple of ``Element`` that indicate all of the
        elements that are defined in the basis set.
        """
        elements = ()
        for elem_range in element_ranges:
            elem_range = elem_range.split("-")
            start = Element(elem_range[0])
            end = Element(elem_range[1])
            for num in range(start.number, end.number+1):
                elements.append(Element(num))
        
        return elements


class BasisSetEnum(Enum, BasisSet):
    """Base class for basis set enums."""

    def __new__(
        cls,
        name: str,
        element_ranges: tuple[str],
        ecp: str | None,
        ecp_elements: tuple[str] | None,
    ):
        self = BasisSet.__new__(cls)
        self._name_ = name
        return self


class PopleBasisSet(BasisSetEnum):
    """All Pople-style (X-YZG) basis sets in ORCA.

    Naming convention for members includes a ``b`` at the start, a
    lowercase ``p`` to denote a " + ".

    Basis sets that use the asterisk shorthand (e.g. 6-31G* or 6-31G**)
    are not explicitly written here as the asterisk shorthand maps to
    existing basis sets. One asterisk is equivalent to (d), and two
    asterisks is equivalent to (d,p).

    For example, 6-31G* translates to 6-31G(d), and 6-31G** translates
    to 6-31G(d,p)
    """

    @classmethod
    def _missing_(cls, value: str):
        """Add translation for sets that use an asterisk."""
        if "**" in value:
            value = value.replace("**", "(d,p)")
        elif "*" in value:
            value = value.replace("*", "(d)")
        
        for member in cls:
            if member.name == value:
                return member
        return None

    bSTO_3G                    = "STO-3G",            ("H-I" ),  None, None
    b3_21G                     = "3-21G",             ("H-Cs"),  None, None
    b3_21GSP                   = "3-21GSP",           ("H-Ar"),  None, None
    b4_22GSP                   = "4-22GSP",           ("H-Ar"),  None, None
    b6_31G                     = "6-31G",             ("H-Zn"),  None, None
    b6_31G_D                   = "6-31G(d)",          ("H-Zn"),  None, None
    b6_31G_D_P                 = "6-31G(d,p)",        ("H-Zn"),  None, None
    b6_31G_2D                  = "6-31G(2d)",         ("H-Zn"),  None, None
    b6_31G_2D_P                = "6-31G(2d,p)",       ("H-Zn"),  None, None
    b6_31G_2D_2P               = "6-31G(2d,2p)",      ("H-Zn"),  None, None
    b6_31G_2DF                 = "6-31G(2df)",        ("H-Zn"),  None, None
    b6_31G_2DF_2P              = "6-31G(2df,2p)",     ("H-Zn"),  None, None
    b6_31G_2DF_2PD             = "6-31G(2df,2pd)",    ("H-Zn"),  None, None
    b6_31_PLUS_G_D             = "6-31+G(d)",         ("H-Zn"),  None, None
    b6_31_PLUS_G_D_P           = "6-31+G(d,p)",       ("H-Zn"),  None, None
    b6_31_PLUS_G_2D            = "6-31+G(2d)",        ("H-Zn"),  None, None
    b6_31_PLUS_G_2D_P          = "6-31+G(2d,p)",      ("H-Zn"),  None, None
    b6_31_PLUS_G_2D_2P         = "6-31+G(2d,2p)",     ("H-Zn"),  None, None
    b6_31_PLUS_G_2DF           = "6-31+G(2df)",       ("H-Zn"),  None, None
    b6_31_PLUS_G_2DF_2P        = "6-31+G(2df,2p)",    ("H-Zn"),  None, None
    b6_31_PLUS_G_2DF_2PD       = "6-31+G(2df,2pd)",   ("H-Zn"),  None, None
    b6_31_PLUS_PLUS_G_D_P      = "6-31++G(d,p)",      ("H-Zn"),  None, None
    b6_31_PLUS_PLUS_G_2D_P     = "6-31++G(2d,p)",     ("H-Zn"),  None, None
    b6_31_PLUS_PLUS_G_2D_2P    = "6-31++G(2d,2p)",    ("H-Zn"),  None, None
    b6_31_PLUS_PLUS_G_2DF_2P   = "6-31++G(2df,2p)",   ("H-Zn"),  None, None
    b6_31_PLUS_PLUS_G_2DF_2PD  = "6-31++G(2df,2pd)",  ("H-Zn"),  None, None
    b6_311G                    = "6-311G",            ("H-Br"),  None, None
    b6_311G_D                  = "6-311G(d)",         ("H-Br"),  None, None
    b6_311G_D_P                = "6-311G(d,p)",       ("H-Br"),  None, None
    b6_311G_2D                 = "6-311G(2d)",        ("H-Br"),  None, None
    b6_311G_2D_P               = "6-311G(2d,p)",      ("H-Br"),  None, None
    b6_311G_2D_2P              = "6-311G(2d,2p)",     ("H-Br"),  None, None
    b6_311G_2DF                = "6-311G(2df)",       ("H-Br"),  None, None
    b6_311G_2DF_2P             = "6-311G(2df,2p)",    ("H-Br"),  None, None
    b6_311G_2DF_2PD            = "6-311G(2df,2pd)",   ("H-Br"),  None, None
    b6_311G_3DF                = "6-311G(3df)",       ("H-Br"),  None, None
    b6_311G_3DF_3PD            = "6-311G(3df,3pd)",   ("H-Br"),  None, None
    b6_311_PLUS_G_D            = "6-311+G(d)",        ("H-Br"),  None, None
    b6_311_PLUS_G_D_P          = "6-311+G(d,p)",      ("H-Br"),  None, None
    b6_311_PLUS_G_2D           = "6-311+G(2d)",       ("H-Br"),  None, None
    b6_311_PLUS_G_2D_P         = "6-311+G(2d,p)",     ("H-Br"),  None, None
    b6_311_PLUS_G_2D_2P        = "6-311+G(2d,2p)",    ("H-Br"),  None, None
    b6_311_PLUS_G_2DF          = "6-311+G(2df)",      ("H-Br"),  None, None
    b6_311_PLUS_G_2DF_2P       = "6-311+G(2df,2p)",   ("H-Br"),  None, None
    b6_311_PLUS_G_2DF_2PD      = "6-311+G(2df,2pd)",  ("H-Br"),  None, None
    b6_311_PLUS_G_3DF          = "6-311+G(3df)",      ("H-Br"),  None, None
    b6_311_PLUS_G_3DF_2P       = "6-311+G(3df,2p)",   ("H-Br"),  None, None
    b6_311_PLUS_G_3DF_3PD      = "6-311+G(3df,3pd)",  ("H-Br"),  None, None
    b6_311_PLUS_PLUS_G_D_P     = "6-311++G(d,p)",     ("H-Br"),  None, None
    b6_311_PLUS_PLUS_G_2D_P    = "6-311++G(2d,p)",    ("H-Br"),  None, None
    b6_311_PLUS_PLUS_G_2D_2P   = "6-311++G(2d,2p)",   ("H-Br"),  None, None
    b6_311_PLUS_PLUS_G_2DF_2P  = "6-311++G(2df,2p)",  ("H-Br"),  None, None
    b6_311_PLUS_PLUS_G_2DF_2PD = "6-311++G(2df,2pd)", ("H-Br"),  None, None
    b6_311_PLUS_PLUS_G_3DF_3PD = "6-311++G(3df,3pd)", ("H-Br"),  None, None
    bm6_31G                    = "m6-31G",            ("Sc-Cu"), None, None
    bm6_31G_STAR               = "m6-31G*",           ("Sc-Cu"), None, None


class def2BasisSet(BasisSetEnum):
    """Karlsruhe def2 family of basis sets."""

    DEF2_SVP        = "def2-SVP",         ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_SV_P_      = "def2-SV(P)",       ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_TZVP       = "def2-TZVP",        ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_TZVP_F_    = "def2-TZVP(-f)",    ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_TZVPP      = "def2-TZVPP",       ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_QZVP       = "def2-QZVP",        ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_QZVPP      = "def2-QZVPP",       ("H-Rn"), "def2-ECP", ("Rb-Rn")

    # Diffuse-Augmented
    DEF2_SVPD       = "def2-SVPD",        ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_TZVPD      = "def2-TZVPD",       ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_TZVPPD     = "def2-TZVPPD",      ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_QZVPD      = "def2-QZVPD",       ("H-Rn"), "def2-ECP", ("Rb-Rn")
    DEF2_QZVPPD     = "def2-QZVPPD",      ("H-Rn"), "def2-ECP", ("Rb-Rn")

    # Minimally Augmented
    MA_DEF2_SVP     = "ma-def2-SVP",      ("H-Rn"), "def2-ECP", ("Rb-Rn")
    MA_DEF2_SV_P_   = "ma-def2-SV(P)",    ("H-Rn"), "def2-ECP", ("Rb-Rn")
    MA_DEF2_MSVP    = "ma-def2-mSVP",     ("H-Rn"), "def2-ECP", ("Rb-Rn")
    MA_DEF2_TZVP    = "ma-def2-TZVP",     ("H-Rn"), "def2-ECP", ("Rb-Rn")
    MA_DEF2_TZVP_F_ = "ma-def2-TZVP(-f)", ("H-Rn"), "def2-ECP", ("Rb-Rn")
    MA_DEF2_TZVPP   = "ma-def2-TZVPP",    ("H-Rn"), "def2-ECP", ("Rb-Rn")
    MA_DEF2_QZVPP   = "ma-def2-QZVPP",    ("H-Rn"), "def2-ECP", ("Rb-Rn")


class JensenBasisSet(BasisSetEnum):
    """Jensen polarization-consistent basis sets and their variants."""

    PC_0         = "pc-0",         ("H-Ca", "Ga-Kr"),         None, None
    PC_1         = "pc-1",         ("H-Kr"),                  None, None
    PC_2         = "pc-2",         ("H-Kr"),                  None, None
    PC_3         = "pc-3",         ("H-Kr"),                  None, None
    PC_4         = "pc-4",         ("H-Kr"),                  None, None
    AUG_PC_0     = "aug-pc-0",     ("H-Ca", "Ga-Kr"),         None, None
    AUG_PC_1     = "aug-pc-1",     ("H-Kr"),                  None, None
    AUG_PC_2     = "aug-pc-2",     ("H-Kr"),                  None, None
    AUG_PC_3     = "aug-pc-3",     ("H-Kr"),                  None, None
    AUG_PC_4     = "aug-pc-4",     ("H-Kr"),                  None, None

    # Segmented contraction variants
    PCSEG_0      = "pcseg-0",      ("H-Kr"),                  None, None
    PCSEG_1      = "pcseg-1",      ("H-Kr"),                  None, None
    PCSEG_2      = "pcseg-2",      ("H-Kr"),                  None, None
    PCSEG_3      = "pcseg-3",      ("H-Kr"),                  None, None
    PCSEG_4      = "pcseg-4",      ("H-Kr"),                  None, None
    AUG_PCSEG_0  = "aug-pcseg-0",  ("H-Kr"),                  None, None
    AUG_PCSEG_1  = "aug-pcseg-1",  ("H-Kr"),                  None, None
    AUG_PCSEG_2  = "aug-pcseg-2",  ("H-Kr"),                  None, None
    AUG_PCSEG_3  = "aug-pcseg-3",  ("H-Kr"),                  None, None
    AUG_PCSEG_4  = "aug-pcseg-4",  ("H-Kr"),                  None, None

    # Optimized for nuclear magnetic shieldings
    PCSSEG_0     = "pcSseg-0",     ("H-Kr"),                  None, None
    PCSSEG_1     = "pcSseg-1",     ("H-Kr"),                  None, None
    PCSSEG_2     = "pcSseg-2",     ("H-Kr"),                  None, None
    PCSSEG_3     = "pcSseg-3",     ("H-Kr"),                  None, None
    PCSSEG_4     = "pcSseg-4",     ("H-Kr"),                  None, None
    AUG_PCSSEG_0 = "aug-pcSseg-0", ("H-Kr"),                  None, None
    AUG_PCSSEG_1 = "aug-pcSseg-1", ("H-Kr"),                  None, None
    AUG_PCSSEG_2 = "aug-pcSseg-2", ("H-Kr"),                  None, None
    AUG_PCSSEG_3 = "aug-pcSseg-3", ("H-Kr"),                  None, None
    AUG_PCSSEG_4 = "aug-pcSseg-4", ("H-Kr"),                  None, None

    # Optimized for spin-spin coupling constants
    PCJ_0        = "pcJ-0",        ("H-He", "B-Ne", "Al-Ar"), None, None
    PCJ_1        = "pcJ-1",        ("H-He", "B-Ne", "Al-Ar"), None, None
    PCJ_2        = "pcJ-2",        ("H-He", "B-Ne", "Al-Ar"), None, None
    PCJ_3        = "pcJ-3",        ("H-He", "B-Ne", "Al-Ar"), None, None
    PCJ_4        = "pcJ-4",        ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCJ_0    = "aug-pcJ-0",    ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCJ_1    = "aug-pcJ-1",    ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCJ_2    = "aug-pcJ-2",    ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCJ_3    = "aug-pcJ-3",    ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCJ_4    = "aug-pcJ-4",    ("H-He", "B-Ne", "Al-Ar"), None, None

    # Optimized for hyperfine coupling constants
    PCH_1        = "pcH-1",        ("H-He", "B-Ne", "Al-Ar"), None, None
    PCH_2        = "pcH-2",        ("H-He", "B-Ne", "Al-Ar"), None, None
    PCH_3        = "pcH-3",        ("H-He", "B-Ne", "Al-Ar"), None, None
    PCH_4        = "pcH-4",        ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCH_1    = "aug-pcH-1",    ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCH_2    = "aug-pcH-2",    ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCH_3    = "aug-pcH-3",    ("H-He", "B-Ne", "Al-Ar"), None, None
    AUG_PCH_4    = "aug-pcH-4",    ("H-He", "B-Ne", "Al-Ar"), None, None

    # Optimized for core spectroscopy
    PCX_1        = "pcX-1",        ("Li-Ar"),                 None, None
    PCX_2        = "pcX-2",        ("Li-Ar"),                 None, None
    PCX_3        = "pcX-3",        ("Li-Ar"),                 None, None
    PCX_4        = "pcX-4",        ("Li-Ar"),                 None, None
    AUG_PCX_1    = "aug-pcX-1",    ("Li-Ar"),                 None, None
    AUG_PCX_2    = "aug-pcX-2",    ("Li-Ar"),                 None, None
    AUG_PCX_3    = "aug-pcX-3",    ("Li-Ar"),                 None, None
    AUG_PCX_4    = "aug-pcX-4",    ("Li-Ar"),                 None, None


class CorrelationConsistentBasisSet(BasisSetEnum):
    """Correlation Consistent basis sets, cc-pVnZ"""

    CC_PVDZ               = "cc-pVDZ",          ("H-Ar", "Ca-Kr"),                          None, None
    CC_PVTZ               = "cc-pVTZ",          ("H-Ar", "Ca-Kr", "Y-Y", "Ag-Ag", "Au-Au"), None, None
    CC_PVQZ               = "cc-pVQZ",          ("H-Ar", "Ca-Kr"),                          None, None
    CC_PV5Z               = "cc-pV5Z",          ("H-Ar", "Ca-Kr"),                          None, None
    CC_PV6Z               = "cc-pV6Z",          ("H-He", "Be-Ne", "Al-Ar"),                 None, None
    AUG_CC_PVDZ           = "aug-cc-pVDZ",      ("H-Ar", "Sc-Kr"),                          None, None
    AUG_CC_PVTZ           = "aug-cc-pVTZ",      ("H-Ar", "Sc-Kr", "Ag-Ag", "Au-Au"),        None, None
    AUG_CC_PVQZ           = "aug-cc-pVQZ",      ("H-Ar", "Sc-Kr"),                          None, None
    AUG_CC_PV5Z           = "aug-cc-pV5Z",      ("H-Ar", "Sc-Kr"),                          None, None
    AUG_CC_PV6Z           = "aug-cc-pV6Z",      ("H-He", "B-Ne", "Al-Ar"),                  None, None
    CC_PVD_PLUS_D_Z       = "cc-pVD(+d)Z",      ("Na-Ar"),                     None, None
    CC_PVT_PLUS_D_Z       = "cc-pVT(+d)Z",      ("Na-Ar"),                     None, None
    CC_PVQ_PLUS_D_Z       = "cc-pVQ(+d)Z",      ("Na-Ar"),                     None, None
    CC_PV5_PLUS_D_Z       = "cc-pV5(+d)Z",      ("Na-Ar"),                     None, None
    AUG_CC_PVD_PLUS_D_Z   = "aug-cc-pVD(+d)Z",  ("Al-Ar"),                     None, None
    AUG_CC_PVT_PLUS_D_Z   = "aug-cc-pVT(+d)Z",  ("Al-Ar"),                     None, None
    AUG_CC_PVQ_PLUS_D_Z   = "aug-cc-pVQ(+d)Z",  ("Al-Ar"),                     None, None
    AUG_CC_PV5_PLUS_D_Z   = "aug-cc-pV5(+d)Z",  ("Al-Ar"),                     None, None
    AUG_CC_PV6_PLUS_D_Z   = "aug-cc-pV6(+d)Z",  ("Al-Ar"),                     None, None
    APR_CC_PV_Q_PLUS_D_Z  = "apr-cc-pV(Q+d)Z",  ("H-Ar"),                      None, None
    MAY_CC_PV_T_PLUS_D_Z  = "may-cc-pV(T+d)Z",  ("H-Ar"),                      None, None
    MAY_CC_PV_Q_PLUS_D_Z  = "may-cc-pV(Q+d)Z",  ("H-Ar"),                      None, None
    JUN_CC_PV_D_PLUS_D_Z  = "jun-cc-pV(D+d)Z",  ("H-Ar"),                      None, None
    JUN_CC_PV_T_PLUS_D_Z  = "jun-cc-pV(T+d)Z",  ("H-Ar"),                      None, None
    JUN_CC_PV_Q_PLUS_D_Z  = "jun-cc-pV(Q+d)Z",  ("H-Ar"),                      None, None
    JUL_CC_PV_D_PLUS_D_Z  = "jul-cc-pV(D+d)Z",  ("H-Ar"),                      None, None
    JUL_CC_PV_T_PLUS_D_Z  = "jul-cc-pV(T+d)Z",  ("H-Ar"),                      None, None
    JUL_CC_PV_Q_PLUS_D_Z  = "jul-cc-pV(Q+d)Z",  ("H-Ar"),                      None, None
    MAUG_CC_PV_D_PLUS_D_Z = "maug-cc-pV(D+d)Z", ("H-Ar"),                      None, None
    MAUG_CC_PV_T_PLUS_D_Z = "maug-cc-pV(T+d)Z", ("H-Ar"),                      None, None
    MAUG_CC_PV_Q_PLUS_D_Z = "maug-cc-pV(Q+d)Z", ("H-Ar"),                      None, None
    CC_PCVDZ              = "cc-pCVDZ",         ("H-Ar", "Ca-Ca", "Ga-Kr"),    None, None
    CC_PCVTZ              = "cc-pCVTZ",         ("H-Ar", "Ca-Ca", "Ga-Kr"),    None, None
    CC_PCVQZ              = "cc-pCVQZ",         ("H-Ar", "Ca-Ca", "Ga-Kr"),    None, None
    CC_PCV5Z              = "cc-pCV5Z",         ("H-Ar", "Ca-Ca", "Ga-Kr"),    None, None
    CC_PCV6Z              = "cc-pCV6Z",         ("H-He", "B-Ne",  "Al-Ar"),    None, None
    AUG_CC_PCVDZ          = "aug-cc-pCVDZ",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCVTZ          = "aug-cc-pCVTZ",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCVQZ          = "aug-cc-pCVQZ",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCV5Z          = "aug-cc-pCV5Z",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCV6Z          = "aug-cc-pCV6Z",     ("H-He", "B-Ne",  "Al-Ar"),    None, None
    CC_PWCVDZ             = "cc-pwCVDZ",        ("H-Ar", "Ca-Ca", "Ga-Kr"),    None, None
    CC_PWCVTZ             = "cc-pwCVTZ",        ("H-Ar", "Ca-Kr", "Ag-Ag", "Au-Au"), None, None
    CC_PWCVQZ             = "cc-pwCVQZ",        ("H-Ar", "Ca-Kr"),             None, None
    CC_PWCV5Z             = "cc-pwCV5Z",        ("H-Ar", "Ca-Kr"),             None, None
    AUG_CC_PWCVDZ         = "aug-cc-pwCVDZ",    ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PWCVTZ         = "aug-cc-pwCVTZ",    ("H-Ar", "Sc-Kr", "Ag-Ag", "Au-Au"), None, None
    AUG_CC_PWCVQZ         = "aug-cc-pwCVQZ",    ("H-Ar", "Sc-Kr"),             None, None
    AUG_CC_PWCV5Z         = "aug-cc-pwCV5Z",    ("H-Ar", "Sc-Kr"),             None, None


class RIApproximation(StrEnum):

    COSJXC     = "COSJXC"
    NOCOSX     = "NoCOSX"
    RI         = "RI" # Turns on Split-RI-J by default
    NORI       = "NoRI"
    RIJCOSX    = "RIJCOSX" # Default for Hybrid DFT
    NORIJCOSX  = "NoRIJCOSX"
    SPLITRIJ   = "Split-RI-J" # Default for non-Hybrid DFT
    NOSPLITRIJ = "NoSplit-RI-J"
    RIJK       = "RI-JK"


class PartialCharges(StrEnum):

    AIM       = "AIM"
    CHELPG    = "CHELPG"
    HIRSHFELD = "Hirshfeld"
    LOEWDIN   = "Loewdin"
    MAYER     = "Mayer"
    MBIS      = "MBIS"
    MULLIKEN  = "Mulliken"

