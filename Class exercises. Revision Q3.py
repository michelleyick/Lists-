#Michelle Yick
#01-01-2015
#Lists class exercises. Revision Q3:

#create a list of the 7 temperatures from sunday-saturday:
def temperatures():
    weekly_temperature=[20.7,23.4,24.5,24,23.8,19.7,20.1]
    total=20.7+23.4+24.5+24+23.8+19.7+20.1
    return total

def calculate_average_temperature(total):
    answer=total/7
    print("The average temperature of the 7 days is {0} degrees.".format(round(answer,2)))

def main():
    total=temperatures()
    answer=calculate_average_temperature(total)
main()

    
    
    
        
    

