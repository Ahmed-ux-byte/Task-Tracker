# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress
import time
import json
import sys
#variable
# Try to open and read the existing data from the file
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        if "ids" not in data or "tasks" not in data:  # Ensure the file contains the correct structure
            data = {"ids": [], "tasks": []}
except (FileNotFoundError, json.JSONDecodeError):
    data = {"ids": [], "tasks": []}  # If the file doesn't exist or is empty/corrupted, initialize with empty structure
id = 0
status = 'todo'
timenow1 = time.ctime(time.time())

argv1=sys.argv[1].lower()
try:
    argv2=sys.argv[2]
except:
    pass

def commands(id):
    if argv1 == "add":
        while True:
            id += 1
            if id in data["ids"]:
                '''id aleardy taken'''
                continue
            else:
                data5 = {"description" : str(argv2),
                        "id" : int(id),
                        "status" : status,
                        "createdAt" : timenow1,
                        "updateAt" : None
                        }
                data["ids"].append(id)  # Add the task ID to the list
                data["tasks"].append(data5)      # Add the task to the tasks list
                # Write the updated data back to the file
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                print(f"Task added: {argv2}")
                sys.exit(0)

    elif argv1 == "update" :
        global argv3
        argv3=sys.argv[3].lower()
        intargv2 = int(argv2)
        for lids in data["ids"]:
            if lids == intargv2:
                for task in data["tasks"]:
                    if task["id"] == intargv2:
                        task["description"] = argv3
                        task["updateAt"] = time.ctime(time.time())
                        with open("data.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                        print(f"Task Id : {argv2} /n Task Updated : {argv3}")
                        sys.exit(0)           
        print("Task not found")
        sys.exit(0)
    elif argv1 == "delete":
        intargv2 = int(argv2)
        for lids in data["ids"]:
            if lids == intargv2:
                data["ids"].remove(lids)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
        for lids in data["tasks"]:
            if lids["id"] == intargv2:
                data["tasks"].remove(lids)  # Remove the task from the list
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                sys.exit(0)
        print("Task not found")
        sys.exit(0)
            
    elif argv1 == "lists":
        print("Tasks:")
        for task in data["tasks"]:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}")
        sys.exit(0)
    elif argv1 == "list":
        if argv2 == "done" or argv2 == "todo" or argv2 == "in-progress":
            for tasks1 in data["tasks"]:
                if tasks1["status"] == argv2:
                    print(f"ID: {tasks1['id']}, Description: {tasks1['description']}, Status: {tasks1['status']}, Created At: {tasks1['createdAt']}")
            sys.exit(0)        
        else:
            intargv2 = int(argv2)
            for taskid in data["ids"]:
                if intargv2 == taskid:
                    for task in data["tasks"]:
                        if task["id"] == intargv2:
                            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}")
                            sys.exit(0)   
            print("Id Not Provided or Invalid or No task whit the status provided")
            sys.exit(0)

    elif argv1 == "mark-in-progress":
        intargv2 = int(argv2)
        for lids in data["ids"]:
            if intargv2 == lids:
                for task in data["tasks"]:
                    if task["id"] == intargv2:
                        task["status"] = "in-progress"
                        with open("data.json","w") as data_file:
                            json.dump(data,data_file, indent=4)
                        sys.exit(0)
        print("Task not found")
        sys.exit(0)
    elif argv1 == "mark-done":
        intargv2 = int(argv2)
        for lids in data["ids"]:
            if intargv2 == lids:
                for task in data["tasks"]:
                    if task["id"] == intargv2:
                        task["status"] = "done"
                        with open("data.json","w") as data_file:
                            json.dump(data,data_file, indent=4)
                        sys.exit(0)
        print("Task not found")
commands(id)
print("Wrong command")

