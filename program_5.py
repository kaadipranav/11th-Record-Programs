#Record Program -5
#Sum of series

n = int(input("Enter the number of terms: "))
sum = 1.0
fact = 1

for i in range(1,n+1):
    fact *= i
    sum += i/fact
    
print("Sum of the series is: ", sum)