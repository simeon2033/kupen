import random
import numpy as np
roundnm = 0 # variabelen resetten aan het begin van de simulatie (de meeste spreken voor zich)
aantal1en = aantal2en = aantal3en = aantal4en = aantal5en = aantal6en = aantal7en = aantal8en = aantal9en = aantal10en = aantal11en = aantal12en = aantal13en = 4
stapel1 = [1]*aantal1en + [2]*aantal2en + [3]*aantal3en + [4]*aantal4en # een lijst van alle kaarten in stapel 1, de variabelen zoals "aantal1en" geven aan hoeveel er nog van die kaart in de stapel zit, dus als er een 1 is gepakt is de kans op nog een 1 kleiner om dat die dan minder "gewicht" heeft
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
player2active = True # dit geeft aan of speler 2 meedoet
diagnostic = False # geeft aan of ik diagnostische data wil om dingen te fixen
winoutput = False # geeft aan of ik elke keer dat iemand wint een output wil
rounds = 100000 # geeft het aantal te simuleren rondes aan
roundtest = p1pushcounter + dealerwincounterfrp1 + dealerwincounterfrp2 + player1wincounter + p2pushcounter

def dice5total(): # deze functie rolt de 5 dobbelstenen
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

while roundnm < rounds: # deze while loop runt de simulatie voor een X aantal rondes
    roundnm = roundnm + 1
    player1money = player1money - player1inzet # geld wordt ingezet
    if player2active == True:
        player2money = player2money - player2inzet # hieronder zetten we alle variabelen die naar iets moeten aan het begin van elke ronde
    p1card = np.zeros(12)
    p2card = np.zeros(12)
    dcard = np.zeros(12)
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

    # Dit stuk van de Code trekt de eerste kaart voor iedereen, dit stuk wordt grotendeels herhaald voor elke kaart (hier leg ik het geheel uit straks is het gewoon hetzelfde)
    for n in range(12):
        if player1stay == 0 or dealerstay == 0 or player2stay == 0: # kaart 2 wordt alleen gepakt als er nog iemand een kaart wil
            dice_total = dice5total() # grotendeels hetzelfde als kaart 1
            if dice_total <= 15:
                if player1stay == 0: # enige verschil met kaart 1 is dat hij nu checkt of elke speler nog een kaart wil
                    p1card[n] = random.choice(stapel1)
                    if p1card[n] == 1 and aantal1en > 0:
                        aantal1en = aantal1en - 1
                    elif p1card[n] == 2 and aantal2en > 0:
                        aantal2en = aantal2en - 1
                    elif p1card[n] == 3 and aantal3en > 0:
                        aantal3en = aantal3en - 1
                    elif p1card[n] == 4 and aantal4en > 0:
                        aantal4en = aantal4en - 1
                if player2active == True and player2stay == 0:
                    p2card[n] = random.choice(stapel1)
                    if p2card[n] == 1 and aantal1en > 0:
                        aantal1en = aantal1en - 1
                    elif p2card[n] == 2 and aantal2en > 0:
                        aantal2en = aantal2en - 1
                    elif p2card[n] == 3 and aantal3en > 0:
                        aantal3en = aantal3en - 1
                    elif p2card[n] == 4 and aantal4en > 0:
                        aantal4en = aantal4en - 1
                if dealerstay == 0:
                    dcard[n] = random.choice(stapel1)
                    if dcard[n] == 1 and aantal1en > 0:
                        aantal1en = aantal1en - 1
                    elif dcard[n] == 2 and aantal2en > 0:
                        aantal2en = aantal2en - 1
                    elif dcard[n] == 3 and aantal3en > 0:
                        aantal3en = aantal3en - 1
                    elif dcard[n] == 4 and aantal4en > 0:
                        aantal4en = aantal4en - 1
            elif dice_total >= 20:
                if player1stay == 0:
                    p1card[n] = random.choice(stapel3)
                    if p1card[n] == 10 and aantal10en > 0:
                        aantal10en = aantal10en - 1
                    elif p1card[n] == 11 and aantal11en > 0:
                        aantal11en = aantal11en - 1
                    elif p1card[n] == 12 and aantal12en > 0:
                        aantal12en = aantal12en - 1
                    elif p1card[n] == 13 and aantal13en > 0:
                        aantal13en = aantal13en - 1
                if player2active == True and player2stay == 0:
                    p2card[n] = random.choice(stapel3)
                    if p2card[n] == 10 and aantal10en > 0:
                        aantal10en = aantal10en - 1
                    elif p2card[n] == 11 and aantal11en > 0:
                        aantal11en = aantal11en - 1
                    elif p2card[n] == 12 and aantal12en > 0:
                        aantal12en = aantal12en - 1
                    elif p2card[n] == 13 and aantal13en > 0:
                        aantal13en = aantal13en - 1
                if dealerstay == 0:
                    dcard[n] = random.choice(stapel3)
                    if dcard[n] == 10 and aantal10en > 0:
                        aantal10en = aantal10en - 1
                    elif dcard[n] == 11 and aantal11en > 0:
                        aantal11en = aantal11en - 1
                    elif dcard[n] == 12 and aantal12en > 0:
                        aantal12en = aantal12en - 1
                    elif dcard[n] == 13 and aantal13en > 0:
                        aantal13en = aantal13en - 1
            else:
                if player1stay == 0:
                    p1card[n] = random.choice(stapel2)
                    if p1card[n] == 5 and aantal5en > 0:
                        aantal5en = aantal5en - 1
                    elif p1card[n] == 6 and aantal6en > 0:
                        aantal6en = aantal6en - 1
                    elif p1card[n] == 7 and aantal7en > 0:
                        aantal7en = aantal7en - 1
                    elif p1card[n] == 8 and aantal8en > 0:
                        aantal8en = aantal8en - 1
                    elif p1card[n] == 9 and aantal9en > 0:
                        aantal9en = aantal9en - 1
                if player2active == True and player2stay == 0:
                    p2card[n] = random.choice(stapel2)
                    if p2card[n] == 5 and aantal5en > 0:
                        aantal5en = aantal5en - 1
                    elif p2card[n] == 6 and aantal6en > 0:
                        aantal6en = aantal6en - 1
                    elif p2card[n] == 7 and aantal7en > 0:
                        aantal7en = aantal7en - 1
                    elif p2card[n] == 8 and aantal8en > 0:
                        aantal8en = aantal8en - 1
                    elif p2card[n] == 9 and aantal9en > 0:
                        aantal9en = aantal9en - 1
                if dealerstay == 0:
                    dcard[n] = random.choice(stapel2)
                    if dcard[n] == 5 and aantal5en > 0:
                        aantal5en = aantal5en - 1
                    elif dcard[n] == 6 and aantal6en > 0:
                        aantal6en = aantal6en - 1
                    elif dcard[n] == 7 and aantal7en > 0:
                        aantal7en = aantal7en - 1
                    elif dcard[n] == 8 and aantal8en > 0:
                        aantal8en = aantal8en - 1
                    elif dcard[n] == 9 and aantal9en > 0:
                        aantal9en = aantal9en - 1
        
            p1card_total = sum(p1card)
            p2card_total = sum(p2card)
            dcard_total = sum(dcard)
            if dcard_total > 23 and (dcard_total > p1card_total or (dcard_total > p2card_total and p2card[1] != 0)): # wanneer moet de dealer stoppen
                dealerstay = 1
            if p1card_total > 23: # waneer moet speler 1 stoppen
                player1stay = 1
            if p2card_total > 23: # waneer moet speler 2 stoppen
                player2stay = 1
   
    #wat gebeurt er bij de speciale uitkomsten
    if p1card[1] == 1 or p1card[1] + p1card[2] == 26: # checken of speler 1 kupo heeft
        if winoutput == True: # wil ik een output voor elke win (zie line 36)
            print("kupo player 1")
        player1kupocounter = player1kupocounter + 1 # hoeveel keer heeft speler 1 kupo gehad
        player1win = 1
        dealerlostfrp1 = 1
    if p2card[1] == 1 or p2card[1] + p2card[2] == 26: # checken of speler 2 kupo heeft
        if winoutput == True:
            print("kupo player 2")
        player2kupocounter = player2kupocounter + 1
        player2win = 1
        dealerlostfrp2 = 1
    if dcard[1] == 1 or dcard[1] + dcard[2] == 26: # checken of dealer kupo heeft
        if winoutput == True:
            print("kupo dealer")
        dealerkupocounter = dealerkupocounter + 1
        dealerwinfrp1 = 1
        player1lost = 1
        if player2active == True:
            dealerwinfrp2 = 1
            player2lost = 1
    if (dcard[1] == 1 or dcard[1] + dcard[2] == 26) and (p1card[1] == 1 or p1card[1] + p1card[2] == 26):
        pushp1 = 1 # checken of speler 1 en de dealer beiden kupo hadden
    elif p1card[1] == 1 or p1card[1] + p1card[2] == 26: # er was geen push
        player1money = player1money + player1inzet * (kupokuperwinmultiplier - normalwinmultiplier) # geld wat speler 1 krijgt als hij Kupo heeft of de dealer Kuper
    if ((dcard[1] == 1 or dcard[1] + dcard[2] == 26) and (p2card[1] == 1 or p2card[1] + p2card[2] == 26)) and player2active == True:
        pushp2 = 1 # checken of speler 2 push had
    elif p2card[1] == 1 or p2card[1] + p2card[2] == 26:
        player2money = player2money + player2inzet * (kupokuperwinmultiplier - normalwinmultiplier) # geld voor speler 2
    if p1card[1] + p1card[2] == 14: # checken of speler 1 Kuper heeft
        if winoutput == True:
            print("Kuper player 1")
        player1kupercounter = player1kupercounter + 1
        player1lost = 1
        dealerwinfrp1 = 1
    if p2card[1] + p2card[2] == 14: # checken of speler 2 Kuper heeft
        if winoutput == True:
            print("Kuper player 2")
        player2kupercounter = player2kupercounter + 1
        player2lost = 1
        dealerwinfrp2 = 1
    if dcard[1] + dcard[2] == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0): # checken of dealer Kuper heeft
        if winoutput == True:
            print("Kuper dealer")
        dealerkupercounter = dealerkupercounter + 1
        dealerlostfrp1 = 1
        player1win = 1
        if player2active == True:
            player2win = 1
            dealerlostfrp2 = 1
    if (dcard[1] + dcard[2] == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0)) and p1card[1] + p1card[2] == 14: # wederom pushes checken en geld geven
        pushp1 = 1
    elif dcard[1] + dcard[2] == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0):
        player1money = player1money + player1inzet * (kupokuperwinmultiplier - normalwinmultiplier)
    if player2active == True and ((dcard[1] + dcard[2] == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0)) and p2card[1] + p2card[2] == 14):
        pushp2 = 1
    elif dcard[1] + dcard[2] == 14 and (dealerwinfrp1 == 0 or dealerwinfrp2 == 0):
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
            
    if player2active == False and dealerlostfrp1 == 0 and dealerwinfrp1 == 0 and player1win == 0 and player1lost == 0: # wat gebeurt er als niemand kuper, kupo heeft of bust is (dit is de code in het geval dat Speler 2 niet mee doet (toch nog een beetje geoptimaliseerd:)))
        if p1card_total < 14 and dcard_total < 14: # berekenen wie er verder van 14 af zit in dit geval
            if 14 - p1card_total > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            elif 14 - p1card_total < 14 - dcard_total:
                dealerwin = 1
                player1lostfrp1 = 1
            else:
                pushp1 = 1
        elif p1card_total > 14 and dcard_total > 14: # berekenen wie er verder van 14 af zit in dit geval
            if p1card_total - 14 > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            elif p1card_total - 14 < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            else:
                pushp1 = 1
        elif p1card_total > 14 and dcard_total < 14: # berekenen wie er verder van 14 af zit in dit geval
            if p1card_total - 14 > 14 - dcard_total:
                player1win = 1
                dealerlostfrp1 = 1
            elif p1card_total - 14 < 14 - dcard_total:
                dealerwinfrp1 = 1
                player1lost = 1
            else:
                pushp1 = 1
        elif p1card_total < 14 and dcard_total > 14: # berekenen wie er verder van 14 af zit in dit geval
            if 14 - p1card_total > dcard_total - 14:
                player1win = 1
                dealerlostfrp1 = 1
            elif 14 - p1card_total < dcard_total - 14:
                dealerwinfrp1 = 1
                player1lost = 1
            else:
                pushp1 = 1
        elif p1card_total == 14: # wat als het totaal precies 14 is
            player1lost = 1
            dealerwinfrp1 = 1
        elif dcard_total == 14:
            player1win = 1
            dealerlostfrp1 = 1
        elif p1card_total == 14 and dcard_total == 14:
            pushp1 = 1

    if player2active == True and ((dealerlostfrp1 == 0 and dealerwinfrp1 == 0 and player1win == 0 and player1lost == 0) or (dealerlostfrp2 == 0 and dealerwinfrp2 == 0  and player2win == 0 and player2lost == 0)): # wat als niemand bust is kupo of kuper heeft en speler 2 meedoet?
        if p1card_total == 14: # wat als het totaal precies 14 is
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
        if p1card_total < 14 and dcard_total < 14 and p2card_total < 14: # checken wie er verder van 14 af zit in dit geval (hieronder is voor elk geval de wiskundige berekening beschreven dit hij moet uitvoeren)
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
    #wie wint? dit kijkt naar de winvariabelen en geeft geld
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
print("Player1bustcounter:", player1bustcounter) # tekst output aan het einde van de simulatie
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
    print("p1card[1]", p1card[1])
    print("p1card[2]", p1card[2])
    print("p1card[3]", p1card[3])
    print("p1card[4]", p1card[4])
    print("p1card[5]", p1card[5])
    print("player1stay", player1stay)
    print("p1card_total", p1card_total)
    print("player1win:", player1win)
    print("player1lost:", player1lost)
    if player2active == True:
        print("p2card[1]", p2card[1])
        print("p2card[2]", p2card[2])
        print("p2card[3]", p2card[3])
        print("p2card[4]", p2card[4])
        print("p2card[5]", p2card[5])
        print("player2stay", player2stay)
        print("p2card_total", p2card_total)
        print("player2win:", player2win)
        print("player2lost:", player2lost)
    print("dcard[1]", dcard[1])
    print("dcard[2]", dcard[2])
    print("dcard[3]", dcard[3])
    print("dcard[4]", dcard[4])
    print("dcard[5]", dcard[5])
    print("dealerstay", dealerstay)
    print("dcard_total", dcard_total)
    print("dealerwinfrp1:", dealerwinfrp1)
    print("dealerlostfrp1:", dealerlostfrp1)
    if player2active == True:
        print("dealerwinfrp2:", dealerwinfrp2)
        print("dealerlostfrp2:", dealerlostfrp2)
    print("round test:", roundtest)