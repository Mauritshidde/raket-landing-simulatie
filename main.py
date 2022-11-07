from math import pi
from gravitation import calc_gravitationforce
from airresistance import calc_airresistance


def main():
    t = 0  # s
    dt = 1  # s
    iterations = 10  # times
    height = 30000  # m
    BURN_RATE = 1529.63 # kg / s
    accelaration = 0  # m/s/s
    velocity = 0  # m/s
    mass_rocket = 549054  # kg (mass falcon 9)
    force_thrust = 7607000  # N (thrust falcon 9 in vacuum)
    TEMPERATURE = 298  # K
    area = 2 * pi * 3.7  # m^2
    for i in range(iterations):
        t += dt
        force_gravitation = calc_gravitationforce(
            height, mass_rocket)  # Nm^2/kg^2
        force_resistance = calc_airresistance(
            height, TEMPERATURE, area, velocity)
        force_netto = force_resistance + force_thrust - force_gravitation

        print()
        print("--- iteration ", i, " ---")
        print('graviatation:', force_gravitation)
        print('resistance:', force_resistance)
        print()


main()
