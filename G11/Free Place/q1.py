def calculate_grade(score):
    if score >= 90 and score <= 100:
        print("Your grade is A.")
    elif score >= 80 and score <= 89:
        print("Your grade is B.")
    elif score >= 70 and score <= 79:
        print("Your score is C.")
    elif score >= 60 and score <= 69:
        print("Your score is D.")
    elif score < 60:
        print("Your score is F.")
    else:
        print("You have entered an invalid score!")

number = int(input("Please enter you score: "))
while number != -1:
    calculate_grade(number)
    number = int(input("Please enter you score: "))
