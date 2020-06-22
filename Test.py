import Physics


def electric_field_test_1():
    env = [Physics.Particle([3, 0], float("3.20E-19"), 0), Physics.Particle([-3, 0], float("-3.20E-19"), 0)]
    assert list(Physics.Point([0, 3]).find_electric_field(env)) == [-2.2627416997969528e-10, 0.0]


def dipole_test_1():
    field = Physics.UEField([], 34.9)
    dipole = Physics.Dipole(float("1.97E-25"), 72.6)
    assert dipole.turn(180, field) == float("4.111990317996545e-24")


electric_field_test_1()
dipole_test_1()
