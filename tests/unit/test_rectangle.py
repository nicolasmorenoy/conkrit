import pytest
from conkrit.geometry.rectangle import Rectangle
from conkrit.utils.units import ureg
Q_ = ureg.Quantity


def test_rectangle_area():
    rect = Rectangle(b=2.0, h=4.0)
    assert rect.area() == 8.0


def test_rectangle_centroid():
    rect = Rectangle(b=2.0, h=4.0)
    cx, cy = rect.centroid()
    assert isinstance((cx, cy), tuple)
    assert pytest.approx(cx, rel=1e-6) == 1.0
    assert pytest.approx(cy, rel=1e-6) == 2.0


def test_rectangle_inertia_y():
    rect = Rectangle(b=2.0, h=4.0)
    inertia = rect.inertia_y()
    # I_y = b*h^3/12 = 2 * 4^3 / 12
    expected = 2.0 * 4.0**3 / 12.0
    assert pytest.approx(inertia, rel=1e-6) == expected


def test_rectangle_area_with_units():
    rect = Rectangle(b=Q_(2, 'm'), h=Q_(4, 'm'))
    area = rect.area()
    # area should be a Quantity with units m**2
    assert hasattr(area, 'to')
    assert pytest.approx(area.to('m**2').magnitude, rel=1e-6) == 8.0
    assert str(area.units) == 'meter ** 2'


def test_rectangle_centroid_with_units():
    rect = Rectangle(b=Q_(2, 'm'), h=Q_(4, 'm'))
    cx, cy = rect.centroid()
    # centroid coordinates should be Quantities with units m
    assert hasattr(cx, 'to') and hasattr(cy, 'to')
    assert pytest.approx(cx.to('m').magnitude, rel=1e-6) == 1.0
    assert pytest.approx(cy.to('m').magnitude, rel=1e-6) == 2.0
    assert str(cx.units) == 'meter' and str(cy.units) == 'meter'


def test_rectangle_inertia_y_with_units():
    rect = Rectangle(b=Q_(2, 'm'), h=Q_(4, 'm'))
    inertia = rect.inertia_y()
    # inertia should be a Quantity with units m**4
    assert hasattr(inertia, 'to')
    expected = 2.0 * 4.0**3 / 12.0
    assert pytest.approx(inertia.to('m**4').magnitude, rel=1e-6) == expected
    assert str(inertia.units) == 'meter ** 4'
