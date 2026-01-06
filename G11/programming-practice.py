total = 0
number = int(input("Please enter a number: "))
length_num = len(str(number))

print(length_num)

while 1 <= length_num:
    total = total + (number // (10 ** (length_num-1)))
    number = number - (number // (10 ** (length_num-1))) * 10**(length_num-1)
    length_num-=1

print(total)