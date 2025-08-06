label going_kitchen01:
    scene bg kitchen
    show thermostat empty
    "You sneak into the kitchen, trying to avoid your mom."
    "You were DEFINITELY still sick in your bed."
    "DEFINITELY recovering."
    "You hear her on an online meeting, and take this oppurtunity to go into the kitchen."
    "Heh what should you take."
    "So many choices."
    

    menu: 
        "Cereal!":
            $ chosen_food = "cereal"
            jump going_kitchen02
        "Yogurt!":
            $ chosen_food = "yogurt"
            jump going_kitchen02
        "Banana!":
            $ chosen_food = "banana"
            jump going_kitchen02