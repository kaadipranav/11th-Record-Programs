#Record Program -11
#Nested List
    
students = []

while True:
    print("\n1. Append (Add new student)")
    print("2. Delete by roll no")
    print("3. Edit marks by roll no")
    print("4. Class average percentage")
    print("5. Display all")
    print("6. Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        per = float(input("Enter Percentage: "))
        if per >= 75:
            remarks = "Distinction"
        elif per >= 60:
            remarks = "First Class"
        elif per >= 50:
            remarks = "Second Class"
        elif per >= 40:
            remarks = "Pass"
        else:
            remarks = "Fail"
        students.append([roll, name, per, remarks])
        print("Student added!")
        
    elif ch == 2:
        roll = int(input("Enter Roll No to delete: "))
        found = False
        for i in range(len(students)):
            if students[i][0] == roll:
                students.pop(i)
                print("Deleted!")
                found = True
                break
        if not found:
            print("Roll No not found!")
            
    elif ch == 3:
        roll = int(input("Enter Roll No to edit marks: "))
        found = False
        for i in range(len(students)):
            if students[i][0] == roll:
                new_per = float(input("Enter new percentage: "))
                students[i][2] = new_per
                if new_per >= 75:
                    students[i][3] = "Distinction"
                elif new_per >= 60:
                    students[i][3] = "First Class"
                elif new_per >= 50:
                    students[i][3] = "Second Class"
                elif new_per >= 40:
                    students[i][3] = "Pass"
                else:
                    students[i][3] = "Fail"
                print("Marks updated!")
                found = True
                break
        if not found:
            print("Roll No not found!")
            
    elif ch == 4:
        if len(students) == 0:
            print("No students!")
        else:
            total = 0
            for s in students:
                total = total + s[2]
            avg = total / len(students)
            print("Class average percentage =", avg)
            
    elif ch == 5:
        if len(students) == 0:
            print("No records!")
        else:
            print("\nRoll No\tName\tPercentage\tRemarks")
            print("-------------------------------------------")
            for s in students:
                print(s[0], "\t", s[1], "\t", s[2], "\t\t", s[3])
                
    elif ch == 6:
        print("Thank you!")
        break