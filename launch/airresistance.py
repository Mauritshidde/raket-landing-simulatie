from math import pow, exp


def calc_airresistance(height, temperature, area, velocity):
    GRAVITATIONAL_CONSTANT = 6.67384 * pow(10, -11)  # Nm^2/kg^2
    GAS_CONSTANT = 8.314472  # j/K/mol
    MOLAIR_MASS = 28.97  # g/mol
    PRESSURE_ZERO = 1013  # hPa
    Cw = 0.82

    pressure_exponent = -MOLAIR_MASS * GRAVITATIONAL_CONSTANT * \
        height / (GAS_CONSTANT * temperature)
    pressure = PRESSURE_ZERO * exp(pressure_exponent)  # hPa
    density = (pressure * MOLAIR_MASS) / (GAS_CONSTANT * temperature)  # kg/m^3
    k = 0.5 * Cw * area * density
    force_airresistance = k * pow(velocity, 2)
    return force_airresistance
