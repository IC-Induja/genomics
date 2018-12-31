""" Contains the RegionBase class, as well as its derivatives LinearRegion and
    CircularRegion. Also contains the Region class, which is an abstraction over
    either LinearRegion or CircularRegion
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class RegionBase(object):
    """Contiguous area on DNA sequence.

    # Properties
    - start (int or iterable of ints): index of first base in region, or indices
        of first base in each section of re
    - stop (int)
    - strand
    - sequence_id
    """
    def __init__(self, start, stop, strand=None, sequence_key=None):
        raise NotImplementedError()

    @property
    def start(self):
        """ pure virtual method """
        raise NotImplementedError()

    @property
    def stop(self):
        """ pure virtual method """
        raise NotImplementedError()

    @property
    def strand(self):
        """ pure virtual method """
        raise NotImplementedError()

    @property
    def seq_id(self):
        """ pure virtual method """
        raise NotImplementedError()

    @property
    def length(self):
        """ pure virtual method """
        raise NotImplementedError()

    def get_start(self):
        """ pure virtual method """
        raise NotImplementedError()

    def get_end(self):
        """ pure virtual method """
        raise NotImplementedError()

    def intersects(self):
        """ pure virtual method """
        raise NotImplementedError()

    def contains(self):
        """ pure virtual method """
        raise NotImplementedError()

    def is_within(self):
        """ pure virtual method """
        raise NotImplementedError()

    def is_upstream_of(self):
        """ pure virtual method """
        raise NotImplementedError()

    def is_downstream_of(self):
        """ pure virtual method """
        raise NotImplementedError()

    def end5(self):
        """ pure virtual method """
        raise NotImplementedError()

    def end3(self):
        """ pure virtual method """
        raise NotImplementedError()

    def as_positive_strand(self):
        """ pure virtual method """
        raise NotImplementedError()

    def as_negative_strand(self):
        """ pure virtual method """
        raise NotImplementedError()

    def as_opposite_strand(self):
        """ pure virtual method """
        raise NotImplementedError()

class ContinuousRegion(RegionBase):
    def __init__(self, start, stop, strand='+', sequence=None, seq_length=None,
                 seq_start_index=1, seq_is_double_stranded=True, seq_id=None,
                 ignore_seq_id=False):

        # Need to provide either sequence or sequence info to check boundaries
        assert (sequence or seq_length)
        assert strand in {'+', '-'}

        if sequence:
            self._seq_length = len(sequence)
            self._seq_start_index = sequence.start_index
            self._seq_is_double_stranded = sequence.is_double_stranded
            self.seq_id = None if ignore_seq_id else sequence.id

        else:
            self._seq_length = seq_length
            # seq_start_index must be non-negative
            assert seq_start_index >= 0
            self._seq_start_index = seq_start_index
            self._seq_is_double_stranded = seq_is_double_stranded
            self.seq_id = None if ignore_seq_id else seq_id

        # NOTE: start and stop coordinates are stored internally as 0-indexed
        #       coordinates on the positive strand
        if strand == '+':
            self._start = start - self._seq_start_index
            self._stop = stop - self._seq_start_index
            self._on_reverse = False
        else:
            self._start = stop - self._seq_start_index
            self._stop = start - self._seq_start_index
            self._on_reverse = True

        assert self._within_sequence(self._start, self._stop)

        # error if region is on negative strand of a sequence w/ no negative strand
        assert(self._seq_is_double_stranded or self.strand == '+')

    @property
    def start(self):
        """
        # Returns

        """
        if self._on_reverse:
            return self._stop + self._seq_start_index

        return self._start + self._seq_start_index

    @property
    def stop(self):
        """
        # Returns

        """
        if self._on_reverse:
            return self._start + self._seq_start_index

        return self._stop + self._seq_start_index

    @property
    def strand(self):
        """
        # Returns

        """
        return '-' if self._on_reverse else '+'

    def end5(self):
        """
        # Arguments

        # Returns

        """
        return __class__.__init__(self.start, self.start, self.strand,
                                  seq_length=self._seq_length,
                                  seq_start_index=self._seq_start_index,
                                  seq_is_double_stranded=self._seq_is_double_stranded,
                                  seq_id=self.seq_id)

    def end3(self):
        """
        # Arguments

        # Returns

        """
        return __class__.__init__(self.stop, self.stop, self.strand,
                                  seq_length=self._seq_length,
                                  seq_start_index=self._seq_start_index,
                                  seq_is_double_stranded=self._seq_is_double_stranded,
                                  seq_id=self.seq_id)

    def as_positive_strand(self):
        """
        # Arguments

        # Returns

        """
        return __class__.__init__(self._start, self._stop, '+',
                                  seq_length=self._seq_length,
                                  seq_start_index=self._seq_start_index,
                                  seq_is_double_stranded=self._seq_is_double_stranded,
                                  seq_id=self.seq_id)

    def as_negative_strand(self):
        """
        # Arguments

        # Returns

        """
        # make sure sequence _has_ negative strand
        assert self._seq_is_double_stranded

        return __class__.__init__(self._stop, self._start, '-',
                                  seq_length=self._seq_length,
                                  seq_start_index=self._seq_start_index,
                                  seq_is_double_stranded=self._seq_is_double_stranded,
                                  seq_id=self.seq_id)

    def as_opposite_strand(self):
        """
        # Arguments

        # Returns

        """
        # make sure sequence _has_ negative strand
        assert self._seq_is_double_stranded

        if self._on_reverse:
            # convert to positive strand
            strand = '+'
            start = self._start
            stop = self._stop
        else:
            # convert to negative strand
            strand = '-'
            start = self._stop
            stop = self._start

        return __class__.__init__(start, stop, strand,
                                  seq_length=self._seq_length,
                                  seq_start_index=self._seq_start_index,
                                  seq_is_double_stranded=self._seq_is_double_stranded,
                                  seq_id=self.seq_id)

    def shift(self):
        """ pure virtual method """
        raise NotImplementedError()

    def expand(self):
        """ pure virtual method """
        raise NotImplementedError()

    def _within_sequence(self, start, stop):
        """Internal method to check whether a the provided start and stop
        are valid for the region's sequence.

        # Arguments
        start (int): start coordinate
        stop (int): stop coordinate

        # Returns
        bool: True if start and stop are valid.
        """

        if start < self._seq_start_index or stop < self._seq_start_index:
            return False

        max_index = self._seq_start_index + self._seq_length
        if start > max_index or stop > max_index:
            return False

        return True

class LinearRegion(ContinuousRegion):
    """Description of a region on a linear sequence.

    Note: Must pass in either sequence or seq_length as an argument.
            Helps ensure start and stop are valid positions on the sequence.

    # Properties
    - start (int): Coordinate of furthest base at 5' end of Region
    - stop (int): Coordinate one base past furthest base at 3' end of Region
    - strand (str): One of {'+', '-'}. Defaults to '+'. By convention,
        uses '+' to refer to the single strand in a single-stranded sequence.
    - sequence (str, None): Id of sequence that Region is on. Defaults to None.
    """

    def __init__(self, start, stop, strand='+', sequence=None, seq_length=None,
                 seq_start_index=1, seq_is_double_stranded=True, seq_id=None,
                 ignore_seq_id=False):

        # throws error if start and stop are in wrong position relative to each other
        assert((strand == '+' and start <= stop)
               or (strand == '-' and stop <= start))

        ContinuousRegion.__init__(self, start, stop, strand, sequence, seq_length,
                                  seq_start_index, seq_is_double_stranded,
                                  seq_id, ignore_seq_id)

    @property
    def length(self):
        return self._start - self._stop

    def __repr__(self):
        if self.seq_id:
            return 'Region<%s:%d-%d:%s>' % (self.seq_id, self.start, self.stop, self.strand)

        return 'Region<%d-%d:%s>' % (self.start, self.stop, self.strand)

    def get_start(self):
        """
        # Arguments

        # Returns

        """
        if self._start != self._stop:
            return self.start

        # region is a zero-length interval, which is represented as an interval
        #   of length 1 (a single base) in the GFF format, with the intended
        #   interval to the **right** of the given base
        return self.start - 1

    def get_end(self):
        """
        # Arguments

        # Returns

        """
        return self.stop - 1

    def shift(self, bases, direction='downstream'):
        """
        # Arguments
        bases (int):
        direction (str): One of: {upstream, downstream}.

        # Returns

        """
        assert direction in {'upstream', 'downstream'}
        shift = -bases if direction == 'upstream' else bases

        if self._on_reverse:
            start = self._stop - shift + self._seq_start_index
            stop = self._start - shift + self._seq_start_index
        else:
            start = self._start + shift + self._seq_start_index
            stop = self._stop + shift + self._seq_start_index

        assert self._within_sequence(start, stop)

        return LinearRegion(start, stop, self.strand,
                            seq_length=self._seq_length,
                            seq_start_index=self._seq_start_index,
                            seq_is_double_stranded=self._seq_is_double_stranded,
                            seq_id=self.seq_id)

    def expand(self, upstream, downstream):
        """
        # Arguments

        # Returns

        """
        if self._on_reverse:
            start = self._stop + upstream
            stop = self._start - downstream
        else:
            start = self._start - upstream
            stop = self._stop + downstream

        assert self._within_sequence(start, stop)

        return LinearRegion(start, stop, self.strand,
                            seq_length=self._seq_length,
                            seq_start_index=self._seq_start_index,
                            seq_is_double_stranded=self._seq_is_double_stranded,
                            seq_id=self.seq_id)

    # def slice(self, start, stop):
    #     """
    #     Slice using python slice notation.
    #
    #     # Arguments
    #
    #     # Returns
    #
    #     """
    #     raise NotImplementedError()

    def contains(self, other_region):
        """
        # Arguments

        # Returns

        """
        return (self._on_reverse == other_region._on_reverse
                and self._start <= other_region._start
                and self._stop >= other_region._stop)

    def is_within(self, other_region):
        """
        # Arguments

        # Returns

        """
        return other_region.contains(self)

    def overlaps(self, other_region):
        """
        # Arguments

        # Returns

        """
        return (self._on_reverse == other_region._on_reverse
                and ((self._start <= other_region._start
                      and other_region._start <= self._stop)
                     or (self._start <= other_region._stop
                         and other_region._stop <= self._stop)))

    def _within_sequence(self, start, stop):
        """Internal method to check whether a the provided start and stop
        are valid for the region's sequence.

        # Arguments
        start (int): start coordinate
        stop (int): stop coordinate

        # Returns
        bool: True if start and stop are valid.
        """

        if start < self._seq_start_index or stop < self._seq_start_index:
            return False

        max_index = self._seq_start_index + self._seq_length
        if start > max_index or stop > max_index:
            return False

        return True

# NOTE: should regions keep track of length of sequence they are on???
class CircularRegion(RegionBase):
    """ Description of a contiguous region on a circular sequence, where the last base
        immediately precedes the first.

    # Properties
    - start (int): Coordinate of base at 5' end of Region
    - end (int): Coordinate of base at 3' end of Region
    - strand (str, None): One of {'+', '-', None}. Defaults to None.
    - sequence (str, None): Id of sequence that Region is on. Defaults to None.
    """

    def __init__(self, start, stop, strand='+', sequence=None, seq_length=None,
                 seq_start_index=1, seq_is_double_stranded=True, seq_id=None,
                 ignore_seq_id=False):
        # Note: all sequence (seq_) parameters are ignored if sequence is provided
        # Need to provide either sequence or sequence info to check boundaries
        ContinuousRegion.__init__(self, start, stop, strand, sequence, seq_length,
                                  seq_start_index, seq_is_double_stranded,
                                  seq_id, ignore_seq_id)

        self._crosses_origin = self._start > self._stop

    @property
    def length(self):
        if self._crosses_origin:
            return self._seq_length - self._start + self._stop

        return self._stop - self._start

    def __repr__(self):
        if self.seq_id:
            return 'Region<%s:%d-%d:%s is_circular=True>' % (self.seq_id, self.start, self.stop, self.strand)

        return 'Region<%d-%d:%s is_circular=True>' % (self.start, self.stop, self.strand)

    def get_start(self):
        raise NotImplementedError()

    def get_end(self):
        raise NotImplementedError()

    def shift(self, bases, direction=None):
        """
        # Arguments

        # Returns

        """
        if self._on_reverse:
            start = ""
            stop = ""
        else:
            start = start + b

    def expand(self, upstream, downstream):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # def slice(self, start, end):
    #     """
    #     # Arguments
    #
    #     # Returns
    #
    #     """
    #     raise NotImplementedError()

    def contains(self, other_region):
        raise NotImplementedError()

    def is_within(self, other_region):
        raise NotImplementedError()

    def overlaps(self, other_region):
        raise NotImplementedError()

class Region(ContinuousRegion):
    """ Wrapper providing abstraction for circular or linear region.
    """
    def __init__(self, start, stop, strand='+', sequence=None,
                 seq_is_circular=False, seq_length=None, seq_start_index=1,
                 seq_is_double_stranded=True, seq_id=None, ignore_seq_id=False):

        if sequence.is_circular or seq_is_circular:
            self._region = CircularRegion(
                start, stop, strand, sequence, seq_length,
                seq_start_index, seq_is_double_stranded,
                seq_id, ignore_seq_id)

        else:
            self._region = LinearRegion(
                start, stop, strand, sequence, seq_length,
                seq_start_index, seq_is_double_stranded,
                seq_id, ignore_seq_id)

    @property
    def start(self):
        return self._region.start

    @property
    def stop(self):
        return self._region.stop

    @property
    def strand(self):
        return self._region.strand

    @property
    def seq_id(self):
        return self._region.seq_id

    @property
    def length(self):
        return self._region.length

    def get_start(self):
        return self._region.get_start()

    def get_end(self):
        return self._region.get_end()

    def intersects(self):
        return self._region.intersects()

    def contains(self):
        return self._region.contains()

    def is_within(self):
        return self._region.is_within()

    def is_upstream_of(self):
        return self._region.is_upstream_of()

    def is_downstream_of(self):
        return self._region.is_downstream_of()

    def end5(self):
        return self._region.end5()

    def end3(self):
        return self._region.end3()

    def as_positive_strand(self):
        return self._region.as_positive_strand()

    def as_negative_strand(self):
        return self._region.as_negative_strand()

    def as_opposite_strand(self):
        return self._region.as_opposite_strand()
