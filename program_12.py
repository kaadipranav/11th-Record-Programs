#Record Program -12
#Tuples

# First create initial tuple
print("Enter elements of tuple separated by space:")
t = tuple(input().split())

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = input("Enter element to insert: ")
        t = t + (item,)        # creating new tuple
        print("Inserted!")
        
    elif choice == 2:
        item = input("Enter element to delete: ")
        temp = ()
        found = False
        for x in t:
            if x != item:
                temp = temp + (x,)
            else:
                found = True
        t = temp
        if found:
            print("Deleted!")
        else:
            print("Element not found!")
            
    elif choice == 3:
        print("Current tuple:", t)
        
    elif choice == 4:
        print("Bye Bye!")
        break