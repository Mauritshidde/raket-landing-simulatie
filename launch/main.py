from math import pi
from gravitation import calc_gravitationforce
from airresistance import calc_airresistance
from plot import *

def main():
    energie_list = []
    kracht_list = []
    tijd_list = []
    snelheid_list = []
    height_list = []

    t = 0  # s
    dt = 1  # s
    Rv = 42.8 * pow(10, 6) # Kerosine in J/kg
    iterations = 100  # times
    height = 30000  # m
    BURN_RATE = 1529.63  # kg / s
    velocity = 0  # m/s
    mass_rocket = 549054  # kg (mass falcon 9)
    force_thrust = 7607000  # N (thrust falcon 9 in vacuum)
    TEMPERATURE = 298  # K
    area = 2 * pi * 3.7  # m^2
    force_netto = 0 # N
    totale_verbruikte_energie = 0
    target_height = 200000 # m
    for i in range(iterations):
        t += dt
        if (height < target_height):
            force_gravitation = calc_gravitationforce(
                height, mass_rocket)  # Nm^2/kg^2
            force_resistance = calc_airresistance(
                height, TEMPERATURE, area, velocity)
            
            if (velocity >= 0):
                force_netto = force_thrust - force_gravitation - force_resistance
            else:
                force_netto = force_resistance + force_thrust - force_gravitation
                
            velocity += force_netto / mass_rocket * dt
            height += velocity * dt

            used_fuel = BURN_RATE * dt
            chemische_energie = used_fuel * Rv
            totale_verbruikte_energie += chemische_energie

        else:
            pass

            
            
        energie_list.append(totale_verbruikte_energie)
        kracht_list.append(force_netto) 
        tijd_list.append(t) 
        height_list.append(height)
        snelheid_list.append(velocity)
            
        print()
        print("--- iteration ", i, " ---")
        print('graviatation:', force_gravitation)
        print('resistance:', force_resistance)
        print(height)

    all_y_list = [energie_list, kracht_list, snelheid_list, height_list]
    all_x_list = [tijd_list, tijd_list, tijd_list, tijd_list]

    plot_values(["energie in Joule", "kracht in Newton", "snelheid in m/s"], ["tijd in s", "tijd in s", "tijd in s"], all_x_list, all_y_list)
    

main()
