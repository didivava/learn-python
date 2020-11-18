from math import radians, acos, sin, cos

t1 = radians(float(input("Enter t1 in degrees = ")))
g1 = radians(float(input("Enter g1 in degrees = ")))
t2 = radians(float(input("Enter t2 in degrees = ")))
g2 = radians(float(input("Enter g2 in degrees = ")))

#t1 = radians(t1)
#g1 = radians(g1)
#t2 = radians(t2)
#g2 = radians(g2)

dist = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))

print("The distances are %.2f km" %dist)
