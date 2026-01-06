numbers = [0] * 10
removed_dup = []

for i in range(10):
    numbers[i] = int(input(f"Please enter number #{i + 1}:"))

for count in range(10):
    if numbers[count] not in removed_dup:
        removed_dup.append(numbers[count])

print("A new list that contains the same numbers but" +
      " with all duplicates removed is: ", removed_dup)