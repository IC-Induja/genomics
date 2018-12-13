""" Contains Set class
"""

class Set(object):
    """ An unordered collection of objects, each identified by unique key

    # Properties
    data:
    data_keys (List<str>):

    """
    # NOTE: Internally, this needs to be implemented w/ some sort of ordering,
    #       to ensure reproducibility of results (for things like find,
    #       find_pattern, etc.)
    def __init__(self, type):
        raise NotImplementedError()

    # NOTE: set should be iterable??
    def __len__(self):
        raise NotImplementedError()

    def __getitem__(self, pos):
        raise NotImplementedError()

    def __add__(self, other):
        """Set Addition"""
        raise NotImplementedError()

    def __sub__(self, other):
        """Set Difference"""
        raise NotImplementedError()

    # TODO: also implement union, intersection, xor, etc. Consider extending
    #       actual python set object?

    # NOTE: Until __repr__ is implemented, leave it commented so default repr is
    #       used.

    # def __repr__(self, other):
    #     """Should show all sets in alphabetical order"""
    #     raise NotImplementedError()

    @property
    def data_keys(self):
        raise NotImplementedError()

    def insert(self, data):
        raise NotImplementedError()

    def remove(self, data):
        raise NotImplementedError()
