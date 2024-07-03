## Conditional Statements, Logical Operators
#
print("Welcome to the rollercoster ride!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")

print("***************")

height = float(input("What is your height in metres? "))
weight = int(input("What is your weight in kgs? "))

bmi = round(weight / (height * height), 5)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

print("***************")

year = int(input("Please enter the year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"So the year {year} is a leap year!")
        else:
            print(f"The year {year} is not a leap year!")
    else:
        print(f"So the year {year} is a leap year!")
else:
    print(f"The year {year} is not a leap year!")

print("***************")

print("Welcome to the rollercoster ride!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill price is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")

print("***************")

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want peperonni? Y or N ")
add_extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if add_extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")

print("***************")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

print("The Love Calculator is calculating your score...")
combined_name = name1 + name2
combined_name = combined_name.lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
first_digit = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

