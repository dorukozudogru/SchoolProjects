import random  # Imports the 'random' module, which provides functions for generating random numbers

sampleString = "IPS Computer Science"  # A sample string
number = 45  # An integer value
deci = 3.1415  # A float value
stringNumber = "4567"  # A numeric string
stringFloat = "9.876"  # A float stored as a string

oldNumber = str(number)  # Converts the integer 45 to a string

print(int(deci))  # Converts the float to an integer (output: 3)

print(stringNumber + stringFloat)  # Concatenates two strings (output: '45679.876')
print(int(stringNumber) + float(stringFloat))  # Converts stringNumber to int and stringFloat to float, then adds them (output: 4576.876)

print(oldNumber + " this is the string")  # Concatenates string version of number with another string (output: '45 this is the string')
print(number, " this is the string")  # Prints multiple values separated by a space using commas

print(sampleString[2])  # Accesses the character at index 2 (3rd character) in the string (output: 'S')

print(chr(65))  # Converts Unicode code 65 to character (output: 'A')
print(ord("a"))  # Returns Unicode code point of character 'a' (output: 97)

print(len("abcasdaksdhbkajsdh"))  # Returns the length of the given string
print(len(sampleString))  # Returns the number of characters in sampleString

print(sampleString.lower())  # Converts all characters in the string to lowercase
print(sampleString.upper())  # Converts all characters in the string to uppercase

print(number, " is the number")  # Prints an integer and a string using comma separation

str1 = "AS & A Level"
str2 = "Computer Science"

print(str1 + str2)  # Concatenates two strings (output: 'AS & A LevelComputer Science')

print(sampleString[:5])  # Slices the string from the beginning to index 4 (output: 'IPS C')
print(sampleString[:-3])  # Slices the string from the beginning up to 3 characters from the end

randomNumber = random.randint(1,100)  # Generates a random integer between 1 and 100 (inclusive)
print(randomNumber)  # Prints the randomly generated number