""" Contains Variant and VariantTable, for representing sequence variation"""

from .core.table import FlatTable

class Variant(object):
    """
    # Properties

    """

    def __init__(self, variant_data, ref=None, alt=None, position=None, sequence=None):
        """ Makes it easy to construct variants from variant string (of either type)
        """
        raise NotImplementedError()

    @property
    def type(self):
        """Example types: insertion, deletion, snp, etc
        """
        raise NotImplementedError()

class ClinvarVariant(Variant):
    """
    # Properties
    - ref
    - alt
    - position (genomic coordinate)
    - sequence (chromosome)
    - gene(s?)
    - condition
    - is_pathogenic
    - pathogenicity_is_known
    - clinical_significance
    - (chr_grch37, loci_grch37, chr_grch38, loci_grch38)
    - variation_id
    - allele_ids(comma seperated value? list?)
    - is_indel
    - is_coding_variant
    - is_synonymous
    - protein_index
    - protein_ref
    - is_missense

    """
    def __init__(self):
        raise NotImplementedError()



class VariantTable(FlatTable):
    """
    # Properties

    """
    def __init__(self):
        raise NotImplementedError()

    def __getitem__(self, key):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    @classmethod
    def from_file(self, path, filetype=None, start_index=1):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    @classmethod
    def from_db(self):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def append(self):
        raise NotImplementedError()

    def sort(self):
        raise NotImplementedError()

    def merge(self):
        raise NotImplementedError()

    def count(self):
        """ Return number of variants (same as __len__)
        """
        raise NotImplementedError()

    def get_noncoding(self):
        raise NotImplementedError()

    def as_df(self):
        raise NotImplementedError()

    def save_as(self, path, filetype=None, overwrite_existing=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

class ClinvarVariantTable(FlatTable):
    """
    # Properties

    """
    def __init__(self):
        raise NotImplementedError()
