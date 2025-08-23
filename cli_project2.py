task_list=[]
def show_task():
    if not task_list:
        print("No Task Yet")
    else:
        for i,task in enumerate(task_list,1):
            print(f"{i}.{task}")

def add_task(task):
    task_list.append(task)
    print("Task added.")

def delete_task(index):
    if 0<index<=len(task_list):
        removed=task_list.pop(index-1)
        print(f"Deleted:{removed}")
    else :
        print("Invalid Task No.")

while True:
    print(" To-Do-List")
    print("1.View Task")
    print("2.Add Task")
    print("3.Delete Task")
    print("4.Exit")
    choice=input("Choose an Opntion(1-4):")
    if choice=='1':
        show_task()
    elif choice=='2':
        task=input("Enter task:")
        add_task(task)
    elif choice=='3':
        show_task()
        try:
            idx=int(input("Enter task No. to Delete"))
            delete_task(idx)
        except ValueError:
            print("Please enter a Valid No.")
    elif choice=='4':
        print("GoodBye!")
        break
    else:
        print("Invalid Option.")

