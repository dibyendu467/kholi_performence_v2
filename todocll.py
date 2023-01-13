import json
from datetime import date

emptyDoc= False
while True:
    with open("todoDB.json","r")as f:
        todoData=json.load(f)
        # f=open("todoDB.json","r")
        # todoData=json.load(f)
        # print(todoData,type(todoData))

        currentDate= date.today()

        if len(todoData)==0:
            emptyDoc=True
            username=input("\nHii there!! Welcome to TodoCLT.Please enter your username:")
            todoData["name"]=username
            todoData["date"]=str(currentDate)
            print("\nCreate a task by writing<create task> or <add task>")
            cmd=input(">>")
            todoData["today"]=[]
            if cmd =="create task" or cmd =="add task":
                task_description=input ("\nEnter your task description:")
                scheduled_time=input("\nEnter schedule time for the task:")

                task={
                    "description":task_description,
                    "scheduled_time":scheduled_time
                }
                todoData["today"].append(task)
                with open("todoDB.json","w")as f:
                    json.dump(todoData,f,indent=4)
        elif "today" in list(todoData.keys()):
            # first print in  the existing task
            tasks=todoData["today"]
            username=todoData["name"]
            currDate=todoData["date"]
            print(f"Today is {date}")
            print(f"\nhey{username}, here are the task for your day\n")

            for task in tasks:
                print(f"\nTask number{tasks.index(task)+1}")
                print("\nTask description:",task["description"])
                print("\nschedule time:",task["scheduled_time"])
            print("\n Create another task")
            cmd=input(">>")
            if cmd =="create task" or cmd =="add task":
                task_description=input ("\nEnter your task description:")
                scheduled_time=input("\nEnter schedule time for the task:")

                task={
                    "description":task_description,
                    "scheduled_time":scheduled_time
                }
                todoData["today"].append(task)
                with open("todoDB.json","r+")as f:
                    f.seek(0)
                    json.dump(todoData,f,indent=4)

                print("task create  successful")
                print("if you want add more task,type add task/create task")
                print("if you are done , please type done ")
                # continue
                
            if cmd ==" done " or cmd == " exit ":
                print("Have a grate day!!")
                break