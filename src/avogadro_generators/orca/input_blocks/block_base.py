"""Base classes and functions for input blocks in ORCA"""

from dataclasses import dataclass
from collections.abc import Sequence
from typing import NewType
from enum import Enum
import builtins


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
    _dtype : ORCAString or str or bool or int or float or Sequence
        Type of the variable, controls formatting in the input.
    options : tuple of dtype, optional
        Tuple of known options for the keyword if they exist.
    default : _dtype or int, optional
        The default value of the keyword or the index of it in ``options``.

        If ``options`` exists, then this is the index of the default
        option. For example, if ``options=("CG", "DIIS", "Pople")`` then
        setting ``default=2`` means the default is ``"Pople"``.
    minimum : int or float, optional
        The minimum possible value.
    maximum : int or float, optional
        The maximum possible value.
    """

    key_name: str
    _dtype: ORCAString | str | bool | int | float | Sequence
    options: tuple[ORCAString | str | bool | int | float | Sequence] | None = None
    default: ORCAString | str | bool | int | float | Sequence | None = None
    minimum: int | float | None = None
    maximum: int | float | None = None

    @property
    def dtype(self) -> str:
        if self._dtype is ORCAString:
            return "string"
        elif self._dtype is str:
            return "string"
        elif self._dtype is bool:
            return "boolean"
        elif self._dtype is int:
            return "integer"
        elif self._dtype is float:
            return "float"
        elif self._dtype is Sequence:
            return "sequence"
        else:
            raise ValueError(
                f"Invalid Type {self._dtype} for BlockEnum member {self}.\n"
                "How did you even get here?"
            )


class BlockEnum(BlockKeyword, Enum):
    """Base class for block keyword enums."""

    def __new__(
        cls,
        key_name: str,
        _dtype: ORCAString | str | bool | int | float | Sequence,
        options: tuple[ORCAString | str | bool | int | float | Sequence] | None = None,
        default: ORCAString | str | bool | int | float | Sequence | None = None,
        minimum: int | float | None = None,
        maximum: int | float | None = None,
    ):
        self = BlockKeyword.__new__(cls)
        self._value_ = key_name
        return self

    def format(
        self,
        value: ORCAString | str | bool | int | float | Sequence,
        indent: int = 4,
    ) -> str:
        """Format a keyword with its value."""
        if not isinstance(value, self._dtype):
            raise TypeError(
                f"Improper type {type(value)} for keyword {self.key_name}!"
            )

        output = " " * indent + f"{self.value} = "
        match self._dtype:
            case ORCAString():
                output += f'"{value}"\n'
            case str():
                output += f"{value}\n"
            case bool():
                output += f"{value!s}\n"
            case int():
                output += f"{value}\n"
            case float():
                output += f"{value:8.6f}\n"
            case Sequence():
                for item in value[:-1]:
                    output += f"{item}, "
                output += f"{value[-1]}\n"

        return output






