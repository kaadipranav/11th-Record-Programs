#Record Program -3
#Payroll

HRA = 0
DA = 0
PF = 0
gross_pay = 0
net_pay = 0

salary = int(input("Salary: "))

if salary <= 10000:
    HRA = 0.20*salary
    DA = 0.80*salary
    PF = 0.05*salary
elif salary <= 20000:
    HRA = 0.25*salary
    DA = 0.90*salary
    PF = 0.10*salary
elif salary > 20000:
    HRA = 0.30*salary
    DA = 0.95*salary
    PF = 0.20*salary
else:
    print("Invalid Salary")
    
gross_pay = salary + HRA + DA
net_pay = gross_pay - PF

print(f"Salary: ₹{salary}")
print(f"HRA: ₹{HRA}")
print(f"DA: ₹{DA}")
print(f"PF: ₹{PF}")
print(f"Gross Pay: ₹{gross_pay}")
print(f"Net Pay: ₹{net_pay}")