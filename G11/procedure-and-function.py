#Creating a Procedure
def InputPositiveNumber():
    number = int(input("Enter a positive number: "))
    while number < 0:
        number = int(input("Enter a positive number: "))
    print("You entered this number: ", number)
    print("You entered this number: " + str(number))
    
#Creating a Function
def InputPositiveNumber2():
    number = int(input("Enter a positive number: "))
    while number < 0:
        number = int(input("Enter a positive number: "))
    return number
    
#Calling a procedure
InputPositiveNumber()

#Calling a function
returningNumber = InputPositiveNumber2()
print("My returned number is: ", returningNumber)