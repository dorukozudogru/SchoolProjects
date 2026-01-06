num = 0
count = 0
total = 0

while count < 5:
    num = int(input("Please enter a number: "))
    # total = total + num
    total += num
    count += 1
    
print("The total of the numbers you've entered is", total)