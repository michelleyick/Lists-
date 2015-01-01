#Michelle Yick
#29-12-2014
#Lists class exercises.  Revision Q2.

#ask for the 6 names and put it in a list:
def get_names():
    names=[]
    count=0
    while count!=6:
        name=input("Please enter a name for person {0}:".format(count+1))
        names.append(name)
        count=count+1
    return names

#prints the names out:
def display(names):
    count=0
    for each in names:
        count=count+1
        print("{0}.{1}".format(count,each))

#slicing the list:
def names_section(names):
    names_slice_lower=int(input("The lower bound of the range that you wish to extract:"))
    names_slice_upper=int(input("The upper bound of the range that you wish to extract:"))
    total=names[names_slice_lower-1:names_slice_upper]
    print(total)

#main program
def main_program():
    names=get_names()
    total=names_section(names)
    display(names)
main_program()
    
    
