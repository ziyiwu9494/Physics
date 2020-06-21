import math
import numpy as np
from sklearn import preprocessing

COULOMB = 9*10**9


class Point:
    def __init__(self, coords: list):
        self.coords = coords


class Particle(Point):
    def __init__(self, coords: list, charge, mass):
        super().__init__(coords)
        self.charge = charge
        self.mass = mass


def distance(a: Point, b: Point):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def get_vector_a_to_b(a: Point, b: Point):
    return np.array(b.coords) - np.array(a.coords)


def find_electric_field(p: Point, universe: list):
    e_vectors = np.empty(shape=(len(universe), len(p.coords)))
    i = 0
    for particle in universe:
        r = get_vector_a_to_b(particle, p)
        e_vector = COULOMB*particle.charge*r/(np.linalg.norm(r))**3
        e_vectors[i] = e_vector
        i += 1
    return np.sum(e_vectors, axis=0)



