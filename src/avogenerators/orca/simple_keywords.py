"""Enums of simple input keywords for ORCA calculations"""

from dataclasses import dataclass
from enum import Enum, StrEnum, Flag, auto
from ..utilities import Element


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

