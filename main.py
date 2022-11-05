# Deze code werkt niet!!!
# zie /version2 voor werkende code (in ander folder i.v.m. merge conflicts)

from Fw import *
from plot import *

def main():
    Fw_array = []
    height_array = []
    velocity_array = []
    height = 1000 # meter
    velocity = 100 # m/s
    force = 6000 # Newton
    Cw = 50 # constant
    massa = 400 # kg
    area = 50 # meter
    temperatuur = 27 + 273 # Kelvin
    step = 0.1 # stap grootte van berekening
    pressure = 0.01 # Pascal
    while height > 0:
        F = 40
        Tb = 27 + 273
        speed = 100
        A = 55
        Fw, pressure = calc_luchtweerstand(velocity, Cw, area, temperatuur, force, height, pressure)
        F -= Fw * step
        velocity += (force/massa) * step
        height -= velocity * step
        Fw_array.append(Fw)
        velocity_array.append(velocity)
        height_array.append(height)
        # print(velocity, "vele", height)
        # print(height)
    # print(height_array[5], "ja")
    # print(Fw_array[5], "ja")
    plot_values("Fw", "Height", Fw_array , velocity_array)

main()