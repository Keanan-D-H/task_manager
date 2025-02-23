#========== task_manager.py =============
# Keanan Hinchliffe April 2024
"""
A program where you must log in according to the login information in users.txt.
Once logged in you can choose to add a new user, add a new task, view all tasks and/or
view the tasks set to your username. 

Tasks are added to and read from tasks.txt.

"""

#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date, timedelta

#====FUNCTION DEFINITIONS====


def check_space_comma(string, character):
    """ 
    Removes commas, spaces or both from a string and returns the result.
    
    Args:
        sting (str): The inputted string that needs changing
        character (str): "," 2 2 or "both" to decide what to remove
        
    Returns:
        str: The resulting string
    """

    if character == "both":
        while string != string.replace(" ", "").replace(",",""):
            string = input("Your input should not contain spaces or commas:\n")
    elif character == ",":
         while string != string.replace(",",""):
            string = input("Your input should not contain commas:\n")
    else:
        while string != string.replace(" ",""):
            string = input("Your input should not contain spaces:\n")

    return string


def check_yes_no(answer):
    """
    Checks if the inputted string is either a yes or a no and asks for an
    input until it is then returns the result.

    Arg:
        answer (str) : a string

    Returns: 
        str: either "yes" or "no"        
    """
    while answer.lower() !='yes' and answer.lower() != 'no':
        answer = input ('Please only put in \'yes\' or \'no\':\n')
    return answer


def display_tasks(tasks):
    """
    Prints a list of lists of tasks in a readable way. 

    Arg:
        tasks (list of lists): A list of all the tasks 

    Returns:
    """
    # I found how to iterate over lists of lists at: 
    # https://www.geeksforgeeks.org/iterate-over-a-list-of-lists-in-python/
    for i, inner_list in enumerate(tasks):
        print("_____________________________________________________________")
        print("\nTask:\t\t\t" + tasks[i][1])
        print("Assigned to:\t\t" + tasks[i][0])
        print("Date assigned:\t\t" + tasks[i][3])
        print("Due date:\t\t" + tasks[i][4])
        print("Task Complete?\t\t" + tasks[i][5])
        print("Task description:\n  " + tasks[i][2])
        print("_____________________________________________________________")
    
    return


#====LOGIN SECTION====

# login_dict is the dictionary which holds the login information. 
login_dict = {}

# Try to open the file then add the username and password as a tuple
# to login_dict.
try: 
   with open("user.txt","r") as f:
    for line in f:
        # Only will record lines which have a username, password arrangement. 
        if line.count(", ") == 1:
            login = tuple(line.strip("\n").split(", "))
            username , password = login
            login_dict[username] = password

# If the file can not be found print an error message.       
except FileNotFoundError:
    print("File \"users.txt\" not found in your directory.")
    exit(1)

username = input("\nPlease enter your username:\n")
# While the username is not a valid username according to user.txt 
# The user will be repeatedly ask for a valid username.
while login_dict.get(username) == None:
        username = input("That is not a valid username. Please try again:\n")

password = input("\nPlease enter your password:\n")
# The password will be checked against the username and whilst not correct
# it will ask the user for the correct password.
while login_dict[username] != password :
        password = input("This password is incorrect. Please re-enter:\n")




while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''\nPlease select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
        
    else: 
        menu = input("""\nPlease select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: """).lower()

    # A string which is used to determine if the user wants to continue.
    carry_on = ""
    # A list of lists which contains all the tasks' information from "tasks.txt".
    all_tasks = []
    # Just the task information which is assigned to one user. 
    my_tasks = []
    # A counter for the number of tasks.
    task_counter = 0 



    # If the admin wishes to register a new user.
    if menu == 'r' and username == "admin":

        reg_username = input("\nPlease input the new username:\n")
        reg_username = check_space_comma(reg_username , "both")
        
        # Whilst the inputted username is already registered, the user will be
        # asked if they wish to carry on registering a new user. If they don't
        # they will skip this registering phase of the loop. If they do, they 
        # will be asked for a new username to register.
        while login_dict.get(reg_username) != None:

            carry_on = input("That username is already registered. Would"
                             +" you like to register a different user?" + 
                             " (yes or no)\n")
            carry_on = check_yes_no(carry_on)

            if  carry_on == "yes":
                reg_username = input("\nPlease enter a new username:\n")
                reg_username = check_space_comma(reg_username , "both")               

            else:
                break

        if carry_on == "no":
            continue  

        # Ask for a password for the new user and to confirm the password. 
        # If the passwords do not match they must enter another password and 
        # confirm it. 
        while True:    

            reg_password = input("\nPlease enter a password for " 
                                 + f"{reg_username}:\n")
            reg_password = check_space_comma(reg_password , "both")
            confirm_password = input("\nPlease re-enter password:\n")
            
            if reg_password != confirm_password:
                print("Passwords do not match!")

            else:
                break

        # Add to login dictionary so it can be checked on the next pass.        
        login_dict[reg_username] = reg_password

        # Add the registered username and password to "user.txt" file.
        with open("user.txt", "a") as file:

            file.write(f"\n{reg_username}, {reg_password}") 


    # If the user wishes to add a task.
    elif menu == 'a':
        
        while True:

            if carry_on == "no":
                break
        
            task_person = input("\nTo whom are you assigning this task?\n")
            # If the person is not registered, ask if the user wants to 
            # assign a task to someone who is registered. If yes ask for a
            # registered user. If not they skip the assigning part of the loop.
            if login_dict.get(task_person) == None:
                carry_on = input("You may only assign tasks to registered" +
                                 " users. \nWould you like to assign a task"
                                 + "to a registered user?\n")
                carry_on = check_yes_no(carry_on)

            else:
                break

        if carry_on == "no":
            continue

        task_title = input("\nWhat would you like to call this task?\n")
        task_title = check_space_comma(task_title , ",")

        task_description = input("\nPlease enter a description of the task:\n")
        task_description = check_space_comma(task_description , ",")

        task_length = input("\nHow long should the task take? (Days)\n")

        # Check the task_length inputted can be cast to an int.
        while True:
            try:
                task_length = int(task_length)
                break

            except:
                task_length = input("Please only enter a whole number!\n")

        # Record todays date and the date the assignment should be complete.
        task_set_date = date.today()
        task_due_date = task_set_date + timedelta(days = task_length)

        # convert the dates to format (day mon year).
        task_set_date = task_set_date.strftime("%d %b %Y")
        task_due_date = task_due_date.strftime("%d %b %Y")

        # Add the task to the file "tasks.txt".
        with open("tasks.txt", "a") as file: 

            file.write(f"\n{task_person}, {task_title}, {task_description}"+ 
                       f", {task_set_date}, {task_due_date}, No")
        

    # If the user wishes to view all the tasks.
    elif menu == 'va':

        try:
            with open("tasks.txt", "r") as file:
                # Read and record the details for each task in a list then 
                # put those lists in the all_tasks list.
                for line in file:

                    # Only records line which has the correct amount of details.
                    if line.count(", ") == 5: 
                        task_detail = line.strip("\n").split(", ")
                        all_tasks.append(task_detail)
        
        except:
            print("""\nFile \"tasks.txt\" not found in your directory.
You will not be able to use the \'va\' or \'vm\' options.""")
            continue

        display_tasks(all_tasks)
        

    # If the user wishes to view their tasks.
    elif menu == 'vm':

        try:
            with open("tasks.txt", "r") as file:

                # Read and record the details for a task if they pertain
                # to the user. 
                for line in file:

                    if line.count(", ") == 5:
                        task_detail = line.strip("\n").split(", ")
                        # Only add tasks set for username to my_task
                        if task_detail[0] == username:
                            my_tasks.append(task_detail)
            
        except:
            print("""\nFile \"tasks.txt\" not found in your directory.
You will not be able to use the \'va\' or \'vm\' options.""")
            continue

        display_tasks(my_tasks)


    elif menu == "ds" and username == "admin":

        with open("tasks.txt", "r") as file:

            for line in file: 

                if line.count(", ") == 5:
                    task_counter += 1
    
        print("_____________________________________________________________")
        print(f"\nNumber of tasks:\t{task_counter}")
        print(f"Number of users:\t{len(login_dict)}")
        print("_____________________________________________________________")
            


    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    else:
        print("You have entered an invalid input. Please try again")





