######### Scope ##########

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

## Local Scope - Exists with in function
def drink_potion():
    # Variable inside function
    potion_strength = 2
    print(potion_strength)
drink_potion()
## NameError - Variable not defined under the scope

## Global Scope - Exists in global scope and available in the file
player_health = 10
def drink_potion():
    # Variable inside function
    print(player_health)
drink_potion()
# NameError - Variable not defined under the scope

## Namespace - Anything given a name is called Namespace and is valid in some scope
def parent_function():
    def child_function():
        print(player_health)

    child_function()    # can be called within the scope of the function
# child_function() # Error out as function scope is within the parent_function() only

## Block Scope
## Python does not have a block scope
## if else, for, while, :, ;, etc... does not create any scope on the variable, ONLY function can bound (indentation and colon) the variable
game_level = 3
enemies = ["Skeleton", "Zombies", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

## Modify variables defined in a global scope
enemies = 1
def increase_enemies():
    # enemies += 1        # enemies += 1 does not work as it expects it to be declared before assignment
    global enemies
    enemies += 2        # we are modifying the global variable "enemies" using the word global
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Instead of UPDATING global variables we should just return the variable ( may be add add or do something on that variable) instead

## Global Constants
# Turn these variables into CAPITAL case seperated with underscore (if we do not modify this anywhere in the program)
PI = 3.14159
URL = "https://www.google.com"
TWITTER = "@piyushs"
