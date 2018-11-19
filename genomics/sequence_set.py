"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class SequenceSet(object):
    """
    """

    def __init__(self, sequences):
        allowed_kwargs = {'index', 'id', 'id_type'}
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def get_subset(self, slice):
        raise NotImplementedError()

    def find(self, query):
        allowed_kwargs = {'strand', 'all'}
        raise NotImplementedError()

    def count(self, query):
        raise NotImplementedError()

    def find_pattern(self, pattern, all=False):
        raise NotImplementedError()

    def count_pattern(self, pattern):
        raise NotImplementedError()

    def compute_distance(self, regionA, regionB, fn="levhenstein"):
        raise NotImplementedError()

    def apply_variant(self, genomic_variant):
        raise NotImplementedError()
