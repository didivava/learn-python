import math

n = int(input("Enter numbers of side = "))
s = int(input("Enter length of side = "))

area = (n * s * s) / (4 * math.tan(math.pi / n))

print("The area is %.2f" % area)
