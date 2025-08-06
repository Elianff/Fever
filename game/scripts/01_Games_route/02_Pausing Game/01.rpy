label pausing_game_01:
    $ games_route_escaped = True
    scene bg wall
    show thermostat little
    "You get up from your chair and go check the wall thermostat."
    "That's odd. It was 68 degrees Fahreinheit. It wasn't even that hot."
    "You went and turned your fan on."
    show thermostat empty
    "Ah much better."
    "Now where were we."
    "Playing games?"
    "Eh you were bored."
    "No more Nightfort."

    
    menu: 
        "That bed looks really appealing right about now." if bed_route_escaped == False:
            jump going_bed01
        "Gluttony calls! Let's go to the kitchen!" if kitchen_route_escaped == False:
            jump going_kitchen01
        "Let's check up on mom!" if bed_route_escaped & games_route_escaped & kitchen_route_escaped:
            jump good_ending01

    
