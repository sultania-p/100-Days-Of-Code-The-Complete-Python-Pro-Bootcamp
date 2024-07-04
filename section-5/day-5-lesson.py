# Debugging in Thonny
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# Exercise - Average Height
student_heights = input("Please enter the class student's height seperated by space.\n")
student_heights = student_heights.split(" ")

total_height = 0
total_students = 0

for n in student_heights:
    total_students += 1
print(f"Total students: {total_students}")

for i in range(0, len(student_heights)):
    total_height += int(student_heights[i])
print(f"Total height: {total_height}")

average_height = round(total_height / total_students)
print(f"The class average height: {average_height}")

# Exercise - High Score
student_scores = input("Please enter the students scores seperated by space.\n")
student_scores = student_scores.split(" ")
# print(student_scores)   # 10 20 15 30 20

max_score = 0
for score in student_scores:
    if max_score < int(score):
        max_score = int(score)

print(f"The highest score in the class is: {max_score}")

## For loop using range..
total = 0
count = 0
for number in range(1, 101):
    total += number
    count += 1
print(f"Average of number 1 to 100: {total/count}")

# Adding even number form 1 to n
target = int(input("Please enter your number:\n"))
total = 0

for number in range(1, target + 1):
    if (number % 2) == 0:
        total += number
print(f"Sum of even numbers between 1 and {target}: {total}")

## Exercise - Fizzbuzz
target = int(input("Please enter your number:\n"))

for number in range(1, target + 1):
    if (number % 3 == 0) and (number % 5) != 0:
        print("Fizz")
    elif (number % 3 != 0) and (number % 5) == 0:
        print("Buzz")
    elif (number % 3 == 0) and (number % 5) == 0:
        print("FizzBuzz")
    else:
        print(number)