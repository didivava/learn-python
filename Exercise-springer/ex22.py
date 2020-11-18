import math

s1 = int(input("Enter length of S1 = "))
s2 = int(input("Enter length of S2 = "))
s3 = int(input("Enter length of S3 = "))

s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("The area is %.2f" %area)
