import math

d = float(input("Enter height in m : "))

vf = math.sqrt(2 * d * 9.8)
time = d / vf

print("Object will fall in %.2f seconds" %time)
