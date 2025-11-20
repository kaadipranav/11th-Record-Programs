#Record Program -15
#Dictionaries 2

marks = {}

# Taking input for 10 students
print("Enter name and marks of 10 students:")
for i in range(10):
    name = input("Enter name: ")
    mark = int(input("Enter marks: "))
    marks[name] = mark

while True:
    print("\n1. Display class average")
    print("2. Highest and lowest marks students")
    print("3. Students scored > 75")
    print("4. Students scored < 40")
    print("5. Display in descending order of marks")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        total = 0
        for m in marks.values():
            total = total + m
        avg = total / 10
        print("Class average =", avg)
        
    elif choice == 2:
        max_marks = -1
        min_marks = 101
        max_name = ""
        min_name = ""
        for name, m in marks.items():
            if m > max_marks:
                max_marks = m
                max_name = name
            if m < min_marks:
                min_marks = m
                min_name = name
        print("Highest:", max_name, "-", max_marks)
        print("Lowest :", min_name, "-", min_marks)
        
    elif choice == 3:
        print("Students with more than 75 marks:")
        for name, m in marks.items():
            if m > 75:
                print(name, "-", m)
                
    elif choice == 4:
        print("Students with less than 40 marks:")
        for name, m in marks.items():
            if m < 40:
                print(name, "-", m)
                
    elif choice == 5:
        print("Students in descending order of marks:")
        # Creating list of (marks, name) and sorting reverse
        items = []
        for name, m in marks.items():
            items.append((m, name))
        # Bubble sort descending (school level)
        for i in range(len(items)):
            for j in range(len(items)-1):
                if items[j][0] < items[j+1][0]:
                    items[j], items[j+1] = items[j+1], items[j]
        for m, name in items:
            print(name, "-", m)
            
    elif choice == 6:
        print("Good Bye!")
        break