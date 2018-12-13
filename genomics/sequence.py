""" Contains the Sequence class, along with its derivatives:
    DNA, RNA, and AminoAcids
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import uuid

import pandas as pd
from .constants import CODON_TABLE
from .annotation import AnnotationTable

class Sequence(object):
    """Base class for annotated sequence.

    # Attributes
    data (str): Sequence contents.
    annotations (AnnotationTable): Description of sequence features. Defaults to None.
    key (str): Identifier. Must be unique within a Genome or other SequenceSet.
        If None, uses a uuid. (Randomly generated unique identifier.)
    key_type (str): Source of key. Defaults to None.
    start_index (int): Index representing first position in data. Default 1
        (1-indexing is common in biology).
    is_circular (bool): Indicates whether last index in sequence immediately
        precedes the first (ie. whether sequence forms a circle).
    accepted_chars (str): Characters that are allowed in the sequence data.
        Ex. If accepted_chars='ATCG', then a sequence containing 'N' would raise
        a ValueError. Defaults to None, which accepts all alphabet characters,
        but not numbers or symbols.
    description (str): Information about the sequence. Useful for storing
        non-identifier data found in certain file formats (Ex. In FASTA headers).
    metadata (dict): Key-value pairs that provide information about the
        sequence. Useful for storing the extensive metadata found in certain
        file formats (ex. Genbank files).
    _is_reference (bool): Indicates whether sequence is directly from
        reference database, and has not been modified.
    _reference_id (string): ID of sequence in reference db
    _reference_db (string): Well-known biological database from which the
        sequence was retrieved. Library currently supports NCBI, EMBL, and DDBJ.
    _index_in_reference(int): Position of first element of this sequence in the
        reference sequence (uses 1-indexing for the referencing)
    """
    # NOTE: strip numbers and spaces from string (ie. accept plaintext format)
    #       add no_gaps_or_numbers option for optimization

    # WARNING: index parameter not implemented yet. Index defaults to 0
    def __init__(self, data, annotations=None, key=None, key_type=None,
                 start_index=1, accepted_chars=None):
        if key:
            self.key = key
            self.key_type = key_type or None
        else:
            if key_type:
                raise ValueError('key_type is provided, but key is not.')
            else:
                self.key = str(uuid.uuid4())
                self.key_type = "uuid"

        self.data = data

        if not annotations:
            self.annotations = None
        elif type(annotations) == AnnotationTable:
            self.annotations = annotations
        else:
            raise ValueError(
                "Annotations provided in unexpected type %s." % type(annotations))

    @classmethod
    def from_file(path, start=None, stop=None, filetype=None, key=None,
                  key_type=None, start_index=1, with_annotations=True,
                  accepted_chars=None):
        # NOTE: How should we handle multiline fasta? Throw error and suggest
        #       using sequence set?
        """Reads sequence data from file.

        Accepts a variety of biological formats (FASTA, Genbank, etc.).
        Also can read a raw sequence from .txt

        Accepted File Extensions:

        - FASTA: .fa, .fasta, .fna, .ffa, .frn, .faa
        - Genbank: .gb, .gbk
        - GFF: .gff, .gff3
        - Plain Text: .txt

        Note: If file contains multiple sequences, use a SequenceSet instead.
        (Multiple sequences will raise ValueError)

        # Arguments
        path (str): Location of file (absolute or relative path, or a URL)
        format (str): Format of file contents. One of the accepted file
            extensions listed above, or one of {fasta, gff, genbank, plaintext}
            If not provided, will be inferred from file extension.
            If gff is provided, sequence must be at the bottom of the file,
            beneath annotations
        with_annotations (bool): if False, all annotation data in the sequence
            file (ex. from a GFF containing a sequence) is ignored.

        # Returns
        One of {
            Sequence, DNASequence, RNASequence, AminoAcidSequence
            }: sequence contained in file, with type determined by file contents

        # Raises
        FileNotFoundError: if either path or annotation_path cannot be found
        ValueError: if file format is not understood
                    if with_annotations is False but annotation_path is specified
                    if key_type is specified and does not equal uuid, but key is
                        not specified
        """
        raise NotImplementedError()

    @classmethod
    def from_db(key, start=None, stop=None, db="ncbi", key_type="accession",
                start_index=1, with_annotations=True, accepted_chars=None):
        """Constructs a sequence by fetching data from a commonly used
        biological database.

        Currently supports NCBI. EMBL, and DDBJ databases to be added in future.

        Supported Key Types:

        - NCBI:
            - 'accession' - also known as the accession.version number. If
                no version is provided, the latest version will be used.
                However, use of accessions without version is **strongly
                discouraged**, as it reduces the reproducibility of the code.
            - ncbi_gi - to be added in future.

        # Arguments
        key (string): Unique identifier for sequences in target db.
            Ex. Accession Number
        start (int): Index of first base to be included in the sequence (if
            entire sequence is not desired)
        stop (int): Index of last base to be included in the sequence (if
            entire sequence is not desired)
        db (string): One of {'ncbi', 'ddbj', 'embl'}. (**Currently only 'ncbi'
            is supported.**) Major biological database. Use a db that contains
            the desired sequence.
        with_annotations (bool): If true, retrieve annotation data in addition
            to the sequence data.
        start_index (int): Index to use for first first character in the
            sequence file. Defaults to 1.

        # Returns
        Sequence, or one of its subclasses DNA, RNA, or AminoAcids:
            sequence contained in file, with type determined from db and
            retrieved data

        # Raises
        ValueError:

        """
        raise NotImplementedError()

    # TODO: implement
    def __len__(self):
        return len(self.data)

    # TODO: implement
    def __repr__(self):
        """ Displays sequence id, as well as a few bases from the start and end
            of sequence. This should allow for quickly checking data without
            flooding output with entire sequence data.
        """
        return "Sequence<id:" + self.key + " " + str(len(self)) + "bp " \
        + " " + self[0:20] + "..." + self[-20:-1] + ">"

    def reindex(self, new_start_index):
        """
        Set a new start index for the sequence, and adjust start and end of
        sequence annotations accordingly (so that the annotations stay at the
        same position relative the sequence, and cover the same part of the data).

        Useful for converting between 0-indexing and 1-indexing.

        # Arguments
        new_start_index (int): index to use for first position in sequence data.

        # Returns
        Sequence: Sequence with new start index, and all annotations adjusted to
            reflect the new index
        """
    # TODO: implement

    # NOTE: should we allow for subsequences to keep their original indexing? or
    # should we have all the sequence methods take a start and stop argument?
    # (To specify what part of the sequence to be searching/ calculating in)
    def get_subsequence(self, region=None, start=None, stop=None, reindex=False,
                        start_index=None):
        # NOTE: what should we call our locations? Which one?: coordinate,
        #       position, loci, index
        """Gets subset of sequence.

        Note: subsequence is inclusive of both start and end indices.

        # Arguments
        start (int): index of first subsequence element. Defaults to start of
            parent sequence.
        stop (int): index of last subsequence element. Defaults to end of
            parent sequence.
        reindex (bool): if true, index of subsequence will start at 1. Otherwise,
            indexing will be unchanged (ie. index to get first element in
            subsequence will be the same as the index in the parent sequence,
            and so on).
        start_index: Index of first element in sequence.
        """
        allowed_kwargs = {'start', 'stop', 'reindex', 'index'}
        raise NotImplementedError()

    # TODO: implement
    def find(self, query, strand=None, all=False):
        """locates query in sequence.

        # Arguments
        query (string): string to search for
        strand (string): One of {'+', '-', None}. If specified, find will only
            search the given strand.

        # Returns
        Region/list of Region: location of first match on sequence, or, if
            all=True, a list containing locations of all matches
        """
        raise NotImplementedError()

    # TODO: implement
    def count(self, query, overlapping=True):
        """counts instances of query in sequence.

        # Arguments
        query (string): string to search for
        overlapping (bool): include overlapping instances of query

        # Returns
        int: number of occurrences of query in sequence
        """
        raise NotImplementedError()

    # TODO: implement
    def find_pattern(self, pattern, all=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement
    def count_pattern(self, pattern, include_overlapping=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def compute_distance(self, regionA, regionB, fn="levhenstein"):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def apply_variants(self, variant_data):
        """applies one or more variants (Variant, Iterable<Variant>, or VariantTable)
            if given string, it will open variant file at that path
        """
        raise NotImplementedError()

    def save_as(self, path, filetype=None, overwrite_existing=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def save_sequence(self, path, filetype=None, overwrite_existing=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def save_annotations(self, path, filetype=None, overwrite_existing=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

class DNA(Sequence):
    """Abstract sequence class.

    # Properties
    key (str): Identifier. Must be unique within a genome. If none is provided,
        uses a uuid.
    key_type (str): Source of identifier.
    data (str): Sequence contents.
    start_index (int): Index representing first position in data. Default 1 (as
        1-indexing is common in biology).
    is_double_stranded (bool): Indicates whether sequence has complementary
        strand. Default True.
    """
    # TODO: implement
    def __init__(self, data, annotations=None, key=None, key_type=None,
                 start_index=1, accepted_chars=None, double_stranded=True,
                 ignore_numbers_and_spaces=True,):
        # NOTE: strip numbers
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
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement
    def find_pattern(self, pattern, all=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement
    def count_pattern(self, pattern, include_overlapping=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement

    def get_dna(self, region):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement
    def get_rna(self, region):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    # TODO: implement
    def get_aa(self, region, codon_table=CODON_TABLE):
        """

        # Arguments

        # Returns

        """
        if len(region) % 3 != 0:
            raise ValueError('Length of region must be multiple of 3')

        raise NotImplementedError()

    # TODO: implement
    def to_rna(self, region=None, start=None, stop=None, strand=None):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def to_aa(self, codon_table=None):
        """

        # Arguments

        # Returns

        """
        if len(self) % 3 != 0:
            raise ValueError('Length of sequence must be multiple of 3')
        raise NotImplementedError()

    def get_genes(self):
        """ Using annotations, determine all genes contained in this sequence.
            This includes determining their exons, introns, and 5' and 3' UTRs

        # Returns
        GeneTable:

        """
        raise NotImplementedError()

    def get_amino_acids(self):
        """ Using annotations, determine all amino acid chains (polypeptides)
            produced by this sequence.

        # Returns
        SequenceSet<AminoAcids> : Amino acid chains.

        # Raises
        ValueError: Sequence does not contain annotations. Annotations are
            required to determine amino acids.
        """
        raise NotImplementedError()

    def get_coding_rnas(self, as_dna=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()
        # Any instances where introns get rearranged after splicing??

    def get_noncoding_rnas(self, as_dna=False):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_cds(self, combine_by_gene=True):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()


class RNA(Sequence):
    """
    # Properties

    """

    def __init__(self, data, annotations=None, key=None, key_type=None,
                 start_index=1, accepted_chars=None, double_stranded=True):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    # NOTE should we be able to get dna from an rna sequence?
    def get_dna(self, region):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_rna(self, region):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def get_amino_acids(self, region, codon_table=CODON_TABLE):
        """

        # Arguments

        # Returns

        """
        if len(region) % 3 != 0:
            raise ValueError('Length of region must be multiple of 3')
                        # mention how many were left

        raise NotImplementedError()

    def convert_to_dna(self, region=None):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def convert_to_amino_acids(self, region=None, codon_table=None):
        """

        # Arguments

        # Returns

        """
        if len(self) % 3 != 0:
            raise ValueError('Length of sequence must be multiple of 3')
        raise NotImplementedError()

class AminoAcids(Sequence):
    """
    # Properties

    """

    def __init__(self, seq, **kwargs):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def get_aa(self, start, stop, index=1):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()

    def reverse_translate(self, as_rna=False, codon_table=None, codon_usage=None):
        """

        # Arguments

        # Returns

        """
        raise NotImplementedError()
