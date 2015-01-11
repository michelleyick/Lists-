#Michelle Yick
#02-01-2014
#Lists class exercises. Development Q1.

#Get the random number from 0-10:
def random():
    import random 
    random_num=random.randint(0,10)
    return random_num

def countries_and_capitals(random_num):
    #Lists(capitals and the countries:
    country=["England","Taiwan","Germany","France","Japan","China","United States of America","Spain","Mexico","South Korea"]
    capital=["London","Taipei","Berlin","Paris","Tokyo","Beijing","Washington","Madrid","Mexico City","Seoul"]
    #Put countries/capitals in another list together:
    capitalsAndCountries=[country,capital]
    capitalsAndCountries[random_num][random_num]
    return capitalAndCountries

def ask_user(country,capital):
    #Ask for the capital guess:
    capitalGuess=input("What is the capital city of {0}".format(country))
    if capitalGuess==capital[random_num]:
        print("Well done. Your guess was correct")
    else:
        print("Incorrect guess")

def main():
    #Main program:
    random_num=random()
    country,capital,capitalAndCountries=countries_and_capitals(random_num)
    ask_user(country,capital)
main()

