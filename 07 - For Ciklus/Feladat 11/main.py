from os import system

kezdo: int = None
vegso: int = None
osszeg: int = 0
osszeg2: int = 1   

print("Adja meg a kezdőértéket > ", end="")
kezdo = int(input().strip())
system('echo.')

print("Adja meg a záróértéket > ", end="")
vegso = int(input().strip())
system('echo.')

if kezdo > vegso:
    for i in range(kezdo, vegso - 1, -1):
        if i%2 == 0:
            osszeg += i
        elif i%2:
            osszeg2 = osszeg2 * i
    print(f"Az összegük: {osszeg}\nA szorzatuk: {osszeg2}")
elif vegso > kezdo:
    for i in range(vegso, kezdo - 1, -1):
        if i%2 == 0:
            osszeg += i
        elif i%2:
            osszeg2 = osszeg2 * i
    print(f"Az összegük: {osszeg}\nA szorzatuk: {osszeg2}")
else:
    print("A két szám vagy egyenlő, vagy érvénytelenek!")