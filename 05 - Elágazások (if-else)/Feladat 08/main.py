from os import system

number: int = None

print("Adj meg egy számot > ", end="")
number = int(input())
system('echo.')

if number%4 == 0 and number%6 == 0:
    print(f"A szám ({number}) OSZTHATÓ 4-gyel és 6-tal is!")
elif number%4 == 0:
    print(f"A szám ({number}) CSAK 4-gyel osztható!")
elif number%6 == 0:
    print(f"A szám ({number}) CSAK 6-tal osztható!")
else:
    print(f"A szám ({number}) NEM OSZTHATÓ 4-gyel, sem 6-tal!")