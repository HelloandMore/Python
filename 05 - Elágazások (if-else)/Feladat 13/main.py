from os import system

number: int = None

print("Írd be a vizsgálandó számot > ", end="")
number = int(input())

if (number>=0 and number<=9):
    print(f"A szám ({number}) EGYJEGYŰ!")
elif (number>=10 and number<=99):
    print(f"A szám ({number}) KÉTJEGYŰ!")
elif (number>=100 and number<=999):
    print(f"A szám ({number}) HÁROMJEGYŰ!")
else:
    print("A szám nem felel meg az egyik feltételnek sem!")