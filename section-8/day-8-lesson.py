# Caesar Cipher - Encryption
# functions, Arguments and Parameters

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()

# FUnctions with Inputs
# Something that is parsed while calling the function is called "Argument" -- ex: "Piyush"
# Name of the data that is parsed to function is called "Parameter" -- ex: name
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Piyush")
greet_with_name("Mike")

# FUnctions with more than one input
# While calling the function the arguments are called Positional Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Welcome to the city of {location}")
greet_with("Piyush", "Boston")

## Keyword Arguments - Adding the parameter name along with assignment while invoking the function -- >> **kwargs
def greet_with(name, age, department, location):
    print(f"Hello {name}")
    print(f"You are of {age} years")
    print(f"How does it feel like to work in {department}?")
    print(f"Welcome to the city of {location}")
greet_with(name="Piyush", location="Boston", age=12, department="Fulfilment Tech.")


# Coding Exercise --
import math

height = int(input("Enter the height of wall: "))
width = int(input("Enter the width of wall: "))
coverage_per_can = 5

def paint_calc(height, width, coverage):
    number_of_cans = math.ceil((height * width) / coverage)
    print(f"Number of cans require to paint the wall: {number_of_cans}")

paint_calc(width=width, height=height, coverage=coverage_per_can)   # Using keyword Arguments Kwargs**

# Exercise - Check whether a number is a prime number
n = int(input("Enter the number to check the prime: "))

def prime_checker(number):
    if number == 1:
        is_prime = False
    else:
        is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"The number {number} is a prime number.")
    else:
        print(f"The number {number} is not a prime number.")

prime_checker(number=n)