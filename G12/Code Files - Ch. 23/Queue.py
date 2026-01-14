# Initialize queue variables
front_of_queue_pointer = 0
end_of_queue_pointer = -1
number_in_queue = 0
max_queue_size = 5
my_queue = [None] * max_queue_size

def add_to_queue(newItem):
    global end_of_queue_pointer, number_in_queue, my_queue  # Declare these variables as global
    if number_in_queue < max_queue_size:
        end_of_queue_pointer = (end_of_queue_pointer + 1) % max_queue_size
        my_queue[end_of_queue_pointer] = newItem
        number_in_queue += 1

def remove_from_queue():
    global front_of_queue_pointer, end_of_queue_pointer, number_in_queue, my_queue  # Declare these variables as global
    if number_in_queue > 0:
        item = my_queue[front_of_queue_pointer]
        number_in_queue -= 1
        if number_in_queue == 0:
            front_of_queue_pointer = 0
            end_of_queue_pointer = -1
        else:
            front_of_queue_pointer = (front_of_queue_pointer + 1) % max_queue_size
        return item

# Example usage
add_to_queue("Z")
add_to_queue("A")

print(remove_from_queue())  # Output: Z
print(remove_from_queue())  # Output: A
