first_num = int(input("Enter your first value: "))
second_num = int(input("Enter your second value: "))

int=first_num

while int <= second_num:
    if int%2==0:
        print(int, end="")
    int+=1