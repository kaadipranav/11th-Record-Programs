#Record Program -10
#List Manipulation

print("Enter numbers in ascending order separated by space:")
lst = list(map(int, input().split()))

while True:
    print("\n1. Insert an element")
    print("2. Delete all occurrence of an element")
    print("3. Display the list")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        x = int(input("Enter element to insert: "))
        lst.append(x)
        lst.sort()
        print("Inserted and sorted!")
        
    elif choice == 2:
        x = int(input("Enter element to delete: "))
        count = 0
        temp = []
        for i in lst:
            if i != x:
                temp.append(i)
            else:
                count = count + 1
        lst = temp
        if count == 0:
            print("Element not found!")
        else:
            print("Deleted", count, "occurrence(s)")
            
    elif choice == 3:
        print("Current list:", lst)
        
    elif choice == 4:
        print("Bye!")
        break