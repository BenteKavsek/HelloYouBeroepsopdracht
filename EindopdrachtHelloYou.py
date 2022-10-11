import random
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
    print("")#nog ff leren


def function7():
    print("Jammer, de toets weegt zwaarder mee dan je dacht, je bent niet geslaagd en moet het jaar over doen, je kan dus niet komend jaar naar het buitenland. Volgende keer beter!")


def function8():
    print("Luckyyy! Je stond er al goed voor, het was dus niet zo erg dat je niet alles wist. je bent geslaagd en krijgt een uitnodiging binnen voor je diploma uitreiking,")
    print("eenmaal daar die je veel docenten weer en praat je bij met je klasgenoten, je verteld ze over de reis naar het buitenland die je wilt gaan maken, spannend!")


def function9():
    print("...")


def function10():
    print("...")


def function11():
    print("...")


def function12():
    print("...")


def function13():
    print("...")


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

elif antwoord4 == "B":
    function6()

a = (random.randint(1, 100))
if a >50:
    function7()
elif a <=50:
    function8()
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#if antwoord... == "...":
#    function...()
#    antwoord... = input("...")
#
#elif antwoord... == "...":
#    function...()
#    antwoord... = input("...")