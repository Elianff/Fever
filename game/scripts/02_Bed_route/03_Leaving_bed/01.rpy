label leaving_bed01:
    $ bed_route_escaped = True
    "You give the bed a pointed glare."
    "All you wanted to do was nap."
    "You turn on the fan and cool down."
    show thermostat empty
    "Whew all better!"
    "So... no sleep.."
    "What else could you do?"
    menu:
        "Gluttony calls! Go to the kitchen." if kitchen_route_escaped == False:
            jump going_kitchen01
        "Hit game NightFort awaits.." if games_route_escaped == False:
            jump playing_games01
        "Let's check up on mom!" if bed_route_escaped & games_route_escaped & kitchen_route_escaped:
            jump good_ending01