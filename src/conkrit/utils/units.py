# File: src/conkrit/utils/units.py
"""
Unit management for the Conkrit library using Pint.

This module provides a central unit registry and parsing function
for interpreting values with units throughout the Conkrit package.
"""

import pint

# Initialize a global unit registry
ureg = pint.UnitRegistry()

# Convenience alias to parse values with units
# Example:
#   >>> units("2 cm")
#   <Quantity(2, 'centimeter')>
def units(value):
    """
    Parse a numeric or string input into a Pint Quantity.

    Parameters:
        value (str or numeric): A string with units (e.g., "20 MPa") or a numeric value already in a Pint unit.

    Returns:
        pint.Quantity: The parsed quantity with units.
    """
    return ureg(value)
