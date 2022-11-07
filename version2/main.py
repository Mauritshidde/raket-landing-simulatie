from math import pi
from temperature import calc_temperature
from gravitation import calc_gravitationforce
from airresistance import calc_airresistance


def main():
    t = 0  # s
    dt = 1  # s
    iterations = 10  # times
    height = 30000  # m
    accelaration = 0  # m/s/s
    velocity = 0  # m/s
    mass_rocket = 549054  # kg (mass falcon 9)
    force_thrust = 8227000  # N (thrust falcon 9 in vacuum)
    area = 2 * pi * 3.7  # m^2

    for i in range(iterations):
        t += dt
        temperature = calc_temperature(height)  # K
        force_gravitation = calc_gravitationforce(
            height, mass_rocket)  # Nm^2/kg^2
        force_resistance = calc_airresistance(
            height, temperature, area, velocity)

        print()
        print("--- iteration ", i, " ---")
        print('graviatation:', force_gravitation)
        print('resistance:', force_resistance)
        print('temperature:', temperature)
        print()


main()
