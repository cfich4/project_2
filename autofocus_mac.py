print("Welcome to the To-Do List App")

todo_list = []
    
def display_list():
    '''This function (that will contain an inside function) is structured to show the user
    their current tasks. This does this by checking if there are any tasks that have been
    already written. Further in the function, the priority status is created.'''
    if not todo_list:
        print("There are currently no tasks.")
        return
    
    print("Tasks: ")

    #I was unsure how to properly create the priortization part of the program. Using Chatgpt, 
    #it encouraged me to make a display_list function and taught me that it is possible
    #to make a function within a function. That being said, I decided if/elifs were the easier option.
    sortable_tasks = []
    for task in todo_list:
        status = task[0]
        priority = task[1]
        name = task[2]
        
        if (status == "[ ]"):
            status_value = 0
        elif (status == "[O]"):
            status_value = 1
        else: 
            # (status == "[X]")
            status_value = 2

        #using Chatgpt to assist with my bugs, I learned that I needed to parethenteses because
        #of the amount of tuples attached to append.
        sortable_tasks.append((status_value, priority, status, name))
    
    #Originally I didn't have this in my code as I didn't know the function .sort()
    #Chatgpt taught me that the .sort() ability sorts whats in there parentheses
    #In this context, .sort() sorts based on status value and priority
    sortable_tasks.sort()

    #It is more practical to start from 1 as that is where the program numbers will begin.
    index = 1
    for status_value, priority, status, name in sortable_tasks:
        print(f"{index}. {status} Priority {priority}: {name}")
        index += 1

    print()

def add_item(task):
    '''This function creates the ability to allow the user to create a new task after they enter
    'add' in the terminal.'''
#    todo_list.append(task)
    name = input("Please type out your new item: ")
    prioritizing = True
    while prioritizing:
        priority_input = input("1 is the highest priority")
        if priority_input.isdigit():
            priority = int(priority_input)
            prioritizing = False
        print("Please enter a number.")
    todo_list.append(("[ ]", priority, name, task))
       

def remove_list(list):
    '''This function is to remove the entire list at the user's command.'''
    todo_list.remove(list)

def prioritize_task():
    '''This function prioritizes tasks throughout the list by asking the user which number (it seems easier) they
    wish to prioritize. No inputs or returns, but it does include while loops. This function also checks to make sure
    the user inputted a functional number.'''
    display_list()
    
    prioritizing = True
    while prioritizing:
        task_input = input("Please enter the number of the task you would like to prioritize: ")
        if (task_input.isdigit() and 1 <= int(task_input) <= len(todo_list)):
            task_index = int(task_input) - 1
            print("Invalid task number.")
            prioritizing = False
    
    checking = True
    while checking:
        priority_input = input("New priority: ")
        if priority_input.isdigit():
            new_priority = int(priority_input)
            checking = False
        print("Invalid priority. Use a number.")

    status, task = todo_list[task_index]
    todo_list[task_index] = (status, new_priority, task)

def mark_done():
    display_list()
    checking = True
    while checking:
        choice = input("Task number to mark complete: ")
        if (choice.isdigit() and 1 <= int(choice) <= len(todo_list)):
            index = int(choice) - 1
            print("That number does not exist.")
            checking = False
        
    priority, name = todo_list[index]
    todo_list[index] = ("[X]", priority, name)
    
running = True
while running:
    print("Please enter 'add'(to add a task), 'delete' if you want to remove the list, or"
   " 'q' (to quit)") 
# or type a number to remove an item: ")
    answer = input("> ")
   # if the user enters 'q':
    if (answer == "q"):
       print(f"Goodbye. Good luck on your tasks of {answer}.")
       # TODO: this renders 'answer' instead of a given task
       running = False
    elif (answer == "delete"):
       display_list()
       remove_list(list)
   # this is to create a list for the user
#    elif (answer.isnumeric()):
#        index = int(answer) - 1
#        # to ensure a user is not trying to remove nothing from a list with no items
#        if (len(todo_list) == 0):
#            print("There is nothing to remove. Your list is empty.")
#        else:
#            # for removing a singular item
#            if (index >= 0 and index < len(todo_list)):
#                todo_list.pop(index)
#            else:
#                print("Sorry, there isn't an item with that number. ")
   # this processes the user's inputted item
    elif (answer == "add"):
       add_item(input("Please type out your new item: "))
       display_list()
   # if the user enters nothing
    else:
       print("Please enter an item or enter 'q' to quit.")


   # to number order and repeat the list to the user before they leave the program'
# for num in range(len(todo_list)):
#        print(f"{num + 1}. {todo_list[num]}")
    #might move to prioritization list