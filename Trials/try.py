class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def talk(animal):
    print(animal.speak())
    
talk(Dog())  # Woof
talk(Cat())  # Meow