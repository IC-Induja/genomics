""" Contains RegionTable, for fast vectorized processing of many regions
"""

from .core.table import Table

class RegionTable(Table):
    """
    # Properties

    """
    def __init__(self):
        raise NotImplementedError()

    @classmethod
    def from_file(self, path, sep='\t', start_col="start", end_col= "end",
        strand_col="strand", sequence_key_col=("key", "accession")):
        """ Should be able to pull regions from tabular files with start and end
            columns (as well as optional strand and sequence_key columns)
        """
        raise NotImplementedError()

    @classmethod
    def from_db(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def save_as(self, path, format=None, overwrite_existing=False):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()
