label bed_route_chase:
    scene bg office5
    show thermostat over
    "You ran out of the office door slamming it shut behind you."
    "Whatever that was, it WAS NOT YOUR MOM."
    "Your vision blurred, as the haze surrounded your peripheral vision."
    "You had to run. FAR."
    
    # time = the time the timer takes to count down to 0.
# timer_range = a number matching time (bar only)
# timer_jump = the label to jump to when time runs out


    $ time = 5
    $ timer_range = 5
    $ timer_jump = "too_slow01"
    show screen countdown
    menu:
        "Run to your room!":
            hide screen countdown
            jump bed_route_bedroom01
        "Run to the kitchen!":
            hide screen countdown
            jump bed_route_kitchen01
        "Run outside!":
            hide screen countdown
            jump bed_route_outside01



    
    
        