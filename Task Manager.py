def task():
    task = [] #empty list
    print("---WELCOME TO THE TASK MANAGEMENT APP---")

    total_task = int(input("enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name = input("enter the task {i} = ")#enter task
        task.append (task_name)
    print(f"Todays task are\n{task}")

    while True:
       operation=int(input("enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\stop"))
       if operation == 1:
         add = (input("enter the task you want to add = "))
         task.append(add) 
         print(f"task {add} has been successfully added...")
          
       elif operation == 2:
            updated_val = (input(f"Enter the task you want to update="))
            if updated_val in task:
                up= input("enter new task= ")
                ind = task.index(updated_val)
                task[ind] = up
                print(f"updated task {up}") 
            
       elif operation == 3:
              del_val = (input("which task you want to delete="))
              if del_val in task:
                 ind = task.index(del_val)#3
                 del task[ind] 
                 print(f" task {del_val} has been deleted")
            
       elif operation == 4:
            print(f"total task={task}") 
            
       elif operation == 5:
           print(f"closing the program")
           break 
       
       else:
           print("Invalid Input")
task()
