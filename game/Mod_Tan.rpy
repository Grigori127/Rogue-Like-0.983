﻿label  Mod_Tan(Girl = "Kitty", time = 5):
    if Girl == "Kitty":
        ch_k "Let's get tanned"
        #K_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, gloves? choker?, extra
        $ K_DynamicTan[0] = time #in days
        $ K_DynamicTan[1] = K_Over
        $ K_DynamicTan[2] = K_Legs
        $ K_DynamicTan[3] = K_Chest
        $ K_DynamicTan[4] = K_Panties
        call Wait(0,0)
        "Kitty sunbathes for a while"
        hide blackscreen onlayer black
        ch_k "I look amazing, don't I"

    return