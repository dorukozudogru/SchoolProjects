numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Initialize max and min with the first element
maximum = numbers[0]
minimum = numbers[0]
total = 0

for num in numbers:
    total += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

average = total / len(numbers)

print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
