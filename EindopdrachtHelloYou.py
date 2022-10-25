import random
from time import sleep
import keyboard

#functions met stukjes verhaaltjes

def function1():
    print("\n\nWelkom bij mijn eindopdracht van periode 1 Hello You, ik heb een textbased applicatie gemaakt die je een verhaal zal laten beleven.") 
    print("Hierin ben jij de hoofdpersoon, en kan je zelf keuzes maken om te zien hoe het verhaal verder gaat en uiteindelijk afloopt.")


def function2():
    print("\nLeuk dat je wilt beginnen , om keuzes te maken typ je alleen de letter die ervoor staat, dus bijvoorbeeld a of b,\n(Let op! het is hoofdletter gevoelig!)\n")


def function3():
    print("Jammer, tot n andere keer!")


def function4():
    print("Je zit in het examenjaar van je opleiding op met MA, maar jullie klas heeft nog 1 belangrijke toets gemist van het begin van het jaar,")
    print("opzich sta je er prima voor, dus de kans is groot dat je het haalt, wat doe je?")


def function5():
    print("Okee lekker zelfverzekerd, nu hopen dat het goedkomt!")


def function6():
    print("Jammer, de toets weegt zwaarder mee dan je dacht, je bent niet geslaagd en moet het jaar over doen, je kan dus niet komend jaar naar het buitenland. Volgende keer beter!")#nog ff leren


def function7():
    print("Luckyyy! Je stond er al goed voor, het was dus niet zo erg dat je niet alles wist. je bent geslaagd en krijgt een uitnodiging binnen voor je diploma uitreiking,")
    print("eenmaal daar die je veel docenten weer en praat je bij met je klasgenoten, je verteld ze over de reis naar het buitenland die je wilt gaan maken, spannend!")


def function8():
    #iets met if en n functie voor eerst print
    print("Slim! Je slaagt en hebt je vakantie dubbel verdient! ")
    print("Je krijgt een uitnodiging binnen voor je diploma uitreiking, eenmaal daar die je veel docenten weer en praat je bij met je klasgenoten,\nje verteld ze over de reis naar het buitenland die je wilt gaan maken, spannend! ")

def function9():
    print("Je gaat een jaar naar het buitenland, gaaf! Hoe wil je gaan? Met het vliegtuig of rijden")


def function10():
    print("Prima! Je vliegt overmorgen om 6:15 naar Palermo in Sicilië")
    print("hier ben je al een keer met je schoonfamilie geweest en het was ongelofelijk mooi, je gaat vanavond afscheid nemen")
    print("ze willen wel graag op bezoek komen en helpen je alvast met inpakken, zo kan je rustig je vakantie in gaan.\n")

def function102():
    print("De volgende ochtend ga je met het OV naar Schiphol, je appt iedereen je vluchtnummer en gegevens en zoekt je gate om in te checken,")
    print("even later, nog voordat je bij security bent lijkt het alsof je iemand herkent, je kan alleen niet plaatsen wie het is of waarvan je hem kent, wat doe je? ")


def function11():
    print("Hahaha, in al je enthousiasme ben je vergeten dat je geen rijbewijs hebt")
    print("je kan nog een last minute vliegticket proberen te scoren dan ben je er snel, of je kan gaan liften, misschien leer je wel allemaal leuke mensen kennen!\n Wat doe je?")


def function12():
    print("...")


def function13():
  print("Gelukkig kunnen je ouders kunnen je wegbrengen richting de grens maar vanaf daar moet je het toch echt zelf gaan doen.")
  print("Zo kom je nog veel meer leuke mensen tegen, na een tijdje ben je bij een leuk eettentje wat gaan eten en opzoek gegaan naar een nieuw iemand om mee te rijden. plots zie je iemand die je lijkt te herkennen maar kan niet plaatsen wie het is, wat doe je? ")


def function14():
    print("Hij draait zich het blijkt Milos te zijn! Hij was onderweg op vakantie en je stapt in, jullie hebben veel bij te praten na al het liften wat je al gedaan hebt.")
    print("Na 2 jaar op het mediacollege heb je je eigen bedrijf je opgericht waar je veel over wilt vertellen.")
    print("Jullie zijn zoveel aan het praten dat jullie de afslag hebben gemist! Jullie rijden langs een rustig tankstation om wat te eten te halen, je stapt in bij een nieuwe auto, wie?")


def function15():
    print("Je stapt uit, en wacht op een andere auto die langsrijdt, na een half uur gewacht te hebben en een stuk gelopen te hebben zie je twee auto’s staan bij een ander tankstation,")
    #een aardige man, die met zn hond in de auto zit, of een groep vrienden die ook aan het roadtrippen is?


def function17():
    print("Gezellig! Ze zijn onderweg richting Italië, daar wilde je al graag heen, ze hebben met zn alle een bus gehuurd waar je de komende week in mee kan.")


def function172():
    print("Jullie hebben het heel gezellig, nieuwe mensen leren kennen en nieuwe dingen proberen houd je van!")
    print("Na 2,5 week het leuk gehad met al deze mensen overweeg je om weer verder te liften, ga je dat ook doen? Er is vanavond een feetje op het stand,  wil je nog 1 weekend blijven?")


def function18():
    print("...")


def function19():
    print("Het was heel gezellig, maar je gaat weer door, de groep zet je af bij een groot winkelcentrum met allemaal verschillende winkels, terwijl je rond loopt kom je een makelaars bedrijfje tegen.")
    print("Ze verkopen allerlei leuke huisjes, precies goed voor 2 personen, en zelf met een zwembad erbij, heerlijk voor de zomer!")
    print("Dit is perfect denk je, dus je belt je vriend op, hij is heel blij om te horen dat je een leuke plek gevonden hebt en hij boekt meteen een ticket naar je toe.")
    print("Jullie kopen het huis en hebben het ongelofelijk naar jullie zin daar, je hebt goede keuzes gemaakt, congrats!")


def function20():
   print("Hij draait zich om en heeft een grijns op zn gezicht, opeens is iedereen om je heen weg, hij loopt langzaam in jou richting, je staat stil van schrik.")
   print("Hij begint steeds sneller begint te lopen en je begint te rennen, ga je het bos in of ren je door de straat op zoek naar andere mensen om je te helpen? ")


def function21():
    print("Je rent het bos in met de hoop dat je die man kwijtraakt, je raakt alleen zo erg in paniek dat je wat paden in rent, links, rechts, rechts, links, naar een paar minuten ben je hem kwijt, maar ben je ook de weg kwijt...")
    print("Je komt het bos niet meer uit, je moet hier nu zien te overleven en hopen dat je nog mensen al zien binnekort, succes..... ")

def function22():
    print("Je rent de straat uit en in de verte zie je twee lampen wat wel koplampen lijken, ze komen naar je toe!")
    print ("Je rent erheen en begint te zwaaien zodat ze je goed kunnen zien, ze remmen zodat je kan instappen en met ze mee kan rijden.")


def function23():
    print("Je bent snel de bus in gesprongen en jullie rijden weg, het is een gezellige vriendengroep die je tegen bent gekomen, wat een geluk.")
    print("Ze vragen of je zin hebt de komende tijd met ze mee te rijden, ze doen een roadtrip door Europa, Natuurlijk wil je dat! ")


def function24():
    print("Hahaha Enjoy! Jullie hebben te tijd van jullie leven en gaan helemaal los, jullie favoriete band is er en je pakt een gitaar en speelt een liedje mee. ")
    print("T festival gaat door tot vroeg in de ochtend, en opeens sta je backstage, in je dronken bui heb je gitaar gespeeld en dat is de band opgevallen.")
    print("Ze vragen je een liedje met hun te spelen en mee te gaan naar hun volgende show, of je dat wil?")


def function25():
    print("Je stapt in bij de man die naar je zwaait, hij ziet er een beetje raar uit, maar ja je denkt er niet te veel van.")
    print("Later merk je aan hem dat hij gedronken heeft, je komt bijna bij een plek om te slapen, nog een kwartiertje, blijf je zitten of stap je uit?(")

def function26():
    print("Helaas, hij heeft veel dronken en bij een bocht raakt de auto van de weg en vliegen jullie het dal in, je overleeft het niet.")


def function27():
    print ("Heel slim van je! Later hoor je dat de man verongelukt is, je hebt goede keuzes gemaakt! Well done! 😊 ")


def function28():
    print("...")


def function29():
  print("Je neemt de show op het strand afscheid van je groep en vliegt met de band mee naar Nederland waar de volgende show is, het publiek gaat los en je geniet er enorm vann")
  print("opeens valt je oog op je vrienden van het MA en besluit je dat het goed zo is, je maakt de show af en bedankt de band, het is goed zo.")
  print("Wat heb je ongelofelijk genoten afgelopen maanden, maar je bent weer thuis.")


def function30():
  print("Goede keuze! Jij bent de gene die vanavond iedereen veilig mee neemt naar een plek om te slapen vannacht, je hebt het heel erg naar je zin gehad vannacht en besluit bij deze groep te blijven.")
  print("Wie weet wat het je allemaal nog gaat brengen.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------

function1()
antwoord1 = input("kleine stukjes uit het verhaal heb ik gebaseerd op mijzelf, Wil je beginnen?\nA, ja! \nB, nee\n")

if antwoord1 == "A":
    function2()
    print("Succes!")
    function4()
    antwoord4 = input("\nA, het komt wel goed, dus je gaat vast vakantie vieren en maakt de toets zonder te leren\nB, het zijn de laatste lootjes, toch nog even knallen voor de zekerheid!")

elif antwoord1 == "B":
    function3()

if antwoord4 == "Ä":
    function5()
    a = (random.randint(1, 100))
    if a >50:
        function7()
    elif a <=50:
        function8()
        sleep(2)
        function9()
        antwoord9 = input("\nA, het vliegtuig\nB,rijden")

elif antwoord4 == "B":
    function8()
    sleep(2)
    function9()
    antwoord9 = input("\nA, het vliegtuig\nB,rijden")

if antwoord9 == "A":
    function10()
    sleep(2)
    function102()

elif antwoord9 == "B":
    function11()
    antwoord11 = input("A, je gaat alsnog vliegen want je kan niet wachten om er te zijn!\nB,Liften! nieuwe mensen leren kennen kan nooit kwaad!")
#--------------------------------------------------------------------------------------------------------------------

#if antwoord... == "...":
#    function...()
#    antwoord... = input("...")
#
#elif antwoord... == "...":
#    function...()
#    antwoord... = input("...")