#Record Program -9
#String Manipulation 2

s = input("Enter a string: ")
upper = 0
lower = 0
digit = 0
special = 0

for i in s:
    if i >= 'A' and i <= 'Z':
        upper = upper + 1
    elif i >= 'a' and i <= 'z':
        lower = lower + 1
    elif i >= '0' and i <= '9':
        digit = digit + 1
    else:
        special = special + 1

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)
print("Digits =", digit)
print("Special characters =", special)