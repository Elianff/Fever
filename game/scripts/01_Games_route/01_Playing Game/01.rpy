label playing_games01:
    scene bg screen
    show thermostat empty
    "You get up out of your bed, leaving the thermometer on your counter."
    "Oh boy oh boy, time to play some NightFort."
    "Cue the game!"
    show thermostat little
    "As you are entranced by the riveting gameplay of such an intricate game, you begin to feel a little hot."
    "Who knew playing games could make you sweat so hard?"
    "A little too hard...."
    "You started to fan yourself with your homework you didn’t do."
    "Was the AC even on?"

    menu: 
        "Turn the AC on.":
            jump pausing_game_01
        "Continue Playing":
            jump continue_playing_02
