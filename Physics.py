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


class Particle(Point):
    """
    n-dimensional particle with charge and mass
    """

    def __init__(self, coords: list, charge, mass):
        super().__init__(coords)
        self.charge = charge
        self.mass = mass


def get_vector_a_to_b(a: Point, b: Point) -> np.ndarray:
    """
    return a vector pointing from point a to point b
    :param a: point a
    :param b: point b
    :return: vector of a-b
    """
    return np.array(b.coords) - np.array(a.coords)


def find_electric_field(p: Point, universe: list) -> np.ndarray:
    """
    find the electric field at point p
    :param p: point p in n-dimensional coordinates
    :param universe: all charged particles to be considered
    note:must have same number of dimensions as p
    :return: electric field vector at point p
    """
    e_vectors = np.empty(shape=(len(universe), len(p.coords)))
    i = 0
    for particle in universe:
        r = get_vector_a_to_b(particle, p)
        e_vector = COULOMB * particle.charge * r / (np.linalg.norm(r)) ** 3
        e_vectors[i] = e_vector
        i += 1
    return np.sum(e_vectors, axis=0)
