#Michelle Yick
#29-12-2014
#Lists class exercises. Revision Q1.

names=[]
for count in range(6):
    name=input("Enter a name")
    names.append(name)
count=0
for each in names:
    count = count+1
    print("{0}.{1}".format(count,each))


