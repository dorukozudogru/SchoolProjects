def Push(item):
    global TopOfStack
    if TopOfStack == 19:
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = item
        return 1

Stack = [-1] * 20
TopOfStack = -1

Push("Atharva")
Push("Yoongun")

print(Stack)
print(TopOfStack)
