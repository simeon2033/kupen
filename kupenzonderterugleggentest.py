import random
roundnm = 0 # variabelen resetten aan het begin van de simulatie
aantal1en = aantal2en = aantal3en = aantal4en = aantal5en = aantal6en = aantal7en = aantal8en = aantal9en = aantal10en = aantal11en = aantal12en = aantal13en = 4
stapel1 = [1]*aantal1en + [2]*aantal2en + [3]*aantal3en + [4]*aantal4en
stapel2 = [5]*aantal5en + [6]*aantal6en + [7]*aantal7en + [8]*aantal8en + [9]*aantal9en
stapel3 = [10]*aantal10en + [11]*aantal11en + [12]*aantal12en + [13]*aantal13en
player1bustcounter = 0
player1kupocounter = 0
player1kupercounter = 0
player1wincounter = 0
player1winpercentage = 0
player2bustcounter = 0
player2kupocounter = 0
player2kupercounter = 0
player2wincounter = 0
player2winpercentage = 0
dealerbustcounter = 0
dealerkupocounter = 0
dealerkupercounter = 0
dealerwincounterfrp1 = 0
dealerwincounterfrp2 = 0
dealerwinpercentage = 0
p1pushcounter = 0
p2pushcounter = 0
p1pushpercentage = 0
p2pushpercentage = 0
roundtest = 0
player1money = 0
player1inzet = 10
player2money = 0
player2inzet = 10
normalwinmultiplier = 2
kupokuperwinmultiplier = 4
player2active = True
diagnostic = False
winoutput = False
rounds = 10000000
roundtest = p1pushcounter + dealerwincounterfrp1 + dealerwincounterfrp2 + player1wincounter + p2pushcounter

def dice5total(): # 5 dobbelstenen functie
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def p1card_totalfunc(): # kaarten totaal speler 1
    return p1card_1 + p1card_2 + p1card_3 + p1card_4 + p1card_5 + p1card_6 + p1card_7 + p1card_8 + p1card_9 + p1card_10 + p1card_11 + p1card_12

def p2card_totalfunc(): # kaarten totaal speler 2
    return p2card_1 + p2card_2 + p2card_3 + p2card_4 + p2card_5 + p2card_6 + p2card_7 + p2card_8 + p2card_9 + p2card_10 + p2card_11 + p2card_12

def dcard_totalfunc(): # kaarten totaal dealer
    return dcard_1 + dcard_2 + dcard_3 + dcard_4 + dcard_5 + dcard_6 + dcard_7 + dcard_8 + dcard_9 + dcard_10 + dcard_11 + dcard_12

while roundnm < rounds: # hoeveelheid rondes
    roundnm = roundnm + 1 # variabelen naar 0 aan het begin van elke ronde
    player1money = player1money - player1inzet
    if player2active == True:
        player2money = player2money - player2inzet
    p1card_1 = p1card_2 = p1card_3 = p1card_4 = p1card_5 = p1card_6 = p1card_7 = p1card_8 = p1card_9 = p1card_10 = p1card_11 = p1card_12 = p2card_1 = p2card_2 = p2card_3 = p2card_4 = p2card_5 = p2card_6 = p2card_7 = p2card_8 = p2card_9 = p2card_10 = p2card_11 = p2card_12 = dcard_1 = dcard_2 = dcard_3 = dcard_4 = dcard_5 = dcard_6 = dcard_7 = dcard_8 = dcard_9 = dcard_10 = dcard_11 = dcard_12 = 0
    aantal1en = aantal2en = aantal3en = aantal4en = aantal5en = aantal6en = aantal7en = aantal8en = aantal9en = aantal10en = aantal11en = aantal12en = aantal13en = 4
    player1stay = 0
    player1lost = 0
    player1win = 0
    player2stay = 0
    player2lost = 0
    player2win = 0
    dealerlostfrp1 = 0
    dealerlostfrp2 = 0
    dealerwinfrp1 = 0
    dealerwinfrp2 = 0
    dealerstay = 0
    pushp1 = 0
    pushp2 = 0
   
    dice_total = dice5total() # kaart 1
    if dice_total <= 15:
        p1card_1 = random.choice(stapel1)
        if p1card_1 == 1 and aantal1en > 0:
            aantal1en = aantal1en - 1
        elif p1card_1 == 2 and aantal2en > 0:
            aantal2en = aantal2en - 1
        elif p1card_1 == 3 and aantal3en > 0:
            aantal3en = aantal3en - 1
        elif p1card_1 == 4 and aantal4en > 0:
            aantal4en = aantal4en - 1
        if player2active == True:
            p2card_1 = random.choice(stapel1)
            if p2card_1 == 1 and aantal1en > 0:
                aantal1en = aantal1en - 1
            elif p2card_1 == 2 and aantal2en > 0:
                aantal2en = aantal2en - 1
            elif p2card_1 == 3 and aantal3en > 0:
                aantal3en = aantal3en - 1
            elif p2card_1 == 4 and aantal4en > 0:
                aantal4en = aantal4en - 1
        dcard_1 = random.choice(stapel1)
        if dcard_1 == 1 and aantal1en > 0:
            aantal1en = aantal1en - 1
        elif dcard_1 == 2 and aantal2en > 0:
            aantal2en = aantal2en - 1
        elif dcard_1 == 3 and aantal3en > 0:
            aantal3en = aantal3en - 1
        elif dcard_1 == 4 and aantal4en > 0:
            aantal4en = aantal4en - 1
    elif dice_total >= 20:
        p1card_1 = random.choice(stapel3)
        if p1card_1 == 10 and aantal10en > 0:
            aantal10en = aantal10en - 1
        elif p1card_1 == 11 and aantal11en > 0:
            aantal11en = aantal11en - 1
        elif p1card_1 == 12 and aantal12en > 0:
            aantal12en = aantal12en - 1
        elif p1card_1 == 13 and aantal13en > 0:
            aantal13en = aantal13en - 1
        if player2active == True:
            p2card_1 = random.choice(stapel3)
            if p2card_1 == 10 and aantal10en > 0:
                aantal10en = aantal10en - 1
            elif p2card_1 == 11 and aantal11en > 0:
                aantal11en = aantal11en - 1
            elif p2card_1 == 12 and aantal12en > 0:
                aantal12en = aantal12en - 1
            elif p2card_1 == 13 and aantal13en > 0:
                aantal13en = aantal13en - 1
        dcard_1 = random.choice(stapel3)
        if dcard_1 == 10 and aantal10en > 0:
            aantal10en = aantal10en - 1
        elif dcard_1 == 11 and aantal11en > 0:
            aantal11en = aantal11en - 1
        elif dcard_1 == 12 and aantal12en > 0:
            aantal12en = aantal12en - 1
        elif dcard_1 == 13 and aantal13en > 0:
            aantal13en = aantal13en - 1
    else:
        p1card_1 = random.choice(stapel2)
        if p1card_1 == 5 and aantal5en > 0:
            aantal5en = aantal5en - 1
        elif p1card_1 == 6 and aantal6en > 0:
            aantal6en = aantal6en - 1
        elif p1card_1 == 7 and aantal7en > 0:
            aantal7en = aantal7en - 1
        elif p1card_1 == 8 and aantal8en > 0:
            aantal8en = aantal8en - 1
        elif p1card_1 == 9 and aantal9en > 0:
            aantal9en = aantal9en - 1
        if player2active == True:
            p2card_1 = random.choice(stapel2)
            if p2card_1 == 5 and aantal5en > 0:
                aantal5en = aantal5en - 1
            elif p2card_1 == 6 and aantal6en > 0:
                aantal6en = aantal6en - 1
            elif p2card_1 == 7 and aantal7en > 0:
                aantal7en = aantal7en - 1
            elif p2card_1 == 8 and aantal8en > 0:
                aantal8en = aantal8en - 1
            elif p2card_1 == 9 and aantal9en > 0:
                aantal9en = aantal9en - 1
        dcard_1 = random.choice(stapel2)
        if dcard_1 == 5 and aantal5en > 0:
            aantal5en = aantal5en - 1
        elif dcard_1 == 6 and aantal6en > 0:
            aantal6en = aantal6en - 1
        elif dcard_1 == 7 and aantal7en > 0:
            aantal7en = aantal7en - 1
        elif dcard_1 == 8 and aantal8en > 0:
            aantal8en = aantal8en - 1
        elif dcard_1 == 9 and aantal9en > 0:
            aantal9en = aantal9en - 1
   
    p1card_total = p1card_totalfunc()
    p2card_total = p2card_totalfunc()
    dcard_total = dcard_totalfunc()
    if dcard_1 < 4 and (dcard_1 < p1card_1 or dcard_1 < p2card_1): # wanneer moet de dealer stoppen
        dealerstay = 1
    if p1card_1 < 4 and p1card_1 < dcard_1: # waneer moet de speler stoppen
        player1stay = 1
    if p2card_1 < 4 and p2card_1 < dcard_1: # waneer moet de speler stoppen
        player2stay = 1
   
    if (p1card_1 != 1 and dcard_1 != 1) or (p2card_1 != 1 and dcard_1 != 1): # kaart 2
        dice_total = dice5total()
        if dice_total <= 15:
            if player1stay == 0:
                p1card_2 = random.choice(stapel1)
                if p1card_2 == 1 and aantal1en > 0:
                    aantal1en = aantal1en - 1
                elif p1card_2 == 2 and aantal2en > 0:
                    aantal2en = aantal2en - 1
                elif p1card_2 == 3 and aantal3en > 0:
                    aantal3en = aantal3en - 1
                elif p1card_2 == 4 and aantal4en > 0:
                    aantal4en = aantal4en - 1
            if player2active == True and player2stay == 0:
                p2card_2 = random.choice(stapel1)
                if p2card_2 == 1 and aantal1en > 0:
                    aantal1en = aantal1en - 1
                elif p2card_2 == 2 and aantal2en > 0:
                    aantal2en = aantal2en - 1
                elif p2card_2 == 3 and aantal3en > 0:
                    aantal3en = aantal3en - 1
                elif p2card_2 == 4 and aantal4en > 0:
                    aantal4en = aantal4en - 1
            if dealerstay == 0:
                dcard_2 = random.choice(stapel1)
                if dcard_2 == 1 and aantal1en > 0:
                    aantal1en = aantal1en - 1
                elif dcard_2 == 2 and aantal2en > 0:
                    aantal2en = aantal2en - 1
                elif dcard_2 == 3 and aantal3en > 0:
                    aantal3en = aantal3en - 1
                elif dcard_2 == 4 and aantal4en > 0:
                    aantal4en = aantal4en - 1
        elif dice_total >= 20:
            if player1stay == 0:
                p1card_2 = random.choice(stapel3)
                if p1card_2 == 10 and aantal10en > 0:
                    aantal10en = aantal10en - 1
                elif p1card_2 == 11 and aantal11en > 0:
                    aantal11en = aantal11en - 1
                elif p1card_2 == 12 and aantal12en > 0:
                    aantal12en = aantal12en - 1
                elif p1card_2 == 13 and aantal13en > 0:
                    aantal13en = aantal13en - 1
            if player2active == True and player2stay == 0:
                p2card_2 = random.choice(stapel3)
                if p2card_2 == 10 and aantal10en > 0:
                    aantal10en = aantal10en - 1
                elif p2card_2 == 11 and aantal11en > 0:
                    aantal11en = aantal11en - 1
                elif p2card_2 == 12 and aantal12en > 0:
                    aantal12en = aantal12en - 1
                elif p2card_2 == 13 and aantal13en > 0:
                    aantal13en = aantal13en - 1
            if dealerstay == 0:
                dcard_2 = random.choice(stapel3)
                if dcard_2 == 10 and aantal10en > 0:
                    aantal10en = aantal10en - 1
                elif dcard_2 == 11 and aantal11en > 0:
                    aantal11en = aantal11en - 1
                elif dcard_2 == 12 and aantal12en > 0:
                    aantal12en = aantal12en - 1
                elif dcard_2 == 13 and aantal13en > 0:
                    aantal13en = aantal13en - 1
        else:
            if player1stay == 0:
                p1card_2 = random.choice(stapel2)
                if p1card_2 == 5 and aantal5en > 0:
                    aantal5en = aantal5en - 1
                elif p1card_2 == 6 and aantal6en > 0:
                    aantal6en = aantal6en - 1
                elif p1card_2 == 7 and aantal7en > 0:
                    aantal7en = aantal7en - 1
                elif p1card_2 == 8 and aantal8en > 0:
                    aantal8en = aantal8en - 1
                elif p1card_2 == 9 and aantal9en > 0:
                    aantal9en = aantal9en - 1
            if player2active == True and player2stay == 0:
                p2card_2 = random.choice(stapel2)
                if p2card_2 == 5 and aantal5en > 0:
                    aantal5en = aantal5en - 1
                elif p2card_2 == 6 and aantal6en > 0:
                    aantal6en = aantal6en - 1
                elif p2card_2 == 7 and aantal7en > 0:
                    aantal7en = aantal7en - 1
                elif p2card_2 == 8 and aantal8en > 0:
                    aantal8en = aantal8en - 1
                elif p2card_2 == 9 and aantal9en > 0:
                    aantal9en = aantal9en - 1
            if dealerstay == 0:
                dcard_2 = random.choice(stapel2)
                if dcard_2 == 5 and aantal5en > 0:
                    aantal5en = aantal5en - 1
                elif dcard_2 == 6 and aantal6en > 0:
                    aantal6en = aantal6en - 1
                elif dcard_2 == 7 and aantal7en > 0:
                    aantal7en = aantal7en - 1
                elif dcard_2 == 8 and aantal8en > 0:
                    aantal8en = aantal8en - 1
                elif dcard_2 == 9 and aantal9en > 0:
                    aantal9en = aantal9en - 1
   
        p1card_total = p1card_totalfunc()
        p2card_total = p2card_totalfunc()
        dcard_total = dcard_totalfunc()
        if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
            dealerstay = 1
        if p1card_total > 23: # waneer moet de speler 1 stoppen
            player1stay = 1
        if p2card_total > 23: # waneer moet speler 2 stoppen
            player2stay = 1
    
        if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 3
            dice_total = dice5total()
            if dice_total <= 15:
                if player1stay == 0:
                    p1card_3 = random.choice(stapel1)
                    if p1card_3 == 1 and aantal1en > 0:
                        aantal1en = aantal1en - 1
                    elif p1card_3 == 2 and aantal2en > 0:
                        aantal2en = aantal2en - 1
                    elif p1card_3 == 3 and aantal3en > 0:
                        aantal3en = aantal3en - 1
                    elif p1card_3 == 4 and aantal4en > 0:
                        aantal4en = aantal4en - 1
                if player2active == True and player2stay == 0:
                    p2card_3 = random.choice(stapel1)
                    if p2card_3 == 1 and aantal1en > 0:
                        aantal1en = aantal1en - 1
                    elif p2card_3 == 2 and aantal2en > 0:
                        aantal2en = aantal2en - 1
                    elif p2card_3 == 3 and aantal3en > 0:
                        aantal3en = aantal3en - 1
                    elif p2card_3 == 4 and aantal4en > 0:
                        aantal4en = aantal4en - 1
                if dealerstay == 0:
                    dcard_3 = random.choice(stapel1)
                    if dcard_3 == 1 and aantal1en > 0:
                        aantal1en = aantal1en - 1
                    elif dcard_3 == 2 and aantal2en > 0:
                        aantal2en = aantal2en - 1
                    elif dcard_3 == 3 and aantal3en > 0:
                        aantal3en = aantal3en - 1
                    elif dcard_3 == 4 and aantal4en > 0:
                        aantal4en = aantal4en - 1
            elif dice_total >= 20:
                if player1stay == 0:
                    p1card_3 = random.choice(stapel3)
                    if p1card_3 == 10 and aantal10en > 0:
                        aantal10en = aantal10en - 1
                    elif p1card_3 == 11 and aantal11en > 0:
                        aantal11en = aantal11en - 1
                    elif p1card_3 == 12 and aantal12en > 0:
                        aantal12en = aantal12en - 1
                    elif p1card_3 == 13 and aantal13en > 0:
                        aantal13en = aantal13en - 1
                if player2active == True and player2stay == 0:
                    p2card_3 = random.choice(stapel3)
                    if p2card_3 == 10 and aantal10en > 0:
                        aantal10en = aantal10en - 1
                    elif p2card_3 == 11 and aantal11en > 0:
                        aantal11en = aantal11en - 1
                    elif p2card_3 == 12 and aantal12en > 0:
                        aantal12en = aantal12en - 1
                    elif p2card_3 == 13 and aantal13en > 0:
                        aantal13en = aantal13en - 1
                if dealerstay == 0:
                    dcard_3 = random.choice(stapel3)
                    if dcard_3 == 10 and aantal10en > 0:
                        aantal10en = aantal10en - 1
                    elif dcard_3 == 11 and aantal11en > 0:
                        aantal11en = aantal11en - 1
                    elif dcard_3 == 12 and aantal12en > 0:
                        aantal12en = aantal12en - 1
                    elif dcard_3 == 13 and aantal13en > 0:
                        aantal13en = aantal13en - 1
            else:
                if player1stay == 0:
                    p1card_3 = random.choice(stapel2)
                    if p1card_3 == 5 and aantal5en > 0:
                        aantal5en = aantal5en - 1
                    elif p1card_3 == 6 and aantal6en > 0:
                        aantal6en = aantal6en - 1
                    elif p1card_3 == 7 and aantal7en > 0:
                        aantal7en = aantal7en - 1
                    elif p1card_3 == 8 and aantal8en > 0:
                        aantal8en = aantal8en - 1
                    elif p1card_3 == 9 and aantal9en > 0:
                        aantal9en = aantal9en - 1
                if player2active == True and player2stay == 0:
                    p2card_3 = random.choice(stapel2)
                    if p2card_3 == 5 and aantal5en > 0:
                        aantal5en = aantal5en - 1
                    elif p2card_3 == 6 and aantal6en > 0:
                        aantal6en = aantal6en - 1
                    elif p2card_3 == 7 and aantal7en > 0:
                        aantal7en = aantal7en - 1
                    elif p2card_3 == 8 and aantal8en > 0:
                        aantal8en = aantal8en - 1
                    elif p2card_3 == 9 and aantal9en > 0:
                        aantal9en = aantal9en - 1
                if dealerstay == 0:
                    dcard_3 = random.choice(stapel2)
                    if dcard_3 == 5 and aantal5en > 0:
                        aantal5en = aantal5en - 1
                    elif dcard_3 == 6 and aantal6en > 0:
                        aantal6en = aantal6en - 1
                    elif dcard_3 == 7 and aantal7en > 0:
                        aantal7en = aantal7en - 1
                    elif dcard_3 == 8 and aantal8en > 0:
                        aantal8en = aantal8en - 1
                    elif dcard_3 == 9 and aantal9en > 0:
                        aantal9en = aantal9en - 1
                    
            p1card_total = p1card_totalfunc()
            p2card_total = p2card_totalfunc()
            dcard_total = dcard_totalfunc()
            if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                dealerstay = 1
            if p1card_total > 23: # waneer moet de speler stoppen
                player1stay = 1
            if p2card_total > 23: # waneer moet speler 2 stoppen
                player2stay = 1
        
            if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 4
                dice_total = dice5total()
                if dice_total <= 15:
                    if player1stay == 0:
                        p1card_4 = random.choice(stapel1)
                        if p1card_4 == 1 and aantal1en > 0:
                            aantal1en = aantal1en - 1
                        elif p1card_4 == 2 and aantal2en > 0:
                            aantal2en = aantal2en - 1
                        elif p1card_4 == 3 and aantal3en > 0:
                            aantal3en = aantal3en - 1
                        elif p1card_4 == 4 and aantal4en > 0:
                            aantal4en = aantal4en - 1
                    if player2active == True and player2stay == 0:
                        p2card_4 = random.choice(stapel1)
                        if p2card_4 == 1 and aantal1en > 0:
                            aantal1en = aantal1en - 1
                        elif p2card_4 == 2 and aantal2en > 0:
                            aantal2en = aantal2en - 1
                        elif p2card_4 == 3 and aantal3en > 0:
                            aantal3en = aantal3en - 1
                        elif p2card_4 == 4 and aantal4en > 0:
                            aantal4en = aantal4en - 1
                    if dealerstay == 0:
                        dcard_4 = random.choice(stapel1)
                        if dcard_4 == 1 and aantal1en > 0:
                            aantal1en = aantal1en - 1
                        elif dcard_4 == 2 and aantal2en > 0:
                            aantal2en = aantal2en - 1
                        elif dcard_4 == 3 and aantal3en > 0:
                            aantal3en = aantal3en - 1
                        elif dcard_4 == 4 and aantal4en > 0:
                            aantal4en = aantal4en - 1    
                elif dice_total >= 20:
                    if player1stay == 0:
                        p1card_4 = random.choice(stapel3)
                        if p1card_4 == 10 and aantal10en > 0:
                            aantal10en = aantal10en - 1
                        elif p1card_4 == 11 and aantal11en > 0:
                            aantal11en = aantal11en - 1
                        elif p1card_4 == 12 and aantal12en > 0:
                            aantal12en = aantal12en - 1
                        elif p1card_4 == 13 and aantal13en > 0:
                            aantal13en = aantal13en - 1
                    if player2active == True and player2stay == 0:
                        p2card_4 = random.choice(stapel3)
                        if p2card_4 == 10 and aantal10en > 0:
                            aantal10en = aantal10en - 1
                        elif p2card_4 == 11 and aantal11en > 0:
                            aantal11en = aantal11en - 1
                        elif p2card_4 == 12 and aantal12en > 0:
                            aantal12en = aantal12en - 1
                        elif p2card_4 == 13 and aantal13en > 0:
                            aantal13en = aantal13en - 1
                    if dealerstay == 0:
                        dcard_4 = random.choice(stapel3)
                        if dcard_4 == 10 and aantal10en > 0:
                            aantal10en = aantal10en - 1
                        elif dcard_4 == 11 and aantal11en > 0:
                            aantal11en = aantal11en - 1
                        elif dcard_4 == 12 and aantal12en > 0:
                            aantal12en = aantal12en - 1
                        elif dcard_4 == 13 and aantal13en > 0:
                            aantal13en = aantal13en - 1
                else:
                    if player1stay == 0:
                        p1card_4 = random.choice(stapel2)
                        if p1card_4 == 5 and aantal5en > 0:
                            aantal5en = aantal5en - 1
                        elif p1card_4 == 6 and aantal6en > 0:
                            aantal6en = aantal6en - 1
                        elif p1card_4 == 7 and aantal7en > 0:
                            aantal7en = aantal7en - 1
                        elif p1card_4 == 8 and aantal8en > 0:
                            aantal8en = aantal8en - 1
                        elif p1card_4 == 9 and aantal9en > 0:
                            aantal9en = aantal9en - 1
                    if player2active == True and player2stay == 0:
                        p2card_4 = random.choice(stapel2)
                        if p2card_4 == 5 and aantal5en > 0:
                            aantal5en = aantal5en - 1
                        elif p2card_4 == 6 and aantal6en > 0:
                            aantal6en = aantal6en - 1
                        elif p2card_4 == 7 and aantal7en > 0:
                            aantal7en = aantal7en - 1
                        elif p2card_4 == 8 and aantal8en > 0:
                            aantal8en = aantal8en - 1
                        elif p2card_4 == 9 and aantal9en > 0:
                            aantal9en = aantal9en - 1
                    if dealerstay == 0:
                        dcard_4 = random.choice(stapel2)
                        if dcard_4 == 5 and aantal5en > 0:
                            aantal5en = aantal5en - 1
                        elif dcard_4 == 6 and aantal6en > 0:
                            aantal6en = aantal6en - 1
                        elif dcard_4 == 7 and aantal7en > 0:
                            aantal7en = aantal7en - 1
                        elif dcard_4 == 8 and aantal8en > 0:
                            aantal8en = aantal8en - 1
                        elif dcard_4 == 9 and aantal9en > 0:
                            aantal9en = aantal9en - 1
                        
                p1card_total = p1card_totalfunc()
                p2card_total = p2card_totalfunc()
                dcard_total = dcard_totalfunc()
                if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                    dealerstay = 1
                if p1card_total > 23: # waneer moet de speler stoppen
                    player1stay = 1
                if p2card_total > 23: # waneer moet speler 2 stoppen
                    player2stay = 1
            
                if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 5
                    dice_total = dice5total()
                    if dice_total <= 15:
                        if player1stay == 0:
                            p1card_5 = random.choice(stapel1)
                            if p1card_5 == 1 and aantal1en > 0:
                                aantal1en = aantal1en - 1
                            elif p1card_5 == 2 and aantal2en > 0:
                                aantal2en = aantal2en - 1
                            elif p1card_5 == 3 and aantal3en > 0:
                                aantal3en = aantal3en - 1
                            elif p1card_5 == 4 and aantal4en > 0:
                                aantal4en = aantal4en - 1
                        if player2active == True and player2stay == 0:
                            p2card_5 = random.choice(stapel1)
                            if p2card_5 == 1 and aantal1en > 0:
                                aantal1en = aantal1en - 1
                            elif p2card_5 == 2 and aantal2en > 0:
                                aantal2en = aantal2en - 1
                            elif p2card_5 == 3 and aantal3en > 0:
                                aantal3en = aantal3en - 1
                            elif p2card_5 == 4 and aantal4en > 0:
                                aantal4en = aantal4en - 1
                        if dealerstay == 0:
                            dcard_5 = random.choice(stapel1)
                            if dcard_5 == 1 and aantal1en > 0:
                                aantal1en = aantal1en - 1
                            elif dcard_5 == 2 and aantal2en > 0:
                                aantal2en = aantal2en - 1
                            elif dcard_5 == 3 and aantal3en > 0:
                                aantal3en = aantal3en - 1
                            elif dcard_5 == 4 and aantal4en > 0:
                                aantal4en = aantal4en - 1
                    elif dice_total >= 20:
                        if player1stay == 0:
                            p1card_5 = random.choice(stapel3)
                            if p1card_5 == 10 and aantal10en > 0:
                                aantal10en = aantal10en - 1
                            elif p1card_5 == 11 and aantal11en > 0:
                                aantal11en = aantal11en - 1
                            elif p1card_5 == 12 and aantal12en > 0:
                                aantal12en = aantal12en - 1
                            elif p1card_5 == 13 and aantal13en > 0:
                                aantal13en = aantal13en - 1
                        if player2active == True and player2stay == 0:
                            p2card_5 = random.choice(stapel3)
                            if p2card_5 == 10 and aantal10en > 0:
                                aantal10en = aantal10en - 1
                            elif p2card_5 == 11 and aantal11en > 0:
                                aantal11en = aantal11en - 1
                            elif p2card_5 == 12 and aantal12en > 0:
                                aantal12en = aantal12en - 1
                            elif p2card_5 == 13 and aantal13en > 0:
                                aantal13en = aantal13en - 1
                        if dealerstay == 0:
                            dcard_5 = random.choice(stapel3)
                            if dcard_5 == 10 and aantal10en > 0:
                                aantal10en = aantal10en - 1
                            elif dcard_5 == 11 and aantal11en > 0:
                                aantal11en = aantal11en - 1
                            elif dcard_5 == 12 and aantal12en > 0:
                                aantal12en = aantal12en - 1
                            elif dcard_5 == 13 and aantal13en > 0:
                                aantal13en = aantal13en - 1
                    else:
                        if player1stay == 0:
                            p1card_5 = random.choice(stapel2)
                            if p1card_5 == 5 and aantal5en > 0:
                                aantal5en = aantal5en - 1
                            elif p1card_5 == 6 and aantal6en > 0:
                                aantal6en = aantal6en - 1
                            elif p1card_5 == 7 and aantal7en > 0:
                                aantal7en = aantal7en - 1
                            elif p1card_5 == 8 and aantal8en > 0:
                                aantal8en = aantal8en - 1
                            elif p1card_5 == 9 and aantal9en > 0:
                                aantal9en = aantal9en - 1
                        if player2active == True and player2stay == 0:
                            p2card_5 = random.choice(stapel2)
                            if p2card_5 == 5 and aantal5en > 0:
                                aantal5en = aantal5en - 1
                            elif p2card_5 == 6 and aantal6en > 0:
                                aantal6en = aantal6en - 1
                            elif p2card_5 == 7 and aantal7en > 0:
                                aantal7en = aantal7en - 1
                            elif p2card_5 == 8 and aantal8en > 0:
                                aantal8en = aantal8en - 1
                            elif p2card_5 == 9 and aantal9en > 0:
                                aantal9en = aantal9en - 1
                        if dealerstay == 0:    
                            dcard_5 = random.choice(stapel2)
                            if dcard_5 == 5 and aantal5en > 0:
                                aantal5en = aantal5en - 1
                            elif dcard_5 == 6 and aantal6en > 0:
                                aantal6en = aantal6en - 1
                            elif dcard_5 == 7 and aantal7en > 0:
                                aantal7en = aantal7en - 1
                            elif dcard_5 == 8 and aantal8en > 0:
                                aantal8en = aantal8en - 1
                            elif dcard_5 == 9 and aantal9en > 0:
                                aantal9en = aantal9en - 1
                
                    p1card_total = p1card_totalfunc()
                    p2card_total = p2card_totalfunc()
                    dcard_total = dcard_totalfunc()
                    if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                        dealerstay = 1
                    if p1card_total > 23: # waneer moet de speler stoppen
                        player1stay = 1
                    if p2card_total > 23: # waneer moet speler 2 stoppen
                        player2stay = 1
                
                    if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 6
                        dice_total = dice5total()
                        if dice_total <= 15:
                            if player1stay == 0:
                                p1card_6 = random.choice(stapel1)
                                if p1card_6 == 1 and aantal1en > 0:
                                    aantal1en = aantal1en - 1
                                elif p1card_6 == 2 and aantal2en > 0:
                                    aantal2en = aantal2en - 1
                                elif p1card_6 == 3 and aantal3en > 0:
                                    aantal3en = aantal3en - 1
                                elif p1card_6 == 4 and aantal4en > 0:
                                    aantal4en = aantal4en - 1
                            if player2active == True and player2stay == 0:
                                p2card_6 = random.choice(stapel1)
                                if p2card_6 == 1 and aantal1en > 0:
                                    aantal1en = aantal1en - 1
                                elif p2card_6 == 2 and aantal2en > 0:
                                    aantal2en = aantal2en - 1
                                elif p2card_6 == 3 and aantal3en > 0:
                                    aantal3en = aantal3en - 1
                                elif p2card_6 == 4 and aantal4en > 0:
                                    aantal4en = aantal4en - 1
                            if dealerstay == 0:
                                dcard_6 = random.choice(stapel1)
                                if dcard_6 == 1 and aantal1en > 0:
                                    aantal1en = aantal1en - 1
                                elif dcard_6 == 2 and aantal2en > 0:
                                    aantal2en = aantal2en - 1
                                elif dcard_6 == 3 and aantal3en > 0:
                                    aantal3en = aantal3en - 1
                                elif dcard_6 == 4 and aantal4en > 0:
                                    aantal4en = aantal4en - 1
                        elif dice_total >= 20:
                            if player1stay == 0:
                                p1card_6 = random.choice(stapel3)
                                if p1card_6 == 10 and aantal10en > 0:
                                    aantal10en = aantal10en - 1
                                elif p1card_6 == 11 and aantal11en > 0:
                                    aantal11en = aantal11en - 1
                                elif p1card_6 == 12 and aantal12en > 0:
                                    aantal12en = aantal12en - 1
                                elif p1card_6 == 13 and aantal13en > 0:
                                    aantal13en = aantal13en - 1
                            if player2active == True and player2stay == 0:
                                p2card_6 = random.choice(stapel3)
                                if p2card_6 == 10 and aantal10en > 0:
                                    aantal10en = aantal10en - 1
                                elif p2card_6 == 11 and aantal11en > 0:
                                    aantal11en = aantal11en - 1
                                elif p2card_6 == 12 and aantal12en > 0:
                                    aantal12en = aantal12en - 1
                                elif p2card_6 == 13 and aantal13en > 0:
                                    aantal13en = aantal13en - 1
                            if dealerstay == 0:
                                dcard_6 = random.randint(10,13)
                                if dcard_6 == 10 and aantal10en > 0:
                                    aantal10en = aantal10en - 1
                                elif dcard_6 == 11 and aantal11en > 0:
                                    aantal11en = aantal11en - 1
                                elif dcard_6 == 12 and aantal12en > 0:
                                    aantal12en = aantal12en - 1
                                elif dcard_6 == 13 and aantal13en > 0:
                                    aantal13en = aantal13en - 1
                        else:
                            if player1stay == 0:
                                p1card_6 = random.choice(stapel2)
                                if p1card_6 == 5 and aantal5en > 0:
                                    aantal5en = aantal5en - 1
                                elif p1card_6 == 6 and aantal6en > 0:
                                    aantal6en = aantal6en - 1
                                elif p1card_6 == 7 and aantal7en > 0:
                                    aantal7en = aantal7en - 1
                                elif p1card_6 == 8 and aantal8en > 0:
                                    aantal8en = aantal8en - 1
                                elif p1card_6 == 9 and aantal9en > 0:
                                    aantal9en = aantal9en - 1
                            if player2active == True and player2stay == 0:
                                p2card_6 = random.choice(stapel2)
                                if p2card_6 == 5 and aantal5en > 0:
                                    aantal5en = aantal5en - 1
                                elif p2card_6 == 6 and aantal6en > 0:
                                    aantal6en = aantal6en - 1
                                elif p2card_6 == 7 and aantal7en > 0:
                                    aantal7en = aantal7en - 1
                                elif p2card_6 == 8 and aantal8en > 0:
                                    aantal8en = aantal8en - 1
                                elif p2card_6 == 9 and aantal9en > 0:
                                    aantal9en = aantal9en - 1
                            if dealerstay == 0:
                                dcard_6 = random.choice(stapel2)
                                if dcard_6 == 5 and aantal5en > 0:
                                    aantal5en = aantal5en - 1
                                elif dcard_6 == 6 and aantal6en > 0:
                                    aantal6en = aantal6en - 1
                                elif dcard_6 == 7 and aantal7en > 0:
                                    aantal7en = aantal7en - 1
                                elif dcard_6 == 8 and aantal8en > 0:
                                    aantal8en = aantal8en - 1
                                elif dcard_6 == 9 and aantal9en > 0:
                                    aantal9en = aantal9en - 1
                                
                        p1card_total = p1card_totalfunc()
                        p2card_total = p2card_totalfunc()
                        dcard_total = dcard_totalfunc()
                        if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                            dealerstay = 1
                        if p1card_total > 23: # waneer moet de speler stoppen
                            player1stay = 1
                        if p2card_total > 23: # waneer moet speler 2 stoppen
                            player2stay = 1
                        
                        if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 7
                            dice_total = dice5total()
                            if dice_total <= 15:
                                if player1stay == 0:    
                                    p1card_7 = random.choice(stapel1)
                                    if p1card_7 == 1 and aantal1en > 0:
                                        aantal1en = aantal1en - 1
                                    elif p1card_7 == 2 and aantal2en > 0:
                                        aantal2en = aantal2en - 1
                                    elif p1card_7 == 3 and aantal3en > 0:
                                        aantal3en = aantal3en - 1
                                    elif p1card_7 == 4 and aantal4en > 0:
                                        aantal4en = aantal4en - 1
                                if player2active == True and player2stay == 0:
                                    p2card_7 = random.choice(stapel1)
                                    if p2card_7 == 1 and aantal1en > 0:
                                        aantal1en = aantal1en - 1
                                    elif p2card_7 == 2 and aantal2en > 0:
                                        aantal2en = aantal2en - 1
                                    elif p2card_7 == 3 and aantal3en > 0:
                                        aantal3en = aantal3en - 1
                                    elif p2card_7 == 4 and aantal4en > 0:
                                        aantal4en = aantal4en - 1
                                if dealerstay == 0:
                                    dcard_7 = random.choice(stapel1)
                                    if dcard_7 == 1 and aantal1en > 0:
                                        aantal1en = aantal1en - 1
                                    elif dcard_7 == 2 and aantal2en > 0:
                                        aantal2en = aantal2en - 1
                                    elif dcard_7 == 3 and aantal3en > 0:
                                        aantal3en = aantal3en - 1
                                    elif dcard_7 == 4 and aantal4en > 0:
                                        aantal4en = aantal4en - 1
                            elif dice_total >= 20:
                                if player1stay == 0:
                                    p1card_7 = random.choice(stapel3)
                                    if p1card_7 == 10 and aantal10en > 0:
                                        aantal10en = aantal10en - 1
                                    elif p1card_7 == 11 and aantal11en > 0:
                                        aantal11en = aantal11en - 1
                                    elif p1card_7 == 12 and aantal12en > 0:
                                        aantal12en = aantal12en - 1
                                    elif p1card_7 == 13 and aantal13en > 0:
                                        aantal13en = aantal13en - 1
                                if player2active == True and player2stay == 0:
                                    p2card_7 = random.choice(stapel3)
                                    if p2card_7 == 10 and aantal10en > 0:
                                        aantal10en = aantal10en - 1
                                    elif p2card_7 == 11 and aantal11en > 0:
                                        aantal11en = aantal11en - 1
                                    elif p2card_7 == 12 and aantal12en > 0:
                                        aantal12en = aantal12en - 1
                                    elif p2card_7 == 13 and aantal13en > 0:
                                        aantal13en = aantal13en - 1
                                if dealerstay == 0:
                                    dcard_7 = random.choice(stapel3)
                                    if dcard_7 == 10 and aantal10en > 0:
                                        aantal10en = aantal10en - 1
                                    elif dcard_7 == 11 and aantal11en > 0:
                                        aantal11en = aantal11en - 1
                                    elif dcard_7 == 12 and aantal12en > 0:
                                        aantal12en = aantal12en - 1
                                    elif dcard_7 == 13 and aantal13en > 0:
                                        aantal13en = aantal13en - 1
                            else:
                                if player1stay == 0:
                                    p1card_7 = random.choice(stapel2)
                                    if p1card_7 == 5 and aantal5en > 0:
                                        aantal5en = aantal5en - 1
                                    elif p1card_7 == 6 and aantal6en > 0:
                                        aantal6en = aantal6en - 1
                                    elif p1card_7 == 7 and aantal7en > 0:
                                        aantal7en = aantal7en - 1
                                    elif p1card_7 == 8 and aantal8en > 0:
                                        aantal8en = aantal8en - 1
                                    elif p1card_7 == 9 and aantal9en > 0:
                                        aantal9en = aantal9en - 1
                                if player2active == True and player2stay == 0:
                                    p2card_7 = random.choice(stapel2)
                                    if p2card_7 == 5 and aantal5en > 0:
                                        aantal5en = aantal5en - 1
                                    elif p2card_7 == 6 and aantal6en > 0:
                                        aantal6en = aantal6en - 1
                                    elif p2card_7 == 7 and aantal7en > 0:
                                        aantal7en = aantal7en - 1
                                    elif p2card_7 == 8 and aantal8en > 0:
                                        aantal8en = aantal8en - 1
                                    elif p2card_7 == 9 and aantal9en > 0:
                                        aantal9en = aantal9en - 1
                                if dealerstay == 0:
                                    dcard_7 = random.choice(stapel2)
                                    if dcard_7 == 5 and aantal5en > 0:
                                        aantal5en = aantal5en - 1
                                    elif dcard_7 == 6 and aantal6en > 0:
                                        aantal6en = aantal6en - 1
                                    elif dcard_7 == 7 and aantal7en > 0:
                                        aantal7en = aantal7en - 1
                                    elif dcard_7 == 8 and aantal8en > 0:
                                        aantal8en = aantal8en - 1
                                    elif dcard_7 == 9 and aantal9en > 0:
                                        aantal9en = aantal9en - 1
                                    
                            p1card_total = p1card_totalfunc()
                            p2card_total = p2card_totalfunc()
                            dcard_total = dcard_totalfunc()
                            if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                                dealerstay = 1
                            if p1card_total > 23: # waneer moet de speler stoppen
                                player1stay = 1
                            if p2card_total > 23: # waneer moet speler 2 stoppen
                                player2stay = 1
                        
                            if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 8
                                dice_total = dice5total()
                                if dice_total <= 15:
                                    if player1stay == 0:
                                        p1card_8 = random.choice(stapel1)
                                        if p1card_8 == 1 and aantal1en > 0:
                                            aantal1en = aantal1en - 1
                                        elif p1card_8 == 2 and aantal2en > 0:
                                            aantal2en = aantal2en - 1
                                        elif p1card_8 == 3 and aantal3en > 0:
                                            aantal3en = aantal3en - 1
                                        elif p1card_8 == 4 and aantal4en > 0:
                                            aantal4en = aantal4en - 1
                                    if player2active == True and player2stay == 0:
                                        p2card_8 = random.choice(stapel1)
                                        if p2card_8 == 1 and aantal1en > 0:
                                            aantal1en = aantal1en - 1
                                        elif p2card_8 == 2 and aantal2en > 0:
                                            aantal2en = aantal2en - 1
                                        elif p2card_8 == 3 and aantal3en > 0:
                                            aantal3en = aantal3en - 1
                                        elif p2card_8 == 4 and aantal4en > 0:
                                            aantal4en = aantal4en - 1
                                    if dealerstay == 0:
                                        dcard_8 = random.choice(stapel1)
                                        if dcard_8 == 1 and aantal1en > 0:
                                            aantal1en = aantal1en - 1
                                        elif dcard_8 == 2 and aantal2en > 0:
                                            aantal2en = aantal2en - 1
                                        elif dcard_8 == 3 and aantal3en > 0:
                                            aantal3en = aantal3en - 1
                                        elif dcard_8 == 4 and aantal4en > 0:
                                            aantal4en = aantal4en - 1
                                elif dice_total >= 20:
                                    if player1stay == 0:
                                        p1card_8 = random.choice(stapel3)
                                        if p1card_8 == 10 and aantal10en > 0:
                                            aantal10en = aantal10en - 1
                                        elif p1card_8 == 11 and aantal11en > 0:
                                            aantal11en = aantal11en - 1
                                        elif p1card_8 == 12 and aantal12en > 0:
                                            aantal12en = aantal12en - 1
                                        elif p1card_8 == 13 and aantal13en > 0:
                                            aantal13en = aantal13en - 1
                                    if player2active == True and player2stay == 0:
                                        p2card_8 = random.choice(stapel3)
                                        if p2card_8 == 10 and aantal10en > 0:
                                            aantal10en = aantal10en - 1
                                        elif p2card_8 == 11 and aantal11en > 0:
                                            aantal11en = aantal11en - 1
                                        elif p2card_8 == 12 and aantal12en > 0:
                                            aantal12en = aantal12en - 1
                                        elif p2card_8 == 13 and aantal13en > 0:
                                            aantal13en = aantal13en - 1
                                    if dealerstay == 0:
                                        dcard_8 = random.choice(stapel3)
                                        if dcard_8 == 10 and aantal10en > 0:
                                            aantal10en = aantal10en - 1
                                        elif dcard_8 == 11 and aantal11en > 0:
                                            aantal11en = aantal11en - 1
                                        elif dcard_8 == 12 and aantal12en > 0:
                                            aantal12en = aantal12en - 1
                                        elif dcard_8 == 13 and aantal13en > 0:
                                            aantal13en = aantal13en - 1
                                else:
                                    if player1stay == 0:
                                        p1card_8 = random.choice(stapel2)
                                        if p1card_8 == 5 and aantal5en > 0:
                                            aantal5en = aantal5en - 1
                                        elif p1card_8 == 6 and aantal6en > 0:
                                            aantal6en = aantal6en - 1
                                        elif p1card_8 == 7 and aantal7en > 0:
                                            aantal7en = aantal7en - 1
                                        elif p1card_8 == 8 and aantal8en > 0:
                                            aantal8en = aantal8en - 1
                                        elif p1card_8 == 9 and aantal9en > 0:
                                            aantal9en = aantal9en - 1
                                    if player2active == True and player2stay == 0:
                                        p2card_8 = random.choice(stapel2)
                                        if p2card_8 == 5 and aantal5en > 0:
                                            aantal5en = aantal5en - 1
                                        elif p2card_8 == 6 and aantal6en > 0:
                                            aantal6en = aantal6en - 1
                                        elif p2card_8 == 7 and aantal7en > 0:
                                            aantal7en = aantal7en - 1
                                        elif p2card_8 == 8 and aantal8en > 0:
                                            aantal8en = aantal8en - 1
                                        elif p2card_8 == 9 and aantal9en > 0:
                                            aantal9en = aantal9en - 1
                                    if dealerstay == 0:
                                        dcard_8 = random.choice(stapel2)
                                        if dcard_8 == 5 and aantal5en > 0:
                                            aantal5en = aantal5en - 1
                                        elif dcard_8 == 6 and aantal6en > 0:
                                            aantal6en = aantal6en - 1
                                        elif dcard_8 == 7 and aantal7en > 0:
                                            aantal7en = aantal7en - 1
                                        elif dcard_8 == 8 and aantal8en > 0:
                                            aantal8en = aantal8en - 1
                                        elif dcard_8 == 9 and aantal9en > 0:
                                            aantal9en = aantal9en - 1
                                        
                                p1card_total = p1card_totalfunc()
                                p2card_total = p2card_totalfunc()
                                dcard_total = dcard_totalfunc()            
                                if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                                    dealerstay = 1
                                if p1card_total > 23: # waneer moet de speler stoppen
                                    player1stay = 1
                                if p2card_total > 23: # waneer moet speler 2 stoppen
                                    player2stay = 1
                            
                                if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 9
                                    dice_total = dice5total()
                                    if dice_total <= 15:
                                        if player1stay == 0:
                                            p1card_9 = random.choice(stapel1)
                                            if p1card_9 == 1 and aantal1en > 0:
                                                aantal1en = aantal1en - 1
                                            elif p1card_9 == 2 and aantal2en > 0:
                                                aantal2en = aantal2en - 1
                                            elif p1card_9 == 3 and aantal3en > 0:
                                                aantal3en = aantal3en - 1
                                            elif p1card_9 == 4 and aantal4en > 0:
                                                aantal4en = aantal4en - 1
                                        if player2active == True and player2stay == 0:
                                            p2card_9 = random.choice(stapel1)
                                            if p2card_9 == 1 and aantal1en > 0:
                                                aantal1en = aantal1en - 1
                                            elif p2card_9 == 2 and aantal2en > 0:
                                                aantal2en = aantal2en - 1
                                            elif p2card_9 == 3 and aantal3en > 0:
                                                aantal3en = aantal3en - 1
                                            elif p2card_9 == 4 and aantal4en > 0:
                                                aantal4en = aantal4en - 1
                                        if dealerstay == 0:
                                            dcard_9 = random.choice(stapel1)
                                            if dcard_9 == 1 and aantal1en > 0:
                                                aantal1en = aantal1en - 1
                                            elif dcard_9 == 2 and aantal2en > 0:
                                                aantal2en = aantal2en - 1
                                            elif dcard_9 == 3 and aantal3en > 0:
                                                aantal3en = aantal3en - 1
                                            elif dcard_9 == 4 and aantal4en > 0:
                                                aantal4en = aantal4en - 1
                                    elif dice_total >= 20:
                                        if player1stay == 0:
                                            p1card_9 = random.choice(stapel3)
                                            if p1card_9 == 10 and aantal10en > 0:
                                                aantal10en = aantal10en - 1
                                            elif p1card_9 == 11 and aantal11en > 0:
                                                aantal11en = aantal11en - 1
                                            elif p1card_9 == 12 and aantal12en > 0:
                                                aantal12en = aantal12en - 1
                                            elif p1card_9 == 13 and aantal13en > 0:
                                                aantal13en = aantal13en - 1
                                        if player2active == True and player2stay == 0:
                                            p2card_9 = random.choice(stapel3)
                                            if p2card_9 == 10 and aantal10en > 0:
                                                aantal10en = aantal10en - 1
                                            elif p2card_9 == 11 and aantal11en > 0:
                                                aantal11en = aantal11en - 1
                                            elif p2card_9 == 12 and aantal12en > 0:
                                                aantal12en = aantal12en - 1
                                            elif p2card_9 == 13 and aantal13en > 0:
                                                aantal13en = aantal13en - 1
                                        if dealerstay == 0:
                                            dcard_9 = random.choice(stapel3)
                                            if dcard_9 == 10 and aantal10en > 0:
                                                aantal10en = aantal10en - 1
                                            elif dcard_9 == 11 and aantal11en > 0:
                                                aantal11en = aantal11en - 1
                                            elif dcard_9 == 12 and aantal12en > 0:
                                                aantal12en = aantal12en - 1
                                            elif dcard_9 == 13 and aantal13en > 0:
                                                aantal13en = aantal13en - 1
                                    else:
                                        if player1stay == 0:
                                            p1card_9 = random.choice(stapel2)
                                            if p1card_9 == 5 and aantal5en > 0:
                                                aantal5en = aantal5en - 1
                                            elif p1card_9 == 6 and aantal6en > 0:
                                                aantal6en = aantal6en - 1
                                            elif p1card_9 == 7 and aantal7en > 0:
                                                aantal7en = aantal7en - 1
                                            elif p1card_9 == 8 and aantal8en > 0:
                                                aantal8en = aantal8en - 1
                                            elif p1card_9 == 9 and aantal9en > 0:
                                                aantal9en = aantal9en - 1
                                        if player2active == True and player2stay == 0:
                                            p2card_9 = random.choice(stapel2)
                                            if p2card_9 == 5 and aantal5en > 0:
                                                aantal5en = aantal5en - 1
                                            elif p2card_9 == 6 and aantal6en > 0:
                                                aantal6en = aantal6en - 1
                                            elif p2card_9 == 7 and aantal7en > 0:
                                                aantal7en = aantal7en - 1
                                            elif p2card_9 == 8 and aantal8en > 0:
                                                aantal8en = aantal8en - 1
                                            elif p2card_9 == 9 and aantal9en > 0:
                                                aantal9en = aantal9en - 1
                                        if dealerstay == 0:
                                            dcard_9 = random.choice(stapel2)
                                            if dcard_9 == 5 and aantal5en > 0:
                                                aantal5en = aantal5en - 1
                                            elif dcard_9 == 6 and aantal6en > 0:
                                                aantal6en = aantal6en - 1
                                            elif dcard_9 == 7 and aantal7en > 0:
                                                aantal7en = aantal7en - 1
                                            elif dcard_9 == 8 and aantal8en > 0:
                                                aantal8en = aantal8en - 1
                                            elif dcard_9 == 9 and aantal9en > 0:
                                                aantal9en = aantal9en - 1
                                            
                                    p1card_total = p1card_totalfunc()
                                    p2card_total = p2card_totalfunc()
                                    dcard_total = dcard_totalfunc()            
                                    if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                                        dealerstay = 1
                                    if p1card_total > 23: # waneer moet de speler stoppen
                                        player1stay = 1
                                    if p2card_total > 23: # waneer moet speler 2 stoppen
                                        player2stay = 1
                                
                                    if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 10
                                        dice_total = dice5total()
                                        if dice_total <= 15:
                                            if player1stay == 0:
                                                p1card_10 = random.choice(stapel1)
                                                if p1card_10 == 1 and aantal1en > 0:
                                                    aantal1en = aantal1en - 1
                                                elif p1card_10 == 2 and aantal2en > 0:
                                                    aantal2en = aantal2en - 1
                                                elif p1card_10 == 3 and aantal3en > 0:
                                                    aantal3en = aantal3en - 1
                                                elif p1card_10 == 4 and aantal4en > 0:
                                                    aantal4en = aantal4en - 1
                                            if player2active == True and player2stay == 0:
                                                p2card_10 = random.choice(stapel1)
                                                if p2card_10 == 1 and aantal1en > 0:
                                                    aantal1en = aantal1en - 1
                                                elif p2card_10 == 2 and aantal2en > 0:
                                                    aantal2en = aantal2en - 1
                                                elif p2card_10 == 3 and aantal3en > 0:
                                                    aantal3en = aantal3en - 1
                                                elif p2card_10 == 4 and aantal4en > 0:
                                                    aantal4en = aantal4en - 1
                                            if dealerstay == 0:
                                                dcard_10 = random.choice(stapel1)
                                                if dcard_10 == 1 and aantal1en > 0:
                                                    aantal1en = aantal1en - 1
                                                elif dcard_10 == 2 and aantal2en > 0:
                                                    aantal2en = aantal2en - 1
                                                elif dcard_10 == 3 and aantal3en > 0:
                                                    aantal3en = aantal3en - 1
                                                elif dcard_10 == 4 and aantal4en > 0:
                                                    aantal4en = aantal4en - 1
                                        elif dice_total >= 20:
                                            if player1stay == 0:
                                                p1card_10 = random.choice(stapel3)
                                                if p1card_10 == 10 and aantal10en > 0:
                                                    aantal10en = aantal10en - 1
                                                elif p1card_10 == 11 and aantal11en > 0:
                                                    aantal11en = aantal11en - 1
                                                elif p1card_10 == 12 and aantal12en > 0:
                                                    aantal12en = aantal12en - 1
                                                elif p1card_10 == 13 and aantal13en > 0:
                                                    aantal13en = aantal13en - 1
                                            if player2active == True and player2stay == 0:
                                                p2card_10 = random.choice(stapel3)
                                                if p2card_10 == 10 and aantal10en > 0:
                                                    aantal10en = aantal10en - 1
                                                elif p2card_10 == 11 and aantal11en > 0:
                                                    aantal11en = aantal11en - 1
                                                elif p2card_10 == 12 and aantal12en > 0:
                                                    aantal12en = aantal12en - 1
                                                elif p2card_10 == 13 and aantal13en > 0:
                                                    aantal13en = aantal13en - 1
                                            if dealerstay == 0:
                                                dcard_10 = random.choice(stapel3)
                                                if dcard_10 == 10 and aantal10en > 0:
                                                    aantal10en = aantal10en - 1
                                                elif dcard_10 == 11 and aantal11en > 0:
                                                    aantal11en = aantal11en - 1
                                                elif dcard_10 == 12 and aantal12en > 0:
                                                    aantal12en = aantal12en - 1
                                                elif dcard_10 == 13 and aantal13en > 0:
                                                    aantal13en = aantal13en - 1
                                        else:
                                            if player1stay == 0:
                                                p1card_10 = random.choice(stapel2)
                                                if p1card_10 == 5 and aantal5en > 0:
                                                    aantal5en = aantal5en - 1
                                                elif p1card_10 == 6 and aantal6en > 0:
                                                    aantal6en = aantal6en - 1
                                                elif p1card_10 == 7 and aantal7en > 0:
                                                    aantal7en = aantal7en - 1
                                                elif p1card_10 == 8 and aantal8en > 0:
                                                    aantal8en = aantal8en - 1
                                                elif p1card_10 == 9 and aantal9en > 0:
                                                    aantal9en = aantal9en - 1
                                            if player2active == True and player2stay == 0:
                                                p2card_10 = random.choice(stapel2)
                                                if p2card_10 == 5 and aantal5en > 0:
                                                    aantal5en = aantal5en - 1
                                                elif p2card_10 == 6 and aantal6en > 0:
                                                    aantal6en = aantal6en - 1
                                                elif p2card_10 == 7 and aantal7en > 0:
                                                    aantal7en = aantal7en - 1
                                                elif p2card_10 == 8 and aantal8en > 0:
                                                    aantal8en = aantal8en - 1
                                                elif p2card_10 == 9 and aantal9en > 0:
                                                    aantal9en = aantal9en - 1
                                            if dealerstay == 0:
                                                dcard_10 = random.choice(stapel2)
                                                if dcard_10 == 5 and aantal5en > 0:
                                                    aantal5en = aantal5en - 1
                                                elif dcard_10 == 6 and aantal6en > 0:
                                                    aantal6en = aantal6en - 1
                                                elif dcard_10 == 7 and aantal7en > 0:
                                                    aantal7en = aantal7en - 1
                                                elif dcard_10 == 8 and aantal8en > 0:
                                                    aantal8en = aantal8en - 1
                                                elif dcard_10 == 9 and aantal9en > 0:
                                                    aantal9en = aantal9en - 1
                                                
                                        p1card_total = p1card_totalfunc()
                                        p2card_total = p2card_totalfunc()
                                        dcard_total = dcard_totalfunc()
                                        if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                                            dealerstay = 1
                                        if p1card_total > 23: # waneer moet de speler stoppen
                                            player1stay = 1
                                        if p2card_total > 23: # waneer moet speler 2 stoppen
                                            player2stay = 1

                                        if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 11
                                            dice_total = dice5total()
                                            if dice_total <= 15:
                                                if player1stay == 0:
                                                    p1card_11 = random.choice(stapel1)
                                                    if p1card_11 == 1 and aantal1en > 0:
                                                        aantal1en = aantal1en - 1
                                                    elif p1card_11 == 2 and aantal2en > 0:
                                                        aantal2en = aantal2en - 1
                                                    elif p1card_11 == 3 and aantal3en > 0:
                                                        aantal3en = aantal3en - 1
                                                    elif p1card_11 == 4 and aantal4en > 0:
                                                        aantal4en = aantal4en - 1
                                                if player2active == True and player2stay == 0:
                                                    p2card_11 = random.choice(stapel1)
                                                    if p2card_11 == 1 and aantal1en > 0:
                                                        aantal1en = aantal1en - 1
                                                    elif p2card_11 == 2 and aantal2en > 0:
                                                        aantal2en = aantal2en - 1
                                                    elif p2card_11 == 3 and aantal3en > 0:
                                                        aantal3en = aantal3en - 1
                                                    elif p2card_11 == 4 and aantal4en > 0:
                                                        aantal4en = aantal4en - 1
                                                if dealerstay == 0:
                                                    dcard_11 = random.choice(stapel1)
                                                    if dcard_11 == 1 and aantal1en > 0:
                                                        aantal1en = aantal1en - 1
                                                    elif dcard_11 == 2 and aantal2en > 0:
                                                        aantal2en = aantal2en - 1
                                                    elif dcard_11 == 3 and aantal3en > 0:
                                                        aantal3en = aantal3en - 1
                                                    elif dcard_11 == 4 and aantal4en > 0:
                                                        aantal4en = aantal4en - 1
                                            elif dice_total >= 20:
                                                if player1stay == 0:
                                                    p1card_11 = random.choice(stapel3)
                                                    if p1card_11 == 10 and aantal10en > 0:
                                                        aantal10en = aantal10en - 1
                                                    elif p1card_11 == 11 and aantal11en > 0:
                                                        aantal11en = aantal11en - 1
                                                    elif p1card_11 == 12 and aantal12en > 0:
                                                        aantal12en = aantal12en - 1
                                                    elif p1card_11 == 13 and aantal13en > 0:
                                                        aantal13en = aantal13en - 1
                                                if player2active == True and player2stay == 0:
                                                    p2card_11 = random.choice(stapel3)
                                                    if p2card_11 == 10 and aantal10en > 0:
                                                        aantal10en = aantal10en - 1
                                                    elif p2card_11 == 11 and aantal11en > 0:
                                                        aantal11en = aantal11en - 1
                                                    elif p2card_11 == 12 and aantal12en > 0:
                                                        aantal12en = aantal12en - 1
                                                    elif p2card_11 == 13 and aantal13en > 0:
                                                        aantal13en = aantal13en - 1
                                                if dealerstay == 0:
                                                    dcard_11 = random.randint(10,13)
                                                    if dcard_11 == 10 and aantal10en > 0:
                                                        aantal10en = aantal10en - 1
                                                    elif dcard_11 == 11 and aantal11en > 0:
                                                        aantal11en = aantal11en - 1
                                                    elif dcard_11 == 12 and aantal12en > 0:
                                                        aantal12en = aantal12en - 1
                                                    elif dcard_11 == 13 and aantal13en > 0:
                                                        aantal13en = aantal13en - 1
                                            else:
                                                if player1stay == 0:
                                                    p1card_11 = random.choice(stapel2)
                                                    if p1card_11 == 5 and aantal5en > 0:
                                                        aantal5en = aantal5en - 1
                                                    elif p1card_11 == 6 and aantal6en > 0:
                                                        aantal6en = aantal6en - 1
                                                    elif p1card_11 == 7 and aantal7en > 0:
                                                        aantal7en = aantal7en - 1
                                                    elif p1card_11 == 8 and aantal8en > 0:
                                                        aantal8en = aantal8en - 1
                                                    elif p1card_11 == 9 and aantal9en > 0:
                                                        aantal9en = aantal9en - 1
                                                if player2active == True and player2stay == 0:
                                                    p2card_11 = random.choice(stapel2)
                                                    if p2card_11 == 5 and aantal5en > 0:
                                                        aantal5en = aantal5en - 1
                                                    elif p2card_11 == 6 and aantal6en > 0:
                                                        aantal6en = aantal6en - 1
                                                    elif p2card_11 == 7 and aantal7en > 0:
                                                        aantal7en = aantal7en - 1
                                                    elif p2card_11 == 8 and aantal8en > 0:
                                                        aantal8en = aantal8en - 1
                                                    elif p2card_11 == 9 and aantal9en > 0:
                                                        aantal9en = aantal9en - 1
                                                if dealerstay == 0:
                                                    dcard_11 = random.choice(stapel2)
                                                    if dcard_11 == 5 and aantal5en > 0:
                                                        aantal5en = aantal5en - 1
                                                    elif dcard_11 == 6 and aantal6en > 0:
                                                        aantal6en = aantal6en - 1
                                                    elif dcard_11 == 7 and aantal7en > 0:
                                                        aantal7en = aantal7en - 1
                                                    elif dcard_11 == 8 and aantal8en > 0:
                                                        aantal8en = aantal8en - 1
                                                    elif dcard_11 == 9 and aantal9en > 0:
                                                        aantal9en = aantal9en - 1
                                                    
                                            p1card_total = p1card_totalfunc()
                                            p2card_total = p2card_totalfunc()
                                            dcard_total = dcard_totalfunc()            
                                            if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card_1 != 0)): # wanneer moet de dealer stoppen
                                                dealerstay = 1
                                            if p1card_total > 23: # waneer moet de speler stoppen
                                                player1stay = 1
                                            if p2card_total > 23: # waneer moet speler 2 stoppen
                                                player2stay = 1
                                        
                                        
                                            if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 12
                                                dice_total = dice5total()
                                                if dice_total <= 15:
                                                    if player1stay == 0:
                                                        p1card_12 = random.choice(stapel1)
                                                        if p1card_12 == 1 and aantal1en > 0:
                                                            aantal1en = aantal1en - 1
                                                        elif p1card_12 == 2 and aantal2en > 0:
                                                            aantal2en = aantal2en - 1
                                                        elif p1card_12 == 3 and aantal3en > 0:
                                                            aantal3en = aantal3en - 1
                                                        elif p1card_12 == 4 and aantal4en > 0:
                                                            aantal4en = aantal4en - 1
                                                    if player2active == True and player2stay == 0:
                                                        p2card_12 = random.choice(stapel1)
                                                        if p2card_12 == 1 and aantal1en > 0:
                                                            aantal1en = aantal1en - 1
                                                        elif p2card_12 == 2 and aantal2en > 0:
                                                            aantal2en = aantal2en - 1
                                                        elif p2card_12 == 3 and aantal3en > 0:
                                                            aantal3en = aantal3en - 1
                                                        elif p2card_12 == 4 and aantal4en > 0:
                                                            aantal4en = aantal4en - 1
                                                    if dealerstay == 0:
                                                        dcard_12 = random.choice(stapel1)
                                                        if dcard_12 == 1 and aantal1en > 0:
                                                            aantal1en = aantal1en - 1
                                                        elif dcard_12 == 2 and aantal2en > 0:
                                                            aantal2en = aantal2en - 1
                                                        elif dcard_12 == 3 and aantal3en > 0:
                                                            aantal3en = aantal3en - 1
                                                        elif dcard_12 == 4 and aantal4en > 0:
                                                            aantal4en = aantal4en - 1
                                                elif dice_total >= 20:
                                                    if player1stay == 0:
                                                        p1card_12 = random.choice(stapel3)
                                                        if p1card_12 == 10 and aantal10en > 0:
                                                            aantal10en = aantal10en - 1
                                                        elif p1card_12 == 11 and aantal11en > 0:
                                                            aantal11en = aantal11en - 1
                                                        elif p1card_12 == 12 and aantal12en > 0:
                                                            aantal12en = aantal12en - 1
                                                        elif p1card_12 == 13 and aantal13en > 0:
                                                            aantal13en = aantal13en - 1
                                                    if player2active == True and player2stay == 0:
                                                        p2card_12 = random.choice(stapel3)
                                                        if p2card_12 == 10 and aantal10en > 0:
                                                            aantal10en = aantal10en - 1
                                                        elif p2card_12 == 11 and aantal11en > 0:
                                                            aantal11en = aantal11en - 1
                                                        elif p2card_12 == 12 and aantal12en > 0:
                                                            aantal12en = aantal12en - 1
                                                        elif p2card_12 == 13 and aantal13en > 0:
                                                            aantal13en = aantal13en - 1
                                                    if dealerstay == 0:
                                                        dcard_12 = random.choice(stapel3)
                                                        if dcard_12 == 10 and aantal10en > 0:
                                                            aantal10en = aantal10en - 1
                                                        elif dcard_12 == 11 and aantal11en > 0:
                                                            aantal11en = aantal11en - 1
                                                        elif dcard_12 == 12 and aantal12en > 0:
                                                            aantal12en = aantal12en - 1
                                                        elif dcard_12 == 13 and aantal13en > 0:
                                                            aantal13en = aantal13en - 1
                                                else:
                                                    if player1stay == 0:
                                                        p1card_12 = random.choice(stapel2)
                                                        if p1card_12 == 5 and aantal5en > 0:
                                                            aantal5en = aantal5en - 1
                                                        elif p1card_12 == 6 and aantal6en > 0:
                                                            aantal6en = aantal6en - 1
                                                        elif p1card_12 == 7 and aantal7en > 0:
                                                            aantal7en = aantal7en - 1
                                                        elif p1card_12 == 8 and aantal8en > 0:
                                                            aantal8en = aantal8en - 1
                                                        elif p1card_12 == 9 and aantal9en > 0:
                                                            aantal9en = aantal9en - 1
                                                    if player2active == True and player2stay == 0:
                                                        p2card_2 = random.choice(stapel2)
                                                        if p2card_1 == 5 and aantal5en > 0:
                                                            aantal5en = aantal5en - 1
                                                        elif p2card_12 == 6 and aantal6en > 0:
                                                            aantal6en = aantal6en - 1
                                                        elif p2card_12 == 7 and aantal7en > 0:
                                                            aantal7en = aantal7en - 1
                                                        elif p2card_12 == 8 and aantal8en > 0:
                                                            aantal8en = aantal8en - 1
                                                        elif p2card_12 == 9 and aantal9en > 0:
                                                            aantal9en = aantal9en - 1
                                                    if dealerstay == 0:
                                                        dcard_12 = random.choice(stapel2)
                                                        if dcard_12 == 5 and aantal5en > 0:
                                                            aantal5en = aantal5en - 1
                                                        elif dcard_12 == 6 and aantal6en > 0:
                                                            aantal6en = aantal6en - 1
                                                        elif dcard_12 == 7 and aantal7en > 0:
                                                            aantal7en = aantal7en - 1
                                                        elif dcard_12 == 8 and aantal8en > 0:
                                                            aantal8en = aantal8en - 1
                                                        elif dcard_12 == 9 and aantal9en > 0:
                                                            aantal9en = aantal9en - 1

    p1card_total = p1card_totalfunc() # kaarten totaal speler 1
    p2card_total = p2card_totalfunc() # kaarten totaal speler 2
    dcard_total = dcard_totalfunc() # kaarten totaal dealer
   
    #wat gebeurt er bij deze uitkomsten
    if p1card_1 == 1 or p1card_1 + p1card_2 == 26: # checken of speler 1 kupo heeft
        if winoutput == True:
            print("kupo player 1")
        player1kupocounter = player1kupocounter + 1
        player1win = 1
        dealerlostfrp1 = 1
    if p2card_1 == 1 or p2card_1 + p2card_2 == 26: # checken of speler 2 kupo heeft
        if winoutput == True:
            print("kupo player 2")
        player2kupocounter = player2kupocounter + 1
        player2win = 1
        dealerlostfrp2 = 1
    if dcard_1 == 1 or dcard_1 + dcard_2 == 26: # checken of dealer kupo heeft
        if winoutput == True:
            print("kupo dealer")
        dealerkupocounter = dealerkupocounter + 1
        dealerwinfrp1 = 1
        player1lost = 1
        if player2active == True:
            dealerwinfrp2 = 1
            player2lost = 1
    if (dcard_1 == 1 or dcard_1 + dcard_2 == 26) and (p1card_1 == 1 or p1card_1 + p1card_2 == 26):
        pushp1 = 1
    elif p1card_1 == 1 or p1card_1 + p1card_2 == 26:
        player1money = player1money + player1inzet * (kupokuperwinmultiplier - normalwinmultiplier)
    if ((dcard_1 == 1 or dcard_1 + dcard_2 == 26) and (p2card_1 == 1 or p2card_1 + p2card_2 == 26)) and player2active == True:
        pushp2 = 1
    elif p2card_1 == 1 or p2card_1 + p2card_2 == 26:
        player2money = player2money + player2inzet * (kupokuperwinmultiplier - normalwinmultiplier)
    if p1card_1 + p1card_2 == 14: # checken of speler 1 Kuper heeft
        if winoutput == True:
            print("Kuper player 1")
        player1kupercounter = player1kupercounter + 1
        player1lost = 1
        dealerwinfrp1 = 1
    if p2card_1 + p2card_2 == 14: # checken of speler 2 Kuper heeft
        if winoutput == True:
            print("Kuper player 2")
        player2kupercounter = player2kupercounter + 1
        player2lost = 1
        dealerwinfrp2 = 1
    if dcard_1 + dcard_2 == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0): # checken of dealer Kuper heeft
        if winoutput == True:
            print("Kuper dealer")
        dealerkupercounter = dealerkupercounter + 1
        dealerlostfrp1 = 1
        player1win = 1
        if player2active == True:
            player2win = 1
            dealerlostfrp2 = 1
    if (dcard_1 + dcard_2 == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0)) and p1card_1 + p1card_2 == 14:
        pushp1 = 1
    elif dcard_1 + dcard_2 == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0):
        player1money = player1money + player1inzet * (kupokuperwinmultiplier - normalwinmultiplier)
    if player2active == True and ((dcard_1 + dcard_2 == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0)) and p2card_1 + p2card_2 == 14):
        pushp2 = 1
    elif dcard_1 + dcard_2 == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0):
        player2money = player2money + player2inzet * (kupokuperwinmultiplier - normalwinmultiplier)
    if p1card_total > 26: # checken of speler 1 bust is
        if winoutput == True:
            print("bust player 1")
        player1bustcounter = player1bustcounter + 1
        player1lost = 1
        dealerwinfrp1 = 1
    if p2card_total > 26: # checken of speler 2 bust is
        if winoutput == True:
            print("bust player 2")
        player2bustcounter = player2bustcounter + 1
        player2lost = 1
        dealerwinfrp2 = 1
    if dcard_total > 26: # checken of dealer bust is
        if winoutput == True:
            print("bust dealer")
        dealerbustcounter = dealerbustcounter + 1
        if player2active == True and player2lost == 0:
            dealerlostfrp2 = 1
            player2win = 1
        if player1lost == 0:
            dealerlostfrp1 = 1
            player1win = 1
            
    if player2active == False and dealerlostfrp1 == 0 and dealerwinfrp1 == 0 and player1win == 0 and player1lost == 0: # wat gebeurt er als niemand kuper, kupo heeft of bust is
        if p1card_total < 14 and dcard_total < 14: # checken wie er verder van 14 af zit
            if 14 - p1card_total > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            elif 14 - p1card_total < 14 - dcard_total:
                dealerwin = 1
                player1lostfrp1 = 1
            else:
                pushp1 = 1
        elif p1card_total > 14 and dcard_total > 14:
            if p1card_total - 14 > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            elif p1card_total - 14 < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            else:
                pushp1 = 1
        elif p1card_total > 14 and dcard_total < 14:
            if p1card_total - 14 > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            elif p1card_total - 14 < 14 - dcard_total:
                dealerwinfrp1 = 1
                player1lost = 1
            else:
                pushp1 = 1
        elif p1card_total < 14 and dcard_total > 14:
            if 14 - p1card_total > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            elif 14 - p1card_total < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            else:
                pushp1 = 1
        elif p1card_total == 14:
            player1lost = 1
            dealerwinfrp1 = 1
        elif dcard_total == 14:
            player1win = 1
            dealerlostfrp1 = 1
        elif p1card_total == 14 and dcard_total == 14:
            pushp1 = 1

    if player2active == True and ((dealerlostfrp1 == 0 and dealerwinfrp1 == 0 and player1win == 0 and player1lost == 0) or (dealerlostfrp2 == 0 and dealerwinfrp2 == 0  and player2win == 0 and player2lost == 0)):
        if p1card_total == 14:
            player1lost = 1
            dealerwinfrp1 = 1
        if p2card_total == 14:
            player2lost = 1
            dealerwinfrp2 = 1
        if dcard_total == 14:
            player1win = 1
            player2win = 1
            dealerlostfrp1 = 1
            dealerlostfrp2 = 1
        if dcard_total == 14 and p1card_total == 14:
            pushp1 = 1
        if dcard_total == 14 and p2card_total == 14:
            pushp2
        if p1card_total < 14 and dcard_total < 14 and p2card_total < 14: # checken wie er verder van 14 af zit
            if 14 - p1card_total > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            if 14 - p2card_total > 14 - dcard_total:
                player2win = 1
                dealerlostfrp2 = 1
            if 14 - p1card_total < 14 - dcard_total:
                dealerwinfrp1 = 1
                player1lost = 1
            if 14 - p2card_total < 14 - dcard_total:
                dealerwinfrp2 = 1
                player2lost = 1
            if 14 - p1card_total == 14 - dcard_total:
                pushp1 = 1
            if 14 - p2card_total == 14 - dcard_total:
                pushp2 = 1
        elif p1card_total > 14 and dcard_total > 14 and p2card_total > 14:
            if p1card_total - 14 > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            if p2card_total - 14 > dcard_total - 14:
                player2win = 1
                dealerlostfrp2 = 1
            if p1card_total - 14 < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            if p2card_total - 14 < dcard_total - 14:
                dealerwinfrp2 = 1
                player2lost = 1
            if p1card_total - 14 == dcard_total - 14:
                pushp1 = 1
            if p2card_total - 14 == dcard_total - 14:
                pushp2 = 1
        elif p1card_total > 14 and dcard_total < 14 and p2card_total < 14:
            if p1card_total - 14 > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            if 14 - p2card_total > 14 - dcard_total:
                player2win = 1
                dealerlostfrp2 = 1
            if 14 - p2card_total < 14 - dcard_total:
                dealerwinfrp2 = 1
                player2lost = 1
            if p1card_total - 14 < 14 - dcard_total:
                dealerwinfrp1 = 1
                player1lost = 1
            if p1card_total - 14 == 14 - dcard_total:
                pushp1 = 1
            if 14 - p2card_total == 14 - dcard_total:
                pushp2 = 1
        elif p1card_total < 14 and dcard_total > 14 and p2card_total < 14:
            if 14 - p1card_total > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            if 14 - p2card_total > dcard_total - 14:
                player2win = 1
                dealerlostfrp2 = 1
            if 14 - p1card_total < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            if 14 - p2card_total < dcard_total - 14:
                dealerwinfrp2 = 1
                player2lost = 1
            if 14 - p1card_total == dcard_total - 14:
               pushp1= 1
            if 14 - p2card_total == dcard_total - 14:
                pushp2 = 1
        elif p1card_total < 14 and dcard_total > 14 and p2card_total > 14:
            if 14 - p1card_total > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            if p2card_total - 14 > dcard_total - 14:
                player2win = 1
                dealerlostfrp2 = 1
            if 14 - p1card_total < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            if p2card_total - 14 < dcard_total - 14:
                dealerwinfrp2 = 1
                player2lost = 1
            if 14 - p1card_total == dcard_total - 14:
                pushp1 = 1
            if p2card_total - 14 == dcard_total - 14:
                pushp2 = 1
        elif p1card_total < 14 and dcard_total < 14 and p2card_total > 14:
            if 14 - p1card_total > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            if p2card_total - 14 > 14 - dcard_total:
                player2win = 1
                dealerlostfrp2 = 1
            if 14 - p1card_total < 14 - dcard_total:
                dealerwinfrp1 = 1
                player1lost = 1
            if p2card_total - 14 < 14 - dcard_total:
                player2lost = 1
                dealerwinfrp2 = 1
            if 14 - p1card_total == 14 - dcard_total:
                pushp1 = 1
            if p2card_total - 14 == 14 - dcard_total:
                pushp2 = 1
        elif p1card_total > 14 and dcard_total < 14 and p2card_total > 14:
            if p1card_total - 14 > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            if p2card_total - 14 > 14 - dcard_total:
                player2win = 1
                dealerlostfrp2 = 1
            if p1card_total - 14 < 14 - dcard_total:
                dealerwinfrp1 = 1
                player1lost = 1
            if p2card_total - 14 < 14 - dcard_total:
                player2lost = 1
                dealerwinfrp2 = 1
            if p1card_total - 14 == 14 - dcard_total:
                pushp1 = 1
            if p2card_total - 14 == 14 - dcard_total:
                pushp2 = 1
        elif p1card_total > 14 and dcard_total > 14 and p2card_total < 14:
            if p1card_total - 14 > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            if 14 - p2card_total > dcard_total - 14:
                player2win = 1
                dealerlostfrp2 = 1
            if p1card_total - 14 < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            if 14 - p2card_total < dcard_total - 14:
                dealerwinfrp2 = 1
                player2lost = 1
            if p1card_total - 14 == dcard_total - 14:
                pushp1 = 1
            if 14 - p2card_total == dcard_total - 14:
                pushp2 = 1
    #wie wint?
    if pushp1 == 1:
        if winoutput == True:
            print("pushp1")
        p1pushcounter = p1pushcounter + 1
        player1money = player1money + player1inzet
    elif dealerwinfrp1 == 1 and player1lost == 1:
        if winoutput == True:
            print("Dealer Wins from player 1!")
        dealerwincounterfrp1 = dealerwincounterfrp1 + 1
    elif player1win == 1 and dealerlostfrp1 == 1:
        if winoutput == True:
            print("Player 1 Wins!")
        player1wincounter = player1wincounter + 1
        player1money = player1money + player1inzet * normalwinmultiplier
    if player2active == True:
        if pushp2 == 1:
            if winoutput == True:
                print("pushp2")
            p2pushcounter = p2pushcounter + 1
            player2money = player2money + player2inzet
        elif dealerwinfrp2 == 1 and player2lost == 1:
            if winoutput == True:
                print("Dealer Wins from player 2!")
            dealerwincounterfrp2 = dealerwincounterfrp2 + 1
        elif player2win == 1 and dealerlostfrp2 == 1:
            if winoutput == True:
                print("Player 2 Wins!")
            player2wincounter = player2wincounter + 1
            player2money = player2money + player2inzet * normalwinmultiplier

#conclusies/output
p1pushpercentage = round(p1pushcounter / rounds * 100, 2) # percentages uitrekenen
p2pushpercentage = round(p2pushcounter / rounds * 100, 2)
player1winpercentage = round(player1wincounter / rounds * 100, 2)
player2winpercentage = round(player2wincounter / rounds * 100, 2)
dealerwinpercentagefrp1 = round(dealerwincounterfrp1 / rounds * 100, 2)
dealerwinpercentagefrp2 = round(dealerwincounterfrp2 / rounds * 100, 2)
p1lossperround = player1money / rounds
p2lossperround = player2money / rounds
roundtest = player1wincounter + dealerwincounterfrp1 + p1pushcounter
print("")
print("Player1bustcounter:", player1bustcounter)
print("Player1kupocounter:", player1kupocounter)
print("Player1kupercounter:", player1kupercounter)
print("")
if player2active == True:
    print("Player2bustcounter:", player2bustcounter)
    print("Player2kupocounter:", player2kupocounter)
    print("Player2kupercounter:", player2kupercounter)
    print("")
print("Dealerbustcounter:", dealerbustcounter)
print("Dealerkupocounter:", dealerkupocounter)
print("Dealerkupercounter:", dealerkupercounter)
print("")
print("p1pushcounter:", p1pushcounter)
print("Player 1 Wins:", player1wincounter)
if player2active == True:
    print("p2pushcounter:", p2pushcounter)
    print("Player 2 Wins:", player2wincounter)
print("Dealer Wins from player 1:", dealerwincounterfrp1)
if player2active == True:
    print("Dealer Wins from Player 2:", dealerwincounterfrp2)
print("")
print("")
print("p1pushpercentage", p1pushpercentage,"%")
print("Player1winpercentage", player1winpercentage,"%")
if player2active == True:
    print("p2pushpercentage:", p2pushpercentage,"%")
    print("Player2winpercentage", player2winpercentage,"%")
print("Dealerwinpercentage from p1:", dealerwinpercentagefrp1,"%")
if player2active == True:
    print("Dealerwinpercentage from p2:", dealerwinpercentagefrp2,"%")
print("")
print("")
print("player1money:", player1money)
print("average loss per round p1", p1lossperround)
if player2active == True:
    print("player2money:", player2money)
    print("average loss per round p2", p2lossperround)
if diagnostic == True: # extra outputs voor troubleshooting
    print("p1card_1", p1card_1)
    print("p1card_2", p1card_2)
    print("p1card_3", p1card_3)
    print("p1card_4", p1card_4)
    print("p1card_5", p1card_5)
    print("player1stay", player1stay)
    print("p1card_total", p1card_total)
    print("player1win:", player1win)
    print("player1lost:", player1lost)
    if player2active == True:
        print("p2card_1", p2card_1)
        print("p2card_2", p2card_2)
        print("p2card_3", p2card_3)
        print("p2card_4", p2card_4)
        print("p2card_5", p2card_5)
        print("player2stay", player2stay)
        print("p2card_total", p2card_total)
        print("player2win:", player2win)
        print("player2lost:", player2lost)
    print("dcard_1", dcard_1)
    print("dcard_2", dcard_2)
    print("dcard_3", dcard_3)
    print("dcard_4", dcard_4)
    print("dcard_5", dcard_5)
    print("dealerstay", dealerstay)
    print("dcard_total", dcard_total)
    print("dealerwinfrp1:", dealerwinfrp1)
    print("dealerlostfrp1:", dealerlostfrp1)
    if player2active == True:
        print("dealerwinfrp2:", dealerwinfrp2)
        print("dealerlostfrp2:", dealerlostfrp2)
    print("round test:", roundtest)