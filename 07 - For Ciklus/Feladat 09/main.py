from os import system

kezdo: int = None
vegso: int = None

print("Adja meg a kezdőértéket > ", end="")
kezdo = int(input().strip())
system('echo.')

print("Adja meg a záróértéket > ", end="")
vegso = int(input().strip())
system('echo.')

print("A páros számok közöttük csökkenő sorrendben:")

if kezdo > vegso:
    if not kezdo % 2 == 0:
        kezdo += 1
    for i in range(kezdo, vegso + 1, -2):
        print(i)
else:
    for i in range(kezdo, vegso + 1, -2):
        print(i)


if vegso > kezdo:
    if not kezdo % 2 == 0:
        kezdo -= 1
        for i in range(vegso, kezdo + 1, -2):
            print(i)
else:
    for i in range(vegso, kezdo + 1, -2):
        print(i)