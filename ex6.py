price = input("Enter price of meal = $ ")
tax = float(price) * 10/100
tip = float(price) * 18/100
total = float(price) + tax + tip

print("Meal price = $ ", price)
print("Tax = $ %.2f" %tax)
print("Tip = $ %.2f" %tip)
print("Grand Total = $ %.2f" %total)
