
Tasks = ['Study', 'Play', 'Stream']
i = 1

while True:
    print("1) Add Task")
    print("2) Remove Task")
    print("3) View Tasks")
    print("4) Exit")
    User_Choice = input("Enter Your Choice: ")    

    if User_Choice == "1":  
        User_Input = input("Enter a task to add in the list: ")
        Tasks.append(User_Input)
        print("Task added Successfully!")
        print(Tasks)
                

    elif User_Choice == "2":
        print("*** Following Are your Current Remaining Tasks! ***")
        for task in Tasks:
            print(task)
            
        User_Input = input("What task do you want to remove: ")
        Tasks.remove(User_Input)
        print(Tasks)
                    
            
    elif User_Choice == "3":
        print("1) View list Vertically") 
        print("2) View List Horizontally")
        User_Input = input("Please select how to display list: ")
        if User_Input == "1":
            for task in Tasks:
                print(task)
        elif User_Input == "2":
            print(Tasks)
        
                    
    elif User_Choice == "4":
        break     