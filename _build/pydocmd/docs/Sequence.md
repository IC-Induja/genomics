<h1 id="genomics.Sequence">Sequence</h1>

```python
Sequence(self, data, annotations=None, key=None, key_type=None, start_index=1, accepted_chars=None)
```
Base class for annotated sequence.

__Attributes__

- `data (str)`: Sequence contents.
- `annotations (AnnotationTable)`: Description of sequence features. Defaults to None.
- `key (str)`: Identifier. Must be unique within a Genome or other SequenceSet.
    If None, uses a uuid. (Randomly generated unique identifier.)
- `key_type (str)`: Source of key. Defaults to None.
- `start_index (int)`: Index representing first position in data. Default 1
    (1-indexing is common in biology).
- `is_circular (bool)`: Indicates whether last index in sequence immediately
    precedes the first (ie. whether sequence forms a circle).
- `accepted_chars (str)`: Characters that are allowed in the sequence data.
    Ex. If accepted_chars='ATCG', then a sequence containing 'N' would raise
    a ValueError. Defaults to None, which accepts all alphabet characters,
    but not numbers or symbols.
- `description (str)`: Information about the sequence. Useful for storing
    non-identifier data found in certain file formats (Ex. In FASTA headers).
- `metadata (dict)`: Key-value pairs that provide information about the
    sequence. Useful for storing the extensive metadata found in certain
    file formats (ex. Genbank files).
- `_is_reference (bool)`: Indicates whether sequence is directly from
    reference database, and has not been modified.
- `_reference_id (string)`: ID of sequence in reference db
- `_reference_db (string)`: Well-known biological database from which the
    sequence was retrieved. Library currently supports NCBI, EMBL, and DDBJ.
- `_index_in_reference(int)`: Position of first element of this sequence in the
    reference sequence (uses 1-indexing for the referencing)

<h2 id="genomics.Sequence.from_file">from_file</h2>

```python
Sequence.from_file(start=None, stop=None, filetype=None, key=None, key_type=None, start_index=1, with_annotations=True, accepted_chars=None)
```
Reads sequence data from file.

Accepts a variety of biological formats (FASTA, Genbank, etc.).
Also can read a raw sequence from .txt

Accepted File Extensions:

- FASTA: .fa, .fasta, .fna, .ffa, .frn, .faa
- Genbank: .gb, .gbk
- GFF: .gff, .gff3
- Plain Text: .txt

Note: If file contains multiple sequences, use a SequenceSet instead.
(Multiple sequences will raise ValueError)

__Arguments__

- __path (str)__: Location of file (absolute or relative path, or a URL)
- __format (str)__: Format of file contents. One of the accepted file
    extensions listed above, or one of {fasta, gff, genbank, plaintext}
    If not provided, will be inferred from file extension.
    If gff is provided, sequence must be at the bottom of the file,
    beneath annotations
- __with_annotations (bool)__: if False, all annotation data in the sequence
    file (ex. from a GFF containing a sequence) is ignored.

__Returns__

One of {
    Sequence, DNASequence, RNASequence, AminoAcidSequence
`}`: sequence contained in file, with type determined by file contents

__Raises__

- `FileNotFoundError`: if either path or annotation_path cannot be found
- `ValueError`: if file format is not understood
            if with_annotations is False but annotation_path is specified
            if key_type is specified and does not equal uuid, but key is
                not specified

<h2 id="genomics.Sequence.from_db">from_db</h2>

```python
Sequence.from_db(start=None, stop=None, db='ncbi', key_type='accession', start_index=1, with_annotations=True, accepted_chars=None)
```
Constructs a sequence by fetching data from a commonly used
biological database.

Currently supports NCBI. EMBL, and DDBJ databases to be added in future.

Supported Key Types:

- NCBI:
    - 'accession' - also known as the accession.version number. If
        no version is provided, the latest version will be used.
        However, use of accessions without version is **strongly
        discouraged**, as it reduces the reproducibility of the code.
    - ncbi_gi - to be added in future.

__Arguments__

- __key (string)__: Unique identifier for sequences in target db.
    Ex. Accession Number
- __start (int)__: Index of first base to be included in the sequence (if
    entire sequence is not desired)
- __stop (int)__: Index of last base to be included in the sequence (if
    entire sequence is not desired)
- __db (string)__: One of {'ncbi', 'ddbj', 'embl'}. (**Currently only 'ncbi'
    is supported.**) Major biological database. Use a db that contains
    the desired sequence.
- __with_annotations (bool)__: If true, retrieve annotation data in addition
    to the sequence data.
- __start_index (int)__: Index to use for first first character in the
    sequence file. Defaults to 1.

__Returns__

`Sequence, or one of its subclasses DNA, RNA, or AminoAcids`:
    sequence contained in file, with type determined from db and
    retrieved data

__Raises__

- `ValueError`:


<h2 id="genomics.Sequence.reindex">reindex</h2>

```python
Sequence.reindex(self, new_start_index)
```

Set a new start index for the sequence, and adjust start and end of
sequence annotations accordingly (so that the annotations stay at the
same position relative the sequence, and cover the same part of the data).

Useful for converting between 0-indexing and 1-indexing.

__Arguments__

- __new_start_index (int)__: index to use for first position in sequence data.

__Returns__

`Sequence`: Sequence with new start index, and all annotations adjusted to
    reflect the new index

<h2 id="genomics.Sequence.get_subsequence">get_subsequence</h2>

```python
Sequence.get_subsequence(self, region=None, start=None, stop=None, reindex=False, start_index=None)
```
Gets subset of sequence.

Note: subsequence is inclusive of both start and end indices.

__Arguments__

- __start (int)__: index of first subsequence element. Defaults to start of
    parent sequence.
- __stop (int)__: index of last subsequence element. Defaults to end of
    parent sequence.
- __reindex (bool)__: if true, index of subsequence will start at 1. Otherwise,
    indexing will be unchanged (ie. index to get first element in
    subsequence will be the same as the index in the parent sequence,
    and so on).
- __start_index__: Index of first element in sequence.

<h2 id="genomics.Sequence.find">find</h2>

```python
Sequence.find(self, query, strand=None, all=False)
```
locates query in sequence.

__Arguments__

- __query (string)__: string to search for
- __strand (string)__: One of {'+', '-', None}. If specified, find will only
    search the given strand.

__Returns__

`Region/list of Region`: location of first match on sequence, or, if
    all=True, a list containing locations of all matches

<h2 id="genomics.Sequence.count">count</h2>

```python
Sequence.count(self, query, overlapping=True)
```
counts instances of query in sequence.

__Arguments__

- __query (string)__: string to search for
- __overlapping (bool)__: include overlapping instances of query

__Returns__

`int`: number of occurrences of query in sequence

<h2 id="genomics.Sequence.find_pattern">find_pattern</h2>

```python
Sequence.find_pattern(self, pattern, all=False)
```


__Arguments__


__Returns__



<h2 id="genomics.Sequence.count_pattern">count_pattern</h2>

```python
Sequence.count_pattern(self, pattern, include_overlapping=False)
```


__Arguments__


__Returns__



<h2 id="genomics.Sequence.compute_distance">compute_distance</h2>

```python
Sequence.compute_distance(self, regionA, regionB, fn='levhenstein')
```


__Arguments__


__Returns__



<h2 id="genomics.Sequence.apply_variants">apply_variants</h2>

```python
Sequence.apply_variants(self, variant_data)
```
applies one or more variants (Variant, Iterable<Variant>, or VariantTable)
if given string, it will open variant file at that path

<h2 id="genomics.Sequence.save_as">save_as</h2>

```python
Sequence.save_as(self, path, filetype=None, overwrite_existing=False)
```


__Arguments__


__Returns__



<h2 id="genomics.Sequence.save_sequence">save_sequence</h2>

```python
Sequence.save_sequence(self, path, filetype=None, overwrite_existing=False)
```


__Arguments__


__Returns__



<h2 id="genomics.Sequence.save_annotations">save_annotations</h2>

```python
Sequence.save_annotations(self, path, filetype=None, overwrite_existing=False)
```


__Arguments__


__Returns__



