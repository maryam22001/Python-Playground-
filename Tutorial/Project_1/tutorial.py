# 1-Car Game
'''
command = ""
while command.lower() != "quit":
    command = input("> ").lower:
    if command =="start":
    print("Gooooooooo")
    elif command == "stop":
    print("Stopping")
    elif command =="help":
        print("""
   start : to start the game
   stop:to stop the game
   quit to quit     
        """        )
'''
#2-Using nested loops I need to draw this shape
'''
XXXXX
XX
xxxxx
xx
xx
'''
'''
nums=[5,2,5,2,2]
for x_count in nums:
    output=''
    for count in range(x_count):
        output+='x'
        print(output)
'''


#3-Lists:
'''
what is lists?
Lists are a collection of items that can be 
of any data type, including numbers, strings,
 or even other lists. They are ordered,
 mutable (changeable), and allow duplicate elements. 
 Lists are defined using square brackets [].
# Example of a list in Python   
my_list = [1, 2, 3, "apple", "banana", [4, 5]]
'''
'''

names = ["John", "Jane", "Doe", "Smith"]
print(names[2:]) # Output: ['Doe']
print(names[0:2])  # Output: ['John', 'Jane']
print(names[1])  # Output: 'Jane'
print(names[:2]) # Output: ['John', 'Jane']
print(names[-1])  # Output: 'Smith'
names.append("Alice")  # Adding a new nameto the list
names.insert(0, "Bob")  # Inserting a name at the beginning
names.remove("Jane")  # Removing a name from the list
names.sort()  # Sorting the list in alphabetical order
names.reverse()  # Reversing the order of the list
names.clear()  # Clearing the list
names_copy = names.copy()  # Creating a copy of the list
#2.1 2DLists:
  2D Lists are lists of lists, allowing for a 
  grid-like structure.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]  
 for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # New line after each row


'''

'''

#Delete the dublicates:
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
unique_numbers = [] # Create an empty list to store unique numbers
for num in numbers :
    if num not in unique_numbers:  # Check if the number is not already in the unique list
        unique_numbers.append(num)  # Add the number to the unique list
        print(unique_numbers)  # Output: [1, 2, 3, 4,
'''

#3-tubles:
'''
Tuples are similar to lists but are immutable (cannot be changed after creation).
They are defined using parentheses ().
# Example of a tuple in Python
my_tuple = (1, 2, 3, "apple", "banana")
# Example of tuple operations
my_tuple = (1, 2, 3, "apple", "banana")

print(my_tuple[0])  # Output: 1
print(my_tuple[1:3])  # Output: (2, 3)
print(my_tuple[-1])  # Output: 'banana'
print(len(my_tuple))  # Output: 5
# Tuples are immutable, so we cannot change them
'''
#4-unpaking features:
'''
# Unpacking allows you to assign the elements of a
#  tuple to multiple variables in a single line.
coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpacking the tuple into variables
this is exactly like:
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(f"x: {x}, y: {y}, z: {z}")  # Output: x: 10, y: 20, z: 30


'''
#5-Dictionaries:
'''Dictionaries are collections of key-value pairs,
where each key is unique and maps to a value.   
They are defined using curly braces {}.
# Example of a dictionary in Python
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
# Adding a new key-value pair
my_dict["country"] = "USA"  # Adding a new key-value pair
# Removing a key-value pair
my_dict.pop("age")  # Removing the key 'age'
# Clearing the dictionary
my_dict.clear()  # Removing all key-value pairs

'''
#6-Emojis:
'''
# Emojis can be represented using Unicode characters.
# Example of using emojis in Python
print("Hello, World! 🌍😊")  # Output: Hello, World! 
🌍😊
emojis = {
    "smile": "😊",
    "heart": "❤️",
    "thumbs_up": "👍",
    "fire": "🔥"
}
message=input(">")
for word in message.split():
    print(emojis.get(word, word), end=" ")
'''
#7-Functions:
''' Functions are reusable blocks of code that perform a specific task. 
They can take inputs (parameters) and return outputs (return values).
>breaking the code into smaller managable chunks 
# Example of a function in Python
def greet(name):
    """This function greets a person with their name."""
    print(f"Hello, {name}!")
greet("Alice")  # Output: Hello, Alice!
# Function with parameters and return value
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b
result = add(5, 3)  # result will be 8
print(f"The sum is: {result}")  # Output: The sum is: 8

#keyword arguments:
def describe_person(name, age, city="Unknown"):
    """This function describes a person with their name, age, and city."""
    print(f"{name} is {age} years old and lives in {city}.")
describe_person("Alice", 30)  # Output: Alice is 30 years old and lives in Unknown.
describe_person("Bob", 25, "New York")  # Output: Bob is 25 years old and lives in New York.

'''
#8-Exceptions:
''' Exceptions are errors that occur during the execution of a program.
They can be handled using try-except blocks to prevent the program from crashing.
# Example of handling exceptions in Python
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")
'''
#9-Classes:
''' Classes are blueprints for creating objects.
They encapsulate data and behavior in a single entity.
python doesnt have an empty class
# Example of a class in Python
class Dog:
    """This class represents a dog."""
    def __init__(self, name, age):
        """Constructor to initialize the dog's name and age."""
        self.name = name
        self.age = age

    def bark(self):
        """Method for the dog to bark."""
        print(f"{self.name} says Woof!")

    def get_age(self):
        """Method to get the dog's age."""
        return self.age

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 5)
my_dog.bark()  # Output: Buddy says Woof!
print(f"{my_dog.name} is {my_dog.get_age()} years old.")  # Output: Buddy is 5 years old.
'''
#10-constructor:
''' The constructor is a special method called when an object is created.
It initializes the object's attributes.
class Car:
    """This class represents a car."""
    def __init__(self, make, model, year):
        """Constructor to initialize the car's make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Method to display the car's information."""
        print(f"{self.year} {self.make} {self.model}")
# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()  # Output: 2020 Toyota Camry
'''
#11-Inheritance:
''' Inheritance allows a class to inherit attributes and methods from another class.
class Animal:
    """This class represents a generic animal."""
    def __init__(self, name):
        """Constructor to initialize the animal's name."""
        self.name = name

    def speak(self):
        """Method for the animal to speak."""
        print(f"{self.name} makes a sound.")
class Dog(Animal):

    """This class represents a dog, inheriting from the Animal class."""
    def speak(self):
        """Method for the dog to bark."""
        print(f"{self.name} says Woof!")
class Cat(Animal):
    """This class represents a cat, inheriting from the Animal class."""
    def speak(self):
        """Method for the cat to meow."""
        print(f"{self.name} says Meow!")
# Creating instances of the Dog and Cat classes
my_dog = Dog("Buddy")   
my_cat = Cat("Whiskers")
my_dog.speak()  # Output: Buddy says Woof!
my_cat.speak()  # Output: Whiskers says Meow!
'''
'''

class Person:
    def __init__(self):
        """Constructor to initialize the person's attributes."""
        self.name = "Maryam"
        self.age = 20
    def talk(self):
        print("Talking...")

Maryam = Person("Maryam")
print(Maryam.name)   # Output: Maryam
print(Maryam.age)    # Output: 30
Maryam.talk()  # Output: Talking...
'''
#12-Polymorphism:
''' Polymorphism allows different classes to 
be treated as instances of the same class through
 a common interface.
class Bird:
    """This class represents a generic bird."""
    def fly(self):
        """Method for the bird to fly."""
        print("The bird is flying.")
class Sparrow(Bird):
    """This class represents a sparrow, inheriting from the Bird class."""
    def fly(self):
        """Method for the sparrow to fly."""
        print("The sparrow is flying quickly.")
class Penguin(Bird):
    """This class represents a penguin, inheriting from the Bird class."""
    def fly(self):
        """Method for the penguin to fly."""
        print("Penguins can't fly, but they can swim!")
        
        
        '''
#12-Modules:
''' 
Modules are files containing Python code that 
can be imported and used in other Python programs.
this gives a better structure and reusability

# Example of importing a module
import math  # Importing the math module
print(math.sqrt(16))  # Output: 4.0

we can import specific functions or classes from a module

'''
#13-Packages:
'''
Packages are a way of organizing related modules 
into a directory hierarchy.  
They allow for better organization and modularity in larger projects.
# Example of creating a package : ecommerce package
'''

#14-Random Values:
'''
import random
random.random()

'''
#15-File Handling
# File handling allows you to read from and write to files on the disk.
'''
Example of file handling in Python:
from pathlib import Path
# Writing to a file 


'''