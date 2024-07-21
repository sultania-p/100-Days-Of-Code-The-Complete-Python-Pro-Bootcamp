############DEBUGGING#####################
# http://www.pythontutor.com -- Debugging tool
# Thonny - debugging
# # Describe Problem
## i run form 1 to 19 and is never 20 and i == 20 never satisfies for the print never executes.
# def my_function():
#   for i in range(1, 20):    # make the final range to 21 to make the print work
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# when the randint generates 6 the index range becomes out of bound as the list is range 0 to 5 both inclusive
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)    # update the last index 6 to 5 to fix the bug
# print(dice_imgs[dice_num])

# # Play Computer
# if year = 1994, non of the condition is satisfied and nothing is printed. Fix by having "=" in either if or elif or add an else condition
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:   # elif year >= 1994 (one solution....)
#   print("You are a Gen Z.")

# # Fix the Errors
# age is string while comparison is with int. This will result in TypeError
# Indentation error..
# age = input("How old are you?") # make it int type     // age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")    # Add an f string to use the variable in the {}

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))   # This is a comparison instead of the assignment .. 0 != 200 so the result of this execution is False / 0
#     # but above line evaluates to False and words_per_page remains 0 as declared
# total_words = pages * word_per_page
# print(pages, word_per_page)
# print(total_words)

# #Use a Debugger
# Expectation is multiple each list item by 2 but the current code is indeed multiplying each item by 2 but appending only the last list item and thus b = [26]
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)   # This should be inside the for loop to work
  print(b_list)

mutate([1,2,3,5,8,13])