age = int(input("Please enter your age: "))

if age < 12:
    print("You are a child!")

elif age >= 12 and age < 18:
    print("You are a teenager!")
    
else:
    print("You are an adult!")