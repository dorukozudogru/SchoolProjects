# Define a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "subject": "Math"
}

# Access values using keys and print them
print("Name:", student_info["name"])
print("Age:", student_info["age"])
print("Grade:", student_info["grade"])
print("Subject:", student_info["subject"])

# Modify the value associated with the key "age"
student_info["age"] = 26

# Add a new key-value pair to the dictionary
student_info["city"] = "New York"

# Print the updated dictionary
print("Updated Student Info:", student_info)
