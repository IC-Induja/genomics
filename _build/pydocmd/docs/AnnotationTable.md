<h1 id="genomics.AnnotationTable">AnnotationTable</h1>

```python
AnnotationTable(self, keep_cds_annotations=False, use_headers=None)
```

__Properties__



<h2 id="genomics.AnnotationTable.get_genes">get_genes</h2>

```python
AnnotationTable.get_genes(self)
```

__Arguments__


__Returns__

`list of Gene`: list of Gene objects, representing each gene in the annotation table

<h2 id="genomics.AnnotationTable.filter">filter</h2>

```python
AnnotationTable.filter(self, fn, col=None)
```

__Arguments__


__Returns__



<h2 id="genomics.AnnotationTable.filter_type">filter_type</h2>

```python
AnnotationTable.filter_type(self, type)
```

__Arguments__


__Returns__



<h2 id="genomics.AnnotationTable.filter_region">filter_region</h2>

```python
AnnotationTable.filter_region(self, region=None, start=None, stop=None, strand=None)
```

__Arguments__


__Returns__



<h2 id="genomics.AnnotationTable.apply">apply</h2>

```python
AnnotationTable.apply(self, fn, col=None)
```

__Arguments__


__Returns__



<h2 id="genomics.AnnotationTable.save_as">save_as</h2>

```python
AnnotationTable.save_as(self, path, filetype=None, overwrite_existing=False)
```

__Arguments__


__Returns__



