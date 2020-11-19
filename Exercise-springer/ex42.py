note = input("Enter note : ")

if note[0] == "c":
    freq = 261.63 / (2 ** (4 - int(note[1])))
elif note[0] == "d" :
    freq = 293.66 / (2 ** (4 - int(note[1])))
elif note[0] == "e" :
    freq = 329.63 / (2 ** (4 - int(note[1])))
elif note[0] == "f" :
    freq = 349.23 / (2 ** (4 - int(note[1])))
elif note[0] == "g" :
    freq = 392.00 / (2 ** (4 - int(note[1])))
elif note[0] == "a" :
    freq = 440.00 / (2 ** (4 - int(note[1])))
elif note[0] == "b" :
    freq = 493.88 / (2 ** (4 - int(note[1])))
else :
    freq = "error"

print(freq)
