""" Prototype implementations of parsers for various biological file formats.
"""

from future.moves.urllib.parse import urlparse
from future.moves.urllib.request import urlopen

import os
import re

from ..sequence import Sequence

def parse_single_fasta(file_object, accepted_chars=None):
    """
    # Arguments
    file_object:
    """
    # NOTE: Warn if writing fasta with accepted chars not being either DNA or RNA alphabet.
    #       If not accepted_chars, first check DNA alphabet then RNA alphabet. If neither,
    #       raise value error

    # parse sequence metadata
    header = file_object.readline()
    assert(header[0] == '>') # fasta header MUST start with '>'

    key = header.split(' ', 1)[0].replace('>', '')
    description = header.split(' ', 1).replace('\n', '')

    sequence_data = file_object.read().replace('\n', '')

    if sequence.find('>') != -1:
        # file contains more than 1 sequence header (and thus more than 1 sequence)
        raise ValueError("File contains multiple sequences. One was expected.")

    return key, description, sequence_data

def parse_multifasta(path, accepted_chars=None):
    raise NotImplementedError()
    return [(key, description, sequence_data)],

def parse_genbank(path, accepted_chars=None):
    raise NotImplementedError()

def parse_gff(path, ignore_sequence=True, accepted_chars=None):
    raise NotImplementedError()

def parse_plaintext(path, accepted_chars=None):
    raise NotImplementedError()

def get_file_from_path(path):
    """
    # Raises
    FileNotFoundError: Could not find file specified by local path.
    ValueError: Unable to open file.
    """
    isUrl = urlparse(path).scheme in ('http', 'https')
    if isUrl:
        # open file object via the internet
        file_object = urlopen(path)
    else:
        # open local file
        file_object = open(path)

    return file_object

def get_filetype_from_extension(path):
    """
    # Raises
    ValueError: File has no extension.
                File extension is not recognized.
    """
    _, file_extension = os.path.splitext(path)
    if not file_extension:
        raise ValueError("File has no extension")

    if file_extension in {'fa', 'fasta', 'fna', 'ffa', 'frn', 'faa'}:
        filetype = 'fasta'
    elif file_extension in {'gb', 'gbk'}:
        filetype = 'genbank'
    elif file_extension in {'gff', 'gff3'}:
        filetype = 'gff'
    elif file_extension == 'txt':
        filetype = 'plaintext'
    else:
        raise ValueError("File extension not recognized")

    return filetype

def parse_sequence_file(path, filetype=None, allow_multiple_sequences=True):
    """
    Read file and extract sequence data

    # Arguments
    path (str): URL or local path to sequence data.
    filetype (str): One of {'fasta', 'genbank', 'gff', 'plaintext'}.
        Indicates format of file contents.
    allow_multiple_sequences (bool): If False, parser produces a seq

    # Returns

    # Raises
    FileNotFoundError:
    ValueError:
    """
    if not filetype:
        try:
            filetype = get_filetype_from_extension(path)
        except ValueError:
            raise ValueError("Need to either specify filetype, or provide a path with valid extension")
    file_object = get_file_from_path(path)


    raise NotImplementedError()

def parse_annotation_file(path, filetype=None):
    raise NotImplementedError()
