from math import pi
from gravitation import calc_gravitationforce
from airresistance import calc_airresistance
from plot import *

def main():
    times = []
    heights = []
    force = []
    velocities = []
    t = 0  # s
    dt = 1  # s
    iterations = 20000  # times
    height = 100000  # m
    BURN_RATE = 1529.63  # kg / s
    velocity = 0  # m/s
    mass_rocket = 69000  # kg (mass falcon 9)
    # force_thrust = 7607000  # N (thrust falcon 9 in vacuum)
    TEMPERATURE = 298  # K
    RADIUS_ROCKET = 3.7 # m
    RADIUS_PARACHUTE = 144 # m
    area = 2 * pi * RADIUS_ROCKET # m^2
    Cw = 0.82
    Cw_parachute = 1.5

    for i in range(iterations):
        if height <= 0:
            print(velocity)
            break

        if velocity >= 0:
            velocity = 0
        
        t += dt
        if height <= 10000:
            area = 2 * pi * RADIUS_PARACHUTE
            Cw = Cw_parachute
        force_gravitation = calc_gravitationforce(
            height, mass_rocket)  # Nm^2/kg^2
        force_resistance = calc_airresistance(
            height, TEMPERATURE, area, velocity, Cw)
        force_netto = force_resistance - force_gravitation
        velocity += force_netto / mass_rocket * dt
        height += velocity * dt
        heights.append(height)
        times.append(t)
        force.append(force_resistance)
        velocities.append(velocity)


    plot_values("time", "height", times, heights)
    

main()
