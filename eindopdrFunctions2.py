import time
import random
import sys
from colorama import Fore, init
from functions import *

#lijsten met verhaal stukjes en antwoord opties
verhaalLijst = ["NUL",
                "Welkom bij mijn eindopdracht van periode 1 Hello You, ik heb een textbased applicatie gemaakt die je een verhaal zal laten beleven.",
                "Hierin ben jij de hoofdpersoon, en kan je zelf keuzes maken om te zien hoe het verhaal verder gaat en uiteindelijk afloopt. wil je beginnen?",
                "Leuk dat je wilt beginnen, om keuzes te maken typ je alleen de letter die ervoor staat, dus bijvoorbeeld a of b, (Let op! het is hoofdletter gevoelig!)",
                "Jammer, tot n andere keer!",
                "Je zit in het examenjaar van je opleiding op met MA, maar jullie klas heeft nog 1 belangrijke toets gemist van het begin van het jaar,",
                "opzich sta je er prima voor, dus de kans is groot dat je het haalt, wat doe je?",
                "Okee lekker zelfverzekerd, nu hopen dat het goedkomt!",
                "Jammer, de toets weegt zwaarder mee dan je dacht, je bent niet geslaagd en moet het jaar over doen, je kan dus niet komend jaar naar het buitenland. Volgende keer beter!",
                "Luckyyy! Je stond er al goed voor, het was dus niet zo erg dat je niet alles wist. je bent geslaagd en krijgt een uitnodiging binnen voor je diploma uitreiking,",
                "eenmaal daar die je veel docenten weer en praat je bij met je klasgenoten, je verteld ze over de reis naar het buitenland die je wilt gaan maken, spannend! Ga je met het vliegtuig of rijden?",
                "Slim! Je slaagt en hebt je vakantie dubbel verdient!",
                "Je krijgt een uitnodiging binnen voor je diploma uitreiking, eenmaal daar die je veel docenten weer en praat je bij met je klasgenoten,\nje verteld ze over de reis naar het buitenland die je wilt gaan maken, spannend!",
                "Prima! Je vliegt overmorgen om 6:15 naar Palermo in Sicilië",
                "hier ben je al een keer met je schoonfamilie geweest en het was ongelofelijk mooi, je gaat vanavond afscheid nemen",
                "ze willen wel graag op bezoek komen en helpen je alvast met inpakken, zo kan je rustig je vakantie in gaan.",
                "De volgende ochtend ga je met het OV naar Schiphol, je appt iedereen je vluchtnummer en gegevens en zoekt je gate om in te checken,",
                "even later, nog voordat je bij security bent lijkt het alsof je iemand herkent, je kan alleen niet plaatsen wie het is of waarvan je hem kent, wat doe je?",
                "Hahaha, in al je enthousiasme ben je vergeten dat je geen rijbewijs hebt",
                "je kan nog een last minute vliegticket proberen te scoren dan ben je er snel, of je kan gaan liften, misschien leer je wel allemaal leuke mensen kennen!",
                "Gelukkig kunnen je ouders kunnen je wegbrengen richting de grens maar vanaf daar moet je het toch echt zelf gaan doen.",
                "Je hebt een koffertje en rugzak mee, je wacht op een tankstation op mensen die je aardig lijken, en je stapt je in, zo ga je de komende dagen reizen en kom je van alles te weten en leer je nieuwe dingen.",
                "Zo kwam je een astronoom tegen, en wist je bijvoorbeeld dat de zonsopgang op mars niet roze of oranje is, maar blauw?",
                "Zo kom je nog veel meer leuke mensen tegen, na een tijdje ben je bij een leuk eettentje wat gaan eten en opzoek gegaan naar een nieuw iemand om mee te rijden. plots zie je iemand die je lijkt te herkennen maar kan niet plaatsen wie het is",
                "Hij draait zich het blijkt Milos te zijn! Hij was onderweg op vakantie en je stapt in, jullie hebben veel bij te praten na al het liften wat je al gedaan hebt.",
                "Na 2 jaar op het mediacollege heb je je eigen bedrijf je opgericht waar je veel over wilt vertellen.",
                "Jullie zijn zoveel aan het praten dat jullie de afslag hebben gemist! Jullie rijden langs een rustig tankstation om wat te eten te halen,",
                "Na een half uur gewacht te hebben en een stuk gelopen te hebben zie je twee auto’s staan bij een ander tankstation,",
                "Gezellig! Ze zijn onderweg richting Italië, daar wilde je al graag heen, ze hebben met zn alle een bus gehuurd waar je de komende week in mee kan.",
                "Jullie hebben het heel gezellig, nieuwe mensen leren kennen en nieuwe dingen proberen houd je van!",
                "Na 2,5 week het leuk gehad met al deze mensen overweeg je om weer verder te liften, ga je dat ook doen? Er is vanavond een feetje op het stand,  wil je nog 1 weekend blijven?",
                "Het was heel gezellig, maar je gaat weer door, de groep zet je af bij een groot winkelcentrum met allemaal verschillende winkels, terwijl je rond loopt kom je een makelaars bedrijfje tegen.",
                "Ze verkopen allerlei leuke huisjes, precies goed voor 2 personen, en zelf met een zwembad erbij, heerlijk voor de zomer!",
                "Dit is perfect denk je, dus je belt je vriend op, hij is heel blij om te horen dat je een leuke plek gevonden hebt en hij boekt meteen een ticket naar je toe.",
                "Jullie kopen het huis en hebben het ongelofelijk naar jullie zin daar, je hebt goede keuzes gemaakt, congrats!",
                "Hij draait zich om en heeft een grijns op zn gezicht, opeens is iedereen om je heen weg, hij loopt langzaam in jou richting, je staat stil van schrik.",
                "Hij begint steeds sneller begint te lopen en je begint te rennen, ga je het bos in of ren je door de straat op zoek naar andere mensen om je te helpen?",
                "Je rent het bos in met de hoop dat je die man kwijtraakt, je raakt alleen zo erg in paniek dat je wat paden in rent, links, rechts, rechts, links, naar een paar minuten ben je hem kwijt, maar ben je ook de weg kwijt...",
                "Je komt het bos niet meer uit, je moet hier nu zien te overleven en hopen dat je nog mensen al zien binnekort, succes..... ",
                "Je rent de straat uit en in de verte zie je twee lampen wat wel koplampen lijken, ze komen naar je toe!",
                "Je rent erheen en begint te zwaaien zodat ze je goed kunnen zien, ze remmen zodat je kan instappen en met ze mee kan rijden.",
                "Je bent snel de bus in gesprongen en jullie rijden weg, het is een gezellige vriendengroep die je tegen bent gekomen, wat een geluk.",
                "Ze vragen of je zin hebt de komende tijd met ze mee te rijden, ze doen een roadtrip door Europa, Natuurlijk wil je dat! ",
                "Enjoy! Er is een feest op het strand, jullie hebben te tijd van jullie leven en gaan helemaal los, een favoriete band is er jullie zingen keihard mee.",
                "T festival gaat door tot vroeg in de ochtend, en opeens sta je backstage, in je dronken bui heb je gitaar gespeeld en dat is de band opgevallen.",
                "Ze vragen je een liedje met hun te spelen en mee te gaan naar hun volgende show, of je dat wil?",
                "Je stapt in bij de man die naar je zwaait, hij ziet er een beetje raar uit, maar ja je denkt er niet te veel van.",
                "Later merk je aan hem dat hij gedronken heeft, je komt bijna bij een plek om te slapen, nog een kwartiertje, blijf je zitten of stap je uit?",
                "Helaas, hij heeft veel dronken en bij een bocht raakt de auto van de weg en vliegen jullie het dal in, je overleeft het niet.",
                "Heel slim van je! Later hoor je dat de man verongelukt is, je hebt goede keuzes gemaakt! Well done! 😊",
                "Je neemt bij de show op het strand afscheid van je groep en vliegt met de band mee naar Nederland waar de volgende show is, het publiek gaat los en je geniet er enorm van",
                "opeens valt je oog op je vrienden van het MA en besluit je dat het goed zo is, je maakt de show af en bedankt de band, het is goed zo.",
                "Wat heb je ongelofelijk genoten afgelopen maanden, maar je bent weer thuis"
                "Goede keuze! Jij bent de gene die vanavond iedereen veilig mee neemt naar een plek om te slapen vannacht, je hebt het heel erg naar je zin gehad vannacht en besluit bij deze groep te blijven.",
                "Wie weet wat het je allemaal nog gaat brengen.",
                "na het vliegen wil je gaan roadtrippen door italie, en gaan liften, je wacht bij het vliegveld waar je net geland bent,"]

antwoordlijst = [Fore.GREEN +"nul", "A, je red het wel, je staat er goed voor dus leren is niet nodig\nB, Voor de zekerheid ga je er toch nog voor het is je allerlaatste toets",
                 "A, Vliegen, dan ben je er sneller\nB, Rijden! muziek aan en genieten van de omgevingen waar je doorheen rijd!",
                 "A, Ach joh, liften is prima, misschien dat je nog leuke mensen leert kennen\nB, Doe dan maar het vliegtuig, ben je er sneller",
                 "A, Je rent het bos in, dan ben je hem zo snel mogelijk kwijt\nB, Je rent de straat door in de hoop andere mensen tegen te komen",
                 "A, Met de groep vrienden, ze zien er gezellig uit!\nB, Doe maar die meneer met zn hond, hij gebaart dat je mee mag",
                 "A, Iets voelt niet goed, je stapt toch maar uit\nB, Er zal vast niks zijn, het is je eerste keer liften dus dat geeft misschien spanning, ik  blijf zitten",
                 "A, Natuurlijk ga je nog een weekendje los, je leeft maar een keer\nB, Nee het is goed zo, je gaat weer nieuwe mensen zoeken",
                 "A, Jaaa natuurlijk! met je favo band op het podium staan, wie wil dat nou niet\nB, Je bent te zenuwchtig en hebt je vrienden al een tijd niet gezien, hell no!",
                 "A, Ja\nB, Nee",  "A, Ja\nB, Nee" + Fore.RESET]

#functions voor het uiterlijk van de code en het makkelijker maken

def slow_chat(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.015)

def printVerhaal(text):
    slow_chat(Fore.CYAN + verhaalLijst[text] + Fore.RESET + "\n")

def printAntwoord(antwoord):
    return (Fore.GREEN + antwoordlijst[antwoord] + Fore.RESET + "\n")

def ongeldig():
    print("Dit was geen geldig antwoord, probeer het opnieuw")


# functions per antwoord optie

def intro1():
    print("\n\n")
    print("""██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝""")
    print("\n")
    q = input(Fore.RED + "Voor de leukste werking van mijn geschreven programma, gebruik: Colorama.\nDruk op Enter om door te gaan." + Fore.RESET)
    print("\n\n")

def intro2():
    printVerhaal(1)
    printVerhaal(2)
antwoord9 = input(printAntwoord(9))

def a9 ():
    printVerhaal(3)
    time.sleep(2)
    printVerhaal(5)
    printVerhaal(6)

def b9():
    printVerhaal(4)

def a1():
    printVerhaal(7)
    dice1 = (random.randint(1, 100))

    if dice1 > 35:
        printVerhaal(8)

    elif dice1 <= 35:
        printVerhaal(9)
        time.sleep(2)
        printVerhaal(12)
        printVerhaal(10)
        antwoord2 = input(printAntwoord(2))

def b1():
    printVerhaal(11)
    time.sleep(2)
    printVerhaal(12)
    printVerhaal(10)

def a2():
    printVerhaal(13)
    printVerhaal(15)
    time.sleep(1.5)
    printVerhaal(55)
    time.sleep(1)

def b2():
    printVerhaal(18)
    printVerhaal(19)

def a3():
    printVerhaal(20)
    printVerhaal(21)
    printVerhaal(22)
    printVerhaal(23)
    dice2 = (random.randint(1, 100))
    return dice2
dice2 = a3

def b3():
    printVerhaal(13)
    printVerhaal(15)
    time.sleep(1.5)
    printVerhaal(55)
    printVerhaal(27)

def diceK50():
    print(verhaalLijst[24] + "\n" + verhaalLijst[25])
    time.sleep(1.5)
    printVerhaal(26)
    time.sleep(1.5)
    printVerhaal(27)

def diceG50():
    printVerhaal(35)
    printVerhaal(36)

def a4():
    printVerhaal(37)
    printVerhaal(38)

def b4():
    printVerhaal(39)
    printVerhaal(40)
    printVerhaal(41)
    time.sleep(2)
    printVerhaal(42)
    time.sleep(1)
    printVerhaal(30)

def a5():
    printVerhaal(28)
    printVerhaal(29)
    time.sleep(1.5)
    printVerhaal(30)

def b5():
    printVerhaal(46)
    printVerhaal(47)

def a6():
    printVerhaal(49)

def b6():
    printVerhaal(48)

def a7():
    printVerhaal(43)
    printVerhaal(44)
    printVerhaal(45)

def b7():
    printVerhaal(31)
    printVerhaal(32)
    printVerhaal(33)
    printVerhaal(34)

def a8():
    printVerhaal(50)
    printVerhaal(51)
    printVerhaal(52)

def b8():
    printVerhaal(53)
    printVerhaal(54)

#code van antwoord naar vraag naar antwoord enz
intro1()
intro2()
antwoord9 = input(printAntwoord(9))
# -------------------------------------
if antwoord9 == "A":
    a9()
    antwoord1 = input(printAntwoord(1))

elif antwoord9 == "B":
    b9()
    antwoord1 = input(printAntwoord(1))

if antwoord9 != "A" and antwoord9 != "B":
    ongeldig()
    intro2()
    antwoord9 = input(printAntwoord(9))
# -------------------------------------
if antwoord1 == "A":
    a1()
    antwoord2 = input(printAntwoord(2))

elif antwoord1 == "B":
    b1()
    antwoord2 = input(printAntwoord(2))

if antwoord1 != "A" and antwoord1 != "B" and antwoord9 == "A":
    ongeldig()
    a9()
    antwoord1 = input(printAntwoord(1))

if antwoord1 != "A" and antwoord1 != "B" and antwoord9 == "B":
    ongeldig()
    b9()
    antwoord1 = input(printAntwoord(1))
# ------------------------------------- 
if antwoord2 == "A":
    a2()
    antwoord5 = input(printAntwoord(5))

elif antwoord2 == "B":
    b2()
    antwoord3 = input(printAntwoord(3))

if antwoord2 != "A" and antwoord2 != "B" and antwoord1 == "A":
    ongeldig()
    a1()
    antwoord2 = input(printAntwoord(2))

if antwoord2 != "A" and antwoord2 != "B" and antwoord1 == "B":
    ongeldig()
    b1()
    antwoord2 = input(printAntwoord(2))
# -------------------------------------
if antwoord3 == "A":
    a3()

elif antwoord3 == "B":
    b3()
    antwoord5 = input(printAntwoord(5))

if dice2 > 50:
    diceK50()
    antwoord5 = input(printAntwoord(5))

elif dice2 <= 50:
    diceG50()
    antwoord4 = input(printAntwoord(4))

if antwoord3 != "A" and antwoord3 != "B" and antwoord2 == "A":
    ongeldig()
    a2()
    antwoord5 = input(printAntwoord(5))

if antwoord3 != "A" and antwoord3 != "B" and antwoord2 == "B":
    ongeldig()
    b2()
    antwoord3 = input(printAntwoord(3))
# ------------------------------------- klopt tm hier
if antwoord4 == "A":
    a4()

elif antwoord4 == "B":
    b4()
    antwoord7 = input(printAntwoord(7))

if antwoord4 != "A" and antwoord4 != "B" and antwoord3 == "A":
    ongeldig()
    a3()
    if dice2 > 50:
        diceK50()
        antwoord5 = input(printAntwoord(5))

    elif dice2 <= 50:
        diceG50()
        antwoord4 = input(printAntwoord(4))
# -------------------------------------
if antwoord5 == "A":
    a5()
    antwoord7 = input(printAntwoord(7))

elif antwoord5 == "B":
    b5()
    antwoord6 = input(printAntwoord(6))

if antwoord5 != "A" and antwoord5 != "B" and antwoord4 == "B":
    ongeldig()
    b4()
    antwoord7 = input(printAntwoord(7))
# -------------------------------------
if antwoord6 == "A":
    a6()

elif antwoord6 == "B":
    b6()

if antwoord6 != "A" and antwoord6 != "B" and antwoord5 == "A":
    ongeldig()
    a5()
    antwoord7 = input(printAntwoord(7))

if antwoord6 != "A" and antwoord6 != "B" and antwoord5 == "B":
    ongeldig()
    b5()
    antwoord6 = input(printAntwoord(6))
# -------------------------------------
if antwoord7 == "A":
    a7()
    antwoord8 = input(printAntwoord(8))

elif antwoord7 == "B":
    b7()

if antwoord7 != "A" and antwoord7 != "B" and antwoord6 == "A":
    ongeldig()
    a6()
    antwoord7 = input(printAntwoord(7))

if antwoord7 != "A" and antwoord7 != "B" and antwoord6 == "B":
    ongeldig()
    b6()
    antwoord7 = input(printAntwoord(7))
# -------------------------------------
if antwoord8 == "A":
    a8()

elif antwoord8 == "B":
    b8()

if antwoord8 != "A" and antwoord8 != "B" and antwoord7 == "A":
    ongeldig()
    a7()
    antwoord8 = input(printAntwoord(8))