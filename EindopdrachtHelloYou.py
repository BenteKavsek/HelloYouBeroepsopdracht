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
    print("Die ochtend zelf ga je met het OV naar Schiphol, je appt iedereen je vluchtnummer en gegevens en zoekt je gate om in te checken,")
    print("even later, nog voordat je bij security bent lijkt het alsof je iemand herkent, je kan alleen niet plaatsen wie het is of waarvan je hem kent, wat doe je? ")


def function11():
    print("Hahaha, in al je enthousiasme ben je vergeten dat je geen rijbewijs hebt")
    print("je kan nog een last minute vliegticket proberen te scoren dan ben je er snel, of je kan gaan liften, misschien leer je wel allem aal leuke mensen kennen!")


def function12():
    print("...")


def function13():
    print("Je ouders kunne je wegbrengen en daarna stap je bij allerlei mensen in, sommige stil, sommige heel gezellig, ziet iemand die je lijkt te herkennen, wat doe je?")


def function14():
    print("...")


def function15():
    print("...")


def function16():
    print("...")


def function17():
    print("...")


def function18():
    print("...")


def function19():
    print("...")


def function20():
    print("...")


def function21():
    print("...")

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