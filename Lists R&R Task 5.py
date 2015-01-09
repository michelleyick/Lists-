#Michelle Yick
#16-12-2014
#Lists R&R. Task 5: Improving the code from task 1.

#Input names:
def get_names():
    names=[]
    count=0
    while count!=8:
        name=input("Please enter a name for person {0}:".format(count+1))
        names.append(name)
        count=count+1
    return names

#Print the names out:
def display_names(names):
    count=0
    for each in names:
        count=count+1
        print("{0}.{1}".format(count,each))

#Edit the names:
def edit_name(names):
    end_program=False
    value_entered=False

    while not value_entered:
        name_edit=int(input("Please enter the number of the name you want to edit or -1 to end the program:"))
        value_entered=True
    if name_edit==-1:
        end_program=True
    else:
        names[name_edit-1]=input("Enter a new name:")
    return end_program,names

#Main program:
def main():
    names=get_names()
    end_program=False
    while not end_program:
        display_names(names)
        end_program,names=edit_name(names)
main()
    
    
