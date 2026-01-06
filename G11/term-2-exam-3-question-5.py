def TwoParts():
    totalA = 0
    totalB = 0
    number1 = -1
    number2 = -1
    count1 = 0
    count2 = 0
    
    while number1 != 0:
        number1 = int(input("Please enter a number: "))
        totalA = totalA + number1
        if number1 != 0:
            count1 += 1
    
    while number2 != 0:
        number2 = int(input("Please enter a number: "))
        totalB = totalB + number2
        if number2 != 0:
            count2 += 1
        
    print("The average of the first group is: ", totalA / count1)
    print("The average of the second group is: ", totalB / count2)
    
TwoParts()