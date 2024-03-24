import random
roundnm = 0 # variabelen resetten aan het begin van de simulatie
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
dealerwincounter = 0
dealerwinpercentage = 0
pushcounter = 0
pushpercentage = 0
roundtest = 0
diagnostic = 0
player1money = 0
player1inzet = 10
player2money = 0
player2inzet = 0
player2active = False
rounds = 10000
roundtest = pushcounter + dealerwincounter + player1wincounter

def dice5total(): # 5 dobbelstenen functie
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def p1card_totalfunc(): # kaarten totaal speler
    return p1card_1 + p1card_2 + p1card_3 + p1card_4 + p1card_5 + p1card_6 + p1card_7 + p1card_8 + p1card_9 + p1card_10 + p1card_11 + p1card_12

def p2card_totalfunc(): # kaarten totaal speler
    return p2card_1 + p2card_2 + p2card_3 + p2card_4 + p2card_5 + p2card_6 + p2card_7 + p2card_8 + p2card_9 + p2card_10 + p2card_11 + p2card_12

def dcard_totalfunc(): # kaarten totaal dealer
    return dcard_1 + dcard_2 + dcard_3 + dcard_4 + dcard_5 + dcard_6 + dcard_7 + dcard_8 + dcard_9 + dcard_10 + dcard_11 + dcard_12

while roundnm < rounds: # hoeveelheid rondes
    roundnm = roundnm + 1 # variabelen naar 0 aan het begin van elke ronde
    p1card_1 = p1card_2 = p1card_3 = p1card_4 = p1card_5 = p1card_6 = p1card_7 = p1card_8 = p1card_9 = p1card_10 = p1card_11 = p1card_12 = p2card_1 = p2card_2 = p2card_3 = p2card_4 = p2card_5 = p2card_6 = p2card_7 = p2card_8 = p2card_9 = p2card_10 = p2card_11 = p2card_12 = dcard_1 = dcard_2 = dcard_3 = dcard_4 = dcard_5 = dcard_6 = dcard_7 = dcard_8 = dcard_9 = dcard_10 = dcard_11 = dcard_12 = 0
    player1stay = 0
    player1lost = 0
    player1win = 0
    player2stay = 0
    player2lost = 0
    player2win = 0
    dealerlost = 0
    dealerwin = 0
    dealerstay = 0
    push = 0
   
    dice_total = dice5total() # kaart 1
    if dice_total <= 15:
        p1card_1 = random.randint(1, 4)
        if player2active == True:
            p2card_1 = random.randint(1, 4)
        dcard_1 = random.randint(1, 4)
    elif dice_total >= 20:
        p1card_1 = random.randint(10, 13)
        if player2active == True:
            p2card_1 = random.randint(10, 13)
        dcard_1 = random.randint(10, 13)
    else:
        p1card_1 = random.randint(5, 9)
        if player2active == True:
            p2card_1 = random.randint(5, 9)
        dcard_1 = random.randint(5, 9)
   
    p1card_total = p1card_totalfunc()
    p2card_total = p2card_totalfunc()
    dcard_total = dcard_totalfunc()
    if dcard_1 < 4 and dcard_1 < p1card_1: # wanneer moet de dealer stoppen
        dealerstay = 1
    if p1card_1 < 4 and p1card_1 < dcard_1: # waneer moet de speler stoppen
        player1stay = 1
   
    if p1card_1 != 1 and dcard_1 != 1: # kaart 2
        dice_total = dice5total()
        if dice_total <= 15:
            if player1stay == 0:
                p1card_2 = random.randint(1, 4)
                if player2active == True and player2stay == 0:
                    p2card_2 = random.randint(1, 4)
            if dealerstay == 0:
                dcard_2 = random.randint(1, 4)
        elif dice_total >= 20:
            if player1stay == 0:
                p1card_2 = random.randint(10, 13)
            if player2active == True and player2stay == 0:
                p2card_2 = random.randint(10, 13)
            if dealerstay == 0:
                dcard_2 = random.randint(10, 13)
        else:
            if player1stay == 0:
                p1card_2 = random.randint(5, 9)
            if player2active == True and player2stay == 0:
                p2card_2 = random.randint(5, 9)
            if dealerstay == 0:
                dcard_2 = random.randint(5, 9)
   
        p1card_total = p1card_totalfunc()
        p2card_total = p2card_totalfunc()
        dcard_total = dcard_totalfunc()
        if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
            dealerstay = 1
        if p1card_total > 23: # waneer moet de speler stoppen
            player1stay = 1
    
        if player1stay == 0 or dealerstay == 0: # kaart 3
            dice_total = dice5total()
            if dice_total <= 15:
                if player1stay == 0:
                    p1card_3 = random.randint(1, 4)
                if player2active == True and player2stay == 0:
                    p2card_3 = random.randint(1, 4)
                if dealerstay == 0:
                    dcard_3 = random.randint(1, 4)
            elif dice_total >= 20:
                if player1stay == 0:
                    p1card_3 = random.randint(10, 13)
                if player2active == True and player2stay == 0:
                    p2card_3 = random.randint(10, 13)
                if dealerstay == 0:
                    dcard_3 = random.randint(10, 13)
            else:
                if player1stay == 0:
                    p1card_3 = random.randint(5, 9)
                if player2active == True and player2stay == 0:
                    p2card_3 = random.randint(5, 9)
                if dealerstay == 0:
                    dcard_3 = random.randint(5, 9)
                    
            p1card_total = p1card_totalfunc()
            p2card_total = p2card_totalfunc()
            dcard_total = dcard_totalfunc()
            if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                dealerstay = 1
            if p1card_total > 23: # waneer moet de speler stoppen
                player1stay = 1
        
            if player1stay == 0 or dealerstay == 0: # kaart 4
                dice_total = dice5total()
                if dice_total <= 15:
                    if player1stay == 0:
                        p1card_4 = random.randint(1, 4)
                        if player2active == True and player2stay == 0:
                            p2card_4 = random.randint(1, 4)
                    if dealerstay == 0:
                        dcard_4 = random.randint(1, 4)
                elif dice_total >= 20:
                    if player1stay == 0:
                        p1card_4 = random.randint(10, 13)
                    if player2active == True and player2stay == 0:
                        p2card_4 = random.randint(10, 13)
                    if dealerstay == 0:
                        dcard_4 = random.randint(10, 13)
                else:
                    if player1stay == 0:
                        p1card_4 = random.randint(5, 9)
                    if player2active == True and player2stay == 0:
                        p2card_4 = random.randint(5, 9)
                    if dealerstay == 0:
                        dcard_4 = random.randint(5, 9)
                        
                p1card_total = p1card_totalfunc()
                p2card_total = p2card_totalfunc()
                dcard_total = dcard_totalfunc()
                if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                    dealerstay = 1
                if p1card_total > 23: # waneer moet de speler stoppen
                    player1stay = 1
            
                if player1stay == 0 or dealerstay == 0: # kaart 5
                    dice_total = dice5total()
                    if dice_total <= 15:
                        if player1stay == 0:
                            p1card_5 = random.randint(1, 4)
                            if player2active == True and player2stay == 0:
                                p2card_5 = random.randint(1, 4)
                        if dealerstay == 0:
                            dcard_5 = random.randint(1, 4)
                    elif dice_total >= 20:
                        if player1stay == 0:
                            p1card_5 = random.randint(10, 13)
                        if player2active == True and player2stay == 0:
                            p2card_5 = random.randint(10, 13)
                        if dealerstay == 0:
                            dcard_5 = random.randint(10, 13)
                    else:
                        if player1stay == 0:
                            p1card_5 = random.randint(5, 9)
                        if player2active == True and player2stay == 0:
                            p2card_5 = random.randint(5, 9)
                        if dealerstay == 0:    
                            dcard_5 = random.randint(5, 9)
                
                    p1card_total = p1card_totalfunc()
                    p2card_total = p2card_totalfunc()
                    dcard_total = dcard_totalfunc()
                    if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                        dealerstay = 1
                    if p1card_total > 23: # waneer moet de speler stoppen
                        player1stay = 1
                
                    if player1stay == 0 or dealerstay == 0: # kaart 6
                        dice_total = dice5total()
                        if dice_total <= 15:
                            if player1stay == 0:
                                p1card_6 = random.randint(1, 4)
                            if player2active == True and player2stay == 0:
                                p2card_6 = random.randint(1, 4)
                            if dealerstay == 0:
                                dcard_6 = random.randint(1, 4)
                        elif dice_total >= 20:
                            if player1stay == 0:
                                p1card_6 = random.randint(10, 13)
                            if player2active == True and player2stay == 0:
                                p2card_6 = random.randint(10, 13)
                            if dealerstay == 0:
                                dcard_6 = random.randint(10,13)
                        else:
                            if player1stay == 0:
                                p1card_6 = random.randint(5, 9)
                            if player2active == True and player2stay == 0:
                                p2card_6 = random.randint(5, 9)
                            if dealerstay == 0:
                                dcard_6 = random.randint(5, 9)
                                
                        p1card_total = p1card_totalfunc()
                        p2card_total = p2card_totalfunc()
                        dcard_total = dcard_totalfunc()
                        if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                            dealerstay = 1
                        if p1card_total > 23: # waneer moet de speler stoppen
                            player1stay = 1
                        
                        if player1stay == 0 or dealerstay == 0: # kaart 7
                            dice_total = dice5total()
                            if dice_total <= 15:
                                if player1stay == 0:    
                                    p1card_7 = random.randint(1, 4)
                                if player2active == True and player2stay == 0:
                                    p2card_7 = random.randint(1, 4)
                                if dealerstay == 0:
                                    dcard_7 = random.randint(1, 4)
                            elif dice_total >= 20:
                                if player1stay == 0:
                                    p1card_7 = random.randint(10, 13)
                                if player2active == True and player2stay == 0:
                                    p2card_7 = random.randint(10, 13)
                                if dealerstay == 0:
                                    dcard_7 = random.randint(10, 13)
                            else:
                                if player1stay == 0:
                                    p1card_7 = random.randint(5, 9)
                                if player2active == True and player2stay == 0:
                                    p2card_7 = random.randint(5, 9)
                                if dealerstay == 0:
                                    dcard_7 = random.randint(5, 9)
                                    
                            p1card_total = p1card_totalfunc()
                            p2card_total = p2card_totalfunc()
                            dcard_total = dcard_totalfunc()
                            if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                                dealerstay = 1
                            if p1card_total > 23: # waneer moet de speler stoppen
                                player1stay = 1
                        
                            if player1stay == 0 or dealerstay == 0: # kaart 8
                                dice_total = dice5total()
                                if dice_total <= 15:
                                    if player1stay == 0:
                                        p1card_8 = random.randint(1, 4)
                                    if player2active == True and player2stay == 0:
                                        p2card_8 = random.randint(1, 4)
                                    if dealerstay == 0:
                                        dcard_8 = random.randint(1, 4)
                                elif dice_total >= 20:
                                    if player1stay == 0:
                                        p1card_8 = random.randint(10, 13)
                                    if player2active == True and player2stay == 0:
                                        p2card_8 = random.randint(10, 13)
                                    if dealerstay == 0:
                                        dcard_8 = random.randint(10, 13)
                                else:
                                    if player1stay == 0:
                                        p1card_8 = random.randint(5, 9)
                                    if player2active == True and player2stay == 0:
                                        p2card_8 = random.randint(5, 9)
                                    if dealerstay == 0:
                                        dcard_8 = random.randint(5, 9)
                                        
                                p1card_total = p1card_totalfunc()
                                p2card_total = p2card_totalfunc()
                                dcard_total = dcard_totalfunc()            
                                if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                                    dealerstay = 1
                                if p1card_total > 23: # waneer moet de speler stoppen
                                    player1stay = 1
                            
                                if player1stay == 0 or dealerstay == 0: # kaart 9
                                    dice_total = dice5total()
                                    if dice_total <= 15:
                                        if player1stay == 0:
                                            p1card_9 = random.randint(1, 4)
                                        if player2active == True and player2stay == 0:
                                            p2card_9 = random.randint(1, 4)
                                        if dealerstay == 0:
                                            dcard_9 = random.randint(1, 4)
                                    elif dice_total >= 20:
                                        if player1stay == 0:
                                            p1card_9 = random.randint(10, 13)
                                        if player2active == True and player2stay == 0:
                                            p2card_9 = random.randint(10, 13)
                                        if dealerstay == 0:
                                            dcard_9 = random.randint(10, 13)
                                    else:
                                        if player1stay == 0:
                                            p1card_9 = random.randint(5, 9)
                                        if player2active == True and player2stay == 0:
                                            p2card_9 = random.randint(5, 9)
                                        if dealerstay == 0:
                                            dcard_9 = random.randint(5, 9)
                                            
                                    p1card_total = p1card_totalfunc()
                                    p2card_total = p2card_totalfunc()
                                    dcard_total = dcard_totalfunc()            
                                    if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                                        dealerstay = 1
                                    if p1card_total > 23: # waneer moet de speler stoppen
                                        player1stay = 1
                                
                                    if player1stay == 0 or dealerstay == 0: # kaart 10
                                        dice_total = dice5total()
                                        if dice_total <= 15:
                                            if player1stay == 0:
                                                p1card_10 = random.randint(1, 4)
                                            if player2active == True and player2stay == 0:
                                                p2card_10 = random.randint(1, 4)
                                            if dealerstay == 0:
                                                dcard_10 = random.randint(1, 4)
                                        elif dice_total >= 20:
                                            if player1stay == 0:
                                                p1card_10 = random.randint(10, 13)
                                            if player2active == True and player2stay == 0:
                                                p2card_10 = random.randint(10, 13)
                                            if dealerstay == 0:
                                                dcard_10 = random.randint(10, 13)
                                        else:
                                            if player1stay == 0:
                                                p1card_10 = random.randint(5, 9)
                                            if player2active == True and player2stay == 0:
                                                p2card_10 = random.randint(5, 9)
                                            if dealerstay == 0:
                                                dcard_10 = random.randint(5, 9)
                                                
                                        p1card_total = p1card_totalfunc()
                                        p2card_total = p2card_totalfunc()
                                        dcard_total = dcard_totalfunc()
                                        if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                                            dealerstay = 1
                                        if p1card_total > 23: # waneer moet de speler stoppen
                                            player1stay = 1

                                        if player1stay == 0 or dealerstay == 0: # kaart 11
                                            dice_total = dice5total()
                                            if dice_total <= 15:
                                                if player1stay == 0:
                                                    p1card_11 = random.randint(1, 4)
                                                if player2active == True and player2stay == 0:
                                                    p2card_11 = random.randint(1, 4)
                                                if dealerstay == 0:
                                                    dcard_11 = random.randint(1, 4)
                                            elif dice_total >= 20:
                                                if player1stay == 0:
                                                    p1card_11 = random.randint(10, 13)
                                                if player2active == True and player2stay == 0:
                                                    p2card_11 = random.randint(10, 13)
                                                if dealerstay == 0:
                                                    dcard_11 = random.randint(10,13)
                                            else:
                                                if player1stay == 0:
                                                    p1card_11 = random.randint(5, 9)
                                                if player2active == True and player2stay == 0:
                                                    p2card_11 = random.randint(5, 9)
                                                if dealerstay == 0:
                                                    dcard_11 = random.randint(5, 9)
                                                    
                                            p1card_total = p1card_totalfunc()
                                            p2card_total = p2card_totalfunc()
                                            dcard_total = dcard_totalfunc()            
                                            if dcard_total > 23 and dcard_total > p1card_total: # wanneer moet de dealer stoppen
                                                dealerstay = 1
                                            if p1card_total > 23: # waneer moet de speler stoppen
                                                player1stay = 1
                                        
                                        
                                            if player1stay == 0 or dealerstay == 0: # kaart 12
                                                dice_total = dice5total()
                                                if dice_total <= 15:
                                                    if player1stay == 0:
                                                        p1card_12 = random.randint(1, 4)
                                                    if player2active == True and player2stay == 0:
                                                        p2card_12 = random.randint(1, 4)
                                                    if dealerstay == 0:
                                                        dcard_12 = random.randint(1, 4)
                                                elif dice_total >= 20:
                                                    if player1stay == 0:
                                                        p1card_12 = random.randint(10, 13)
                                                    if player2active == True and player2stay == 0:
                                                        p2card_12 = random.randint(10, 13)
                                                    if dealerstay == 0:
                                                        p1dcard_12 = random.randint(10, 13)
                                                else:
                                                    if player1stay == 0:
                                                        p1card_12 = random.randint(5, 9)
                                                    if player2active == True and player2stay == 0:
                                                        p2card_2 = random.randint(5, 9)
                                                    if dealerstay == 0:
                                                        dcard_12 = random.randint(5, 9)

    p1card_total = p1card_totalfunc() # kaarten totaal speler 1
    p2card_total = p2card_totalfunc() # kaarten totaal speler 2
    dcard_total = dcard_totalfunc() # kaarten totaal dealer
   
    #wat gebeurt er bij deze uitkomsten
    if p1card_1 == 1 or p1card_1 + p1card_2 == 26: # checken of speler 1 kupo heeft
        print("kupo player 1")
        player1kupocounter = player1kupocounter + 1
        player1money = player1money + player1inzet * 3
        player1win = 1
        dealerlost = 1
    if p2card_1 == 1 or p2card_1 + p2card_2 == 26: # checken of speler 2 kupo heeft
        print("kupo player 2")
        player2kupocounter = player2kupocounter + 1
        player2money = player2money + player2inzet * 3
        player2win = 1
        dealerlost = 1
    if dcard_1 == 1 or dcard_1 + dcard_2 == 26: # checken of dealer kupo heeft
        print("kupo dealer")
        dealerkupocounter = dealerkupocounter + 1
        player1money = player1money - player1inzet
        dealerwin = 1
        player1lost = 1
    elif p1card_1 + p1card_2 == 14: # checken of speler 1 Kuper heeft
        print("Kuper player 1")
        player1kupercounter = player1kupercounter + 1
        player1money = player1money - player1inzet
        player1lost = 1
        dealerwin = 1
        if p2card_1 + p1card_2 == 14: # checken of speler 2 Kuper heeft
            print("Kuper player 2")
            player2kupercounter = player2kupercounter + 1
            player2money = player2money - player2inzet
            player2lost = 1
            dealerwin = 1
    elif dcard_1 + dcard_2 == 14 and dealerwin == 0: # checken of dealer Kuper heeft
        print("Kuper dealer")
        dealerkupercounter = dealerkupercounter + 1
        player1money = player1money + player1inzet * 2.5
        dealerlost = 1
        player1win = 1
        if player2active == True:
            player2win = 1
    elif p1card_total > 26: # checken of speler 1 bust is
        print("bust player 1")
        player1bustcounter = player1bustcounter + 1
        player1money = player1money - player1inzet
        player1lost = 1
        dealerwin = 1
        if p2card_total > 26: # checken of speler 2 bust is
            print("bust player 2")
            player2bustcounter = player2bustcounter + 1
            player2money = player2money - player2inzet
            player2lost = 1
            dealerwin = 1
    elif dcard_total > 26: # checken of dealer bust is
        print("bust dealer")
        dealerbustcounter = dealerbustcounter + 1
        player1money = player1money + player1inzet
        dealerlost = 1
        player1win = 1
        if player2active == True:
            player2win = 1
    else: # wat gebeurt er als niemand kuper, kupo heeft of bust is
        if player2active == False:
            if p1card_total < 14 and dcard_total < 14: # checken wie er verder van 14 af zit
                if 14 - p1card_total < 14 - dcard_total:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                elif 14 - p1card_total > 14 - dcard_total:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
            elif p1card_total > 14 and dcard_total > 14:
                if p1card_total - 14 > dcard_total - 14:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                elif p1card_total - 14 < dcard_total - 14:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
            elif p1card_total > 14 and dcard_total < 14:
                if p1card_total - 14 > 14 - dcard_total:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                elif p1card_total - 14 < 14 - dcard_total:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                else:
                    player1win = 1
                    dealerwin = 1
            elif p1card_total < 14 and dcard_total > 14:
                if 14 - p1card_total > dcard_total - 14:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                elif 14 - p1card_total < dcard_total - 14:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                else:
                    player1win = 1
                    dealerwin = 1
            elif p1card_total == 14:
                player1lost = 1
                dealerwin = 1
                player1money = player1money - player1inzet
            elif dcard_total == 14:
                player1win = 1
                dealerlost = 1
                player1money = player1money + player1inzet

        if player2active == True:
            if p1card_total < 14 and dcard_total < 14 and p2card_total < 14: # checken wie er verder van 14 af zit
                if 14 - p1card_total < 14 - dcard_total:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if 14 - p2card_total < 14 - dcard_total:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if 14 - p1card_total > 14 - dcard_total:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if 14 - p2card_total > 14 - dcard_total:
                    dealerwin = 1
                    player2lost = 1
                    player2money = player2money - player2inzet
                if 14 - p1card_total == 14 - dcard_total or 14 - p2card_total == 14 - dcard_total:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1
            elif p1card_total > 14 and dcard_total > 14 and p2card_total > 14:
                if p1card_total - 14 > dcard_total - 14:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if p2card_total - 14 > dcard_total - 14:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if p1card_total - 14 < dcard_total - 14:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if p2card_total - 14 < dcard_total - 14:
                    dealerwin = 1
                    player2lost = 1
                    player2money = player2money - player2inzet
                if p1card_total - 14 == dcard_total - 14 or p2card_total - 14 == dcard_total - 14:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1
            elif p1card_total > 14 and dcard_total < 14 and p2card_total < 14:
                if p1card_total - 14 > 14 - dcard_total:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if 14 - p2card_total < 14 - dcard_total:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if 14 - p2card_total > 14 - dcard_total:
                    dealerwin = 1
                    player2lost = 1
                    player2money = player2money - player2inzet
                if p1card_total - 14 < 14 - dcard_total:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if p1card_total - 14 == 14 - dcard_total or 14 - p2card_total == 14 - dcard_total:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1
            elif p1card_total < 14 and dcard_total > 14 and p2card_total < 14:
                if 14 - p1card_total > dcard_total - 14:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if p2card_total - 14 > 14 - dcard_total:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if 14 - p1card_total < dcard_total - 14:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if p2card_total - 14 < 14 - dcard_total:
                    dealerwin = 1
                    player2lost = 1
                    player2money = player2money - player2inzet
                if 14 - p1card_total == dcard_total - 14 or p2card_total - 14 == 14 - dcard_total:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1
            elif p1card_total < 14 and dcard_total > 14 and p2card_total > 14:
                if 14 - p1card_total > dcard_total - 14:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if p2card_total - 14 > dcard_total - 14:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if 14 - p1card_total < dcard_total - 14:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if p2card_total - 14 < dcard_total - 14:
                    dealerwin = 1
                    player2lost = 1
                    player2money = player2money - player2inzet
                if 14 - p1card_total == dcard_total - 14 or p2card_total - 14 == dcard_total - 14:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1
            elif p1card_total < 14 and dcard_total < 14 and p2card_total > 14:
                if 14 - p1card_total > 14 - dcard_total:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if p2card_total - 14 > 14 - dcard_total:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if 14 - p1card_total < 14 - dcard_total:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if p2card_total - 14 < 14 - dcard_total:
                    player2lost = 1
                    dealerwin = 1
                    player2money = player2money - player2inzet
                if 14 - p1card_total == dcard_total - 14 or p2card_total - 14 == dcard_total - 14:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1
            elif p1card_total > 14 and dcard_total < 14 and p2card_total > 14:
                if p1card_total - 14 > 14 - dcard_total:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if p2card_total - 14 > 14 - dcard_total:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if p1card_total - 14 < 14 - dcard_total:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if p2card_total - 14 < 14 - dcard_total:
                    player2lost = 1
                    dealerwin = 1
                    player2money = player2money - player2inzet
                if 14 - p1card_total == dcard_total - 14 or p2card_total - 14 == dcard_total - 14:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1
            elif p1card_total > 14 and dcard_total > 14 and p2card_total < 14:
                if p1card_total - 14 > dcard_total - 14:
                    player1win = 1
                    dealerlost = 1
                    player1money = player1money + player1inzet
                if p2card_total - 14 > 14 - dcard_total:
                    player2win = 1
                    dealerlost = 1
                    player2money = player2money + player2inzet
                if p1card_total - 14 < dcard_total - 14:
                    dealerwin = 1
                    player1lost = 1
                    player1money = player1money - player1inzet
                if p2card_total - 14 < 14 - dcard_total:
                    dealerwin = 1
                    player2lost = 1
                    player2money = player2money - player2inzet
                if 14 - p1card_total == dcard_total - 14 or p2card_total - 14 == dcard_total - 14:
                    player1win = 1
                    player2win = 1
                    dealerwin = 1

            if p1card_total == 14:
                player1lost = 1
                dealerwin = 1
                player1money = player1money - player1inzet
            if p2card_total == 14:
                player2lost = 1
                dealerwin = 1
            if dcard_total == 14:
                player1win = 1
                dealerlost = 1
                player1money = player1money + player1inzet
       
    #wie wint?
    # hier ff 2 speler wincheck inplementeren
    if player1win == 1 and dealerwin == 1 or player1lost == 1 and dealerlost == 1 or p1card_total == dcard_total:
        print("push")
        pushcounter = pushcounter + 1
    elif dealerwin == 1 and player1lost == 1:
        print("Dealer Wins!")
        dealerwincounter = dealerwincounter + 1
    elif player1win == 1 and dealerlost == 1:
        print("Player Wins!")
        player1wincounter = player1wincounter + 1

#conclusies/output
pushpercentage = round(pushcounter / rounds * 100, 2) # percentages uitrekenen
player1winpercentage = round(player1wincounter / rounds * 100, 2)
dealerwinpercentage = round(dealerwincounter / rounds * 100, 2)
lossperround = player1money / rounds
roundtest = player1wincounter + dealerwincounter + pushcounter    
print("")
print("Player1bustcounter:", player1bustcounter)
print("Player1kupocounter:", player1kupocounter)
print("Player1kupercounter:", player1kupercounter)
print("")
print("Dealerbustcounter:", dealerbustcounter)
print("Dealerkupocounter:", dealerkupocounter)
print("Dealerkupercounter:", dealerkupercounter)
print("")
print("pushcounter:", pushcounter)
print("Player 1 Wins:", player1wincounter)
print("Dealer Wins:", dealerwincounter)
print("")
print("")
print("pushpercentage", pushpercentage,"%")
print("Player1winpercentage", player1winpercentage,"%")
print("Dealerwinpercentage", dealerwinpercentage,"%")
print("")
print("")
print("player1money", player1money)
print("average loss per round", lossperround)
if diagnostic == 1: # extra outputs voor troubleshooting
    print("p1card_1", p1card_1)
    print("p1card_2", p1card_2)
    print("p1card_3", p1card_3)
    print("p1card_4", p1card_4)
    print("p1card_5", p1card_5)
    print("player1stay", player1stay)
    print("p1card_total", p1card_total)
    print("player1win:", player1win)
    print("player1lost:", player1lost)
    print("dcard_1", dcard_1)
    print("dcard_2", dcard_2)
    print("dcard_3", dcard_3)
    print("dcard_4", dcard_4)
    print("dcard_5", dcard_5)
    print("dealerstay", dealerstay)
    print("dcard_total", dcard_total)
    print("dealerwin:", dealerwin)
    print("dealerlost:", dealerlost)
    print("round test:", roundtest)
