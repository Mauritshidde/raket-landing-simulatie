from math import pow, exp


def calc_airresistance(height, temperature, area, velocity):
    valversnelling = 9.81 # m/s^2
    # GRAVITATIONAL_CONSTANT = 6.67384 * pow(10, -11)  # Nm^2/kg^2
    GAS_CONSTANT = 8.314472  # j/K/mol
    MOLAIR_MASS = 0.02897  # kg/mol
    PRESSURE_ZERO = 1013  # hPa
    Cw = 0.82

    pressure_exponent = -MOLAIR_MASS * valversnelling * height / (GAS_CONSTANT * temperature)
    pressure = PRESSURE_ZERO * exp(pressure_exponent)  # hPa
    density = (pressure * MOLAIR_MASS) / (GAS_CONSTANT * temperature)  # kg/m^3
    print(pressure_exponent)
    k = 0.5 * Cw * area * density
    force_airresistance = k * pow(velocity, 2)
    return force_airresistance
