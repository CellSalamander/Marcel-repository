#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
print("\n")
username = input("enter username: ")
password = input("enter password: ")

dict_users = {}

with open("user.txt","r") as file:
    for line in file:
        file_user = line[0:line.find(',')]
        file_password = line[line.find(',')+2:]
        dict_users[file_user] = file_password.strip()

    file.close()

if dict_users.get(username) == password:
    print("User found")
else:
    print("User not found")

        

while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - statistics
e - exit
: ''').lower()

    if menu == 'r':
        pass
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        if username == "admin":
            new_user = input("enter new username: ")
            new_pass = input("enter new password: ")
            confirm_pass = input("confirm password: ")
        
            if confirm_pass == new_pass:
                print("password confirmed")
            
                with open("user.txt",'a') as file:
                    file.write("\n" + new_user + ', ' + new_pass)
                    file.close()
            
                print("user added")
            else:
                print("password doesn't match")
        else:
            print("Only admins can register new users")
        

        

    elif menu == 'a':
        pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        
        user = input("for who is this task assigned: ")
        title = input("title of task: ")
        description = input("description of task: ")
        due_date = input("due date of task (y-m-d): ")
        current_date = datetime.today().strftime('%Y-%m-%d')
        
        with open("tasks.txt",'a') as file:
            file.write("\n" + user + ', ' + title + ', ' + description + ', ' + due_date + ', ' + current_date + ', No')
            file.close()
            
            

    elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        with open("tasks.txt",'r') as file:
            counter = 0
            for line in file:
                counter += 1
                user = line[:line.find(',')]
                marker = line.find(',')+2
                title = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                description = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                due_date = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                current_date = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                complete = line[marker:]
                
                print("Task "+str(counter))
                print("User: "+user)
                print("Title: "+title)
                print("description: : "+description)
                print("due_date: "+due_date)
                print("PostDate: "+current_date)
                print("Complete: "+complete)
                
            file.close()
                
                
                

    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        
        with open("tasks.txt",'r') as file:
            counter = 0
            for line in file:
                counter += 1
                user = line[:line.find(',')]
                if user == username:
                    pass
                else:
                    continue
                    
                marker = line.find(',')+2
                title = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                description = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                due_date = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                current_date = line[marker:line.find(',',marker)]
                marker = line.find(',',marker)+2
                complete = line[marker:]
                
                print("Task "+str(counter))
                print("User: "+user)
                print("Title: "+title)
                print("description: : "+description)
                print("due_date: "+due_date)
                print("PostDate: "+current_date)
                print("Complete: "+complete)
                
            file.close()
    
    elif menu == 's':
        
        if username == "admin":
            pass
        else:
            print("only admins can see stats")
            continue
        
        counter = 0
        with open("tasks.txt",'r') as file:
            for line in file:
                counter += 1
            file.close()
        
        print("Number of tasks: "+str(counter))
        
        counter = 0
        with open("user.txt",'r') as file:
            for line in file:
                counter += 1
            file.close()
        
        print("Number of Users: "+str(counter))

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")