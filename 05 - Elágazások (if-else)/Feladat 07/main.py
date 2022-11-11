from os import system

number: int = None

print("Add meg a vizsgálandó számot > ", end="")
number = int(input())
system('echo.')

if number%5 == 0:
    print(f"A szám ({number}) OSZTHATÓ 5-tel!")
else:
    print(f"A szám ({number}) NEM osztható 5-tel!")