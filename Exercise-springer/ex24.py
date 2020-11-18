day = int(input("Enter days = "))
hour = int(input("Enter hours = "))
minute = int(input("Enter minutes = "))
second = int(input("Enter seconds = "))

total = (day * 24 * 60 * 60) + (hour * 60 * 60) + (minute * 60) + second

print("Total %i seconds" %total)
