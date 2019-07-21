label  mod_hide_Emma_SexSprite:
    if renpy.showing("Emma_SexSprite"):
        hide Emma_SexSprite
    elif renpy.showing("Emma_Doggy"):
        hide Emma_Doggy
        if E_Gag == "ballgag":
            $ E_Gag = 0
    return