label continue_playing03:
    show thermostat full
    play music "audio/warm.wav" loop
    "You shrug it off."
    "Eh you were sick who cares."
    "Maybe you could skip tomorrow too."
    "You sit back down focusing on the screen,ignoring the heat."
    scene bg screen3
    show thermostat full
    "Until...you couldn’t ignore it anymore."
    "Your mouth was parched, your sweat clung to your back."
    "Why was it so hot?"
    "Your fevers were never like this, never this painful."
    "You couldn’t even pay attention to your game anymore."
    "Everything blurred together and every press of the mouse hurt."

    "It was so so so so so so so HOT."
    menu: 
        "Please stop playing. Please stop playing.":
            jump pause_game_02
        "Bro I need to get my XP for Nightfort.":
            jump continue_playing04