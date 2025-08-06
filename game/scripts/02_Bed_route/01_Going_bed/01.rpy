label going_bed01:
    scene bg bed
    show thermostat empty
    "Hells yeah. You get to sleep in. How great is that."
    "You plop yourself into bed and immediately pass out."
    scene bg black
    show thermostat little
    "Instead of sweet dreams, you saw hot flashes."
    scene bg haze
    show thermostat little
    "A perpetual blur similar to heat waves."
    "Suffocating. Couldn't breath."
    scene bg stressbed
    show thermostat little
    "And you wrenched yourself awake."
    "Sheets clinging to your body, you wipe the sweat off."
    "What was that?"

    menu: 
        "You don't think you want to find out! Let's do something else!":
            jump leaving_bed01
        "Who cares. Go back to sleep.":
            jump going_bed02