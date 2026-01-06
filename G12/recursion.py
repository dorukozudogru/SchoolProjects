def factorial(x):
    if x == 1:
        return 1
    else:
        a = x * factorial(x-1)
        return a
    
print(factorial(4))