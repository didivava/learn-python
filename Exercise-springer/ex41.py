a = int(input("Enter length of side 1 = "))
b = int(input("Enter length of side 2 = "))
c = int(input("Enter length of side 3 = "))

if a == b and a == c and b == c :
    name = "scalene"
elif a == b or a == c or b == c :
    name = "equilateral"
else :
    name = "isosceles"

print(name)
