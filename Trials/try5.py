TopOfStack = -1
MaxSize = 20
Stack = [-1] * MaxSize

def Push(NewItem):
    global TopOfStack, Stack
    if TopOfStack < MaxSize - 1:
        TopOfStack += 1
        Stack[TopOfStack] = NewItem
        return 1
    else:
        return -1