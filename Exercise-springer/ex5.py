small = input("Enter number of small bottle (<= 1 litre) = ")
large = input("Enter number of large bottle (> 1 litre) = ")

refund = (float(small) * 0.1) + (float(large) * 0.25)

print("Refund = $ %.2f" %refund)
