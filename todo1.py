import json
from datetime import date

emptyDoc= False

while True:
    with open("todoDB.json","r") as f:
        todoData= json.load(f)
    # f=open("todoDB.json","r")
    # todoData=json.load(f)
    # print(todoData,type(todoData))

    currentDate=date.today()
    if len(todoData)==0:
        emptyDoc=True
        username=input("\nHii there!! Welcome to TodoCLI. Please enter your username")
        todoData["name"]=username
        todoData["date"]=str(currentDate)
        print(f"Hey {username}! i hope you have a good start of the day")


        cmd=input(">>")
        
        print("Create a task by writing <create task> or <add task>")
        todoData["today"]=[]

        if cmd=="create task" or cmd=="add task":
            task_description=input("\nEnter your task description: ")
            scheduled_time=input("\nEnter scheduled time for the task: ")
            

            task={
                "description":task_description,
                "scheduled_time":scheduled_time
            }

            todoData["today"].append(task)

            with open("todoDB.json","w") as f:
                json.dump(todoData,f,indent=4)
    
    elif "today" in list(todoData.keys()):
        # First print the existing tasks
        tasks=todoData["today"]
        username=todoData["name"]
        currDate=todoData["date"]
        print(f"Today is {date}")
        print(f"\nHey {username}, here are the tasks for your day\n")

        for task in tasks:
            print(f"\nTask number{tasks.index(task)+1}")
            print("\nTask Description: ",task["description"])
            print("\nScheduled time:",task["scheduled_time"])

        print("\n Create another task")
        cmd=input(">>")

        if cmd =="create task" or cmd=="add task":
            task_description=input("\nEnter your task description: ")
            scheduled_time=input("\nEnter your scheduled time: ")

            task={
                "description":task_description,
                "scheduled_time":scheduled_time
            }

            todoData["today"].append(task)

            with open("todoDB.json","r+") as f:
                f.seek(0)
                json.dump(todoData,f,indent=4)

            print("Task created successfully")
            print("If you want to add more task,type add task/create task")
            print("If you are done for now ,please type done")
            
        if cmd=="done" or cmd=="exit":
            print("Have a good day!!")
            break