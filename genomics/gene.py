"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .annotation import Annotation

# Note: should we be able to add sequence to annotation at a later time/ have annotations w/ no sequence???
class Gene(Annotation):
    """Gene. Located on DNA or RNA sequence.

    # Properties
    - id
    - start
    - stop
    - strand
    - sequence
    """

    def __init__(self, **kwargs):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def get_utr5(self):
        raise NotImplementedError()

    def get_utr3(self):
        raise NotImplementedError()

    def get_exon(self, exon_number, index=1):
        raise NotImplementedError()

    def get_exons(self):
        raise NotImplementedError()

    def get_intron(self, intron_number, index=1):
        raise NotImplementedError()

    def get_introns(self, intron_number, index=1):
        raise NotImplementedError()
