change = float(input("Enter your changes = $ "))

toonies = change // 2
loonies = (change - (toonies * 2)) // 1
quarter = (change - (toonies * 2) - loonies) // 0.25
dimes = (change - (toonies * 2) - loonies - (quarter * 0.25)) // 0.1
nickels = (change - (toonies * 2) - loonies - (quarter * 0.25) - (dimes * 0.1)) // 0.05
pennies = (change - (toonies * 2) - loonies - (quarter * 0.25) - (dimes * 0.1) - (nickels * 0.05)) // 0.01

print("Your changes :")
print("%.0f toonies" %toonies)
print("%.0f loonies" %loonies)
print("%.0f quarter" %quarter)
print("%.0f dimes" %dimes)
print("%.0f nickels" %nickels)
print("%.0f pennies" %pennies)
