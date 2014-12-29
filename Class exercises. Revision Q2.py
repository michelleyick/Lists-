#Michelle Yick
#29-12-2014
#Lists class exercises.  Revision Q2.

#Ask for the 6 names nad put it in a list:
def names():
    names=[]
    for count in range(6):
        name=input("Enter a name")
        names.append(name)
    count=0
    for each in names:
        count=count+1
        print("{0}.{1}".format(count,each))
    return names

#Slicing the list and displaying the sliced part:
def names_slicing(names):
    name_wanted=int(input("The number of the name you want"))
    print(names="[{0}]".format(name_wanted))

#Main program:
def list_of_names():
    names()
    names_slicing(names)
list_of_names()
