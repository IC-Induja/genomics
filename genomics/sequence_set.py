""" SequenceSet class
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class SequenceSet(object):
    """Abstract class for a collection of sequences.

    # Properties
    id (str): Identifier. If none is provided, uses a uuid.
    id_type (str): Source of identifier.
    sequences (list of sequences): Genome contents.
    start_index (int): TODO
    annotations (AnnotationTable): table containing all annotations, created by
        concatenating the individual AnnotationTable for every Sequence in the
        SequenceSet
    """

    def __init__(self, sequences, start_index=None):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    @classmethod
    def from_file(path, filetype=None):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def reindex(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_subset(self, slice):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def find(self, query, limit=1):
        """
        # Arguments

        # Returns

        """
        allowed_kwargs = {'strand', 'all'}
        raise NotImplementedError()

    def count(self, query):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def find_pattern(self, pattern, limit=1, overlapping=True):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def count_pattern(self, pattern):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def compute_distance(self, regionA, regionB, fn="levhenstein"):
        """
        # Arguments

        # Returns

        """
        # NOTE: need to look into commonly used functions, determine most
        #       commonly used/best one, and set that to default
        raise NotImplementedError()

    def apply_variant(self, genomic_variant):
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

    def save_sequences(self, path, filetype=None, overwrite_existing=False):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def save_annotations(self, path, filetype=None, overwrite_existing=False):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

class DNASet(SequenceSet):
    """ SequenceSet with DNA-specific methods for fetching and storing
    """
    # NOTE: Use Sequence constructor until this is implemented
    # def __init__(self):
    #     raise NotImplementedError()

    def calculate_gc(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    @classmethod
    def from_db(data_specification, db="ncbi", key_type="accession",
                with_annotations=True, start_index=1, allowed_chars=None,
                start_col=("start"), end_col=("end", "stop"),
                key_col=("key", "accession"), keys_from_file=False,
                tabular_file=False):
                # NOTE: if parsing from file, col names are case_insensitive
        """ Fetches multiple sequences or sequence subsets from external db

        Compatible with multiple ways of specifying data.
        When `keys_from_file=False`:
        - If data_specification is iterable of strings, each string should be
        an key for a distinct sequence in the db.
        - If data_specification is iterable of tuples, each tuple should be in
        the format (key, start, stop) where:
            - key is the db key for the sequence
            - start is the index of the first element to be included
            - end is the index of the last element to be included.
        If stop is omitted, uses index of last
        element in db sequence. If both start and stop are omitted, entire
        sequence will be used.

        When `keys_from_file=True`:
        - if data_specification is string, should be a path or url to either:
            - if `from_tabular_file=False`: a file containing a list of db keys
            - if `from_tabular_file=True`: a tabular file with a column
            containing db keys, an (optional) column containing start indexes,
            and an (optional) column containing stop indexes
        - if data_specification is pandas DataFrame, if should contain a column
            of data keys, (optional) column of start indexes and (optional)
            column of stop indexes

        # Arguments
        data_specification (iterable, str, or pd.DataFrame): sequences specified
            in the above format



        # Returns

        # Raises
        ValueError:
        """
        raise NotImplementedError()

class RNASet(SequenceSet):
    """ SequenceSet with RNA-specific methods for fetching and storing
    """

    def calculate_gc(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def from_db(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

class AminoAcidsSet(SequenceSet):
    """ SequenceSet with AminoAcids-specific methods for fetching and storing
    """

    def from_db(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()
