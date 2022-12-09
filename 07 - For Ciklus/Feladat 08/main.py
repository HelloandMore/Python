from os import system

kezdo: int = None
vegso: int = None

print("Adja meg a kezdőértéket > ", end="")
kezdo = int(input())
system('echo.')

print("Adja meg a záróértéket > ", end="")
vegso = int(input())
system('echo.')

print("A páratlan számok közöttük növekső sorrendben:")

if kezdo>vegso:
    for i in range(vegso, kezdo + 1, 1):
        if not i%2 == 0:
            print(i)


if vegso>kezdo:
    for i in range(kezdo, vegso + 1, 1):
        if not i%2 == 0:
            print(i)