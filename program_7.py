#Record Program -7
#Hollow Triangle

rows = int(input("Enter the number of rows:"))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end = "")
    for j in range(2*i + 1):
        if j == 0 or j == 2*i or i == rows - 1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()