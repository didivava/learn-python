p = float(input("Enter preassure in pascal = "))
v = float(input("Enter volume in liter = "))
t = float(input("Enter temperature in celcius = "))

n = (p * v) / (8.314 * (273.15 + t))

print("%.2f moles of gas in the tank" %n )
