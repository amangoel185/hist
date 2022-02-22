from __future__ import annotations


def test_ND_text_repr_double(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b", growth=True)
        .Double()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)


def test_ND_text_repr_unlimited(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b", growth=True)
        .Unlimited()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)


def test_ND_text_repr_int64(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b", growth=True)
        .Int64()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)


def test_ND_text_repr_atomicint64(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b", growth=True)
        .AtomicInt64()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)


def test_ND_text_repr_weight(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b", growth=True)
        .Weight()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)


def test_ND_text_repr_mean(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b", growth=True)
        .Mean()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)


def test_ND_text_repr_weightedmean(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b", growth=True)
        .WeightedMean()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)
