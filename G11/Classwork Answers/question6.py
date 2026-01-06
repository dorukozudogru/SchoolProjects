#Solution 1
def initials(name):
    parts = name.strip().split()
    result = ""
    for part in parts:
        result += part[0].upper() + "."
    return result

#Another Solution
# def initials(name):
#     initials_output = ""
#     word_start = True

#     for ch in name:
#         if ch != " " and word_start:
#             initials_output += ch.upper() + "."
#             word_start = False
#         elif ch == " ":
#             word_start = True

#     return initials_output

full_name = input("Enter your full name: ")
print("Your initials are:", initials(full_name))