from math import pi, pow
from gravitation import calc_gravitationforce
from airresistance import calc_airresistance
from plot import *


def main():
    times = []
    heights = []
    force = []
    velocities = []
    t = 0  # s
    dt = 0.0001  # s
    height = 200000  # m
    BURN_RATE = 1529.63  # kg / s
    velocity = 0  # m/s
    mass_rocket = 3000  # kg (mass falcon 9)
    # force_thrust = 7607000  # N (thrust falcon 9 in vacuum)
    TEMPERATURE = 298  # K
    RADIUS_ROCKET = 3.7  # m
    RADIUS_PARACHUTE = 25  # m
    area = pi * pow(RADIUS_ROCKET, 2)  # m^2
    Cw = 0.82
    Cw_parachute = 1.5

    while height >= 0:
        t += dt
        if height <= 5000:
            area = pi * pow(RADIUS_PARACHUTE, 2)
            Cw = Cw_parachute
        force_gravitation = calc_gravitationforce(
            height, mass_rocket)  # Nm^2/kg^2
        force_resistance = calc_airresistance(
            height, TEMPERATURE, area, velocity, Cw)
        force_netto = force_resistance - force_gravitation
        velocity += force_netto / mass_rocket * dt
        if velocity >= 0:  # correct inaccuracy
            velocity = 0
        height += velocity * dt
        heights.append(height)
        times.append(t)
        force.append(force_gravitation)
        velocities.append(-velocity)
    else:
        print("t",t, "v", velocity)

    plot_values("Snelheid met parachute", "tijd(s)", "Snelheid (m/s)", times, velocities)


main()
