# tests/unit/test_units.py

import pytest
from conkrit.utils import units
from pint import UnitRegistry

ureg = UnitRegistry()

def test_magnitude_property_returns_number():
    qty = 5 * ureg.meter
    # .magnitude should be a plain Python float/int
    assert isinstance(qty.magnitude, (int, float))
    assert qty.magnitude == 5

def test_to_converts_units_correctly():
    qty = 200 * ureg.centimeter
    in_m = qty.to('meter')
    assert pytest.approx(in_m.magnitude) == 2.0
