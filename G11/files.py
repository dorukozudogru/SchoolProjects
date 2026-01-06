# Open the file "files-g11.txt" in write mode ("w") — this creates the file if it doesn't exist,
# or overwrites it if it does.
file = open("G11/files-g11.txt", "w")
# Write a single line of text to the file
file.write("This is a line for Computer Science G11 Lesson")
# Close the file to save changes and free system resources
file.close()

# Open the same file in read mode ("r")
file = open('G11/files-g11.txt', 'r')
# Read the entire content of the file into a variable
readContent = file.read()
# Close the file after reading
file.close()
# Print the content read from the file to the console
print(readContent)

# Open the file again, this time in append mode ("a") to add new content without overwriting existing data
file = open("G11/files-g11.txt", "a")
# Add a new line of text at the end of the file
file.write("\nThis line has been added using Pyhton!")  # Note: "Python" is misspelled as "Pyhton"
# Close the file after appending
file.close()