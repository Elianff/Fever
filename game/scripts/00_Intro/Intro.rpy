# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.
label start:

    scene bg temp
    play music "audio/fever.wav" loop
    
    m "Tell me the truth now."
    m "You're not faking a fever just to get out of school, right?"
    "She looks at the child with one eyebrow raised."
    "She knew."
    c "No m'am!"
    "The child starts coughing, sneaking a peak at their mother."
    c "I am very, VERY sick. I can't go to school!"
    "The mother rolls her eyes with a gentle smile."
    m "Dont call me m'am."
    "She gently flicks the child’s head and ruffles their hair."
    m "Fine then. We wouldn’t want someone as sick as you infecting other students."
    "The child beamed. The plan was working."
    "The mother leans in to whisper something."
    m "But I expect you to go to school tomorrow and the day after. Got it?"
    "The child nods and the mother leaves the room with a shake of her head."

    "The child did it! No school!"

    scene bg start
    "Woah.. Who would have known. YOU'RE the child"
    "And you are now free to do whatever you want."
    "Fever? What fever?"
    "That was all part of your ploy."
    "It’s a wonder what dousing your head in hot water could do."
    "What should you do first with your new found freedom?"


    menu: 
        "Play games on your computer":
            jump playing_games01

        "Sleep in!":
            jump going_bed01
        
        "Sneak into the kitchen :)":
            jump going_kitchen01

    return
