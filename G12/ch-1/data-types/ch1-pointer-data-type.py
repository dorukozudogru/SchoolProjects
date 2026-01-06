# Simulated pointer behavior using list (mutable object)
class TIntegerPointer:
    def __init__(self, reference):
        self.ref = reference

    def get(self):
        # Prints the address of the reference number
        print(self)
        # Prints the number
        print(self.ref[0])
        return self.ref[0]

# Declare variables
Number1 = [200]  # Using list to simulate a reference (pointer)
Number2 = None

# Pointer assignment
MyIntegerPointer = TIntegerPointer(Number1)

# Dereference and compute
Number2 = MyIntegerPointer.get() * 2

# Output result
print(Number2)