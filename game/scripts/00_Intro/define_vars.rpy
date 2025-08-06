define m = Character("Mom")
define c = Character("Child")
define o = Character("Officer")

$ chosen_food= "nothing"


default games_route_escaped = False
default kitchen_route_escaped = False
default bed_route_escaped = False

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
       
init:
    $ timer_range = 0
    $ timer_jump = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
