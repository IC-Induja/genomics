""" Contains Table class, as well as its derivative FlatTable which restrcts
    nested rows.
"""

class Table(object):
    """
    """
    def __init__(self):
        raise NotImplementedError()

    def filter(self, fn, col=None):
        raise NotImplementedError()

    def apply(self, fn, col=None):
        raise NotImplementedError()

    def save_as(self, path, filetype=None, overwrite_existing=False):
        raise NotImplementedError()

class FlatTable(Table):
    """
    """
    def __init__(self):
        raise NotImplementedError()

    def as_df():
        raise NotImplementedError()
