front_of_queue_pointer = 0
end_of_queue_pointer = -1
number_in_queue = 0
max_queue_size = 5
my_queue = [None] * max_queue_size

def add_to_queue(newItem):
    global end_of_queue_pointer, number_in_queue
    if number_in_queue < max_queue_size:
        end_of_queue_pointer = end_of_queue_pointer + 1
        #ADDED: wrap around if at the end
        if end_of_queue_pointer == max_queue_size:
            end_of_queue_pointer = 0
        #END ADDED
        my_queue[end_of_queue_pointer] = newItem
        number_in_queue += 1
    else:
        print("Queue is full")

def remove_from_queue():
    global front_of_queue_pointer, end_of_queue_pointer, number_in_queue
    if number_in_queue > 0:
        item = my_queue[front_of_queue_pointer]
        my_queue[front_of_queue_pointer] = None  # Optional: Clear the slot
        number_in_queue -= 1

        if number_in_queue == 0:
            front_of_queue_pointer = 0
            end_of_queue_pointer = -1
        else:
            front_of_queue_pointer = front_of_queue_pointer + 1
            #ADDED: wrap around if at the end
            if front_of_queue_pointer == max_queue_size:
                front_of_queue_pointer = 0
            #END ADDED

        return item
    else:
        print("Queue is empty")

# Example usage
add_to_queue("Z")
print(my_queue)
add_to_queue("A")
print(my_queue)

print(remove_from_queue())
print(my_queue)

add_to_queue("B")
print(my_queue)
add_to_queue("C")
print(my_queue)
add_to_queue("D")
print(my_queue)
add_to_queue("E")
print(my_queue)

remove_from_queue()
remove_from_queue()
print(my_queue)