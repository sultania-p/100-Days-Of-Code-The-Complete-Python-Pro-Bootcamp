## Randomisation - Pseudo Random Number generation
## Module - Segment of code that can be split and worked independently and used in any other module
import random  # random module
#
# random_integer = random.randint(1, 100)
# print(random_integer)
#
# random_float = random.random()  # generates random float point number between 0 and 1
# print(random_float)
# print("Random number between 0 and 5: ", random_float * 5)

## Heads or Tails
# toss = random.randint(0, 1)
# if toss == 1:
#     print("You got a Head!")
# else:
#     print("Oh.. it's a Tail!")

## Lists and work on lists
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina",
#                      "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
#                      "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
#                      "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
#                      "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# print("First State - ", states_of_america[0])
# print("Last State = ", states_of_america[-1])

# states_of_america[1] = "Pencilvinia"    # update an item of list
# states_of_america.append("Alaska")      # Add an item in list
# states_of_america.extend(["Maine", "Connecticut", "Michigan"])  # extend a list with multiple items
# states_of_america.insert(2, "Colorado")     # inserts an item at i position
# states_of_america.pop()     # pops out a list item from end

# print(states_of_america)
# print(states_of_america[49])
#
# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states - 1])


## Exercise - Banker Roulette
# import random
#
# names_string = input("Please enter the names in the format.. name1, name2, name3,.. so on.\n")
# names = names_string.split(", ")
# names_count = len(names)
#
# random_number = random.randint(0, names_count - 1)
# print(f"{names[random_number]} is going to buy the meal today!")

## Nested List
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[1][1])
# fruits[-1] = "Mango"    # Updates the list with the item at the i index
# print(fruits)

## Exercise - Treasure Map ..
line1 = ["⬜", "⬜", "⬜"]
line2 = ["⬜", "⬜", "⬜"]
line3 = ["⬜", "⬜", "⬜"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?\n")
# Write your code below this row 👇
# print(map)
column = position[0].upper()
row = position[1]

column_index = ["A", "B", "C"]
column = column_index.index(column)
row = int(row) - 1

print(f"Row - {row}, Column - {column}")
map[row][column] = "X"

print(f"{line1}\n{line2}\n{line3}")
