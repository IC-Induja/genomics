"""
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class Annotation(object):
    """
    """

    def __init__(self, **kwargs):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()


class DNAAnnotation(object):
    """
    """

    def gc(self):
        raise NotImplementedError()
