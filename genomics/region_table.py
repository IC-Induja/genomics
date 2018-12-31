""" Contains RegionTable, for vectorized processing of many regions at once
"""

from .core.table import Table

class BaseRegionTable(Table):
    """
    # Properties

    """
    def __init__(self):
        raise NotImplementedError()

    def __getitem__(self, key):
        raise NotImplementedError()

    def __len__(self):
        """returns number of items in the table, NOT list of region lengths
        """
        raise NotImplementedError()
    # start of BaseRegion interface
    @property
    def start(self):
        raise NotImplementedError()

    @property
    def stop(self):
        raise NotImplementedError()

    @property
    def strand(self):
        raise NotImplementedError()

    @property
    def sequence_id(self):
        raise NotImplementedError()

    @property
    def length(self):
        raise NotImplementedError()

    def get_start(self):
        raise NotImplementedError()

    def get_end(self):
        raise NotImplementedError()

    def intersects(self):
        raise NotImplementedError()

    def contains(self):
        raise NotImplementedError()

    def is_within(self):
        raise NotImplementedError()

    def is_upstream_of(self):
        raise NotImplementedError()

    def is_downstream_of(self):
        raise NotImplementedError()

class ContinuousRegionTable(BaseRegionTable):
    def __init__(self):
        raise NotImplementedError()

    def end5(self):
        raise NotImplementedError()

    def end3(self):
        raise NotImplementedError()

    def as_positive_strand(self):
        raise NotImplementedError()

    def as_negative_strand(self):
        raise NotImplementedError()

    def as_opposite_strand(self):
        raise NotImplementedError()

    def shift(self):
        """virtual"""
        raise NotImplementedError()

    def expand(self):
        """virtual"""
        raise NotImplementedError()

class LinearRegionTable(ContinuousRegionTable):
    def __init__(self):
        raise NotImplementedError()

    def get_start(self):
        raise NotImplementedError()

    def get_end(self):
        raise NotImplementedError()

    def shift(self):
        raise NotImplementedError()

    def expand(self):
        raise NotImplementedError()


class CircularRegionTable(ContinuousRegionTable):
    def __init__(self):
        raise NotImplementedError()

    def get_start(self):
        raise NotImplementedError()

    def get_end(self):
        raise NotImplementedError()

    def shift(self):
        raise NotImplementedError()

    def expand(self):
        raise NotImplementedError()

class RegionTable(ContinuousRegionTable):
    """
    # Properties

    """
    def __init__(self):
        raise NotImplementedError()
    # needs to implement continuous region table interface (ie. "Region" interface)
    def __getitem__(self, key):
        raise NotImplementedError()

    def __len__(self):
        """returns number of items in the table, NOT list of region lengths
        """
        raise NotImplementedError()

    @property
    def start(self):
        raise NotImplementedError()

    @property
    def stop(self):
        raise NotImplementedError()

    @property
    def strand(self):
        raise NotImplementedError()

    @property
    def sequence_id(self):
        raise NotImplementedError()

    @property
    def length(self):
        raise NotImplementedError()

    def get_start(self):
        raise NotImplementedError()

    def get_end(self):
        raise NotImplementedError()

    def intersects(self):
        raise NotImplementedError()

    def contains(self):
        raise NotImplementedError()

    def is_within(self):
        raise NotImplementedError()

    def is_upstream_of(self):
        raise NotImplementedError()

    def is_downstream_of(self):
        raise NotImplementedError()

    def end5(self):
        raise NotImplementedError()

    def end3(self):
        raise NotImplementedError()

    def as_positive_strand(self):
        raise NotImplementedError()

    def as_negative_strand(self):
        raise NotImplementedError()

    def as_opposite_strand(self):
        raise NotImplementedError()

    def shift(self):
        raise NotImplementedError()

    def expand(self):
        raise NotImplementedError()
    # end of continuous region interface
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
