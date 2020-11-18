import math

r = float(input("Enter radius = "))

area = math.pi * (r * r)
volume = (4 * math.pi * r * r * r) / 3

print("Area = %.2f and Volume = %.2f" %(area, volume))
