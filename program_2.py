#Record Program -2
#Greates of three numbers

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x>y and x>z:
    print(f"{x} is the greatest number")
elif y>x and y>z:
    print(f"{y} is the greatest number")
elif z>x and z>y:
    print(f"{z} is the greatest nuumber")
else:
    print("All values are numerically equal, please try again with different values")