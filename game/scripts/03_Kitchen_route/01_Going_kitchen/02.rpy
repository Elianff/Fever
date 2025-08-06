label going_kitchen02:
    "You take your [chosen_food] to the table."
    "Yum Yummy Yum."
    "That was quite a meal."
    show thermostat little
    "Now that you finished, you realize your head was starting to hurt."
    "And now that you noticed...you also felt a little hot."
    "What was in that [chosen_food] ahahaha."
    "Maybe you needed to eat something cold."
    menu: 
        "Eat some ice cream!":
            jump leaving_kitchen01
        "Hmm but you really want some hot food...Eat a hot pocket instead :)":
            jump going_kitchen03

