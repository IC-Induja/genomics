<h1 id="genomics.BaseRegion">BaseRegion</h1>

```python
BaseRegion(self, start, stop, strand=None, sequence_key=None)
```
Is contiguous

<h2 id="genomics.BaseRegion.get_start">get_start</h2>

```python
BaseRegion.get_start(self)
```

__Arguments__


__Returns__



<h2 id="genomics.BaseRegion.get_stop">get_stop</h2>

```python
BaseRegion.get_stop(self)
```

__Arguments__


__Returns__



<h1 id="genomics.LinearRegion">LinearRegion</h1>

```python
LinearRegion(self, start, stop, strand=None, sequence=None)
```
Description of a region on a linear sequence.

__Properties__

- start (int): Coordinate of furthest base at 5' end of Region
- stop (int): Coordinate of furthest base at 3' end of Region
- strand (str, None): One of {'+', '-', None}. Defaults to None.
- sequence (str, None): Id of sequence that Region is on. Defaults to None.

<h2 id="genomics.LinearRegion.shift">shift</h2>

```python
LinearRegion.shift(self, bases, direction=None)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.expand">expand</h2>

```python
LinearRegion.expand(self, upstream, downstream)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.slice">slice</h2>

```python
LinearRegion.slice(self, start, stop)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.end5">end5</h2>

```python
LinearRegion.end5(self)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.end3">end3</h2>

```python
LinearRegion.end3(self)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.as_positive_strand">as_positive_strand</h2>

```python
LinearRegion.as_positive_strand(self)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.as_negative_strand">as_negative_strand</h2>

```python
LinearRegion.as_negative_strand(self)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.as_opposite_strand">as_opposite_strand</h2>

```python
LinearRegion.as_opposite_strand(self)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.intersects">intersects</h2>

```python
LinearRegion.intersects(self, other_region)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.contains">contains</h2>

```python
LinearRegion.contains(self, other_region)
```

__Arguments__


__Returns__



<h2 id="genomics.LinearRegion.is_within">is_within</h2>

```python
LinearRegion.is_within(self, other_region)
```

__Arguments__


__Returns__



<h1 id="genomics.CircularRegion">CircularRegion</h1>

```python
CircularRegion(self, start, stop, strand=None, sequence=None)
```
Description of a contiguous region on a circular sequence, where the last base
immediately precedes the first.

__Properties__

- start (int): Coordinate of base at 5' end of Region
- stop (int): Coordinate of base at 3' end of Region
- strand (str, None): One of {'+', '-', None}. Defaults to None.
- sequence (str, None): Id of sequence that Region is on. Defaults to None.

<h2 id="genomics.CircularRegion.shift">shift</h2>

```python
CircularRegion.shift(self, bases, direction=None)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.expand">expand</h2>

```python
CircularRegion.expand(self, upstream, downstream)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.slice">slice</h2>

```python
CircularRegion.slice(self, start, stop)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.end5">end5</h2>

```python
CircularRegion.end5(self)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.end3">end3</h2>

```python
CircularRegion.end3(self)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.as_positive_strand">as_positive_strand</h2>

```python
CircularRegion.as_positive_strand(self)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.as_negative_strand">as_negative_strand</h2>

```python
CircularRegion.as_negative_strand(self)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.as_opposite_strand">as_opposite_strand</h2>

```python
CircularRegion.as_opposite_strand(self)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.intersects">intersects</h2>

```python
CircularRegion.intersects(self, other_region)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.contains">contains</h2>

```python
CircularRegion.contains(self, other_region)
```

__Arguments__


__Returns__



<h2 id="genomics.CircularRegion.is_within">is_within</h2>

```python
CircularRegion.is_within(self, other_region)
```

__Arguments__


__Returns__



<h1 id="genomics.Region">Region</h1>

```python
Region(self, start, stop, strand=None, sequence_key=None)
```
Wrapper providing abstraction for circular or linear region.

