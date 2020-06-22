import math
import numpy as np
from sklearn import preprocessing

COULOMB = 9 * 10 ** 9


class Point:
    """
    n-dimensional point object
    """

    def __init__(self, coords: list):
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
        find the electric field at point p
        :param p: point p in n-dimensional coordinates
        :param universe: all charged particles to be considered
        note:must have same number of dimensions as p
        :return: electric field vector at point p
        """
        e_vectors = np.empty(shape=(len(universe), len(self.coords)))
        i = 0
        for particle in universe:
            r = particle.get_vector_to_b(self)
            e_vector = COULOMB * particle.charge * r / (np.linalg.norm(r)) ** 3
            e_vectors[i] = e_vector
            i += 1
        return np.sum(e_vectors, axis=0)


class Particle(Point):
    """
    n-dimensional particle with charge and mass
    """

    def __init__(self, coords: list, charge, mass):
        super().__init__(coords)
        self.charge = charge
        self.mass = mass


class UEField:
    """
    uniform electric field
    """

    def __init__(self,  vector: list, magnitude):
        self.vector = vector
        self.magnitude = magnitude


class Dipole:
    """
    electric dipole
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
        return self.p * field.magnitude * (math.cos(theta_i)-math.cos(theta_i+theta))








