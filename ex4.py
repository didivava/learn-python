length = input("Length in feet = ")
width = input("Width in feet = ")

area = float(width) * float(length)
area_acre = area / 43560
print("The area is %.2f acre" % area_acre)
