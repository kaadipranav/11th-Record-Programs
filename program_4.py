#Record Program -4
#Armstrong numbers

start=int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Armstrong numbers between {start} and {end} are: ")

while start<=end:
    num = start
    temp = num
    sum = 0
    
    count = 0
    temp2 = num
    while temp2 > 0:
        count += 1
        temp2 = temp2 // 10
        
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10
        
    if sum == num:
        print(num)
    
    start += 1