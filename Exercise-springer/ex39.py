month = input("Enter a month of year in lowcase = ")

if month == "january" or month == "march" or month == "may" or month == "july" or month == "september" or month == "november":
    day = "31 days"

elif month == "april" or month == "june" or month == "august" or month == "october" or month == "december":
    day = "30 days"

elif month == "february":
    day = "28 or 29 days"

else :
    day = "error"

print(day)
