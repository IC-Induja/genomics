<h1 id="genomics.Sequence">Sequence</h1>

```python
Sequence(self, seq, **kwargs)
```
Abstract sequence class.

__Properties__

id (str): Identifier. Must be unique within a genome. If none is provided, uses a uuid.
id_type (str): Source of identifier.
data (str): Sequence contents.
start_index (int): Index representing first position in data. Default 1 (as 1-indexing is common in biology).

<h2 id="genomics.Sequence.from_file">from_file</h2>

```python
Sequence.from_file(format=None, **kwargs)
```
Reads sequence data from file.

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

__Arguments__

- __filepath (str)__: Location of file (absolute or relative filepath, or a URL)
- __format (str)__: Format of file contents. If not provided, will be inferred form file extention.

__Returns__

`Sequence`: sequence contained in file

<h2 id="genomics.Sequence.from_db">from_db</h2>

```python
Sequence.from_db(db='ncbi')
```
Constructs a sequence by fetching data from a commonly used
biological database.

Supports NCBI, EMBL, and DDOJ databases.

__Arguments__


__Returns__

`Sequence`: Sequence retreived from database.

<h2 id="genomics.Sequence.get_subsequence">get_subsequence</h2>

```python
Sequence.get_subsequence(self, **kwargs)
```
Gets subset of sequence.

Note: subsequence is inclusive of both start and end indices.

__Arguments__

- __start (int)__: index of first subsequence element. Defaults to start of sequence.
- __stop (int)__: index of last subsequence element. Defaults to end of sequence.
- __reindex (bool)__: if true, indexing of sequence will start at 1. Otherwise,
    indexing will be unchanged (ie. index of first element in sequence
    will be it's current position in the sequence, and so on)

<h2 id="genomics.Sequence.find">find</h2>

```python
Sequence.find(self, query, strand=None)
```
locates query in sequence.

__Arguments__

- __query (string)__: string to search for

__Returns__

`Region`: location of first match on sequence

