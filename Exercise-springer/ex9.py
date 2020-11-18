init = float(input("Enter your initial balace = $"))
year1 = init + (init * 4 / 100)
year2 = year1 + (year1 * 4 / 100)
year3 = year2 + (year2 * 4 / 100)

print("Your balance are First year $ %.2f, Second year $ %.2f, third year $ %.2f" %(year1, year2, year3))
