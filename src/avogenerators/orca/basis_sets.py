from dataclasses import dataclass
from enum import Enum
from ..utilities import Element


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
            if "-" not in elem_range:
                elements.append(Element(elem_range))
            else:
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

    bSTO_3G                    = "STO-3G",            ("H-I", ),  None, None
    b3_21G                     = "3-21G",             ("H-Cs",),  None, None
    b3_21GSP                   = "3-21GSP",           ("H-Ar",),  None, None
    b4_22GSP                   = "4-22GSP",           ("H-Ar",),  None, None
    b6_31G                     = "6-31G",             ("H-Zn",),  None, None
    b6_31G_D                   = "6-31G(d)",          ("H-Zn",),  None, None
    b6_31G_D_P                 = "6-31G(d,p)",        ("H-Zn",),  None, None
    b6_31G_2D                  = "6-31G(2d)",         ("H-Zn",),  None, None
    b6_31G_2D_P                = "6-31G(2d,p)",       ("H-Zn",),  None, None
    b6_31G_2D_2P               = "6-31G(2d,2p)",      ("H-Zn",),  None, None
    b6_31G_2DF                 = "6-31G(2df)",        ("H-Zn",),  None, None
    b6_31G_2DF_2P              = "6-31G(2df,2p)",     ("H-Zn",),  None, None
    b6_31G_2DF_2PD             = "6-31G(2df,2pd)",    ("H-Zn",),  None, None
    b6_31_PLUS_G_D             = "6-31+G(d)",         ("H-Zn",),  None, None
    b6_31_PLUS_G_D_P           = "6-31+G(d,p)",       ("H-Zn",),  None, None
    b6_31_PLUS_G_2D            = "6-31+G(2d)",        ("H-Zn",),  None, None
    b6_31_PLUS_G_2D_P          = "6-31+G(2d,p)",      ("H-Zn",),  None, None
    b6_31_PLUS_G_2D_2P         = "6-31+G(2d,2p)",     ("H-Zn",),  None, None
    b6_31_PLUS_G_2DF           = "6-31+G(2df)",       ("H-Zn",),  None, None
    b6_31_PLUS_G_2DF_2P        = "6-31+G(2df,2p)",    ("H-Zn",),  None, None
    b6_31_PLUS_G_2DF_2PD       = "6-31+G(2df,2pd)",   ("H-Zn",),  None, None
    b6_31_PLUS_PLUS_G_D_P      = "6-31++G(d,p)",      ("H-Zn",),  None, None
    b6_31_PLUS_PLUS_G_2D_P     = "6-31++G(2d,p)",     ("H-Zn",),  None, None
    b6_31_PLUS_PLUS_G_2D_2P    = "6-31++G(2d,2p)",    ("H-Zn",),  None, None
    b6_31_PLUS_PLUS_G_2DF_2P   = "6-31++G(2df,2p)",   ("H-Zn",),  None, None
    b6_31_PLUS_PLUS_G_2DF_2PD  = "6-31++G(2df,2pd)",  ("H-Zn",),  None, None
    b6_311G                    = "6-311G",            ("H-Br",),  None, None
    b6_311G_D                  = "6-311G(d)",         ("H-Br",),  None, None
    b6_311G_D_P                = "6-311G(d,p)",       ("H-Br",),  None, None
    b6_311G_2D                 = "6-311G(2d)",        ("H-Br",),  None, None
    b6_311G_2D_P               = "6-311G(2d,p)",      ("H-Br",),  None, None
    b6_311G_2D_2P              = "6-311G(2d,2p)",     ("H-Br",),  None, None
    b6_311G_2DF                = "6-311G(2df)",       ("H-Br",),  None, None
    b6_311G_2DF_2P             = "6-311G(2df,2p)",    ("H-Br",),  None, None
    b6_311G_2DF_2PD            = "6-311G(2df,2pd)",   ("H-Br",),  None, None
    b6_311G_3DF                = "6-311G(3df)",       ("H-Br",),  None, None
    b6_311G_3DF_3PD            = "6-311G(3df,3pd)",   ("H-Br",),  None, None
    b6_311_PLUS_G_D            = "6-311+G(d)",        ("H-Br",),  None, None
    b6_311_PLUS_G_D_P          = "6-311+G(d,p)",      ("H-Br",),  None, None
    b6_311_PLUS_G_2D           = "6-311+G(2d)",       ("H-Br",),  None, None
    b6_311_PLUS_G_2D_P         = "6-311+G(2d,p)",     ("H-Br",),  None, None
    b6_311_PLUS_G_2D_2P        = "6-311+G(2d,2p)",    ("H-Br",),  None, None
    b6_311_PLUS_G_2DF          = "6-311+G(2df)",      ("H-Br",),  None, None
    b6_311_PLUS_G_2DF_2P       = "6-311+G(2df,2p)",   ("H-Br",),  None, None
    b6_311_PLUS_G_2DF_2PD      = "6-311+G(2df,2pd)",  ("H-Br",),  None, None
    b6_311_PLUS_G_3DF          = "6-311+G(3df)",      ("H-Br",),  None, None
    b6_311_PLUS_G_3DF_2P       = "6-311+G(3df,2p)",   ("H-Br",),  None, None
    b6_311_PLUS_G_3DF_3PD      = "6-311+G(3df,3pd)",  ("H-Br",),  None, None
    b6_311_PLUS_PLUS_G_D_P     = "6-311++G(d,p)",     ("H-Br",),  None, None
    b6_311_PLUS_PLUS_G_2D_P    = "6-311++G(2d,p)",    ("H-Br",),  None, None
    b6_311_PLUS_PLUS_G_2D_2P   = "6-311++G(2d,2p)",   ("H-Br",),  None, None
    b6_311_PLUS_PLUS_G_2DF_2P  = "6-311++G(2df,2p)",  ("H-Br",),  None, None
    b6_311_PLUS_PLUS_G_2DF_2PD = "6-311++G(2df,2pd)", ("H-Br",),  None, None
    b6_311_PLUS_PLUS_G_3DF_3PD = "6-311++G(3df,3pd)", ("H-Br",),  None, None
    bm6_31G                    = "m6-31G",            ("Sc-Cu",), None, None
    bm6_31G_STAR               = "m6-31G*",           ("Sc-Cu",), None, None


class def2BasisSet(BasisSetEnum):
    """Karlsruhe def2 family of basis sets."""

    DEF2_SVP        = "def2-SVP",         ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_SV_P_      = "def2-SV(P)",       ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_TZVP       = "def2-TZVP",        ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_TZVP_F_    = "def2-TZVP(-f)",    ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_TZVPP      = "def2-TZVPP",       ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_QZVP       = "def2-QZVP",        ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_QZVPP      = "def2-QZVPP",       ("H-Rn",), "def2-ECP", ("Rb-Rn",)

    # Diffuse-Augmented
    DEF2_SVPD       = "def2-SVPD",        ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_TZVPD      = "def2-TZVPD",       ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_TZVPPD     = "def2-TZVPPD",      ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_QZVPD      = "def2-QZVPD",       ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    DEF2_QZVPPD     = "def2-QZVPPD",      ("H-Rn",), "def2-ECP", ("Rb-Rn",)

    # Minimally Augmented
    MA_DEF2_SVP     = "ma-def2-SVP",      ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    MA_DEF2_SV_P_   = "ma-def2-SV(P)",    ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    MA_DEF2_MSVP    = "ma-def2-mSVP",     ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    MA_DEF2_TZVP    = "ma-def2-TZVP",     ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    MA_DEF2_TZVP_F_ = "ma-def2-TZVP(-f)", ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    MA_DEF2_TZVPP   = "ma-def2-TZVPP",    ("H-Rn",), "def2-ECP", ("Rb-Rn",)
    MA_DEF2_QZVPP   = "ma-def2-QZVPP",    ("H-Rn",), "def2-ECP", ("Rb-Rn",)


class JensenBasisSet(BasisSetEnum):
    """Jensen polarization-consistent basis sets and their variants."""

    PC_0         = "pc-0",         ("H-Ca", "Ga-Kr"), None, None
    PC_1         = "pc-1",         ("H-Kr",),         None, None
    PC_2         = "pc-2",         ("H-Kr",),         None, None
    PC_3         = "pc-3",         ("H-Kr",),         None, None
    PC_4         = "pc-4",         ("H-Kr",),         None, None
    AUG_PC_0     = "aug-pc-0",     ("H-Ca", "Ga-Kr"), None, None
    AUG_PC_1     = "aug-pc-1",     ("H-Kr",),         None, None
    AUG_PC_2     = "aug-pc-2",     ("H-Kr",),         None, None
    AUG_PC_3     = "aug-pc-3",     ("H-Kr",),         None, None
    AUG_PC_4     = "aug-pc-4",     ("H-Kr",),         None, None

    # Segmented contraction variants
    PCSEG_0      = "pcseg-0",      ("H-Kr",), None, None
    PCSEG_1      = "pcseg-1",      ("H-Kr",), None, None
    PCSEG_2      = "pcseg-2",      ("H-Kr",), None, None
    PCSEG_3      = "pcseg-3",      ("H-Kr",), None, None
    PCSEG_4      = "pcseg-4",      ("H-Kr",), None, None
    AUG_PCSEG_0  = "aug-pcseg-0",  ("H-Kr",), None, None
    AUG_PCSEG_1  = "aug-pcseg-1",  ("H-Kr",), None, None
    AUG_PCSEG_2  = "aug-pcseg-2",  ("H-Kr",), None, None
    AUG_PCSEG_3  = "aug-pcseg-3",  ("H-Kr",), None, None
    AUG_PCSEG_4  = "aug-pcseg-4",  ("H-Kr",), None, None

    # Optimized for nuclear magnetic shieldings
    PCSSEG_0     = "pcSseg-0",     ("H-Kr",), None, None
    PCSSEG_1     = "pcSseg-1",     ("H-Kr",), None, None
    PCSSEG_2     = "pcSseg-2",     ("H-Kr",), None, None
    PCSSEG_3     = "pcSseg-3",     ("H-Kr",), None, None
    PCSSEG_4     = "pcSseg-4",     ("H-Kr",), None, None
    AUG_PCSSEG_0 = "aug-pcSseg-0", ("H-Kr",), None, None
    AUG_PCSSEG_1 = "aug-pcSseg-1", ("H-Kr",), None, None
    AUG_PCSSEG_2 = "aug-pcSseg-2", ("H-Kr",), None, None
    AUG_PCSSEG_3 = "aug-pcSseg-3", ("H-Kr",), None, None
    AUG_PCSSEG_4 = "aug-pcSseg-4", ("H-Kr",), None, None

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
    PCX_1        = "pcX-1",        ("Li-Ar",), None, None
    PCX_2        = "pcX-2",        ("Li-Ar",), None, None
    PCX_3        = "pcX-3",        ("Li-Ar",), None, None
    PCX_4        = "pcX-4",        ("Li-Ar",), None, None
    AUG_PCX_1    = "aug-pcX-1",    ("Li-Ar",), None, None
    AUG_PCX_2    = "aug-pcX-2",    ("Li-Ar",), None, None
    AUG_PCX_3    = "aug-pcX-3",    ("Li-Ar",), None, None
    AUG_PCX_4    = "aug-pcX-4",    ("Li-Ar",), None, None


class CorrelationConsistentBasisSet(BasisSetEnum):
    """Correlation Consistent basis sets, cc-pVnZ"""

    CC_PVDZ               = "cc-pVDZ",          ("H-Ar", "Ca-Kr"),             None, None
    CC_PVTZ               = "cc-pVTZ",          ("H-Ar", "Ca-Kr", "Y", "Ag", "Au"), None, None
    CC_PVQZ               = "cc-pVQZ",          ("H-Ar", "Ca-Kr"),             None, None
    CC_PV5Z               = "cc-pV5Z",          ("H-Ar", "Ca-Kr"),             None, None
    CC_PV6Z               = "cc-pV6Z",          ("H-He", "Be-Ne", "Al-Ar"),    None, None
    AUG_CC_PVDZ           = "aug-cc-pVDZ",      ("H-Ar", "Sc-Kr"),             None, None
    AUG_CC_PVTZ           = "aug-cc-pVTZ",      ("H-Ar", "Sc-Kr", "Ag", "Au"), None, None
    AUG_CC_PVQZ           = "aug-cc-pVQZ",      ("H-Ar", "Sc-Kr"),             None, None
    AUG_CC_PV5Z           = "aug-cc-pV5Z",      ("H-Ar", "Sc-Kr"),             None, None
    AUG_CC_PV6Z           = "aug-cc-pV6Z",      ("H-He", "B-Ne", "Al-Ar"),     None, None
    CC_PVD_PLUS_D_Z       = "cc-pVD(+d)Z",      ("Na-Ar",),                    None, None
    CC_PVT_PLUS_D_Z       = "cc-pVT(+d)Z",      ("Na-Ar",),                    None, None
    CC_PVQ_PLUS_D_Z       = "cc-pVQ(+d)Z",      ("Na-Ar",),                    None, None
    CC_PV5_PLUS_D_Z       = "cc-pV5(+d)Z",      ("Na-Ar",),                    None, None
    AUG_CC_PVD_PLUS_D_Z   = "aug-cc-pVD(+d)Z",  ("Al-Ar",),                    None, None
    AUG_CC_PVT_PLUS_D_Z   = "aug-cc-pVT(+d)Z",  ("Al-Ar",),                    None, None
    AUG_CC_PVQ_PLUS_D_Z   = "aug-cc-pVQ(+d)Z",  ("Al-Ar",),                    None, None
    AUG_CC_PV5_PLUS_D_Z   = "aug-cc-pV5(+d)Z",  ("Al-Ar",),                    None, None
    AUG_CC_PV6_PLUS_D_Z   = "aug-cc-pV6(+d)Z",  ("Al-Ar",),                    None, None
    APR_CC_PV_Q_PLUS_D_Z  = "apr-cc-pV(Q+d)Z",  ("H-Ar",),                     None, None
    MAY_CC_PV_T_PLUS_D_Z  = "may-cc-pV(T+d)Z",  ("H-Ar",),                     None, None
    MAY_CC_PV_Q_PLUS_D_Z  = "may-cc-pV(Q+d)Z",  ("H-Ar",),                     None, None
    JUN_CC_PV_D_PLUS_D_Z  = "jun-cc-pV(D+d)Z",  ("H-Ar",),                     None, None
    JUN_CC_PV_T_PLUS_D_Z  = "jun-cc-pV(T+d)Z",  ("H-Ar",),                     None, None
    JUN_CC_PV_Q_PLUS_D_Z  = "jun-cc-pV(Q+d)Z",  ("H-Ar",),                     None, None
    JUL_CC_PV_D_PLUS_D_Z  = "jul-cc-pV(D+d)Z",  ("H-Ar",),                     None, None
    JUL_CC_PV_T_PLUS_D_Z  = "jul-cc-pV(T+d)Z",  ("H-Ar",),                     None, None
    JUL_CC_PV_Q_PLUS_D_Z  = "jul-cc-pV(Q+d)Z",  ("H-Ar",),                     None, None
    MAUG_CC_PV_D_PLUS_D_Z = "maug-cc-pV(D+d)Z", ("H-Ar",),                     None, None
    MAUG_CC_PV_T_PLUS_D_Z = "maug-cc-pV(T+d)Z", ("H-Ar",),                     None, None
    MAUG_CC_PV_Q_PLUS_D_Z = "maug-cc-pV(Q+d)Z", ("H-Ar",),                     None, None
    CC_PCVDZ              = "cc-pCVDZ",         ("H-Ar", "Ca",   "Ga-Kr"),     None, None
    CC_PCVTZ              = "cc-pCVTZ",         ("H-Ar", "Ca",   "Ga-Kr"),     None, None
    CC_PCVQZ              = "cc-pCVQZ",         ("H-Ar", "Ca",   "Ga-Kr"),     None, None
    CC_PCV5Z              = "cc-pCV5Z",         ("H-Ar", "Ca",   "Ga-Kr"),     None, None
    CC_PCV6Z              = "cc-pCV6Z",         ("H-He", "B-Ne", "Al-Ar"),     None, None
    AUG_CC_PCVDZ          = "aug-cc-pCVDZ",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCVTZ          = "aug-cc-pCVTZ",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCVQZ          = "aug-cc-pCVQZ",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCV5Z          = "aug-cc-pCV5Z",     ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PCV6Z          = "aug-cc-pCV6Z",     ("H-He", "B-Ne",  "Al-Ar"),    None, None
    CC_PWCVDZ             = "cc-pwCVDZ",        ("H-Ar", "Ca",    "Ga-Kr"),    None, None
    CC_PWCVTZ             = "cc-pwCVTZ",        ("H-Ar", "Ca-Kr", "Ag", "Au"), None, None
    CC_PWCVQZ             = "cc-pwCVQZ",        ("H-Ar", "Ca-Kr"),             None, None
    CC_PWCV5Z             = "cc-pwCV5Z",        ("H-Ar", "Ca-Kr"),             None, None
    AUG_CC_PWCVDZ         = "aug-cc-pwCVDZ",    ("H-Ar", "Ga-Kr"),             None, None
    AUG_CC_PWCVTZ         = "aug-cc-pwCVTZ",    ("H-Ar", "Sc-Kr", "Ag", "Au"), None, None
    AUG_CC_PWCVQZ         = "aug-cc-pwCVQZ",    ("H-Ar", "Sc-Kr"),             None, None
    AUG_CC_PWCV5Z         = "aug-cc-pwCV5Z",    ("H-Ar", "Sc-Kr"),             None, None


class RelativisticBasisSet(BasisSetEnum):
    """Relativistic basis sets for the DKH, ZORA, or X2C approaches."""

    # Recontracted Ahlrichs Basis Sets
    DKH_SV_P_   = "DKH-SV(P)",   ("H-Kr",), None, None
    DKH_SVP     = "DKH-SVP",     ("H-Kr",), None, None
    DKH_TZV_P_  = "DKH-TZV(P)",  ("H-Kr",), None, None
    DKH_TZVP    = "DKH-TZVP",    ("H-Kr",), None, None
    DKH_TZVPP   = "DKH-TZVPP",   ("H-Kr",), None, None
    DKH_QZVP    = "DKH-QZVP",    ("H-Kr",), None, None
    DKH_QZVPP   = "DKH-QZVPP",   ("H-Kr",), None, None
    ZORA_SV_P_  = "ZORA-SV(P)",  ("H-Kr",), None, None
    ZORA_SVP    = "ZORA-SVP",    ("H-Kr",), None, None
    ZORA_TZV_P_ = "ZORA-TZV(P)", ("H-Kr",), None, None
    ZORA_TZVP   = "ZORA-TZVP",   ("H-Kr",), None, None
    ZORA_TZVPP  = "ZORA-TZVPP",  ("H-Kr",), None, None
    ZORA_QZVP   = "ZORA-QZVP",   ("H-Kr",), None, None
    ZORA_QZVPP  = "ZORA-QZVPP",  ("H-Kr",), None, None

    # Recontracted def2 basis sets
    DKH_DEF2_SVP         = "DKH-def2-SVP",          ("H-Kr",), None, None
    DKH_DEF2_SV_P_       = "DKH-def2-SV(P)",        ("H-Kr",), None, None
    DKH_DEF2_TZVP        = "DKH-def2-TZVP",         ("H-Kr",), None, None
    DKH_DEF2_TZVP_F_     = "DKH-def2-TZVP(-f)",     ("H-Kr",), None, None
    DKH_DEF2_TZVPP       = "DKH-def2-TZVPP",        ("H-Kr",), None, None
    DKH_DEF2_QZVPP       = "DKH-def2-QZVPP",        ("H-Kr",), None, None
    ZORA_DEF2_SVP        = "ZORA-def2-SVP",         ("H-Kr",), None, None
    ZORA_DEF2_SV_P_      = "ZORA-def2-SV(P)",       ("H-Kr",), None, None
    ZORA_DEF2_TZVP       = "ZORA-def2-TZVP",        ("H-Kr",), None, None
    ZORA_DEF2_TZVP_F_    = "ZORA-def2-TZVP(-f)",    ("H-Kr",), None, None
    ZORA_DEF2_TZVPP      = "ZORA-def2-TZVPP",       ("H-Kr",), None, None
    ZORA_DEF2_QZVPP      = "ZORA-def2-QZVPP",       ("H-Kr",), None, None
    # Minimally augmented variants
    MA_DKH_DEF2_SVP      = "ma-DKH-def2-SVP",       ("H-Kr",), None, None
    MA_DKH_DEF2_SV_P_    = "ma-DKH-def2-SV(P)",     ("H-Kr",), None, None
    MA_DKH_DEF2_TZVP     = "ma-DKH-def2-TZVP",      ("H-Kr",), None, None
    MA_DKH_DEF2_TZVP_F_  = "ma-DKH-def2-TZVP(-f)",  ("H-Kr",), None, None
    MA_DKH_DEF2_TZVPP    = "ma-DKH-def2-TZVPP",     ("H-Kr",), None, None
    MA_DKH_DEF2_QZVPP    = "ma-DKH-def2-QZVPP",     ("H-Kr",), None, None
    MA_ZORA_DEF2_SVP     = "ma-ZORA-def2-SVP",      ("H-Kr",), None, None
    MA_ZORA_DEF2_SV_P_   = "ma-ZORA-def2-SV(P)",    ("H-Kr",), None, None
    MA_ZORA_DEF2_TZVP    = "ma-ZORA-def2-TZVP",     ("H-Kr",), None, None
    MA_ZORA_DEF2_TZVP_F_ = "ma-ZORA-def2-TZVP(-f)", ("H-Kr",), None, None
    MA_ZORA_DEF2_TZVPP   = "ma-ZORA-def2-TZVPP",    ("H-Kr",), None, None
    MA_ZORA_DEF2_QZVPP   = "ma-ZORA-def2-QZVPP",    ("H-Kr",), None, None

    # Segmented all-electron relativistically contracted basis sets
    SARC_DKH_SVP    = "SARC-DKH-SVP",    ("Hf-Hg",),         None, None
    SARC_DKH_TZVP   = "SARC-DKH-TZVP",   ("Rb-Rn", "Ac-Lr"), None, None
    SARC_DKH_TZVPP  = "SARC-DKH-TZVPP",  ("Rb-Rn", "Ac-Lr"), None, None
    SARC_ZORA_SVP   = "SARC-ZORA-SVP",   ("Hf-Hg",),         None, None
    SARC_ZORA_TZVP  = "SARC-ZORA-TZVP",  ("Rb-Rn", "Ac-Lr"), None, None
    SARC_ZORA_TZVPP = "SARC-ZORA-TZVPP", ("Rb-Rn", "Ac-Lr"), None, None

    # Quadruple-zeta SARC basis sets for lanthanides
    SARC2_DKH_QZV   = "SARC2-DKH-QZV",   ("La-Lu",), None, None
    SARC2_DKH_QZVP  = "SARC2-DKH-QZVP",  ("La-Lu",), None, None
    SARC2_ZORA_QZV  = "SARC2-ZORA-QZV",  ("La-Lu",), None, None
    SARC2_ZORA_QZVP = "SARC2-ZORA-QZVP", ("La-Lu",), None, None

    # All-electron X2C Basis Sets
    X2C_SV_P_ALL      = "x2c-SV(P)all",      ("H-Rn",), None, None
    X2C_SVPALL        = "x2c-SVPall",        ("H-Rn",), None, None
    X2C_TZVPALL       = "x2c-TZVPall",       ("H-Rn",), None, None
    X2C_TZVPPALL      = "x2c-TZVPPall",      ("H-Rn",), None, None
    X2C_QZVPALL       = "x2c-QZVPall",       ("H-Rn",), None, None
    X2C_QZVPPALL      = "x2c-QZVPPall",      ("H-Rn",), None, None
    # NMR Shielding Optimized
    X2C_SV_P_ALL_S    = "x2c-SV(P)all-s",    ("H-Rn",), None, None
    X2C_SVPALL_S      = "x2c-SVPall-s",      ("H-Rn",), None, None
    X2C_TZVPALL_S     = "x2c-TZVPall-s",     ("H-Rn",), None, None
    X2C_TZVPPALL_S    = "x2c-TZVPPall-s",    ("H-Rn",), None, None
    X2C_QZVPALL_S     = "x2c-QZVPall-s",     ("H-Rn",), None, None
    X2C_QZVPPALL_S    = "x2c-QZVPPall-s",    ("H-Rn",), None, None
    # Two-component variants, not actually implemented yet
    # X2C_SV_P_ALL_2C   = "x2c-SV(P)all-2c",   ("H-Rn",), None, None
    # X2C_SVPALL_2C     = "x2c-SVPall-2c",     ("H-Rn",), None, None
    # X2C_TZVPALL_2C    = "x2c-TZVPall-2c",    ("H-Rn",), None, None
    # X2C_TZVPPALL_2C   = "x2c-TZVPPall-2c",   ("H-Rn",), None, None
    # X2C_QZVPALL_2C    = "x2c-QZVPall-2c",    ("H-Rn",), None, None
    # X2C_QZVPPALL_2C   = "x2c-QZVPPall-2c",   ("H-Rn",), None, None
    # X2C_QZVPALL_2C_S  = "x2c-QZVPall-2c-s",  ("H-Rn",), None, None
    # X2C_QZVPPALL_2C_S = "x2c-QZVPPall-2c-s", ("H-Rn",), None, None

    # Correlation-Consistent Relativistic Basis Set
    CC_PVDZ_DK       = "cc-pVDZ-DK",       ("H-Ar", "Sc-Kr"),                            None, None
    CC_PVTZ_DK       = "cc-pVTZ-DK",       ("H-Ar", "Sc-Kr", "Y-Xe",  "Hf-Rn"),          None, None
    CC_PVQZ_DK       = "cc-pVQZ-DK",       ("H-Ar", "Sc-Kr", "In-Xe", "Tl-Rn"),          None, None
    CC_PV5Z_DK       = "cc-pV5Z-DK",       ("H-Ar", "Sc-Kr"),                            None, None
    CC_PVDZ_DK3      = "cc-pVDZ-DK3",      ("U",),                                       None, None
    CC_PVTZ_DK3      = "cc-pVTZ-DK3",      ("U",),                                       None, None
    CC_PVQZ_DK3      = "cc-pVQZ-DK3",      ("U",),                                       None, None
    AUG_CC_PVDZ_DK   = "aug-cc-pVDZ-DK",   ("H-Ar", "Sc-Kr"),                            None, None
    AUG_CC_PVTZ_DK   = "aug-cc-pVTZ-DK",   ("H-Ar", "Sc-Kr", "Y-Xe",  "Hf-Rn"),          None, None
    AUG_CC_PVQZ_DK   = "aug-cc-pVQZ-DK",   ("H-Ar", "Sc-Kr", "In-Xe", "Tl-Rn"),          None, None
    AUG_CC_PV5Z_DK   = "aug-cc-pV5Z-DK",   ("H-Ar", "Sc-Kr"),                            None, None
    CC_PWCVDZ_DK     = "cc-pwCVDZ-DK",     ("H-Be", "Na-Mg", "Ca-Zn"),                   None, None
    CC_PWCVTZ_DK     = "cc-pwCVTZ-DK",     ("H-Be", "Na-Mg", "Ca-Zn", "Y-Xe",  "Hf-Rn"), None, None
    CC_PWCVQZ_DK     = "cc-pwCVQZ-DK",     ("H-Be", "Na-Mg", "Ca-Zn", "In-Xe", "Tl-Rn"), None, None
    CC_PWCV5Z_DK     = "cc-pwCV5Z-DK",     ("H-Be", "Na-Mg", "Ca-Zn"),                   None, None
    CC_PWCVDZ_DK3    = "cc-pwCVDZ-DK3",    ("U",),                                       None, None
    CC_PWCVTZ_DK3    = "cc-pwCVTZ-DK3",    ("U",),                                       None, None
    CC_PWCVQZ_DK3    = "cc-pwCVQZ-DK3",    ("U",),                                       None, None
    AUG_CC_PWCVDZ_DK = "aug-cc-pwCVDZ-DK", ("H-Be", "Na-Mg", "Sc-Zn"),                   None, None
    AUG_CC_PWCVTZ_DK = "aug-cc-pwCVTZ-DK", ("H-Be", "Na-Mg", "Sc-Zn", "Y-Xe",  "Hf-Rn"), None, None
    AUG_CC_PWCVQZ_DK = "aug-cc-pwCVQZ-DK", ("H-Be", "Na-Mg", "Sc-Zn", "In-Xe", "Tl-Rn"), None, None
    AUG_CC_PWCV5Z_DK = "aug-cc-pwCV5Z-DK", ("H-Be", "Na-Mg", "Sc-Zn"),                   None, None

    # Relativistically Contracted ANO Basis Sets
    ANO_RCC_Full = "ANO-RCC-Full", ("H-Cm",), None, None
    ANO_RCC_DZP  = "ANO-RCC-DZP",  ("H-Cm",), None, None
    ANO_RCC_TZP  = "ANO-RCC-TZP",  ("H-Cm",), None, None
    ANO_RCC_QZP  = "ANO-RCC-QZP",  ("H-Cm",), None, None


@dataclass(init=False, frozen=True)
class AuxBasisSet:
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
        parent_basis: BasisSetEnum,
        ecp: str | None = None,
        ecp_elements: tuple[str] | None = None,
    ):
        self.name = name
        self.elements = BasisSet.split_elements(element_ranges)
        self.parent_basis = parent_basis


class AuxBasisSetEnum(Enum, AuxBasisSet):
    """Base class for auxiliary basis set enums."""

    def __new__(
        cls,
        name: str,
        element_ranges: tuple[str],
        parent_basis: BasisSetEnum,
    ):
        self = BasisSet.__new__(cls)
        self._name_ = name
        return self


class AuxJBasisSet(AuxBasisSetEnum):
    """Coulomb-fitting auxiliary basis sets"""

    DEF2_J        = "def2/J",        ("H-Lr",), def2BasisSet
    DEF2_MTZVP_J  = "def2-mTZVP/J",  ("H-Lr",), def2BasisSet
    DEF2_MTZVPP_J = "def2-mTZVPP/J", ("H-Lr",), def2BasisSet
    X2C_J         = "x2c/J",         ("H-Rn",),         RelativisticBasisSet
    SARC_J        = "SARC/J",        ("H-Rn", "Ac-Lr"), RelativisticBasisSet


class AuxJKBasisSet(AuxBasisSetEnum):
    """Coulomb- and exchange-fitting auxiliary basis sets"""

    DEF2_JK            = "def2/JK",            ("H-Rn"),          def2BasisSet
    DEF2_JK_SMALL      = "def2/JKsmall",       ("H-Ra", "Th-Lr"), def2BasisSet

    CC_PVTZ_JK         = "cc-pVTZ/JK",         ("H", "B-F", "Al-Cl", "Ga-Br"), CorrelationConsistentBasisSet
    CC_PVQZ_JK         = "cc-pVQZ/JK",         ("H", "B-F", "Al-Cl", "Ga-Br"), CorrelationConsistentBasisSet
    CC_PV5Z_JK         = "cc-pV5Z/JK",         ("H", "B-F", "Al-Cl", "Ga-Br"), CorrelationConsistentBasisSet
    AUG_CC_PVTZ_JK     = "aug-cc-pVTZ/JK",     ("H", "B-F", "Al-Cl", "Ga-Br"), CorrelationConsistentBasisSet
    AUG_CC_PVQZ_JK     = "aug-cc-pVQZ/JK",     ("H", "B-F", "Al-Cl", "Ga-Br"), CorrelationConsistentBasisSet
    AUG_CC_PV5Z_JK     = "aug-cc-pV5Z/JK",     ("H", "B-F", "Al-Cl", "Ga-Br"), CorrelationConsistentBasisSet

    SARC2_DKH_QZV_JK   = "SARC2-DKH-QZV/JK",   ("La-Lu",), RelativisticBasisSet
    SARC2_DKH_QZVP_JK  = "SARC2-DKH-QZVP/JK",  ("La-Lu",), RelativisticBasisSet
    SARC2_ZORA_QZV_JK  = "SARC2-ZORA-QZV/JK",  ("La-Lu",), RelativisticBasisSet
    SARC2_ZORA_QZVP_JK = "SARC2-ZORA-QZVP/JK", ("La-Lu",), RelativisticBasisSet


class AuxCBasisSet(AuxBasisSetEnum):
    """Auxiliary basis sets for correlated wavefunction methods."""

    DEF2_SVP_C    = "def2-SVP/C",        ("H-Rn",),         def2BasisSet
    DEF2_TZVP_C   = "def2-TZVP/C",       ("H-Rn",),         def2BasisSet
    DEF2_TZVPP_C  = "def2-TZVPP/C",      ("H-Rn",),         def2BasisSet
    DEF2_QZVPP_C  = "def2-QZVPP/C",      ("H-Rn",),         def2BasisSet
    DEF2_SVPD_C   = "def2-SVPD/C",       ("H-La", "Hf-Rn"), def2BasisSet
    DEF2_TZVPD_C  = "def2-TZVPD/C",      ("H-La", "Hf-Rn"), def2BasisSet
    DEF2_TZVPPD_C = "def2-TZVPPD/C",     ("H-La", "Hf-Rn"), def2BasisSet
    DEF2_QZVPPD_C = "def2-QZVPPD/C",     ("H-La", "Hf-Rn"), def2BasisSet

    CC_PVDZ_C     = "cc-pVDZ/C",         ("H-Ar", "Ga-Kr"),                   CorrelationConsistentBasisSet
    CC_PVTZ_C     = "cc-pVTZ/C",         ("H-Ar", "Sc-Kr"),                   CorrelationConsistentBasisSet
    CC_PVQZ_C     = "cc-pVQZ/C",         ("H-Ar", "Sc-Kr"),                   CorrelationConsistentBasisSet
    CC_PV5Z_C     = "cc-pV5Z/C",         ("H-Ar", "Ga-Kr"),                   CorrelationConsistentBasisSet
    CC_PV6Z_C     = "cc-pV6Z/C",         ("H-He", "B-Ne",  "Al-Ar"),          CorrelationConsistentBasisSet
    AUG_CC_PVDZ_C = "aug-cc-pVDZ/C",     ("H-He", "Be-Ne", "Mg-Ar", "Ga-Kr"), CorrelationConsistentBasisSet
    AUG_CC_PVTZ_C = "aug-cc-pVTZ/C",     ("H-He", "Be-Ne", "Mg-Ar", "Sc-Kr"), CorrelationConsistentBasisSet
    AUG_CC_PVQZ_C = "aug-cc-pVQZ/C",     ("H-He", "Be-Ne", "Mg-Ar", "Sc-Kr"), CorrelationConsistentBasisSet
    AUG_CC_PV5Z_C = "aug-cc-pV5Z/C",     ("H-Ne", "Al-Ar", "Ga-Kr"),          CorrelationConsistentBasisSet
    AUG_CC_PV6Z_C   = "aug-cc-pV6Z/C",   ("H-He", "B-Ne", "Al-Ar"),           CorrelationConsistentBasisSet
    CC_PWCVDZ_C     = "cc-pwCVDZ/C",     ("H-He", "B-Ne", "Al-Ar", "Ga-Kr"),  CorrelationConsistentBasisSet
    CC_PWCVTZ_C     = "cc-pwCVTZ/C",     ("H-He", "B-Ne", "Al-Ar", "Sc-Kr"),  CorrelationConsistentBasisSet
    CC_PWCVQZ_C     = "cc-pwCVQZ/C",     ("H-He", "B-Ne", "Al-Ar", "Ga-Kr"),  CorrelationConsistentBasisSet
    CC_PWCV5Z_C     = "cc-pwCV5Z/C",     ("H-Ne", "Al-Ar"),                   CorrelationConsistentBasisSet
    AUG_CC_PWCVDZ_C = "aug-cc-pwCVDZ/C", ("H-He", "B-Ne", "Al-Ar", "Ga-Kr"),  CorrelationConsistentBasisSet
    AUG_CC_PWCVTZ_C = "aug-cc-pwCVTZ/C", ("H-He", "B-Ne", "Al-Ar", "Sc-Kr"),  CorrelationConsistentBasisSet
    AUG_CC_PWCVQZ_C = "aug-cc-pwCVQZ/C", ("H-He", "B-Ne", "Al-Ar", "Ga-Kr"),  CorrelationConsistentBasisSet
    AUG_CC_PWCV5Z_C = "aug-cc-pwCV5Z/C", ("H-Ne", "Al-Ar"),                   CorrelationConsistentBasisSet




