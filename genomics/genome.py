"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .sequence_set import SequenceSet

class Genome(SequenceSet):
    """
    # Properties

    """

    def __init__(self, sequences):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def calculate_gc(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_genes(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_transcripts(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_proteins(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()
