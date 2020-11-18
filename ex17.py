vol = float(input("Enter volume of water in liter = "))
t1 = float(input("Enter current temp in celcius = "))
t2 = float(input("Enter desire temp in celcius = "))

m = vol * 1000
dt = t2 - t1

q = m * 4186 * dt
price = 8.9 * q * 0.0000002778

print("To heat %.2f liter of water to %.2f celcius you'll need %.2f cents" %(vol, t2, price))
