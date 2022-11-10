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
    dt = 0.01  # s
    Rv = 42.8 * pow(10, 6) # Kerosine in J/kg
    iterations = 1000000  # times
    height = 0  # m
    BURN_RATE = 1529.63  # kg / s
    velocity = 0  # m/s
    capsule_mass = 3000 # kg
    mass_fuel_rocket = 395700 # kg
    mass_empty_rocket = 25600 # kg
    mass_rocket = 549054  # kg (mass falcon 9)
    force_thrust = 7607000  # N (thrust falcon 9 in vacuum)
    TEMPERATURE = 298  # K
    area = 2 * pi * 3.7  # m^2
    force_netto = 0 # N
    totale_verbruikte_energie = 0
    target_height = 200000 # m
    second_stage_fuel_mass = 3900 # kg
    second_stage_vehicle_mass = 92670 # kg
    for i in range(iterations):
        t += dt
        if (height < target_height):
            if height >= 100000:
                force_thrust = 981000 # N
                mass_rocket = second_stage_fuel_mass + second_stage_vehicle_mass
                BURN_RATE = 233.425 #kg / s
            else:
                mass_rocket = capsule_mass + mass_fuel_rocket + mass_empty_rocket + second_stage_fuel_mass + second_stage_vehicle_mass

            force_gravitation = calc_gravitationforce(
                height, mass_rocket)  # Nm^2/kg^2
            force_resistance, aird = calc_airresistance(
                height, TEMPERATURE, area, velocity)
            
                # force_resistance = 0
            if height >= 100000:
                if (second_stage_fuel_mass < BURN_RATE * dt):
                    force_thrust = 0
                else:
                    second_stage_fuel_mass -= BURN_RATE * dt
                
                print(second_stage_fuel_mass)
                # print()
            else:
                mass_fuel_rocket -= BURN_RATE * dt

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
            print(t)
            break
            pass

        # if (height >= 40000):
        #     print(height, force_resistance, aird)
        #     break
            
        energie_list.append(force_gravitation)
        kracht_list.append(force_netto) 
        tijd_list.append(t) 
        height_list.append(height)
        snelheid_list.append(velocity)
            
        # print()
        # print("--- iteration ", i, " ---")
        # print('graviatation:', force_gravitation)
        # print('resistance:', force_resistance)
        # print(height)

    all_y_list = [energie_list, kracht_list, snelheid_list, height_list]
    all_x_list = [tijd_list, tijd_list, tijd_list, tijd_list]

    plot_values(["energie in Joule", "kracht in Newton", "snelheid in m/s"], ["tijd in s", "tijd in s", "tijd in s"], all_x_list, all_y_list)
    

main()
