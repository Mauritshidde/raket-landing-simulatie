
Cw = 5
def calc_luchtweerstand(v, Cw, A, T, F): #per meter
    # p = airdensity, M = molaire massa lucht, R = gasconstante
    Tper_m = 9.8 / 1000
    
    T = T - Tper_m
    G = 6.67384 * 10^-11
    M = 28.97 # constant
    R = 8.314472 # constant
    p = p * exp(-M*G*H/(R*T))
    Rho = (p * M) / (R * T)
    k = 0.5 * Cw * A * Rho
    Fw = k * v * v

    return Fw






def main():
    notLanded = True
    while notLanded:
        F = 40
        Tb = 27 + 273
        speed = 100
        A = 55
        Fw = calc_luchtweerstand(speed, Cw, A, Tb, F)
        F = Fw
        print(Fw)

main()