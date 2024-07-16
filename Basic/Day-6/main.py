# My solution amd th comment below are being used avoid errors showing on my local machine

def turn_right():
    turn_left() # type: ignore
    turn_left() # type: ignore
    turn_left() # type: ignore 

while not at_goal(): # type: ignore
    if front_is_clear(): # type: ignore
        move() # type: ignore
        if not wall_on_right(): # type: ignore
            turn_right()
    else:
        turn_left() # type: ignore