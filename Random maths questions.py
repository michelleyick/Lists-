#Michelle Yick
#11-01-2015
#Lists controlled assessment. Task 1/2 guess:

#Import the numbers and the operations: 
def importRandomNumbersAndOperations():
    import random
    number1=random.randint(1,100)
    number2=random.randint(1,100)
    ways=["+","-","*","/"]
    operation=random.choice(ways)
    return number1,number2,operation
    
#Execute the calculation:
def execute_calculation(number1,number2,operation):
    if operation=="+":
        calc=number1+number2
    elif operation=="-":
        calc=number1-number2
    elif operation=="*":
        calc=number1*number2
    elif operation=="/":
        calc=number1/number2
    return round(calc,2)

#If answer is correct/ incorrect:
def input_numbers(number1,number2,operation):
    answer=float(input("Work out the answer to {0} {1} {2}. Round to 2 decimal places if needed.".format(number1,operation,number2)))
    correctAnswer=0
    calc=execute_calculation(number1,number2,operation)
    if answer==calc:
        print("Well done")
        correctAnswer=correctAnswer+1
    elif answer!=0:
        print("Wrong answer")
    return correctAnswer

#Main program:
def main():
    count=0
    correctAnswer=0
    for count in range(10):
        number1,number2,operation=importRandomNumbersAndOperations()
        calc=execute_calculation(number1,number2,operation)
        answer=input_numbers(number1,number2,operation)
    print("You got {0} out of 10 correct".format(correctAnswer))
main()
        
    
    
