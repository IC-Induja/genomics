from future.moves.urllib.parse import urlencode

import pandas as pd

from .parsers import parse_annotation_file, parse_sequence_file

def fetch_dna_data(key, db="ncbi", key_type="accession"):
    """

    # Arguments

    # Returns
    str: 1-indexed contents of sequence
    """
    if db == 'ncbi':
        if key_type == 'accession':
            # -- read sequence from NCBI fasta --
            seq_params = urlencode({
                "db": "nuccore", "report": "fasta", "id":key})
            seq_url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?%s' % seq_params
            sequence_data = parse_sequence_file(
                seq_url, filetype='fasta', allow_multiple_sequences=False)
            return sequence_data

        else:
            ValueError('The key_type %s is not recognized for the %s database.' % (key_type, db))
    elif db in ('embl', 'ddbj'):
        raise ValueError('The %s database is not currently supported, but '
        'will be added in future updates.' % db)
    else:
        raise ValueError('The database %s is unrecognized.' % db)

def fetch_rna_data(key, db="ncbi", key_type="accession"):
    raise NotImplementedError()

def fetch_amino_acid_data(key, db="ncbi", key_type="accession"):
    raise NotImplementedError()

def fetch_annotations(key, db="ncbi", key_type="accession"):
    if db == 'ncbi':
        if key_type == 'accession':
            # -- read annotations from NCBI gff3 --
            annotation_params = urlencode({
                "db": "nuccore", "report": "gff3", "id":key})
            annotation_url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?%s' % annotation_params
            annotations = parse_annotation_file(annotation_url)
            return annotations

        else:
            ValueError('The key_type %s is not recognized for the %s database.' % (key_type, db))
    elif db in ('embl', 'ddbj'):
        raise ValueError('The %s database is not currently supported, but '
        'will be added in future updates.' % db)
    else:
        raise ValueError('The database %s is unrecognized.' % db)
    raise NotImplementedError()
