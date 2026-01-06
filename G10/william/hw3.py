def celcius(f):
   returnedvalue = (f - 32) * (5/9)
   return returnedvalue

degree = float(input("Enter Fahrenheit: "))
retVal = celcius(degree)
print(retVal)