"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class BaseRegion(object):
    """
    """
    def __len__(self):
        raise NotImplementedError()

    def get_start(self):
        raise NotImplementedError()

    def get_stop(self):
        raise NotImplementedError()

# NOTE: should regions keep track of length of sequence they are on???
class Region(BaseRegion):
    """Description of a region on a sequence or genome.

    # Properties
    - start (int):
    - stop (int):
    - strand (str):
    - sequence (Sequence):
    - _crosses_origin (bool):
    """

    # NOTE: should start be the location of the 5' end? or the smaller number?
    def __init__(self, start, stop, strand=None, sequence=None):
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def shift(self, bases, direction=None):
        raise NotImplementedError()

    def expand(self, upstream, downstream):
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def slice(self, start, stop):
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def end5(self):
        return Region(self.start, self.start, self.strand, self.sequence)

    # TODO: implement TODO: Ana
    def end3(self):
        return Region(self.stop, self.stop, self.strand, self.sequence)

    # TODO: implement TODO: Ana
    def as_positive_strand(self):
        if self.strand == '+':
            return Region(self.start, self.stop, self.strand, self.sequence)
        elif self.strand == '-':
            return Region(self.stop, self.start, "+", self.sequence)

    # TODO: implement TODO: Ana
    def as_negative_strand(self):
        if self.strand == '-':
            return Region(self.start, self.stop, self.strand, self.sequence)
        elif self.strand == '+':
            return Region(self.stop, self.start, "-", self.sequence)

    # TODO: implement TODO: Ana
    def as_opposite_strand(self):
        if self.strand == '+':
            return Region(self.stop, self.start, '-', self.sequence)
        elif self.strand == '-':
            return Region(self.stop, self.start, "+", self.sequence)

    # TODO: implement TODO: Ana
    def intersects(self, other_region):
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def contains(self, other_region):
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def is_within(self, other_region):
        raise NotImplementedError()


class DisjointRegion(BaseRegion):
    """
    """

    def __init__(self, start, stop, strand):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def get_regions(self):
        raise NotImplementedError()

    def get_superset(self):
        raise NotImplementedError()

    def end5(self):
        raise NotImplementedError()

    def end3(self):
        raise NotImplementedError()
