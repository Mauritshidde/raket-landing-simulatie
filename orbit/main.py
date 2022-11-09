from math import pi
from gravitation import calc_gravitationforce
from airresistance import calc_airresistance
from plot import *

def main():
    afgelegde_afstand_list =[]
    time_list = []
    energie_list = []
    t = 0  # s
    dt = 1  # s
    Rv = 42.8 * pow(10, 6) # Kerosine in J/kg
    iterations = 10000  # times
    height = 30000  # m
    BURN_RATE = 1529.63  # kg / s
    velocity = 5000  # m/s
    mass_rocket = 549054  # kg (mass falcon 9)
    force_thrust = 7607000  # N (thrust falcon 9 in vacuum)
    TEMPERATURE = 298  # K
    area = 2 * pi * 3.7  # m^2
    R_aarde = 6.371 * pow(10, 6) # m
    max_hoogte = 200000 # m
    omtrek_baan = 2 * pi * (R_aarde + max_hoogte) # m^2
    afstand_afteleggen = omtrek_baan/2
    afstand_afgelegd = 0
    used_energie = 0
    totale_verbruikte_energie = 0
    for i in range(iterations):
        t += dt
        if (afstand_afgelegd < afstand_afteleggen):
            force_gravitation = calc_gravitationforce(
                height, mass_rocket)  # Nm^2/kg^2
            force_resistance = calc_airresistance(
                height, TEMPERATURE, area, velocity)
            
            horizontal_force_thrust = force_resistance
            vertical_force_thrust = force_gravitation
            needed_thrust_force = horizontal_force_thrust + vertical_force_thrust
            

            used_fuel = (BURN_RATE/force_thrust) * needed_thrust_force
            chemische_energie = used_fuel * Rv
            totale_verbruikte_energie += chemische_energie


            # force_netto = force_resistance + force_thrust - force_gravitation
            # velocity += force_netto / mass_rocket * dt
            # height += velocity * dt
            afstand_afgelegd += velocity * dt
        else:
            print("ja")
            pass

        energie_list.append(chemische_energie)
        time_list.append(t)
        afgelegde_afstand_list.append(afstand_afgelegd)
                

        print()
        print("--- iteration ", i, " ---")
        # print('graviatation:', force_gravitation)
        # print('resistance:', force_resistance)
        print(afstand_afgelegd)
    plot_values("time", "energie", time_list, afgelegde_afstand_list)

main()
