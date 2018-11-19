"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .sequence_set import SequenceSet

class Genome(SequenceSet):
    """
    """

    def __init__(self, sequences):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def gc(self):
        raise NotImplementedError()

    def get_genes(self):
        raise NotImplementedError()

    def get_transcripts(self):
        raise NotImplementedError()

    def get_proteins(self):
        raise NotImplementedError()
