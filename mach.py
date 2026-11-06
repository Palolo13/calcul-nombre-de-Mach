from math import sqrt

altitude = float(input("Altitude en mètres : "))
print(altitude)
T = 288.15 - 0.0065*altitude
a = sqrt(1.4*287*T)
v = float(input("Vitesse de l'avion en m/s : "))
print(v)
print(v/a, "est le nombre de Mach")