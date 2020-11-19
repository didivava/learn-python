hy = float(input("Enter human year of dog's life = "))

if hy <= 2 and hy >= 0:
    dy = hy * 10.5 / 2

elif hy > 2 :
    dy = (hy * 10.5 / 2) + ((hy - 2) * 4)

else :
    dy = "Error"

print(dy)
