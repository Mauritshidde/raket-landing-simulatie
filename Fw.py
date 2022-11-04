import math
def calc_luchtweerstand(velocity, Cw, area, temperatuur, force, hoogte, pressure): #per meter
    # p = airdensity, M = molaire massa lucht, R = gasconstante
    # Tper_m = 9.8 / 1000
    # pressure = 1
    # T = T - Tper_m
    GRAVITATIE_CONSTANT = 6.67384 * pow(10, -11)
    MOLAIRE_MASSA = 28.97 # constant
    R_GASCONSTANTE = 8.314472 # constant
    pressure = pressure * math.exp(-MOLAIRE_MASSA * GRAVITATIE_CONSTANT * hoogte /(R_GASCONSTANTE * temperatuur))
    Rho = (pressure * MOLAIRE_MASSA) / (R_GASCONSTANTE * temperatuur)
    k = 0.5 * Cw * area * Rho
    Fw = k * velocity * velocity
    # print(Fw)
    return Fw, pressure

# for i in range(100):
#     v = 100
#     F = 10000
#     a = 10
#     # calc_luchtweerstand()