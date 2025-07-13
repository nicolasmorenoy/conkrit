# src/conkrit/geometry/base.py

from abc import ABC, abstractmethod
from typing import Tuple

class Shape(ABC):
    """Abstract base for all cross‐section shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the cross‐sectional area."""
        ...

    @abstractmethod
    def centroid(self) -> Tuple[float, float]:
        """
        Return the centroid location (x̄, ȳ)
        in local coordinates.
        """
        ...

    @abstractmethod
    def inertia_y(self) -> float:
        """
        Return the second moment of area about
        the horizontal centroidal axis (Iᵧ).
        """
        ...
