from os import system

number: int = None

print("Add meg a számot > ", end="")
number = int(input())
system('echo.')

if number%2 == 0:
    print(f"A szám ({number}) PÁROS", end="")
elif not number%2 == 0:
    print(f"A szám ({number}) PÁRATLAN", end="")

if number>0:
    print(", pozitív", end="")
elif number<0:
    print(", negatív", end="")
elif number == 0:
    print(", pontosan nulla", end="")

if number == 0:
    print(", ezért NEM osztható!")
elif number%5 == 0:
    print(", és osztható 5-tel!")
else:
    print(", és NEM osztható 5-tel!")