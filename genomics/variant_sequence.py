"""
"""

from .sequence import Sequence
from .sequence_set import SequenceSet

class VariantSequence(Sequence):
    """
    # Properties

    """
    def __init__(self, variant_data, sequence):
        raise NotImplementedError()

class VariantSequenceSet(SequenceSet):
    """
    # Properties

    """
    def __init__(self, variant_data, sequence_set):
        raise NotImplementedError()

class VariantGenome(VariantSequenceSet):
    """
    # Properties

    """
    def __init__(self, variant_data, sequence):
        raise NotImplementedError()
