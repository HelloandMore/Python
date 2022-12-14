from os import system

kezdo: int = None
vegso: int = None

print("Adja meg a kezdőértéket > ", end="")
kezdo = int(input().strip())
system('echo.')

print("Adja meg a záróértéket > ", end="")
vegso = int(input().strip())
system('echo.')

print("A számok közöttük csökkenő sorrendben:")

if kezdo>vegso:
    for i in range(kezdo, vegso + 1, -1):
        print(i)

if vegso>kezdo:
    for i in range(vegso, kezdo + 1, -1):
        print(i)