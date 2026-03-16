"""Base classes and functions for input blocks in ORCA"""

from dataclasses import dataclass
from collections.abc import Sequence
from typing import NewType
from enum import Enum


#: Strings that are specially recognized by ORCA, for example in the
#: %method block you can use ``method HF`` and it will be recognized
#: without needing double quotes around ``HF``.
ORCAString = NewType("ORCAString", str)


@dataclass(frozen=True)
class BlockKeyword:
    """Base class for input block keywords.

    Attributes
    ----------
    name : str
        Keyword name.
    var_type : ORCAString | str | bool | int | float | Sequence
        Type of the variable, controls formatting in the input.
    simple : bool, default=False
        Mark the variable as being available as a simple input keyword.
    """

    name: str
    var_type: ORCAString | str | bool | int | float | Sequence
    simple: bool = False


class BlockEnum(BlockKeyword, Enum):
    """Base class for block keyword enums."""

    def __new__(
        cls,
        name: str,
        var_type: ORCAString | str | bool | int | float | Sequence,
        simple: bool = False,
    ):
        self = BlockKeyword.__new__(cls)
        self._value_ = name
        return self

    def format(
        self,
        value: ORCAString | str | bool | int | float | Sequence,
        indent: int = 4,
    ) -> str:
        """Format a keyword with its value."""
        if not isinstance(value, self.var_type):
            raise TypeError(
                f"Improper type {type(value)} for keyword {self.name}!"
            )

        output = " " * indent
        match self.var_type:
            case ORCAString():
                ...

        return output







