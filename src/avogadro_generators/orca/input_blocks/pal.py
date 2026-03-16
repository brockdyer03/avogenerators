"""Classes and methods for the %pal block."""

from .block_base import BlockEnum

class PAL(BlockEnum):

    NPROCS = "nprocs", int, None, 0
