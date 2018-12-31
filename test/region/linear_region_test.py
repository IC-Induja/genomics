import pytest

from genomics import LinearRegion

def test_shift():
    region_a = Region("chr1", 500, 700, "+")
    region_b = Region("chr1", 600, 700, "+")
    region_c = Region("chr2", 600, 700, "+")
    region_d = Region("chr1", 600, 700, "-")

    assert region_b.is_within(region_a)
    assert not region_a.is_within(region_b)
    assert not region_c.is_within(region_a)
    assert not region_d.is_within(region_a)

def test_expand():
    raise NotImplementedError()

def test_intersects():
    raise NotImplementedError()

def test_contains():
    raise NotImplementedError()

def test_is_within():
    region_a = LinearRegion()
    raise NotImplementedError()

if __name__ == '__main__':
    pytest.main([__file__])
