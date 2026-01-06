def procedureOfMultiplying(multipliedNumber):
    result = multipliedNumber * 10
    print(multipliedNumber ,"* 10 =", result)
    
def functionOfDividing(divisionNumber):
    resultOfDivision = divisionNumber / 10
    return resultOfDivision

# Take the number from the user
number = int(input("Please enter a number: "))

# Call the procedure and send the number to the prosedure
procedureOfMultiplying(number)

# Call the function and send the number to the function
# and take the return value with 'resultOfFunction' variable
resultOfFunction = functionOfDividing(number)
print(number, "/ 10 =", resultOfFunction)