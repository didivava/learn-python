freq = float(input("Enter freq : "))
c, d, e, f, g, a, b = 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88

if freq >= c - 1 and freq <= c + 1 :
    note = "C4"
elif freq >= d - 1 and freq <= d + 1 :
    note = "D4"
elif freq >= e - 1 and freq <= e + 1 :
    note = "E4"
elif freq >= f - 1 and freq <= f + 1 :
    note = "F4"
elif freq >= g - 1 and freq <= g + 1 :
    note = "G4"
elif freq >= a - 1 and freq <= a + 1 :
    note = "A4"
elif freq >= b - 1 and freq <= b + 1 :
    note = "B4"
else :
    note = "Error"
    
print(note)
