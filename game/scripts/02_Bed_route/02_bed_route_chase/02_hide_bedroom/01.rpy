label bed_route_bedroom01:
    "You're going...back to the bed?"
    "Back to where this started?"
    "When you run into the bedroom, you look for somewhere to hide."
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'too_slow01'
    show screen countdown
    menu:
        "The bed":
            hide screen countdown
            jump bed_route_bedroom02
        "Jump. Out. The. Window.":
            hide screen countdown
            jump bed_route_bedroom03

    return