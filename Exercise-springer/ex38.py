side = int(input("Enter number of side = "))

if side == 3:
    shape = "Triangle"
elif side == 4:
    shape = "Rectangle"
elif side == 5:
    shape = "Pentagon"
elif side == 6:
    shape = "Hexagon"
elif side == 7:
    shape = "Heptagon"
elif side == 8:
    shape = "Octagon"
elif side == 9:
    shape = "Nonagon"
elif side == 10:
    shape = "decagon"
else :
    shape = "Sorry, error"

print(shape)
