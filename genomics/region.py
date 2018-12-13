""" Contains the BaseRegion class, as well as its derivatives LinearRegion and
    CircularRegion and the Region class, which is an abstraction over either
    LinearRegion or CircularRegion
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class BaseRegion(object):
    """Is contiguous
    """
    def __init__(self, start, stop, strand=None, sequence_key=None):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def get_start(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_stop(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

# NOTE: should regions keep track of length of sequence they are on???
class LinearRegion(BaseRegion):
    """Description of a region on a linear sequence.

    # Properties
    - start (int): Coordinate of furthest base at 5' end of Region
    - stop (int): Coordinate of furthest base at 3' end of Region
    - strand (str, None): One of {'+', '-', None}. Defaults to None.
    - sequence (str, None): Id of sequence that Region is on. Defaults to None.
    """

    def __init__(self, start, stop, strand=None, sequence=None):
        self.start = start
        self.stop = stop
        self.strand = strand
        self.sequence = sequence


        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def shift(self, bases, direction=None):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def expand(self, upstream, downstream):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def slice(self, start, stop):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def end5(self):
        """
        # Arguments

        # Returns

        """
        return Region(self.start, self.start, self.strand, self.sequence)

    # TODO: implement TODO: Ana
    def end3(self):
        """
        # Arguments

        # Returns

        """
        return Region(self.stop, self.stop, self.strand, self.sequence)

    # TODO: implement TODO: Ana
    def as_positive_strand(self):
        """
        # Arguments

        # Returns

        """
        if self.strand == '+':
            return Region(self.start, self.stop, self.strand, self.sequence)
        elif self.strand == '-':
            return Region(self.stop, self.start, "+", self.sequence)

    # TODO: implement TODO: Ana
    def as_negative_strand(self):
        """
        # Arguments

        # Returns

        """
        if self.strand == '-':
            return Region(self.start, self.stop, self.strand, self.sequence)
        elif self.strand == '+':
            return Region(self.stop, self.start, "-", self.sequence)

    # TODO: implement TODO: Ana
    def as_opposite_strand(self):
        """
        # Arguments

        # Returns

        """
        if self.strand == '+':
            return Region(self.stop, self.start, '-', self.sequence)
        elif self.strand == '-':
            return Region(self.stop, self.start, "+", self.sequence)

    # TODO: implement TODO: Ana
    def intersects(self, other_region):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def contains(self, other_region):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def is_within(self, other_region):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

# NOTE: should regions keep track of length of sequence they are on???
class CircularRegion(BaseRegion):
    """ Description of a contiguous region on a circular sequence, where the last base
        immediately precedes the first.

    # Properties
    - start (int): Coordinate of base at 5' end of Region
    - stop (int): Coordinate of base at 3' end of Region
    - strand (str, None): One of {'+', '-', None}. Defaults to None.
    - sequence (str, None): Id of sequence that Region is on. Defaults to None.
    """

    def __init__(self, start, stop, strand=None, sequence=None):
        self.start = start
        self.stop = stop
        self.strand = strand
        self.sequence = sequence

        # re
        self._crosses_origin = (
            (self.start > self.stop and ((not strand) or self.strand == '+')) or
            (self.start < self.stop and self.strand == '-'))

    # TODO: implement TODO: Ana
    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def shift(self, bases, direction=None):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def expand(self, upstream, downstream):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def slice(self, start, stop):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

# TODO: handle code duplication
### START of code duplication ###
    def end5(self):
        """
        # Arguments

        # Returns

        """
        return Region(self.start, self.start, self.strand, self.sequence)

    def end3(self):
        """
        # Arguments

        # Returns

        """
        return Region(self.stop, self.stop, self.strand, self.sequence)

    def as_positive_strand(self):
        """
        # Arguments

        # Returns

        """
        if self.strand == '+':
            return Region(self.start, self.stop, self.strand, self.sequence)
        elif self.strand == '-':
            return Region(self.stop, self.start, "+", self.sequence)

    def as_negative_strand(self):
        """
        # Arguments

        # Returns

        """
        if self.strand == '-':
            return Region(self.start, self.stop, self.strand, self.sequence)
        elif self.strand == '+':
            return Region(self.stop, self.start, "-", self.sequence)

    def as_opposite_strand(self):
        """
        # Arguments

        # Returns

        """
        if self.strand == '+':
            return Region(self.stop, self.start, '-', self.sequence)
        elif self.strand == '-':
            return Region(self.stop, self.start, "+", self.sequence)
### END of code duplication ###
    # TODO: implement TODO: Ana
    def intersects(self, other_region):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def contains(self, other_region):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement TODO: Ana
    def is_within(self, other_region):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

class Region(BaseRegion):
    """ Wrapper providing abstraction for circular or linear region.
    """

class DisjointRegion(BaseRegion):
    """
    # Properties

    """

    def __init__(self, start, stop, strand):
        raise NotImplementedError()

    def __len__(self):
        """DisjointRegion length. Sum of lengths of each Region contained in
        DisjointRegion.

        # Returns
        int: length
        """
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def get_regions(self):
        """Get Regions contained in DisjointRegion
        """
        raise NotImplementedError()

    def get_superset(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def end5(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def end3(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()
