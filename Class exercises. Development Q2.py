#Michelle Yick
#06-01-2015
#Lists class exercises. Development Q2:

#Get the random number from 0-10:
def random():
    import random 
    random_num=random.randint(0,10)
    return random_num
#Lists(capitals and the countries):
def list1():
    column1=["England","Taiwan","Germany","France","Japan","China","United States of America","Spain","Mexico","South Korea"]
    return column1
def list2 ():
    column2=["London","Taipei","Berlin","Paris","Tokyo","Beijing","Washington","Madrid","Mexico City","Seoul"]
    return column2

#Cut the list:
def cut_list1(column1,random_num):
    country=column1[random_num]
    return country
#Cut the list to get the capital(slicing+list of lists):
def cut_list2 (column2,random_num):
    capital=column2[random_num]
    return capital
def ask_user(country,capital):


    answer=input("What is the capital {0}: ".format(country))
    if answer==capital:
        print("correct")
    else:
        print("That is an incorrect guess")

#Main program:
count=0
for count in range(5):
    count=count+1
    print("You got {0} guesses right out of the 5 times".format(count))

    random_num=random()
    column1=list1()
    column2=list2()
    country=cut_list1(column1,random_num)
    capital=cut_list2(column2,random_num)
    ask_user(country,capital)

