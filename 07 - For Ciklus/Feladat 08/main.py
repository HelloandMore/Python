from os import system

szam1: int = None
szam2: int = None

print("Adja meg a kezdőértéket > ", end="")
szam1 = int(input())
system('echo.')

print("Adja meg a záróértéket > ", end="")
szam2 = int(input())
system('echo.')

print("A páratlan számok közöttük növekső sorrendben:")

if szam1>szam2:
    for i in range(szam2, szam1 + 1, 1):
        if not i%2 == 0:
            print(i)


if szam2>szam1:
    for i in range(szam1, szam2 + 1, 1):
        if not i%2 == 0:
            print(i)