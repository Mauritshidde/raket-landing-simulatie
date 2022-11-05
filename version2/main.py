from gravitation import calc_gravitationforce
import resistance

def main():
  t = 0 # s
  dt = 1 # s
  iterations = 1000 # times
  height = 30000 # m
  accelaration = 0 # m/s/s
  speed = 0 # m/s
  mass_rocket = 549054 # kg (mass falcon 9)
  force_thrust = 8227000 # N (thrust falcon 9 in vacuum)

  for i in range(iterations):
    t += dt
    force_gravitation = calc_gravitationforce(height, mass_rocket) # Nm^2/kg^2
    # force_resistance = calc_resistance()
    print(force_gravitation)

main()