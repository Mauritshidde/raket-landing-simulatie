from math import pow


def calc_grafitatiekracht(height, MASS_ROCKET):
    GRAFITATIONAL_CONSTANT = 6.67384 * pow(10, -11)  # Nm^2/kg^2
    RADIUS_EARTH = 6.371 * pow(10, 6)  # m
    MASS_EARTH = 5.972 * pow(10, 24)  # kg

    FORCE_GRAFITATIE = GRAFITATIONAL_CONSTANT * \
        MASS_EARTH * MASS_ROCKET / pow(RADIUS_EARTH + height, 2) # N

    return FORCE_GRAFITATIE

print(calc_grafitatiekracht(100, 100))