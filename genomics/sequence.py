""" Contains the base Sequence class, along with its derivatives:
    DNASequence, RNASequence, and AminoAcidSequence
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .constants import CODON_TABLE

class Sequence(object):
    """Abstract sequence class.

    # Properties
    id (str): Identifier. Must be unique within a genome. If none is provided, uses a uuid.
    id_type (str): Source of identifier.
    data (str): Sequence contents.
    start_index (int): Index representing first position in data. Default 1 (as 1-indexing is common in biology).
    """
    # NOTE: HOW to handle sequences w/ multiple (2) strands? find/count/etc don't work...

    # TODO: implement
    def __init__(self, seq, **kwargs):
        allowed_kwargs = {'id', 'id_type', 'index'}
        raise NotImplementedError()

    @classmethod
    def from_file(filepath, format=None, **kwargs):
        # NOTE: How should we handle multiline fasta? Ignore all but first sequence?
        # return array of sequences? Throw error? Throw error and suggest using sequence set?
        """Reads sequence data from file.

        Accepts a variety of biological formats (FASTA, Genbank, etc.).
        Also can read a raw sequence from .txt

        Accepted File Extentions:

        - 2bit:
        - FASTA: .fa, .fasta (if multiline FASTA, only first sequence is returned)
        - Genbank: .gbk
        - GFF: .gff, .gff3
        - Nibble: .nib
        - Plain Text: .txt

        Note: Annotation data in the file is ignored when constructing a sequence.

        # Arguments
        filepath (str): Location of file (absolute or relative filepath, or a URL)
        format (str): Format of file contents. If not provided, will be inferred form file extention.

        # Returns
        Sequence: sequence contained in file
        """
        allowed_kwargs = {'accepted_chars', 'id', 'id_type', 'index'}
        raise NotImplementedError()

    # TODO: implement
    @classmethod
    def from_db(id, db="ncbi"):
        """Constructs a sequence by fetching data from a commonly used
        biological database.

        Supports NCBI, EMBL, and DDOJ databases.

        # Arguments

        # Returns
        Sequence: Sequence retreived from database.
        """
        raise NotImplementedError()

    # TODO: implement
    def __len__(self):
        """Sequence length.

        # Returns
        int: length
        """
        raise NotImplementedError()

    # TODO: implement
    def __repr__(self):
        raise NotImplementedError()

    # TODO: implement

    # NOTE: should we allow for subsequences to keep their original indexing? or
    # should we have all the sequence methods take a start and stop argument?
    # (To specify what part of the sequence to be searching/ calculating in)
    def get_subsequence(self, **kwargs):
        # NOTE: what should we call our locations? Which one?: coordinate, position, loci, index
        """Gets subset of sequence.

        Note: subsequence is inclusive of both start and end indices.

        # Arguments
        start (int): index of first subsequence element. Defaults to start of sequence.
        stop (int): index of last subsequence element. Defaults to end of sequence.
        reindex (bool): if true, indexing of sequence will start at 1. Otherwise,
            indexing will be unchanged (ie. index of first element in sequence
            will be it's current position in the sequence, and so on)
        """
        allowed_kwargs = {'start', 'stop', 'reindex', 'index'}
        raise NotImplementedError()

    # TODO: implement
    def find(self, query, strand=None):
        """locates query in sequence.

        # Arguments
        query (string): string to search for

        # Returns
        Region: location of first match on sequence
        """
        raise NotImplementedError()

    # TODO: implement
    def count(self, query):
        raise NotImplementedError()

    # TODO: implement
    def find_pattern(self, pattern, all=False):
        raise NotImplementedError()

    # TODO: implement
    def count_pattern(self, pattern, include_overlapping=False):
        raise NotImplementedError()

    def compute_distance(self, regionA, regionB, fn="levhenstein"):
        raise NotImplementedError()

    def apply_variant(self, variant):
        raise NotImplementedError()

def compute_sequence_distance(sequenceA, sequenceB, fn="levhenstein"):
    raise NotImplementedError()

class DNASequence(Sequence):
    """Abstract sequence class.

    # Properties
    id (str): Identifier. Must be unique within a genome. If none is provided, uses a uuid.
    id_type (str): Source of identifier.
    data (str): Sequence contents.
    start_index (int): Index representing first position in data. Default 1 (as 1-indexing is common in biology).
    is_double_stranded (bool): Indicates whether sequence has complementary strand. Default True.
    """
    # TODO: implement
    def __init__(self, seq, **kwargs):
        raise NotImplementedError()

    # TODO: implement
    def __repr__(self):
      raise NotImplementedError()

    # NOTE: see if find can find overlapping matches
    # TODO: implement
    def find(self, query, strand=None):
        """locates query in sequence.

        # Arguments
        query (string): string to search for
        strand (string): One of {'+', '-'}. If provided, find will only search
            the given strand.

        # Returns
        Region: location of first match on sequence
        """
        raise NotImplementedError()

    # TODO: implement
    def count(self, query):
        raise NotImplementedError()

    # TODO: implement
    def find_pattern(self, pattern, all=False):
        raise NotImplementedError()

    # TODO: implement
    def count_pattern(self, pattern, include_overlapping=False):
        raise NotImplementedError()


    # TODO: implement
    def get_dna(self, region):
        raise NotImplementedError()

    # TODO: implement
    def get_rna(self, region):  ## CDS??
        raise NotImplementedError()

    # TODO: implement
    def get_aa(self, region, codon_table=CODON_TABLE):
        if len(region) % 3 != 0:
            raise ValueError('Length of region must be multiple of 3')

        raise NotImplementedError()

    # TODO: implement
    def to_rna(self):
        raise NotImplementedError()

    def to_aa(self, codon_table=CODON_TABLE):
        if len(self) % 3 != 0:
            raise ValueError('Length of sequence must be multiple of 3')
        raise NotImplementedError()

    def get_genes(self):
        raise NotImplementedError()

    def get_transcripts(self):
        raise NotImplementedError()

class RNASequence(Sequence):
    """
    """

    def __init__(self, seq, **kwargs):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def get_dna(self, region):
        raise NotImplementedError()

    def get_rna(self, region):
        raise NotImplementedError()

    def get_amino_acids(self, region, codon_table=CODON_TABLE):
        # consistent
        if len(region) % 3 != 0:
            raise ValueError('Length of region must be multiple of 3') # mention how many were left

        raise NotImplementedError()

    def to_dna(self):
        raise NotImplementedError()

    def to_aa(self, codon_table=CODON_TABLE):
        if len(self) % 3 != 0:
            raise ValueError('Length of sequence must be multiple of 3')
        raise NotImplementedError()

class AminoAcidSequence(Sequence):
    """
    """

    def __init__(self, seq, **kwargs):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def get_aa(self, start, stop, index=1):
        raise NotImplementedError()

    def reverse_translate(self, output_type, **kwargs):
        allowed_kwargs = {'codon_table', 'codon_usage'}
