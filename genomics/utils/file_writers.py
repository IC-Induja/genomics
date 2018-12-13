import os

def write_fasta(filepath, sequence, line_width=80, multiline=True,
                accepted_chars=None):
    """
    # Arguments
    filepath (str): Location of file (absolute or relative filepath)
    """
    raise NotImplementedError()

def write_mulifasta(filepath, sequence_set, line_width=80, multiline=True,
                    accepted_chars=None):
    raise NotImplementedError()

def write_genbank(filepath, accepted_chars=None):
    raise NotImplementedError()

def parse_gff(filepath):
    raise NotImplementedError()

def parse_plaintext(filepath, accepted_chars=None):
    raise NotImplementedError()

def parse_sequence_file(filepath, format=None):
    if not format:
        filename, file_extension = os.path.splitext(filepath)
        format = file_extension
    raise NotImplementedError()

def parse_annotation_file(filepath, format=None):
    raise NotImplementedError()
