## Functions
## https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def my_function():
    print("Hello..")
    print("Bye..")


# execute/calling the function
my_function()

## reborg
# def turn_around():
#     turn_left()
#     turn_left()
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

## https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# def turn_around():
#     turn_left()
#     turn_left()
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for i in range(0, 6):
#     hurdle()

## While loops...

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()

    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()



