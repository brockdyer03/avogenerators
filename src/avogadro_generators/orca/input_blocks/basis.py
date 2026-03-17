"""Classes and methods for the %basis block in ORCA."""


from .block_base import BlockEnum, ORCAString


class Basis(BlockEnum):

    BASIS    = "Basis", str
    AUXJ     = "AuxJ",  str
    AUXJK    = "AuxJK", str
    AUXC     = "AuxC",  str
    CABS     = "CABS",  str
    ECP      = "ECP",   str
    GHOSTECP = "GhostECP", bool, None, False

    # Decontraction Options
    DECONTRACT      = "Decontract",      bool, None, False
    DECONTRACTBAS   = "DecontractBas",   bool, None, False
    DECONTRACTAUXJ  = "DecontractAuxJ",  bool, None, False
    DECONTRACTAUXJK = "DecontractAuxJK", bool, None, False
    DECONTRACTAUXC  = "DecontractAuxC",  bool, None, False
    DECONTRACTCABS  = "DecontractCABS",  bool, None, False

    #* Not sure if this should be included.
    # Reading basis sets from a file
    # GTONAME      = "GTOName",      str
    # GTOAUXJNAME  = "GTOAuxJName",  str
    # GTOAUXNAME   = "GTOAuxName",   str
    # GTOAUXJKNAME = "GTOAuxJKName", str
    # GTOAUXCNAME  = "GTOAuxCName",  str
    # GTOCABSNAME  = "GTOCABSName",  str

    # Removal of linear dependence
    PCDTRIMBAS   = "PCDTrimBas",   ORCAString, ("Overlap", "Coulomb")
    PCDTRIMAUXJ  = "PCDTrimAuxJ",  ORCAString, ("Overlap", "Coulomb")
    PCDTRIMAUXJK = "PCDTrimAuxJK", ORCAString, ("Overlap", "Coulomb")
    PCDTRIMAUXC  = "PCDTrimAuxC",  ORCAString, ("Overlap", "Coulomb")
    PCDTHRESH    = "PCDThresh",    float, None, -1

    # AutoAux Keywords
    AUTOAUXSIZE   = "AutoAuxSize",   int,   None, 1, 0, 3
    AUTOAUXLMAX   = "AutoAuxLmax",   bool,  None, False
    AUTOAUXLLIMIT = "AutoAuxLLimit", int,   None, -1
    AUTOAUXF_0    = "AutoAuxF[0]",   float, None, 20.0
    AUTOAUXF_1    = "AutoAuxF[1]",   float, None, 7.0
    AUTOAUXF_2    = "AutoAuxF[2]",   float, None, 4.0
    AUTOAUXF_3    = "AutoAuxF[3]",   float, None, 4.0
    AUTOAUXF_4    = "AutoAuxF[4]",   float, None, 3.5
    AUTOAUXF_5    = "AutoAuxF[5]",   float, None, 2.5
    AUTOAUXF_6    = "AutoAuxF[6]",   float, None, 2.0
    AUTOAUXF_7    = "AutoAuxF[7]",   float, None, 2.0
    AUTOAUXB_0    = "AutoAuxB[0]",   float, None, 1.8
    AUTOAUXB_1    = "AutoAuxB[1]",   float, None, 2.0
    AUTOAUXB_2    = "AutoAuxB[2]",   float, None, 2.2
    AUTOAUXB_3    = "AutoAuxB[3]",   float, None, 2.2
    AUTOAUXB_4    = "AutoAuxB[4]",   float, None, 2.2
    AUTOAUXB_5    = "AutoAuxB[5]",   float, None, 2.3
    AUTOAUXB_6    = "AutoAuxB[6]",   float, None, 3.0
    AUTOAUXB_7    = "AutoAuxB[7]",   float, None, 3.0
    AUTOAUXTIGHTB = "AutoAuxTightB", bool,  None, True
    OLDAUTOAUX    = "OldAutoAux",    bool,  None, False


