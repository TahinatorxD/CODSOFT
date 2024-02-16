print("1. Add Contacts.\n"
      "2. Search Contacts.\n"
      "3. Display All Contacts.")
Entry = input("Enter your choice (1 / 2 / 3): ")

book = open('Details', 'a')

if Entry == '1':
    print("Add Contacts...")
    First_Name = (input("Enter Name:- "))
    Number = (input("Enter Contacts:- "))

    with open('Details', 'a') as book:
        book.write(f"{First_Name}:{Number}\n")
        book.close()

elif Entry == '2':
    print("Search Contacts... ")
    Searching = (input("Enter the Name you are looking for: "))
    found = False
    with open('Details', 'r') as book:
        for line in book:
            name, address = line.strip().split(":")
            if name in Searching:
                print(f"Contact Details: {name}-{address} ")
                found = True
                break
        if not found:
            print("User Not Found.")

elif Entry == '3':
    print("Display All Contacts...")
    with open('Details', 'r') as book:
        for line in book:
            name, number = line.strip().split(":")
            print(f"Contact Details: {name}-{number}")