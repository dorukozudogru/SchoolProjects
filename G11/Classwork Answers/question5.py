def is_valid_password(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_digit = False
    
    #has_upper = any(char.isupper() for char in password)
    #has_digit = any(char.isdigit() for char in password)
    for char in password:
        # Manually check if character is uppercase
        if char >= 'A' and char <= 'Z':
            has_upper = True

        # Manually check if character is a digit
        if char >= '0' and char <= '9':
            has_digit = True

    if has_upper and has_digit:
        return True
    else:
        return False
    
    #return has_upper and has_digit

while True:
    pwd = input("Enter a password: ")
    if is_valid_password(pwd):
        print("Password is valid.")
        break
    else:
        print("Invalid password. Must be at least 8 characters long, contain a digit and an uppercase letter.")
