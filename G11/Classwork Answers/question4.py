students = [
    ["Alice", 85],
    ["Bob", 78],
    ["Charlie", 92],
    ["Diana", 88],
    ["Ethan", 95]
]
total = 0

# Find average score
for student in students:
    total += student[1]
average = total / len(students)
#total = sum([s[1] for s in students])

# Find max score
max_score = students[0][1]
for student in students:
    if student[1] > max_score:
        max_score = student[1]
#max_score = max([s[1] for s in students])

print("Top scorer(s):")
for name, score in students:
    if score == max_score:
        print(name)

print("\nStudents who scored above average:")
for name, score in students:
    if score > average:
        print(f"{name} ({score})")
