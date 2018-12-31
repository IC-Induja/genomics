"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .core.table import FlatTable
from .region import RegionBase

class Annotation(RegionBase):
    """
    # Properties

    """

    def __init__(self, annotation_data, region=None, start=None, stop=None, strand=None):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

class DNAAnnotation(Annotation):
    """
    # Properties

    """

    def compute_gc(self):
        raise NotImplementedError()

class AnnotationTable(FlatTable):
    """
    # Properties
    - start
    - stop
    - strand
    - seqid
    - source
    - type
    - score
    - phase
    - attributes (a dict?? ordered dict?? variable length array??)
    - _pointer to a sequence
    - _seq_is_double_stranded (? redundant)
    - _seq_length
    - _seq_is_double_stranded
    - _ignore_boundary_checks

    """
    # NOTE: basically a RegionTable w/ additional columns
    def __init__(self, keep_cds_annotations=False, use_headers=None):
        raise NotImplementedError()

    @property
    def genes(self):
        """
        # Arguments

        # Returns
        list of Gene: list of Gene objects, representing each gene in the annotation table
        """
        raise NotImplementedError()

    @property
    def transcripts(self):
        raise NotImplementedError()

    def ORFs(self):
        raise NotImplementedError()

    def apply(self, fn, col=None):
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
