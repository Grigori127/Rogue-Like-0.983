label  mod_default_Variables:
    default CheatsEnabled = 1
    default R_Tan = 0
    default R_BodySuit = 0
    default R_HairColor = 0
    default R_Plugged = 0
    default R_BodySuitOff = 0
    default R_Accessory = 0
    default R_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, gloves? choker?, extra
    default K_Tan = 0
    default K_HairColor = 0
    default K_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, gloves? choker?, extra
    default K_Gloves = 0
    default K_Blindfold = 0
    default K_Headband = 0
    default K_Plugged = 0
    default K_Spank = 0
    default E_Tan = 0
    default E_HairColor = 0
    default E_DynamicTan = [0,0,0,0,0,0,0,0]  #controller, over, legs, chest, panties, gloves? choker?, extra
    default E_Gloves = 0
    default E_Blindfold = 0
    default E_Headband = 0
    default E_Plugged = 0
    default E_Spank = 0
    default E_LegsUp = 0

    default R_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    default K_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    default E_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    default L_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom8 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom9 = [0,0,0,0,0,0,0,0,0,0,0]

    default R_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default K_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default E_OutfitShame = [50,0,5,0,25,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default L_OutfitShame = [50,0,5,0,25,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0]

    return

label  mod_Save_Version:

    if len(R_OutfitShame) < 21:
        $ R_OutfitShame.append(0) #[15] 16
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)
        $ R_OutfitShame.append(0)

    if len(K_OutfitShame) < 21:
        $ K_OutfitShame.append(0) #[15] 16
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)
        $ K_OutfitShame.append(0)

    if len(E_OutfitShame) < 21:
        $ E_OutfitShame.append(0) #[15] 16
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)
        $ E_OutfitShame.append(0)

    if len(L_OutfitShame) < 21:
        $ L_OutfitShame.append(0) #[15] 16
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)
        $ L_OutfitShame.append(0)

    return