from __future__ import annotations

import numpy as np
import pytest

from hist import Hist


@pytest.fixture(autouse=True)
def mockoverlay_test(monkeypatch):
    monkeypatch.setattr(Hist, "plot1d", plot1doverlay_mock)


def plot1doverlay_mock(*args, **kwargs):
    return "called plot1d"


def test_overlay_plot():
    testOverlay = (
        Hist.new.Reg(20, 0, 10, name="S", label="s [units]", flow=False)
        .IntCat(range(10), name="W", label="w [units]")
        .Int64()
    )

    testOverlay.fill(
        S=np.random.normal(size=100_000) + np.ones(100_000),
        W=np.random.normal(size=100_000),
    )

    assert testOverlay.plot1d(overlay="S") == "called plot1d"
