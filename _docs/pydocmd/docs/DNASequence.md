<h1 id="genomics.DNASequence">DNASequence</h1>

```python
DNASequence(self, seq, **kwargs)
```
Abstract sequence class.

__Properties__

id (str): Identifier. Must be unique within a genome. If none is provided, uses a uuid.
id_type (str): Source of identifier.
data (str): Sequence contents.
start_index (int): Index representing first position in data. Default 1 (as 1-indexing is common in biology).
is_double_stranded (bool): Indicates whether sequence has complementary strand. Default True.

<h2 id="genomics.DNASequence.find">find</h2>

```python
DNASequence.find(self, query, strand=None)
```
locates query in sequence.

__Arguments__

- __query (string)__: string to search for
- __strand (string)__: One of {'+', '-'}. If provided, find will only search
    the given strand.

__Returns__

`Region`: location of first match on sequence

