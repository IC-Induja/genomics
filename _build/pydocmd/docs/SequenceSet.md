<h1 id="genomics.SequenceSet">SequenceSet</h1>

```python
SequenceSet(self, sequences, start_index=None)
```
Abstract class for a collection of sequences.

__Properties__

id (str): Identifier. If none is provided, uses a uuid.
id_type (str): Source of identifier.
sequences (list of sequences): Genome contents.
start_index (int): TODO
annotations (AnnotationTable): table containing all annotations, created by
    concatenating the individual AnnotationTable for every Sequence in the
    SequenceSet

<h2 id="genomics.SequenceSet.from_file">from_file</h2>

```python
SequenceSet.from_file(filetype=None)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.reindex">reindex</h2>

```python
SequenceSet.reindex(self)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.get_subset">get_subset</h2>

```python
SequenceSet.get_subset(self, slice)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.find">find</h2>

```python
SequenceSet.find(self, query, limit=1)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.count">count</h2>

```python
SequenceSet.count(self, query)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.find_pattern">find_pattern</h2>

```python
SequenceSet.find_pattern(self, pattern, limit=1, overlapping=True)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.count_pattern">count_pattern</h2>

```python
SequenceSet.count_pattern(self, pattern)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.compute_distance">compute_distance</h2>

```python
SequenceSet.compute_distance(self, regionA, regionB, fn='levhenstein')
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.apply_variant">apply_variant</h2>

```python
SequenceSet.apply_variant(self, genomic_variant)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.save_as">save_as</h2>

```python
SequenceSet.save_as(self, path, filetype=None, overwrite_existing=False)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.save_sequences">save_sequences</h2>

```python
SequenceSet.save_sequences(self, path, filetype=None, overwrite_existing=False)
```

__Arguments__


__Returns__



<h2 id="genomics.SequenceSet.save_annotations">save_annotations</h2>

```python
SequenceSet.save_annotations(self, path, filetype=None, overwrite_existing=False)
```

__Arguments__


__Returns__



<h1 id="genomics.DNASet">DNASet</h1>

```python
DNASet(self, sequences, start_index=None)
```
SequenceSet with DNA-specific methods for fetching and storing

<h2 id="genomics.DNASet.calculate_gc">calculate_gc</h2>

```python
DNASet.calculate_gc(self)
```

__Arguments__


__Returns__



<h2 id="genomics.DNASet.from_db">from_db</h2>

```python
DNASet.from_db(db='ncbi', key_type='accession', with_annotations=True, start_index=1, allowed_chars=None, start_col='start', end_col=('end', 'stop'), key_col=('key', 'accession'), keys_from_file=False, tabular_file=False)
```
Fetches multiple sequences or sequence subsets from external db

Compatible with multiple ways of specifying data.
When `keys_from_file=False`:
- If data_specification is iterable of strings, each string should be
an key for a distinct sequence in the db.
- If data_specification is iterable of tuples, each tuple should be in
the format (key, start, stop) where:
    - key is the db key for the sequence
    - start is the index of the first element to be included
    - end is the index of the last element to be included.
If stop is omitted, uses index of last
element in db sequence. If both start and stop are omitted, entire
sequence will be used.

When `keys_from_file=True`:
- if data_specification is string, should be a path or url to either:
    - if `from_tabular_file=False`: a file containing a list of db keys
    - if `from_tabular_file=True`: a tabular file with a column
    containing db keys, an (optional) column containing start indexes,
    and an (optional) column containing stop indexes
- if data_specification is pandas DataFrame, if should contain a column
    of data keys, (optional) column of start indexes and (optional)
    column of stop indexes

__Arguments__

- __data_specification (iterable, str, or pd.DataFrame)__: sequences specified
    in the above format



__Returns__


__Raises__

- `ValueError`:

<h1 id="genomics.RNASet">RNASet</h1>

```python
RNASet(self, sequences, start_index=None)
```
SequenceSet with RNA-specific methods for fetching and storing

<h2 id="genomics.RNASet.calculate_gc">calculate_gc</h2>

```python
RNASet.calculate_gc(self)
```

__Arguments__


__Returns__



<h2 id="genomics.RNASet.from_db">from_db</h2>

```python
RNASet.from_db(self)
```

__Arguments__


__Returns__



<h1 id="genomics.AminoAcidsSet">AminoAcidsSet</h1>

```python
AminoAcidsSet(self, sequences, start_index=None)
```
SequenceSet with AminoAcids-specific methods for fetching and storing

<h2 id="genomics.AminoAcidsSet.from_db">from_db</h2>

```python
AminoAcidsSet.from_db(self)
```

__Arguments__


__Returns__



