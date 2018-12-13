<h1 id="genomics.RegionTable">RegionTable</h1>

```python
RegionTable(self)
```

__Properties__



<h2 id="genomics.RegionTable.from_file">from_file</h2>

```python
RegionTable.from_file(path, sep='\t', start_col='start', end_col='end', strand_col='strand', sequence_key_col=('key', 'accession'))
```
Should be able to pull regions from tabular files with start and end
columns (as well as optional strand and sequence_key columns)

<h2 id="genomics.RegionTable.from_db">from_db</h2>

```python
RegionTable.from_db()
```

__Arguments__


__Returns__



<h2 id="genomics.RegionTable.save_as">save_as</h2>

```python
RegionTable.save_as(self, path, format=None, overwrite_existing=False)
```

__Arguments__


__Returns__



