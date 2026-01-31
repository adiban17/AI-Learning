#define tasks
tasks=["Go for a Run","Wash the Dishes","Clean the Clothes","Pay the Bills","Do Work"]
completed_tasks=[]
incomplete_tasks=list(tasks)
control=1

#task menu
while control==1:
    print("Press\n1-view all tasks\n2-view incomplete tasks\n3-view completed tasks\n4-add a task")
    action=int(input())

    match action:
        case 1:
            for x in tasks:
                print(x)

            check=input(("Do you want to check off a task:(y/n):"))
            if(check=='y'):
                task_index=int(input('Enter Task Number:'))-1
                for x,y in enumerate(incomplete_tasks):
                    if tasks[task_index]==x:
                        incomplete_tasks.pop(y)
                    

                completed_tasks.append(tasks[task_index])
                completed_tasks.append(tasks[task_index])
                

            control=int(input("Press 1 to continue/0 to exit:"))
                

        case 2:
            for x in completed_tasks:
                print(x)
            control=int(input("Press 1 to continue/0 to exit:"))

        case 3:
            for x in incomplete_tasks:
                print(x)
            
            check=input(("Do you want to check off a task:(y/n):"))
            if(check=='y'):
                task_index=int(input('Enter Task Number:'))-1
                completed_tasks.append(incomplete_tasks[task_index])
                incomplete_tasks.pop(task_index)

            control=int(input("Press 1 to continue/0 to exit:"))


        case 4:
            new_task=input("Enter Task Name:\n")
            tasks.append(new_task)

            control=int(input("Press 1 to continue/0 to exit:"))
                
print("Thank You for using our platform!!!")


    