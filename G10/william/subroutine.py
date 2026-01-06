def Operations(william):
    william = william + 10
    william = william * 5
    william = william / 2
    william = william - 75
    return william

number = int(input("Please enter a number: "))

returnedValue = Operations(number)

print("Number 1: ", returnedValue)

number2 = int(input("Please enter the second number: "))

smth = Operations(number2)

print("Number 2: ", smth)