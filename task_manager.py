# imported the date class from datetime
from datetime import date
# user friendly formatting
BLUE = "\033[94m"
BOLD = "\033[1m"
# create empty lists to store the usernames and passwords
usernames_list = []
passwords_list = []

# open the "user.txt" file in reading and writing mode
with open("user.txt", "r+", encoding="utf-8") as l1:
    # iterated over each line in the file
    # split up the line into two variables using split() and strip() methods
    # used append() method to add variables to empty list
    for line in l1:
        users, passwords = line.strip("\n").split(", ")
        usernames_list.append(users)
        passwords_list.append(passwords)

    # prompted user to enter username
    login_user = input("Enter your username: ").lower()

    # used while loop to prompt user enter a valid username
    while login_user not in usernames_list:
        print("Invalid user name, please try again!")
        login_user = input("Enter your username: ").lower()

    # if username was correct, prompted user to enter a password
    login_password = input("Enter your passwords: ").lower()

    # used index() method to get the username entered in list
    verify = usernames_list.index(login_user)

    # used while loop to prompt user enter a valid password
    while login_password != passwords_list[verify]:
        print("Invalid password, please try again!")
        login_password = input("Enter your passwords: ").lower()

    # printed welcome message if password entered was correct
    print(f"Welcome! {login_user}")
    # present the menu to the user
    while True:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    ds - display statistics
    e - Exit
    : ''').lower()
        # if user entered 'r' then registration inputs displayed
        if menu == 'r':
            # only if the username is "admin" will they be able to register users
            if login_user == "admin":
                new_username = input("Enter a new username: ").lower()
                new_password = input("Enter a new password: ").lower()
                conformation = input("Confirm the password: ").lower()
                # if the new password == conformation then will open user.txt file in append mode
                # written the the new username and password into the user.txt file
                if new_password == conformation:
                    with open("user.txt", "a+", encoding="utf-8") as l2:
                        l2.write(f"{new_username}, {new_password}\n")
                # if password and conformation != then error message displayed
                # user prompted to input password and conformation again
                else:
                    print("Invalid input, Please try again!")
                    new_password = input("Enter a new password: ").lower()
                    conformation = input("Confirm the password: ").lower()
            else:
                print("You are not allowed to register users!")      
        # if user entered 'a' then tasks are added
        elif menu == 'a':
            # prompt user input task details
            user_task = input("Enter the username of the person who the task is assigned to: ").lower()
            title_task = input("Enter the title of a task: ").lower()
            desc_task = input("Enter a description of the task: ").lower()
            date_task = input("Enter the due date of the task - dd mm yyyy: ")
            complete = input("Has the task been completed:(yes/no): ")
            # used date.today() method to get the current date
            # then used strftime() method to get it into (dd mm yyyy) string format
            today = date.today()
            current_date = today.strftime("%d%m%Y")
            # opened task.txt file in append mode
            # wrote the task details to the file
            with open("tasks.txt", "a+", encoding="utf-8") as task:
                task.write(f"\n{user_task}, {title_task}, {desc_task}, {date_task}, {current_date}, {complete}")
        # if user entered 'va' in menu then all tasks displayed
        elif menu == 'va':
            # opened tasks.txt in reading mode
            with open("tasks.txt", "r+", encoding="utf-8") as l3:
                # read all lines in file
                data2 = l3.readlines()
                # iterated over the lines and split at the comma and space using split() method
                for line in data2:
                    split_line = line.split(", ")
                    output = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                    output += "\n"
                    output += f"{BOLD}{BLUE}Task:                 {split_line[1]}\n"
                    output += f"{BOLD}{BLUE}Assigned to           {split_line[0]}\n"
                    output += f"{BOLD}{BLUE}Date assigned:        {split_line[3]}\n"
                    output += f"{BOLD}{BLUE}Due date:             {split_line[4]}\n"
                    output += f"{BOLD}{BLUE}Task complete?        {split_line[5]}\n"
                    output += f"{BOLD}{BLUE}Task description:\n {split_line[2]}\n"
                    output += "\n"
                    output +="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                # printed the results in the format in output 2
                print(output)
        # if user entered 'vm' in menu then their tasks are displayed
        elif menu == 'vm':
            # opened the tasks.txt file in reading mode
            with open("tasks.txt", "r+", encoding="utf-8") as l4:
                # read all lines in file
                output = l4.readlines()
                # iterated over the lines and split at the commma and space
                for line in output:
                    split_data = line.split(", ")
                    # checked if the username entered == the user read from tasks file
                    output = ""
                    if login_user == split_data[0]:
                            output = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                            output += "\n"
                            output += f"{BOLD}{BLUE}Task:                 {split_data[1]}\n"
                            output += f"{BOLD}{BLUE}Assigned to           {split_data[0]}\n"
                            output += f"{BOLD}{BLUE}Date assigned:        {split_data[3]}\n"
                            output += f"{BOLD}{BLUE}Due date:             {split_data[4]}\n"
                            output += f"{BOLD}{BLUE}Task complete?        {split_data[5]}\n"
                            output += f"{BOLD}{BLUE}Task description:\n   {split_data[2]}\n"
                            output += "\n"
                            output += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                    # results printed similar to 'va' format
                    print(output)
        # if user entered "ds" display statistics only if user is "admin"
        elif menu == "ds":
            if login_user == "admin":
                # display menu only accessable by admin user
                display_stats = input('''Select one of the following Options below:
                    tn - View total number of tasks
                    un - View total number of users
                    e - Exit
                    : ''').lower()
                # open "tasks.txt" file in reading mode
                with open("tasks.txt", "r", encoding="utf-8") as tasks_read:
                    # use len() function to get number of read lines in file
                    task_nums = len(tasks_read.readlines())
                # used the len() function to get the number of users in the usernames_list
                user_nums = len(usernames_list)
                # created if and elif statements for the user inputs
                if display_stats == "tn":
                    print(f"{BLUE}{BOLD}Total number of tasks: {task_nums}")
                elif display_stats == "un":
                    print(f"{BOLD}{BLUE}Total number of users: {user_nums}")
                else:
                    print("You have exited the display statistics menu!")
                    exit()
            # if login_user != "admin" error message displayed
            else:
                print("Error! Not authorised to view this menu")
        # if user entered 'e' in menu
        elif menu == 'e':
            # exit message printed
            # exit() method = exited from loop
            print('Goodbye!!!')
            exit()
        # else if invalid input - error message printed
        else:
            print("You have made a wrong choice, Please Try again")