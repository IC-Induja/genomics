""" Contains Variant and VariantTable, for representing sequence variation"""

from .core.table import FlatTable

class Variant(object):
    """
    # Properties

    """
    def __init(self, ref, alt, position, sequence=None):
        raise NotImplementedError()

class VariantTable(FlatTable):
    """
    # Properties

    """
    def __init__(self):
        raise NotImplementedError()

    @classmethod
    def from_file(self, path, filetype=None, start_index=1):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    @classmethod
    def from_db(self):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def save_as(self, path, filetype=None, overwrite_existing=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()
