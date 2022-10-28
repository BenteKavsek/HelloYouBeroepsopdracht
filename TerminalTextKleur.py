from colorama import Fore, init
init()

list = [Fore.CYAN + 'some cyan text', Fore.GREEN + 'groene text']

print (list[0] + "\n" + list[1])