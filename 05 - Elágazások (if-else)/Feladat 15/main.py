from asyncio.windows_events import selector_events
from doctest import ELLIPSIS_MARKER
from os import system
import sys

zoldsegLeves: bool =  False
husleves: bool = False
gyumolcsLeves: bool = False

sultcsirkecomb: bool = False
sultcsirkemell: bool = False
rakottzoldseg: bool = False
spagetti: bool = False
pizza: bool = False

rizs: bool = False
paroltzoldseg: bool = False
gyumolcs: bool = False
sultkrumpli: bool = False
salata: bool = False
kola: bool = False

selection: str = None

print("Előétel: \nzöldségleves, húsleves, gyümölcsleves")
system('echo.')
print("Főétel: \nsültcsirkecomb, sült csirkemell, rakottzöldség, spagetti, pizza")
system('echo.')
print("Köret: \nrizs, pároltzöldség, gyümölcs, sültkrumpli, saláta, kóla")
system('echo.')

system('echo.')
print("Zöldségleves: 1\bHúsleves: 2\bGyülöcsleves: 3")
print("Válassz előételt > ", end="")
selection = int(input())

if selection == 1:
    zoldsegLeves = True
elif selection == 2:
    husleves = True
elif selection == 3:
    gyumolcsLeves = True
else:
    print("A megadott érték nem felel meg egyiknek sem!")

system('echo.')

print("Sültcsirkecomb: 1\bSült csirkemell: 2\bRakottzöldség: 3\bSpagetti: 4\bPizza: 5\b")
print("Válassz főételt > ", end="")
selection = int(input())

if selection == 1:
    sultcsirkecomb = True
elif selection == 2:
    sultcsirkemell = True
elif selection == 3:
    rakottzoldseg = True
elif selection == 4:
    spagetti = True
elif selection == 5:
    pizza = True
else:
    print("A megadott érték nem felel meg egyiknem sem!")

system('echo.')

print("Rizs: 1\bPároltzöldség: 2\bGyümölcs: 3\bSültkrumpli: 4\bSaláta: 5\bKóla: 5\b")
print("Válassz köretet > ", end="")
selection = int(input())

if selection == 1:
    rizs = True
elif selection == 2:
    paroltzoldseg = True
elif selection == 3:
    gyumolcs = True
elif selection == 4:
    sultkrumpli = True
elif selection == 5:
    salata = True
elif selection == 6:
    kola = True

system('echo.')

