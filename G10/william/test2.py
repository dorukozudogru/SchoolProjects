while True:
    password = input("Enter a new password that has at least 12 characters: ")

    if len(password) >= 12:
        print ("Your password has met the requirements")
        break
    else:
        print("Your password has not met the requirements please try again")