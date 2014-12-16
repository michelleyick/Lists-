#Michelle Yick
#16-12-2014
#Lists R&R. Task 5: Improving the code from task 1.

def get_data():
    name1 = input("Please enter a name for the first student:")
    name2 = input("Please enter a name for the second student:")
    name3 = input("Please enter a name for the third student:")
    name4 = input("Please enter a name for the fourth student:")
    name5 = input("Please enter a name for the fifth student:")
    name6 = input("Please enter a name for the sixth student:")
    name7 = input("Please enter a name for the seventh student:")
    name8 = input("Please enter a name for the eighth student:")

    #Put the names into a list:
    names = [name1,name2,name3,name4,name5,name6,name7,name8]
    return names
#Print the names out:
def display(names):
    #Prints it out:
    count = 0
    for each in names:
        count = count+1
        print("{0}.{1}".format(count,each))

#Get name that the user wants to edit and let them edit it. Display the newly edited list.
def edit(names):
    num_edit = int(input("Please enter number of name you want to edit:"))
    names[num_edit-1] = input("Please enter a new name:")
    #Prints new list out with name in right place:
    count = 0
    for each in names:
        count = count-1
        print("{0}.{1}".format(count,each))

#Main program - Editing a list of names:
def list_of_names():
    names = get_data()
    display(names)
    names = edit(names)
list_of_names()
    
