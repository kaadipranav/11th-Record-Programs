#Record Program -14
#Dictionaries 1

phonebook = {}

while True:
    print("\n1. Add")
    print("2. Modify by name")
    print("3. Delete by name")
    print("4. Display by name")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print("Added!")
        
    elif ch == 2:
        name = input("Enter name to modify: ")
        if name in phonebook:
            newphone = input("Enter new phone number: ")
            phonebook[name] = newphone
            print("Modified!")
        else:
            print("Name not found!")
            
    elif ch == 3:
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Deleted!")
        else:
            print("Name not found!")
            
    elif ch == 4:
        name = input("Enter name to search: ")
        if name in phonebook:
            print(name, ":", phonebook[name])
        else:
            print("Not found!")
            
    elif ch == 5:
        print("Thank you!")
        break