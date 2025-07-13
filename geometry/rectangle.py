# src/conkrit/geometry/rectangle.py

from .base import Shape
from typing import Tuple

class Rectangle(Shape):
    """
    Rectangular shape with width b and height h.
    Centroid at (b/2, h/2).
    """

    def __init__(self, b: float, h: float):
        self.b = b
        self.h = h

    def area(self) -> float:
        return self.b * self.h

    def centroid(self) -> Tuple[float, float]:
        return (self.b / 2.0, self.h / 2.0)

    def inertia_y(self) -> float:
        # I about horizontal axis through centroid:
        return (self.b * self.h**3) / 12.0
