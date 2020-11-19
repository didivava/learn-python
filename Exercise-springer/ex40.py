db = float(input("Enter sound level in dB = "))

if db < 40 :
    result = "Quiter than quite room"
elif db == 40 :
    result = "Quite room"
elif db > 40 and db < 70 :
    result = "Between quite room and alarm clock"
elif db == 70 :
    result = "Alarm clock"
elif db > 70 and db < 106 :
    result = "Between alarm clock and gas lawnmower"
elif db == 106 :
    result = "Gas lawnmower"
elif db > 106 and db < 130 :
    result = "Between gas lawnmower and jackhammer"
elif db == 130 :
    result = "Jackhammer"
else :
    result = "Louder than jackhammer"

print(result)
