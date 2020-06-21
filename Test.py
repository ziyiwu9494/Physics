import Physics


def electric_field_test_1():
    env = [Physics.Particle([3, 0], float("3.20E-19"), 0), Physics.Particle([-3, 0], float("-3.20E-19"), 0)]
    assert list(Physics.find_electric_field(Physics.Point([0, 3]), env)) == [-2.2627416997969528e-10, 0.0]




