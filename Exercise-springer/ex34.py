fresh = int(input("Number of fresh bread = "))
old = int(input("Number of day-old bread = "))

total_fresh = fresh * 3.49
total_old = old * 3.49 * 0.6
total = total_old + total_fresh

print("Fresh bread = $ %.2f" %total_fresh)
print("Day-old bread = $ %.2f" %total_old)
print("Grand total = $ %.2f" %total)
