label leaving_kitchen01:
    $ kitchen_route_escaped = True
    show thermostat empty
    "Just holding the ice cream container was starting to cool you down."
    "You put some in a plate and began devouring it."
    "Thank goodness, you thought you were going to explode."
    "You didn't want to eat anything anymore."
    "Just the thought of eating something made your stomach woozy."
    "Time to get out of there."

    menu: 
        "Oh boy, you could use some rest right about now.." if bed_route_escaped == False:
            jump going_bed01
        "Games :)" if games_route_escaped == False:
            jump playing_games01
        "Let's check up on mom!" if bed_route_escaped & games_route_escaped & kitchen_route_escaped:
            jump good_ending01
        