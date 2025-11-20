#Record Program -6
#Binary to Decimal

x = int(input("Enter a number: "))
n = x
total = 0
i = 0

while i<x:
    y = n%10
    n//=10
    total += y*(2**i)
    i += 1
print(total)