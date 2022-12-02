from os import system

number: int = None

print("Adj meg egy számot > ", end="")
number = int(input())
system('echo.')

if number>=10 and number<=20:
    print(f"A szám ({number}) +10 & +20 között van!")
elif number<=-10 and number>=-20:
    print(f"A szám ({number}) -10 & -20 között van!")
else:
    print(f"A szám ({number}) NINCS se -10 & -20, illetve +10 & +20 között!")