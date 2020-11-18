sec = int(input("Enter seconds = "))

minute = sec // 60
sec1 = sec - (minute * 60)

hour = minute // 60
min1 = minute - (hour * 60)

day = hour // 24
hour1 = hour - (day * 24)

print("DD : HH : MM : SS = %d : %2d : %2d : %2d" %(day, hour1, min1, sec1))
