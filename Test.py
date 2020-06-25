import Physics
import numpy as np


def electric_field_test_1():
    env = [Physics.Particle([3, 0], float("3.20E-19"), 0), Physics.Particle([-3, 0], float("-3.20E-19"), 0)]
    assert list(Physics.Point([0, 3]).find_electric_field(env).vector) == [-2.2627416997969528e-10, 0.0]


def electric_field_test_2():
    env = [
        Physics.Particle([0, 0.045], float("7.3E-9"), 0),
        Physics.Particle([0.045, 0.045], float("-17.5E-9"), 0),
        Physics.Particle([0.045, 0], float("17.5E-9"), 0),
        Physics.Particle([0, 0], float("-7.3E-9"), 0),
    ]
    assert np.linalg.norm(Physics.Point([0.0225, 0.0225]).find_electric_field(env).vector) == 128222.02965516063


def electric_field_test_3():
    pos = [[-1, 0], [1, 0], [0, 1], [0, 2]]
    charge_e = [4, 4, 2, -8]
    charge = [e*float("1.6E-19") for e in charge_e]
    env = [
        Physics.Particle([p[0]*float("4.56E-6"), p[1]*float("4.56E-6")], q, 0) for p, q in zip(pos, charge)
    ]
    assert np.linalg.norm(Physics.Point([0, 0]).find_electric_field(env).vector) == 0


def electric_field_test_4():
    env = [
        Physics.Particle([0, 0], float("-3.65E-7"), 0),
        Physics.Particle([0.218, 0], float("3.65E-7"), 0),
    ]
    assert str(Physics.Point([0.109, 0]).find_electric_field(env)) == "[-552983.7555761299, 0.0]"


def electric_field_test_dipole():
    """
    maybe make actual dipoles behave like this?
    :return:
    """
    env = [
        Physics.Particle([0, float("1.61E-6")], float("6.68E-6"), 0),
        Physics.Particle([0, float("-1.61E-6")], float("-6.68E-6"), 0)
    ]
    assert np.linalg.norm(Physics.Point([0.0893, 0]).find_electric_field(env).vector) == 271.8444474330574


def dipole_test_1():
    field = Physics.UEField([], 34.9)
    dipole = Physics.Dipole(float("1.97E-25"), 72.6)
    assert dipole.turn(180, field) == float("4.111990317996545e-24")


electric_field_test_1()
electric_field_test_2()
electric_field_test_3()
electric_field_test_4()
electric_field_test_dipole()
dipole_test_1()
