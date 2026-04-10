def function_hash(name):
    return len(name) % 10

size_of_hash_table = 10
hash_table = [None] * size_of_hash_table
collision_array = []
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

for name in names:
    returned_hash_number = function_hash(name)
    if hash_table[returned_hash_number] is None:
        hash_table[returned_hash_number] = name
    else:
        # print("Name couldn't be added to the hash table!")
        collision_array.append(name)

print()
print("Hash Table:", hash_table)
print("Collisions:", collision_array)

for count in range(len(hash_table)):
    if hash_table[count] is None:
        hash_table[count] = collision_array.pop(0)
        print()
        print("Hash Table:", hash_table)
        print("Collisions:", collision_array)

print()
print("Hash Table:", hash_table)
print("Collisions:", collision_array)