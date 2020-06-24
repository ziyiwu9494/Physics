import math
from typing import List

import numpy as np

COULOMB = 9 * 10 ** 9
GRAVITY = 9.81


class Point:
    """
    n-dimensional point object
    """

    def __init__(self, coords: List[float]):
        self.coords = coords

    def get_vector_to_b(self, b) -> np.ndarray:
        """
        return a vector pointing from current point to point b
        :param b: Point b
        :return: vector of a-b
        """
        return np.array(b.coords) - np.array(self.coords)

    def find_electric_field(self, universe: list) -> np.ndarray:
        """
        find the electric field at the current point
        :param universe: all charged particles to be considered
        note:must have same number of dimensions as p
        :return: electric field vector at point p in N/C
        """
        e_vectors = np.empty(shape=(len(universe), len(self.coords)))
        i = 0
        for particle in universe:
            e_vectors[i] = particle.find_electric_field(self)
            i += 1
        return UEField(np.sum(e_vectors, axis=0))


class Particle(Point):
    """
    n-dimensional particle with charge in C and mass in kg
    """

    def __init__(self, coords: List[float], charge, mass):
        super().__init__(coords)
        self.charge = charge
        self.mass = mass

    def find_electric_field(self, p: Point) -> np.ndarray:
        """
        find the electric field vector of the current particle at the coords
        :param p: point with coordinates of the point to find the particle in meters
        :return: electric field vector in N/C
        """
        r = self.get_vector_to_b(p)
        e_vector = COULOMB * self.charge * r / (np.linalg.norm(r)) ** 3
        return e_vector


class UEField:
    """
    uniform electric field in N/C
    """

    def __init__(self, vector: np.ndarray, magnitude=0):
        """

        :param vector: electric field vector
        :param magnitude: feature for problem solving (N/C)
        """
        self.vector = vector
        self.magnitude = magnitude if magnitude != 0 else np.linalg.norm(vector)

    def __str__(self):
        return str(list(self.vector))

    def force(self, p: Particle) -> np.ndarray:
        """
        force exerted by the electric field on particle p
        :param p: charged particle p
        :return: force vector exerted on p
        """
        return self.magnitude * p.charge * self.vector / np.linalg.norm(self.vector)


class Dipole:
    """
    electric dipole with dipole moment in C*M
    """

    def __init__(self, mag_p, theta, mode="degrees"):
        self.p = mag_p
        self.mode = mode
        self.theta = math.radians(theta) if mode == "degrees" else theta

    def turn(self, theta: float, field: UEField) -> float:
        """
        turns dipole by theta degrees or radians and returns the amount of work done in the turn

        :param theta: final angle
        :param field: electric field
        note: ignores direction
        :return: work in joules
        """
        theta = math.radians(theta) if self.mode == "degrees" else theta
        theta_i = self.theta
        self.theta = theta
        return self.p * field.magnitude * (math.cos(theta_i) - math.cos(theta_i + theta))







