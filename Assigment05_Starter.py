# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# RRoot,1.1.2030,Created started script
# EPark,8.6.2020,Added code to complete assignment 5, attempt #1
# EPark 8.7.2020 Attempt #2- managed to call file
# EPark 8.8.2020 Managed to store file but spent most of time trying to unravel the tuples, lists and dics
# EPark 8.9.2020 Got several options to work (including the save function)
# EPark 8.10.2020 Finalized run and failed to troubleshoot blank lines issue from text file
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt","r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"TaskID": lstRow[0], "Details":lstRow[1], "Priority":lstRow[2]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        objFile = open("ToDoList.txt", "a")
        t = input ("Assign an ID number for the task: ")
        d = input ("Briefly Describe the Task: ")
        p = input ("Is this a priority task? (y/n): ")
        dicRow={"TaskID":t,"Details":d,"Priority":p}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItem = str(input("type Task ID to remove:"))
        for row in lstTable:
            if row["TaskID"]== str(strItem):
                lstTable.remove(row)
                print("row removed")
            continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file

    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["TaskID"]) + ',' + str(row["Details"]) + ',' + str(row["Priority"]))
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print ("You are exiting the program.")
        break  # and Exit the program
