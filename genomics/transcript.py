"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Note: should we be able to add sequence to annotation at a later time/ have annotations w/ no sequence???
class Transcript(object):
    """Transcript.

    # Properties
    - start
    - stop
    - strand
    - sequence
    """
    # show polyadenylation site?? poly-a tail?

    def __init__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    @property
    def exons(self):
        """
        Get all exons.

        # Returns
        SequenceSet: exons

        """
        raise NotImplementedError()

    @property
    def introns(self, intron_number, index=1):
        """
        Get all introns.

        # Returns
        SequenceSet: introns

        """
        raise NotImplementedError()

    @property
    def utr5(self):
        """
        Get the 5' untranslated region (non-coding region at the 5' end of the
        RNA transcript, before the first exon).

        # Returns
        Sequence: 5' untranslated region

        """
        raise NotImplementedError()

    @property
    def utr3(self):
        """
        Get the 3' untranslated region (non-coding region at the 3' end of the
        RNA transcript, after the final exon).

        # Returns
        Sequence: 3' untranslated region

        """
        raise NotImplementedError()

    @property
    def CDSs(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    @property
    def ORF(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_exon(self, exon_number, start_index=1):
        """
        Get specified exon (coding region within the gene). By default, first
        exon has index 1.

        # Arguments
        exon_number (int): desired exon
        start_index (int): index of first exon

        # Returns
        Sequence: exon

        """
        raise NotImplementedError()

    def get_intron(self, intron_number, index=1):
        """
        Get specified intron (non-coding region within the gene, between two
        exons). By default, first intron has index 1.

        # Arguments
        intron_number (int): desired intron
        start_index (int): index of first intron

        # Returns
        Sequence: intron

        """
        raise NotImplementedError()

    def get_cds(self, intron_number, index=1):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_polypeptide(self):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()


    def save_as(self):
        """
        Supported file formats: .arrow, .csv, .tsv, .gff
        """
        raise NotImplementedError()
