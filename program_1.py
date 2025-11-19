#Record Program -1
#Library 

days = int(input("How many days was the book borrowed for: "))
cost = 0

if days <= 3:
    cost = 5
elif days <= 10:
    cost = 5 + ((3)*(days-3))
elif days > 10:
    cost = 26 + (days-10)*(10)
    
print(f"• You have borrowed the book for {days} days")
print(f"• Balance to be paid = ₹{cost}")