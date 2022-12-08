from os import system

szam1: int = None
szam2: int = None
osszeg: int = 0
osszeg2: int = 1   

print("Adja meg a kezdőértéket > ", end="")
szam1 = int(input())
system('echo.')

print("Adja meg a záróértéket > ", end="")
szam2 = int(input())
system('echo.')

if szam1 > szam2:
    for i in range(szam1, szam2 - 1, -1):
        if i%2 == 0:
            osszeg += i
        elif i%2:
            osszeg2 = osszeg2 * i
    print(f"Az összegük: {osszeg}\nA szorzatuk: {osszeg2}")
elif szam2 > szam1:
    for i in range(szam2, szam1 - 1, -1):
        if i%2 == 0:
            osszeg += i
        elif i%2:
            osszeg2 = osszeg2 * i
    print(f"Az összegük: {osszeg}\nA szorzatuk: {osszeg2}")
else:
    print("A két szám vagy egyenlő, vagy érvénytelenek!")