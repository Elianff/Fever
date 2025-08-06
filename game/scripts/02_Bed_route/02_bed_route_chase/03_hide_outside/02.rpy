label let_yourself_suffocate02:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = "let_yourself_suffocate02"
    show screen countdown
    menu: 
        "Let yourself suffocate.":
            hide screen countdown
            jump suffocate03
        "That's the only choice.":
            hide screen countdown
            jump suffocate03
        "No matter how long you wait.":
            hide screen countdown
            jump suffocate03
        "It will end the same.":
            hide screen countdown
            jump suffocate03
