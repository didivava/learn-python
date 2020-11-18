import math

ta = float(input("Input air temp in celc = "))
v = float(input("Input wind speed in km/h = "))

wci = 13.12 + (0.6215 * ta) - (11.37 * math.pow(v,0.16)) + (0.3965 * ta * math.pow(v,0.16))

print("The WCI is %.2f" %wci)
