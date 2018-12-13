<h1 id="genomics.DNA">DNA</h1>

```python
DNA(self, data, annotations=None, key=None, key_type=None, start_index=1, accepted_chars=None, double_stranded=True, ignore_numbers_and_spaces=True)
```
Abstract sequence class.

__Properties__

key (str): Identifier. Must be unique within a genome. If none is provided,
    uses a uuid.
key_type (str): Source of identifier.
data (str): Sequence contents.
start_index (int): Index representing first position in data. Default 1 (as
    1-indexing is common in biology).
is_double_stranded (bool): Indicates whether sequence has complementary
    strand. Default True.

<h2 id="genomics.DNA.find">find</h2>

```python
DNA.find(self, query, strand=None)
```
locates query in sequence.

__Arguments__

- __query (string)__: string to search for
- __strand (string)__: One of {'+', '-'}. If provided, find will only search
    the given strand.

__Returns__

`Region`: location of first match on sequence

<h2 id="genomics.DNA.count">count</h2>

```python
DNA.count(self, query)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.find_pattern">find_pattern</h2>

```python
DNA.find_pattern(self, pattern, all=False)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.count_pattern">count_pattern</h2>

```python
DNA.count_pattern(self, pattern, include_overlapping=False)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.get_dna">get_dna</h2>

```python
DNA.get_dna(self, region)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.get_rna">get_rna</h2>

```python
DNA.get_rna(self, region)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.get_aa">get_aa</h2>

```python
DNA.get_aa(self, region, codon_table={})
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.to_rna">to_rna</h2>

```python
DNA.to_rna(self, region=None, start=None, stop=None, strand=None)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.to_aa">to_aa</h2>

```python
DNA.to_aa(self, codon_table=None)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.get_genes">get_genes</h2>

```python
DNA.get_genes(self)
```
Using annotations, determine all genes contained in this sequence.
This includes determining their exons, introns, and 5' and 3' UTRs

__Returns__

`GeneTable`:


<h2 id="genomics.DNA.get_amino_acids">get_amino_acids</h2>

```python
DNA.get_amino_acids(self)
```
Using annotations, determine all amino acid chains (polypeptides)
produced by this sequence.

__Returns__

`SequenceSet<AminoAcids> `: Amino acid chains.

__Raises__

- `ValueError`: Sequence does not contain annotations. Annotations are
required to determine amino acids.

<h2 id="genomics.DNA.get_coding_rnas">get_coding_rnas</h2>

```python
DNA.get_coding_rnas(self, as_dna=False)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.get_noncoding_rnas">get_noncoding_rnas</h2>

```python
DNA.get_noncoding_rnas(self, as_dna=False)
```


__Arguments__


__Returns__



<h2 id="genomics.DNA.get_cds">get_cds</h2>

```python
DNA.get_cds(self, combine_by_gene=True)
```


__Arguments__


__Returns__



