def Push(variable):
    global TopOfStack
    if(TopOfStack == 19):
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = variable
        return 1
    
def Pop():
    global TopOfStack
    count = 0
    for i in range (20):
        if Stack[i] == -1:
            count += 1
    
    if count == 20:
        return -1
    else:
        returnVal = Stack[TopOfStack].strip()
        TopOfStack -= 1
        return returnVal
    
def ReadData(fileName):
    try:
        file = open(fileName)
        for line in file:
            returnValue = Push(line)
            if(returnValue == -1):
                return "Stack full"
        file.close()
    except:
        return -1
    
def Calculate():
    global Stack
    global TopOfStack
    total = Pop()
    total = int(total)
    isOperator = True
    popedOperator = 0
    temp = 0
    while(TopOfStack != -1):
        temp = Pop()
        if isOperator == False:
            popedData = int(temp)
            if popedOperator == "+":
                total = total + popedData
            elif popedOperator == "-":
                total = total - popedData
            elif popedOperator == "/":
                total = total / popedData
            elif popedOperator == "*":
                total = total * popedData
            elif popedOperator == "^":
                total = total ** popedData
            isOperator = True
                
        else:
            popedOperator = temp
            isOperator = False
            
    return total
    
    
    

Stack = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
TopOfStack = -1

fileName = input("Please enter a file name: ")
ReadData(fileName)
total = Calculate()
print("The final total is", total)

# File Name:
# G12/may-june-2025-42/StackData.txt