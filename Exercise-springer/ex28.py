wgh = int(input("Enter your weight in kg = "))
hgh = int(input("Enter your height in cm = "))

bmi = wgh / ((hgh / 100) * wgh)

print("Your bmi is %.2f" %bmi)
