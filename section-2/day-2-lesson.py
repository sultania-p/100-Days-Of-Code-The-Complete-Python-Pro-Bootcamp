# Data Types

word = "Hello"

print(word[0], word[4])
print(123_456_678)

###
num_char = len(input("What is your name?\n"))
print(type(num_char))
num_char = str(num_char)
print(type(num_char))
print("Your name has " + num_char + " characters")

num = 65
print(float(num))

###
two_digit_number = input("Enter the 2 digit number?\n")
if len(two_digit_number) != 2:
    print('Invalid input')
else:
    sum_of_digits = int(two_digit_number[0]) + int(two_digit_number[1])
    print(sum_of_digits)

num1 = 10
num2 = 5
result = num1 // num2
print(type(result))
print(result)

height = input("Enter the height?\n")
weight = input("Enter the weight?\n")

bmi = int(weight) // (float(height) ** 2)
print(bmi)

print(round(8 / 3, 2))

score = 20
height = 1.8
isWinning = True
print("your score is " + str(score))

# f-string -->> It helps to reduce the type conversions
print(f"Your score is {score} and height is {height}, you are winning is {isWinning}")

# Exercise
age = input("Enter your age?\n")
print(f"You have " + f"{52 * (90 - int(age))}" + " weeks left.")