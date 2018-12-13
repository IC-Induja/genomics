"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .core.table import FlatTable

class Annotation(object):
    """
    # Properties

    """

    def __init__(self, annotation_data, region=None, start=None, stop=None, strand=None):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

# NOTE: if I don't come up w/ other useful methods for this, remove class
class DNAAnnotation(Annotation):
    """
    # Properties

    """

    def compute_gc(self):
        raise NotImplementedError()

class AnnotationTable(FlatTable):
    """
    # Properties

    """
    def __init__(self, keep_cds_annotations=False, use_headers=None):
        raise NotImplementedError()

    def get_genes(self):
        """
        # Arguments

        # Returns
        list of Gene: list of Gene objects, representing each gene in the annotation table
        """
        raise NotImplementedError()

    def filter(self, fn, col=None):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def filter_type(self, type):
        """
        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def filter_region(self, region=None, start=None, stop=None, strand=None):
        """
        # Arguments

        # Returns

        """
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
