## Dictionary and Nesting
## Grouping similar objects together and mark them tag, can be treated as a table (Key (like word), Value)
## Syntax = {Key: Value}
#
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# ## Retrieve an element form dictionary
# print(programming_dictionary["Bug"])
#
# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

## Empty dictionary and add element
# country_capitals = {}
#
# country_capitals["India"] = "Delhi"
# country_capitals["Germany"] = "Berlin"
# country_capitals["England"] = "London"
# print(country_capitals)
#
# ## Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# ## Edit an item in dictionary
# country_capitals["India"] = "New Delhi"
# print(country_capitals)
#
# ## Loop through a dictionary
# for key in country_capitals:
#     print(country_capitals[key])

## Coding Exercise
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
#     "Mark": 80,
#     "Jasmine": 70,
# }
#
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)

## Nesting - Putting one or more items inside another item
## nested_dictionary = {Key: [List] , Key2: {Dict}, ..}
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# # Nesting a list
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

#Nesting a dictionary within a dictionary
# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# print(travel_log)

# Nesting a dictionary in a list
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# ]
# print(travel_log)

## Coding Exercise --
country = input("Enter the country: ")
visits = int(input("Enter the number of visits: "))
list_of_cities = eval(input("Enter the list of cities visited: "))

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

    print(travel_log)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")