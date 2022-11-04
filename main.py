from Fw import *


def main():
    height = 10000  # km
    while height > 0:
        F = 40
        Tb = 27 + 273
        speed = 100
        A = 55
        Fw = calc_luchtweerstand(speed, Cw, A, Tb, F)
        F = Fw
        print(Fw)


main()
